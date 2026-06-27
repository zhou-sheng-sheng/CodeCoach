import React, { useEffect, useState } from 'react'
import './MistakeBook.css'

interface ErrorItem {
  question_id: string
  question: string
  options: string[]
  answer: number
  topic: string
  difficulty: string
  explanation: string
  error_count: number
  first_error_time: string
  last_error_time: string
}

interface MistakeBookProps {
  backendPort: number
  language: string
  userId: string
}

const DIFF_LABELS: Record<string, string> = { easy: '简单', medium: '中等', hard: '困难' }
const DIFF_CLASS: Record<string, string> = { easy: 'diff-easy', medium: 'diff-medium', hard: 'diff-hard' }
const OPTION_LABELS = ['A', 'B', 'C', 'D', 'E']

const LANGUAGES = [
  { value: 'python', label: 'Python' },
  { value: 'javascript', label: 'JavaScript' },
  { value: 'typescript', label: 'TypeScript' },
  { value: 'java', label: 'Java' },
  { value: 'go', label: 'Go' },
  { value: 'rust', label: 'Rust' },
  { value: 'cpp', label: 'C++' },
  { value: 'sql', label: 'SQL' },
]

const MistakeBook: React.FC<MistakeBookProps> = ({ backendPort, language, userId }) => {
  const [errors, setErrors] = useState<ErrorItem[]>([])
  const [loading, setLoading] = useState(true)
  const [fetchError, setFetchError] = useState('')
  const [expanded, setExpanded] = useState<string | null>(null)
  const [filter, setFilter] = useState({ topic: '', difficulty: '' })

  useEffect(() => {
    setLoading(true)
    fetch(`http://127.0.0.1:${backendPort}/api/errors/book?language=${language}&user_id=${encodeURIComponent(userId)}`)
      .then(r => r.json())
      .then(d => {
        if (d.error) {
          setFetchError(d.error)
        } else {
          const items = Object.entries(d).map(([id, item]: [string, any]) => ({
            question_id: id,
            ...item,
          }))
          items.sort((a, b) => new Date(b.last_error_time).getTime() - new Date(a.last_error_time).getTime())
          setErrors(items)
        }
      })
      .catch(e => setFetchError(`加载失败：${e.message}`))
      .finally(() => setLoading(false))
  }, [backendPort, language])

  const topics = [...new Set(errors.map(e => e.topic))].sort()
  const difficulties = [...new Set(errors.map(e => e.difficulty))].sort()

  const filtered = errors.filter(e => {
    if (filter.topic && e.topic !== filter.topic) return false
    if (filter.difficulty && e.difficulty !== filter.difficulty) return false
    return true
  })

  if (loading) {
    return (
      <div className="mistake-container">
        <div className="mistake-loading">加载错题本...</div>
      </div>
    )
  }

  if (fetchError) {
    return (
      <div className="mistake-container">
        <div className="mistake-error">{fetchError}</div>
      </div>
    )
  }

  return (
    <div className="mistake-container">
      <div className="mistake-header">
        <h2>错题本</h2>
        <span className="mistake-count">共 {errors.length} 道错题</span>
      </div>

      {/* 当前语言标签 */}
      <div className="mistake-lang-tag">
        当前语言：{LANGUAGES.find(l => l.value === language)?.label || language}
      </div>

      {/* 筛选 */}
      <div className="mistake-filters">
        <select
          className="filter-select"
          value={filter.topic}
          onChange={e => setFilter(prev => ({ ...prev, topic: e.target.value }))}
        >
          <option value="">全部主题</option>
          {topics.map(t => <option key={t} value={t}>{t}</option>)}
        </select>
        <select
          className="filter-select"
          value={filter.difficulty}
          onChange={e => setFilter(prev => ({ ...prev, difficulty: e.target.value }))}
        >
          <option value="">全部难度</option>
          {difficulties.map(d => (
            <option key={d} value={d}>{DIFF_LABELS[d] || d}</option>
          ))}
        </select>
      </div>

      {filtered.length === 0 ? (
        <div className="mistake-empty">
          {errors.length === 0
            ? '暂无错题，继续练习吧！'
            : '当前筛选条件下无错题'}
        </div>
      ) : (
        <div className="mistake-list">
          {filtered.map(item => {
            const isOpen = expanded === item.question_id
            return (
              <div key={item.question_id} className="mistake-card">
                <div
                  className="mistake-card-header"
                  onClick={() => setExpanded(isOpen ? null : item.question_id)}
                >
                  <div className="card-header-left">
                    <span className={`diff-tag ${DIFF_CLASS[item.difficulty] || ''}`}>
                      {DIFF_LABELS[item.difficulty] || item.difficulty}
                    </span>
                    <span className="topic-tag">{item.topic}</span>
                    <span className="error-badge">
                      错 {item.error_count} 次
                    </span>
                  </div>
                  <div className="card-header-right">
                    <span className="card-date">
                      {item.last_error_time?.slice(0, 10)}
                    </span>
                    <span className={`expand-icon ${isOpen ? 'open' : ''}`}>
                      &#9660;
                    </span>
                  </div>
                </div>

                <div className="card-question-preview" onClick={() => setExpanded(isOpen ? null : item.question_id)}>
                  <pre className="question-text">{item.question}</pre>
                </div>

                {isOpen && (
                  <div className="card-detail">
                    <div className="detail-options">
                      <div className="detail-label">选项：</div>
                      {item.options.map((opt, i) => (
                        <div
                          key={i}
                          className={`option-item ${i === item.answer ? 'option-correct' : ''}`}
                        >
                          <span className="option-letter">{OPTION_LABELS[i]}</span>
                          <span className="option-text">{opt}</span>
                          {i === item.answer && <span className="correct-mark">&#10003; 正确答案</span>}
                        </div>
                      ))}
                    </div>
                    <div className="detail-explanation">
                      <div className="detail-label">解析：</div>
                      <p className="explanation-text">{item.explanation}</p>
                    </div>
                  </div>
                )}
              </div>
            )
          })}
        </div>
      )}
    </div>
  )
}

export default MistakeBook
