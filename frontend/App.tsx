import React, { useState, useRef, useEffect } from 'react'
import Login from './components/Login/Login'
import ChatPanel from './components/ChatPanel/ChatPanel'
import StudyPlan from './components/StudyPlan/StudyPlan'
import Exercise from './components/Exercise/Exercise'
import Learn from './components/Learn/Learn'
import Dashboard from './components/Dashboard/Dashboard'
import Assessment from './components/Assessment/Assessment'
import Interview from './components/Interview/Interview'
import MistakeBook from './components/MistakeBook/MistakeBook'
import Notebook from './components/Notebook/Notebook'
import CodeEditor from './components/CodeEditor/CodeEditor'
import Settings from './components/Settings/Settings'

type ViewName = 'chat' | 'plan' | 'learn' | 'exercise' | 'assessment' | 'interview' | 'dashboard' | 'mistakebook' | 'notebook' | 'sandbox' | 'settings'

const views: { key: ViewName; label: string }[] = [
  { key: 'chat', label: 'AI 陪练' },
  { key: 'plan', label: '学习计划' },
  { key: 'learn', label: '知识点学习' },
  { key: 'exercise', label: '习题练习' },
  { key: 'assessment', label: '基础评估' },
  { key: 'interview', label: '模拟面试' },
  { key: 'dashboard', label: '数据看板' },
  { key: 'mistakebook', label: '错题本' },
  { key: 'notebook', label: '笔记' },
  { key: 'sandbox', label: '沙箱' },
]

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

const Placeholder: React.FC<{ title: string }> = ({ title }) => (
  <div className="placeholder-view">
    <div className="placeholder-icon">&#128736;</div>
    <h3>{title}</h3>
    <p>该模块正在开发中，敬请期待。</p>
  </div>
)

const App: React.FC = () => {
  const [backendReady, setBackendReady] = useState(false)
  const [backendPort, setBackendPort] = useState<number | null>(null)
  const [activeView, setActiveView] = useState<ViewName>('chat')
  const [language, setLanguage] = useState('python')
  const [loggedIn, setLoggedIn] = useState(false)
  const [username, setUsername] = useState('')
  const [menuOpen, setMenuOpen] = useState(false)
  const menuRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    const handler = (e: MouseEvent) => {
      if (menuRef.current && !menuRef.current.contains(e.target as Node)) {
        setMenuOpen(false)
      }
    }
    document.addEventListener('mousedown', handler)
    return () => document.removeEventListener('mousedown', handler)
  }, [])

  React.useEffect(() => {
    let retryCount = 0
    const MAX_RETRIES = 20
    let timerId: ReturnType<typeof setTimeout> | null = null

    const checkBackend = async () => {
      try {
        if (window.electronAPI) {
          const status = await window.electronAPI.getBackendStatus()
          const port = await window.electronAPI.getBackendPort()
          if (status && port) {
            setBackendReady(true)
            setBackendPort(port)
            return
          }
        }
      } catch {}

      retryCount++
      if (retryCount >= MAX_RETRIES) {
        console.warn('[App] Backend not available after', MAX_RETRIES, 'retries, proceeding without backend')
        setBackendReady(true)
        setBackendPort(18080)
        return
      }
      timerId = setTimeout(checkBackend, 1000)
    }
    checkBackend()

    return () => {
      if (timerId !== null) clearTimeout(timerId)
    }
  }, [])

  if (!backendReady) {
    return (
      <div className="loading-screen">
        <div className="loading-spinner" />
        <h2>编程AI陪练</h2>
        <p>正在启动后端服务...</p>
      </div>
    )
  }

  if (!loggedIn) {
    return (
      <Login onLogin={(name) => {
        setUsername(name)
        setLoggedIn(true)
      }} />
    )
  }

  const renderContent = () => {
    switch (activeView) {
      case 'chat':
        return <ChatPanel backendPort={backendPort!} language={language} userId={username} />
      case 'plan':
        return <StudyPlan backendPort={backendPort!} language={language} userId={username} />
      case 'learn':
        return <Learn backendPort={backendPort!} language={language} />
      case 'exercise':
        return <Exercise backendPort={backendPort!} language={language} userId={username} />
      case 'assessment':
        return <Assessment backendPort={backendPort!} language={language} userId={username} />
      case 'interview':
        return <Interview backendPort={backendPort!} language={language} userId={username} />
      case 'dashboard':
        return <Dashboard backendPort={backendPort!} language={language} userId={username} onNavigate={(v) => setActiveView(v as ViewName)} />
      case 'mistakebook':
        return <MistakeBook backendPort={backendPort!} language={language} userId={username} />
      case 'notebook':
        return <Notebook backendPort={backendPort!} userId={username} />
      case 'sandbox':
        return <CodeEditor backendPort={backendPort!} userId={username} language={language} />
      case 'settings':
        return <Settings />
    }
  }

  return (
    <div className="app-container">
      <aside className="sidebar">
        <div className="sidebar-header">
          <h2>编程AI陪练</h2>
          <div className="user-menu" ref={menuRef}>
            <button
              className="user-avatar"
              onClick={() => setMenuOpen(!menuOpen)}
              title={username}
            >
              {username.charAt(0).toUpperCase()}
            </button>
            {menuOpen && (
              <div className="user-dropdown">
                <div className="dropdown-user-info">{username}</div>
                <div className="dropdown-divider" />
                <button
                  className="dropdown-item"
                  onClick={() => { setActiveView('settings'); setMenuOpen(false) }}
                >
                  <span className="dropdown-icon">&#9881;</span> 设置
                </button>
                <button
                  className="dropdown-item dropdown-item-danger"
                  onClick={() => { setLoggedIn(false); setMenuOpen(false) }}
                >
                  <span className="dropdown-icon">&#10149;</span> 退出登录
                </button>
              </div>
            )}
          </div>
        </div>
        <div className="language-selector">
          <label>语言</label>
          <select value={language} onChange={(e) => setLanguage(e.target.value)}>
            {LANGUAGES.map((l) => (
              <option key={l.value} value={l.value}>{l.label}</option>
            ))}
          </select>
        </div>
        <nav className="sidebar-nav">
          {views.map((v) => (
            <button
              key={v.key}
              className={`nav-item ${activeView === v.key ? 'active' : ''}`}
              onClick={() => setActiveView(v.key)}
            >
              {v.label}
            </button>
          ))}
        </nav>
        <div className="sidebar-footer">
          <span className="version-tag">v0.1.0</span>
        </div>
      </aside>
      <main className="main-content">
        {renderContent()}
      </main>
    </div>
  )
}

export default App

// Electron API type declaration
declare global {
  interface Window {
    electronAPI?: {
      getBackendStatus: () => Promise<boolean>
      getBackendPort: () => Promise<number>
      platform: string
    }
  }
}
