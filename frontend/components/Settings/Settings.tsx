import React, { useState, useEffect, useCallback } from 'react'
import './Settings.css'

const PRESET_COLORS = [
  { name: '蓝', hex: '#6b9fd4' },
  { name: '绿', hex: '#5a9e6f' },
  { name: '紫', hex: '#8b6fbf' },
  { name: '橙', hex: '#c4903a' },
  { name: '粉', hex: '#d47b8a' },
  { name: '青', hex: '#4da6a0' },
  { name: '红', hex: '#c45a5a' },
  { name: '灰', hex: '#7a7a7a' },
]

const BG_MODES = [
  { value: 'cover', label: '覆盖' },
  { value: 'tile', label: '平铺' },
  { value: 'center', label: '居中' },
]

const THEME_KEY = 'accent_color'
const BG_KEY = 'custom_background'
const BG_MODE_KEY = 'background_mode'
const DARK_MODE_KEY = 'dark_mode'

const DARK_VARS: Record<string, string> = {
  '--bg-primary': '#1e1e2e',
  '--bg-secondary': '#252538',
  '--bg-tertiary': '#2e2e42',
  '--bg-card': '#2a2a3c',
  '--bg-hover': '#333348',
  '--border-color': '#3a3a4a',
  '--text-primary': '#e0e0e0',
  '--text-secondary': '#a0a0b0',
  '--text-muted': '#7a7a90',
  '--text-tertiary': '#606078',
  '--code-bg': '#252538',
}

function getAccentColorFromCSS(): string {
  const root = document.documentElement
  return getComputedStyle(root).getPropertyValue('--accent-blue').trim() || '#6b9fd4'
}

function injectAccentColor(hex: string) {
  const root = document.documentElement
  root.style.setProperty('--accent-blue', hex)

  // 计算 rgb 值用于透明度场景
  const r = parseInt(hex.slice(1, 3), 16)
  const g = parseInt(hex.slice(3, 5), 16)
  const b = parseInt(hex.slice(5, 7), 16)
  root.style.setProperty('--accent-rgb', `${r}, ${g}, ${b}`)
}

function injectDarkMode(enabled: boolean) {
  const root = document.documentElement
  if (enabled) {
    Object.entries(DARK_VARS).forEach(([key, value]) => {
      root.style.setProperty(key, value)
    })
  } else {
    Object.keys(DARK_VARS).forEach((key) => {
      root.style.removeProperty(key)
    })
  }
}

function applyBackground(base64: string | null, mode: string) {
  const root = document.getElementById('root')
  if (!root) return
  if (base64) {
    root.style.backgroundImage = `url(${base64})`
    switch (mode) {
      case 'tile':
        root.style.backgroundSize = 'auto'
        root.style.backgroundRepeat = 'repeat'
        root.style.backgroundPosition = 'top left'
        break
      case 'center':
        root.style.backgroundSize = 'auto'
        root.style.backgroundRepeat = 'no-repeat'
        root.style.backgroundPosition = 'center'
        break
      case 'cover':
      default:
        root.style.backgroundSize = 'cover'
        root.style.backgroundRepeat = 'no-repeat'
        root.style.backgroundPosition = 'center'
        break
    }
  } else {
    root.style.backgroundImage = ''
    root.style.backgroundSize = ''
    root.style.backgroundRepeat = ''
    root.style.backgroundPosition = ''
  }
}

const Settings: React.FC = () => {
  const [accentColor, setAccentColor] = useState(() => {
    return localStorage.getItem(THEME_KEY) || getAccentColorFromCSS()
  })
  const [customHex, setCustomHex] = useState('')
  const [bgMode, setBgMode] = useState(() => {
    return localStorage.getItem(BG_MODE_KEY) || 'cover'
  })
  const [hasBg, setHasBg] = useState(() => {
    return !!localStorage.getItem(BG_KEY)
  })
  const [message, setMessage] = useState('')
  const [darkMode, setDarkMode] = useState(() => {
    return localStorage.getItem(DARK_MODE_KEY) === 'true'
  })

  // 初始化时注入主题色
  useEffect(() => {
    injectAccentColor(accentColor)
  }, [])

  // 初始化背景
  useEffect(() => {
    const savedBg = localStorage.getItem(BG_KEY)
    const savedMode = localStorage.getItem(BG_MODE_KEY) || 'cover'
    if (savedBg) {
      applyBackground(savedBg, savedMode)
    }
  }, [])

  // 初始化暗色模式
  useEffect(() => {
    injectDarkMode(darkMode)
  }, [])

  const showMessage = useCallback((msg: string) => {
    setMessage(msg)
    setTimeout(() => setMessage(''), 2000)
  }, [])

  const handleColorSelect = (hex: string) => {
    setAccentColor(hex)
    setCustomHex('')
    localStorage.setItem(THEME_KEY, hex)
    injectAccentColor(hex)
    showMessage(`主题色已切换为 ${hex}`)
  }

  const handleCustomHexApply = () => {
    const hex = customHex.trim()
    if (!/^#[0-9a-fA-F]{6}$/.test(hex)) {
      showMessage('请输入有效的 hex 颜色（如 #ff6600）')
      return
    }
    setAccentColor(hex)
    localStorage.setItem(THEME_KEY, hex)
    injectAccentColor(hex)
    showMessage(`自定义主题色已应用: ${hex}`)
  }

  const handleBgUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (!file) return

    const allowed = ['image/jpeg', 'image/png', 'image/gif']
    if (!allowed.includes(file.type)) {
      showMessage('仅支持 JPG、PNG、GIF 格式')
      return
    }

    const reader = new FileReader()
    reader.onload = () => {
      const base64 = reader.result as string
      localStorage.setItem(BG_KEY, base64)
      localStorage.setItem(BG_MODE_KEY, bgMode)
      applyBackground(base64, bgMode)
      setHasBg(true)
      showMessage('自定义背景已应用')
    }
    reader.readAsDataURL(file)
  }

  const handleBgModeChange = (mode: string) => {
    setBgMode(mode)
    localStorage.setItem(BG_MODE_KEY, mode)
    const savedBg = localStorage.getItem(BG_KEY)
    if (savedBg) {
      applyBackground(savedBg, mode)
      showMessage(`背景模式已切换为 ${BG_MODES.find(m => m.value === mode)?.label}`)
    }
  }

  const handleResetBg = () => {
    localStorage.removeItem(BG_KEY)
    localStorage.removeItem(BG_MODE_KEY)
    setBgMode('cover')
    setHasBg(false)
    applyBackground(null, 'cover')
    showMessage('已恢复默认背景')
  }

  const handleResetTheme = () => {
    const defaultHex = '#6b9fd4'
    setAccentColor(defaultHex)
    setCustomHex('')
    localStorage.setItem(THEME_KEY, defaultHex)
    injectAccentColor(defaultHex)
    showMessage('已恢复默认主题色')
  }

  const handleDarkModeToggle = (enabled: boolean) => {
    setDarkMode(enabled)
    localStorage.setItem(DARK_MODE_KEY, String(enabled))
    injectDarkMode(enabled)
    showMessage(enabled ? '已切换为暗色模式' : '已切换为亮色模式')
  }

  return (
    <div className="settings-container">
      <div className="settings-header">
        <h2>设置</h2>
        <p className="settings-subtitle">自定义外观和背景</p>
      </div>

      {message && <div className="settings-toast">{message}</div>}

      <div className="settings-section">
        <h3 className="section-title">外观模式</h3>
        <p className="section-desc">切换亮色或暗色主题，暗色模式下背景和卡片颜色会变深。</p>
        <div className="mode-switch-row">
          <button
            className={`mode-switch-btn light ${!darkMode ? 'active' : ''}`}
            onClick={() => handleDarkModeToggle(false)}
          >
            <span className="mode-icon">&#9788;</span>
            <span>亮色</span>
          </button>
          <button
            className={`mode-switch-btn dark ${darkMode ? 'active' : ''}`}
            onClick={() => handleDarkModeToggle(true)}
          >
            <span className="mode-icon">&#9790;</span>
            <span>暗色</span>
          </button>
        </div>
      </div>

      <div className="settings-section">
        <h3 className="section-title">主题色</h3>
        <p className="section-desc">选择或输入你喜欢的主题色，会应用到全局 UI。</p>

        <div className="color-presets">
          {PRESET_COLORS.map((c) => (
            <button
              key={c.hex}
              className={`color-swatch ${accentColor.toLowerCase() === c.hex.toLowerCase() ? 'active' : ''}`}
              style={{ backgroundColor: c.hex }}
              onClick={() => handleColorSelect(c.hex)}
              title={`${c.name} (${c.hex})`}
            >
              {accentColor.toLowerCase() === c.hex.toLowerCase() && (
                <span className="swatch-check">&#10003;</span>
              )}
            </button>
          ))}
        </div>

        <div className="custom-color-row">
          <input
            type="text"
            className="hex-input"
            placeholder="#自定义色值"
            value={customHex}
            onChange={(e) => setCustomHex(e.target.value)}
            maxLength={7}
          />
          <button className="btn-apply" onClick={handleCustomHexApply}>应用</button>
          <button className="btn-reset" onClick={handleResetTheme}>恢复默认</button>
        </div>
      </div>

      <div className="settings-section">
        <h3 className="section-title">自定义背景</h3>
        <p className="section-desc">上传图片作为应用背景，支持覆盖/平铺/居中三种模式。</p>

        <div className="bg-controls">
          <label className="btn-upload">
            &#128193; 选择背景图片
            <input
              type="file"
              accept="image/jpeg,image/png,image/gif"
              onChange={handleBgUpload}
              hidden
            />
          </label>

          <div className="bg-mode-group">
            <span className="mode-label">模式：</span>
            {BG_MODES.map((m) => (
              <button
                key={m.value}
                className={`btn-mode ${bgMode === m.value ? 'active' : ''}`}
                onClick={() => handleBgModeChange(m.value)}
              >
                {m.label}
              </button>
            ))}
          </div>

          {hasBg && (
            <button className="btn-reset" onClick={handleResetBg}>
              恢复默认背景
            </button>
          )}
        </div>

        {hasBg && (
          <div className="bg-preview-note">
            当前已设置自定义背景，模式：{BG_MODES.find(m => m.value === bgMode)?.label}
          </div>
        )}
      </div>
    </div>
  )
}

export default Settings
