import React, { useState, useEffect, useRef, useCallback } from 'react'
import './Notebook.css'

interface Note {
  id: string
  title: string
  content: string
  topic: string
  created_at: number
  updated_at: number
}

interface NotebookProps {
  backendPort: number
  userId: string
}

const baseUrl = (port: number) => `http://127.0.0.1:${port}`

/** 将 HTML 内容转为纯文本，用于卡片预览 */
const stripHtml = (html: string) => {
  const div = document.createElement('div')
  div.innerHTML = html
  return div.textContent || div.innerText || ''
}

/** 格式化时间戳为简短日期 */
const fmt = (ts: number) => {
  const d = new Date(ts)
  return `${d.getMonth() + 1}/${d.getDate()} ${String(d.getHours()).padStart(2, '0')}:${String(d.getMinutes()).padStart(2, '0')}`
}

const Notebook: React.FC<NotebookProps> = ({ backendPort, userId }) => {
  const [notes, setNotes] = useState<Note[]>([])
  const [editingId, setEditingId] = useState<string | null>(null)
  const [title, setTitle] = useState('')
  const [content, setContent] = useState('')
  const [topic, setTopic] = useState('')
  const [search, setSearch] = useState('')
  const [loading, setLoading] = useState(false)

  const editorRef = useRef<HTMLDivElement>(null)

  // ── 后端 API ──

  const fetchNotes = useCallback(async () => {
    setLoading(true)
    try {
      const res = await fetch(`${baseUrl(backendPort)}/api/notebook?user_id=${encodeURIComponent(userId)}`)
      const data = await res.json()
      if (data.success) setNotes(data.notes || [])
    } catch (err) {
      console.error('加载笔记失败:', err)
    } finally {
      setLoading(false)
    }
  }, [backendPort, userId])

  useEffect(() => {
    fetchNotes()
  }, [fetchNotes])

  const apiCreate = async (note: Omit<Note, 'id' | 'created_at' | 'updated_at'>) => {
    const res = await fetch(`${baseUrl(backendPort)}/api/notebook`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        user_id: userId,
        title: note.title,
        content: note.content,
        topic: note.topic,
      }),
    })
    const data = await res.json()
    if (data.success) setNotes(prev => [data.note, ...prev])
    return data
  }

  const apiUpdate = async (id: string, payload: { title?: string; content?: string; topic?: string }) => {
    const res = await fetch(`${baseUrl(backendPort)}/api/notebook/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ user_id: userId, ...payload }),
    })
    const data = await res.json()
    if (data.success) {
      setNotes(prev => prev.map(n => n.id === id ? data.note : n))
    }
    return data
  }

  const apiDelete = async (id: string) => {
    const res = await fetch(`${baseUrl(backendPort)}/api/notebook/${id}?user_id=${encodeURIComponent(userId)}`, {
      method: 'DELETE',
    })
    const data = await res.json()
    if (data.success) setNotes(prev => prev.filter(n => n.id !== id))
    return data
  }

  // ── 富文本工具栏 ──

  const execCmd = (cmd: string, value?: string) => {
    document.execCommand(cmd, false, value)
    editorRef.current?.focus()
    // 同步 content 状态
    if (editorRef.current) {
      setContent(editorRef.current.innerHTML)
    }
  }

  const insertCodeBlock = () => {
    const sel = window.getSelection()
    if (!sel || sel.rangeCount === 0) return
    const range = sel.getRangeAt(0)
    const text = range.toString()
    if (text) {
      const pre = document.createElement('pre')
      const code = document.createElement('code')
      code.textContent = text
      pre.appendChild(code)
      range.deleteContents()
      range.insertNode(pre)
    } else {
      // 无选中文本，插入空代码块模板
      const pre = document.createElement('pre')
      const code = document.createElement('code')
      code.textContent = '// 在此输入代码'
      pre.appendChild(code)
      range.insertNode(pre)
      // 选中 code 内文本方便直接替换
      const newRange = document.createRange()
      newRange.selectNodeContents(code)
      sel.removeAllRanges()
      sel.addRange(newRange)
    }
    if (editorRef.current) {
      setContent(editorRef.current.innerHTML)
    }
    editorRef.current?.focus()
  }

  // ── 编辑操作 ──

  const startNew = () => {
    const tempId = 'temp_' + Date.now()
    setEditingId(tempId)
    setTitle('')
    setContent('')
    setTopic('')
    setTimeout(() => {
      if (editorRef.current) {
        editorRef.current.innerHTML = ''
        editorRef.current.focus()
      }
    }, 0)
  }

  const startEdit = (note: Note) => {
    setEditingId(note.id)
    setTitle(note.title)
    setContent(note.content)
    setTopic(note.topic)
    setTimeout(() => {
      if (editorRef.current) {
        editorRef.current.innerHTML = note.content
        editorRef.current.focus()
      }
    }, 0)
  }

  const saveNote = async () => {
    if (!editingId) return
    const htmlContent = editorRef.current ? editorRef.current.innerHTML : content
    const plainText = stripHtml(htmlContent)

    if (!title.trim() && !plainText.trim()) {
      // 空笔记：若是临时 ID 则放弃，否则删除
      if (editingId.startsWith('temp_')) {
        cancelEdit()
        return
      }
      await apiDelete(editingId)
      cancelEdit()
      return
    }

    if (editingId.startsWith('temp_')) {
      await apiCreate({ title: title.trim(), content: htmlContent, topic: topic.trim() })
    } else {
      await apiUpdate(editingId, {
        title: title.trim(),
        content: htmlContent,
        topic: topic.trim(),
      })
    }
    cancelEdit()
  }

  const cancelEdit = () => {
    setEditingId(null)
    setTitle('')
    setContent('')
    setTopic('')
  }

  const deleteNote = async (id: string) => {
    await apiDelete(id)
    if (editingId === id) cancelEdit()
  }

  // ── 过滤 ──

  const filtered = notes.filter(n => {
    if (!search) return true
    const q = search.toLowerCase()
    return n.title.toLowerCase().includes(q)
      || stripHtml(n.content).toLowerCase().includes(q)
      || n.topic.toLowerCase().includes(q)
  })

  return (
    <div className="notebook-container">
      <div className="notebook-header">
        <h2>学习笔记</h2>
        <button className="btn-primary btn-sm" onClick={startNew}>
          + 新建笔记
        </button>
      </div>

      {notes.length > 0 && (
        <div className="notebook-search">
          <input
            type="text"
            className="search-input"
            placeholder="搜索笔记..."
            value={search}
            onChange={e => setSearch(e.target.value)}
          />
        </div>
      )}

      {/* 富文本编辑器 */}
      {editingId !== null && (
        <div className="note-editor">
          <input
            type="text"
            className="editor-title-input"
            placeholder="笔记标题"
            value={title}
            onChange={e => setTitle(e.target.value)}
            autoFocus
          />
          <input
            type="text"
            className="editor-topic-input"
            placeholder="主题标签（如：数据结构、算法）"
            value={topic}
            onChange={e => setTopic(e.target.value)}
          />
          {/* 工具栏 */}
          <div className="editor-toolbar">
            <button
              type="button"
              className="toolbar-btn"
              title="加粗"
              onMouseDown={e => { e.preventDefault(); execCmd('bold') }}
            >
              <strong>B</strong>
            </button>
            <button
              type="button"
              className="toolbar-btn"
              title="斜体"
              onMouseDown={e => { e.preventDefault(); execCmd('italic') }}
            >
              <em>I</em>
            </button>
            <button
              type="button"
              className="toolbar-btn"
              title="代码块"
              onMouseDown={e => { e.preventDefault(); insertCodeBlock() }}
            >
              {'</>'}
            </button>
          </div>
          <div
            ref={editorRef}
            className="rich-editor"
            contentEditable
            suppressContentEditableWarning
            onInput={() => {
              if (editorRef.current) setContent(editorRef.current.innerHTML)
            }}
            onKeyDown={e => {
              // Ctrl+S 保存
              if ((e.ctrlKey || e.metaKey) && e.key === 's') {
                e.preventDefault()
                saveNote()
              }
            }}
          />
          <div className="editor-actions">
            <button className="btn-primary" onClick={saveNote}>
              保存
            </button>
            <button className="btn-secondary" onClick={cancelEdit}>
              取消
            </button>
          </div>
        </div>
      )}

      {/* 笔记列表 */}
      {loading && notes.length === 0 ? (
        <div className="notebook-empty">加载中...</div>
      ) : filtered.length === 0 ? (
        <div className="notebook-empty">
          {notes.length === 0
            ? '还没有笔记，点击上方按钮创建第一篇笔记'
            : '未找到匹配的笔记'}
        </div>
      ) : (
        <div className="notes-grid">
          {filtered.map(note => (
            <div key={note.id} className="note-card">
              <div className="note-card-header">
                <h3 className="note-title" onClick={() => startEdit(note)}>
                  {note.title || '无标题笔记'}
                </h3>
                {note.topic && (
                  <span className="note-topic-tag">{note.topic}</span>
                )}
              </div>
              <p className="note-preview" onClick={() => startEdit(note)}>
                {stripHtml(note.content).slice(0, 150)}
                {stripHtml(note.content).length > 150 ? '...' : ''}
              </p>
              <div className="note-card-footer">
                <span className="note-date">{fmt(note.updated_at)}</span>
                <div className="note-card-actions">
                  <button className="btn-link" onClick={() => startEdit(note)}>
                    编辑
                  </button>
                  <button className="btn-link btn-link-danger" onClick={() => deleteNote(note.id)}>
                    删除
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default Notebook
