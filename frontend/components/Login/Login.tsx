import React, { useState } from 'react'
import './Login.css'

interface LoginProps {
  onLogin: (username: string) => void
}

const Login: React.FC<LoginProps> = ({ onLogin }) => {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [errorMsg, setErrorMsg] = useState('')

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    setErrorMsg('')

    if (!username.trim()) {
      setErrorMsg('请输入用户名')
      return
    }

    onLogin(username.trim())
  }

  return (
    <div className="login-container">
      {/* 左侧：装饰图 */}
      <div className="login-decoration">
        <img
          src="./login-bg.png"
          alt="编程AI陪练"
          className="login-bg-image"
        />
      </div>

      {/* 右侧：表单区域 */}
      <div className="login-form-area">
        <div className="login-form-card">
          <h2 className="login-title">欢迎回来</h2>
          <p className="login-subtitle">登录即注册，输入用户名即可开始</p>

          <form onSubmit={handleSubmit} className="login-form">
            <div className="form-group">
              <label htmlFor="username" className="form-label">账号</label>
              <input
                id="username"
                type="text"
                className="form-input"
                placeholder="请输入用户名"
                value={username}
                onChange={e => setUsername(e.target.value)}
                autoFocus
              />
            </div>
            <div className="form-group">
              <label htmlFor="password" className="form-label">密码</label>
              <input
                id="password"
                type="password"
                className="form-input"
                placeholder="请输入密码"
                value={password}
                onChange={e => setPassword(e.target.value)}
              />
            </div>
            {errorMsg && <p className="login-error">{errorMsg}</p>}
            <button type="submit" className="login-btn" disabled={!username.trim()}>
              登录
            </button>
            <p className="login-hint">首次登录将自动创建账号，无需额外注册</p>
          </form>
        </div>
      </div>
    </div>
  )
}

export default Login
