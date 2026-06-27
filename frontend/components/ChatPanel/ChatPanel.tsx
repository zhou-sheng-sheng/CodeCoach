import React, { useState, useRef, useEffect } from 'react'
import ReactMarkdown from 'react-markdown'
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter'
import { vscDarkPlus } from 'react-syntax-highlighter/dist/esm/styles/prism'
import './ChatPanel.css'

interface Message {
  id: string
  role: 'user' | 'assistant'
  content: string
  timestamp: number
}

interface ChatPanelProps {
  backendPort: number
  language: string
  userId: string
}

const ChatPanel: React.FC<ChatPanelProps> = ({ backendPort, language, userId }) => {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: 'welcome',
      role: 'assistant',
      content: '你好！我是你的编程AI陪练。我可以帮你：\n\n- 解答编程问题\n- 审查和优化代码\n- 讲解概念和原理\n- Debug 辅助\n\n直接发代码或提问吧！',
      timestamp: Date.now()
    }
  ])
  const [input, setInput] = useState('')
  const [isStreaming, setIsStreaming] = useState(false)
  const messagesEndRef = useRef<HTMLDivElement>(null)
  const textareaRef = useRef<HTMLTextAreaElement>(null)
  const abortControllerRef = useRef<AbortController | null>(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const sendMessage = async () => {
    const text = input.trim()
    if (!text || isStreaming) return

    const userMsg: Message = {
      id: `user-${Date.now()}`,
      role: 'user',
      content: text,
      timestamp: Date.now()
    }
    setMessages(prev => [...prev, userMsg])
    setInput('')
    setIsStreaming(true)

    const assistantMsgId = `assistant-${Date.now()}`
    setMessages(prev => [...prev, {
      id: assistantMsgId,
      role: 'assistant',
      content: '',
      timestamp: Date.now()
    }])

    abortControllerRef.current = new AbortController()

    try {
      const response = await fetch(`http://127.0.0.1:${backendPort}/api/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: text, language, user_id: userId, history: messages.map(m => ({ role: m.role, content: m.content })) }),
        signal: abortControllerRef.current.signal
      })

      if (!response.ok) throw new Error(`HTTP ${response.status}`)

      const reader = response.body?.getReader()
      if (!reader) throw new Error('No response body')

      const decoder = new TextDecoder()
      let content = ''

      while (true) {
        const { done, value } = await reader.read()
        if (done) break

        content += decoder.decode(value, { stream: true })
        setMessages(prev => prev.map(m =>
          m.id === assistantMsgId ? { ...m, content } : m
        ))
      }
    } catch (err: any) {
      if (err.name !== 'AbortError') {
        setMessages(prev => prev.map(m =>
          m.id === assistantMsgId
            ? { ...m, content: `错误：无法连接到后端服务。请确保 Python 后端已启动。（${err.message}）` }
            : m
        ))
      }
    } finally {
      setIsStreaming(false)
      abortControllerRef.current = null
    }
  }

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      sendMessage()
    }
  }

  const handleStop = () => {
    abortControllerRef.current?.abort()
    setIsStreaming(false)
  }

  const adjustTextareaHeight = () => {
    const el = textareaRef.current
    if (el) {
      el.style.height = 'auto'
      el.style.height = Math.min(el.scrollHeight, 200) + 'px'
    }
  }

  return (
    <div className="chat-panel">
      <div className="chat-messages">
        {messages.map(msg => (
          <div key={msg.id} className={`message ${msg.role}`}>
            <div className="message-avatar">
              {msg.role === 'assistant' ? 'AI' : 'You'}
            </div>
            <div className="message-content">
              <ReactMarkdown
                components={{
                  code({ className, children, ...props }) {
                    const match = /language-(\w+)/.exec(className || '')
                    const codeStr = String(children).replace(/\n$/, '')
                    if (match) {
                      return (
                        <div className="code-block-wrapper">
                          <div className="code-block-header">
                            <span className="code-lang">{match[1]}</span>
                            <button
                              className="copy-btn"
                              onClick={() => navigator.clipboard.writeText(codeStr)}
                            >
                              复制
                            </button>
                          </div>
                          <SyntaxHighlighter
                            style={vscDarkPlus}
                            language={match[1]}
                            PreTag="div"
                          >
                            {codeStr}
                          </SyntaxHighlighter>
                        </div>
                      )
                    }
                    return (
                      <code className="inline-code" {...props}>
                        {children}
                      </code>
                    )
                  }
                }}
              >
                {msg.content || (msg.role === 'assistant' && isStreaming ? '...' : '')}
              </ReactMarkdown>
            </div>
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>

      <div className="chat-input-container">
        <textarea
          ref={textareaRef}
          className="chat-input"
          value={input}
          onChange={(e) => { setInput(e.target.value); adjustTextareaHeight() }}
          onKeyDown={handleKeyDown}
          placeholder="输入你的问题，或者粘贴代码..."
          rows={1}
          disabled={isStreaming}
        />
        <div className="chat-actions">
          <span className="input-hint">Enter 发送 · Shift+Enter 换行</span>
          {isStreaming ? (
            <button className="send-btn stop-btn" onClick={handleStop}>
              停止
            </button>
          ) : (
            <button
              className="send-btn"
              onClick={sendMessage}
              disabled={!input.trim()}
            >
              发送
            </button>
          )}
        </div>
      </div>
    </div>
  )
}

export default ChatPanel
