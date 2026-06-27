import React, { useState, useEffect } from 'react'
import './Assessment.css'

interface Question {
  id: string
  question: string
  options: string[]
  difficulty: string
  topic: string
}

interface AssessmentDetail {
  id: string
  question: string
  user_answer: number
  correct_answer: number
  correct_label: string
  is_correct: boolean
  is_unsure?: boolean
  explanation: string
  difficulty: string
  topic: string
}

interface AssessmentResult {
  score: number
  correct: number
  total: number
  level: string
  advice: string
  details: AssessmentDetail[]
  weak_topics: string[]
}

interface UserProfile {
  level: string
  tags: string[]
  goals: string[]
  time_budget: string
  style: string
  weaknesses: string[]
  strengths: string[]
  summary: string
}

interface KnowledgeMatch {
  id: string
  content: string
  metadata: Record<string, string>
  distance: number
}

interface CustomPlanPhase {
  phase: number
  title: string
  duration: string
  focus: string
  items: string[]
  resources: string[]
}

interface WeeklySchedule {
  sessions_per_week: number
  minutes_per_session: number
  routine: string
}

interface CustomPlan {
  overview: string
  priority_topics: string[]
  phases: CustomPlanPhase[]
  weekly_schedule: WeeklySchedule
  tips: string[]
}

interface AssessmentProps {
  backendPort: number
  language: string
  userId: string
}

const Assessment: React.FC<AssessmentProps> = ({ backendPort, language, userId }) => {
  // 阶段：profile -> answering -> result
  const [phase, setPhase] = useState<'profile' | 'loading' | 'answering' | 'result'>('profile')
  const [questions, setQuestions] = useState<Question[]>([])
  const [answers, setAnswers] = useState<number[]>([])
  const [currentIndex, setCurrentIndex] = useState(0)
  const [result, setResult] = useState<AssessmentResult | null>(null)
  const [error, setError] = useState('')

  // 人物画像状态
  const [profile, setProfile] = useState<UserProfile | null>(null)
  const [customPlan, setCustomPlan] = useState<CustomPlan | null>(null)
  const [profileForm, setProfileForm] = useState({
    experience: '',
    current_level: '',
    goals: '',
    time_per_week: '',
    learning_style: '',
    notes: '',
  })
  const [profileLoading, setProfileLoading] = useState(false)

  const apiBase = `http://127.0.0.1:${backendPort}`

  // ========== 人物画像生成 ==========
  const submitProfile = async () => {
    setProfileLoading(true)
    setError('')
    try {
      const res = await fetch(`${apiBase}/api/assessment/profile`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          ...profileForm,
          languages_known: [],
          target_language: language,
        }),
      })
      if (!res.ok) throw new Error(`HTTP ${res.status}`)
      const data = await res.json()
      setProfile(data.profile)
      // 继续进入答题
      startAssessment()
    } catch (e: any) {
      setError(`画像生成失败：${e.message}`)
      setProfileLoading(false)
    }
  }

  const skipProfile = () => {
    startAssessment()
  }

  // ========== 答题流程 ==========
  const startAssessment = async () => {
    setPhase('loading')
    setError('')
    setProfileLoading(false)
    try {
      const res = await fetch(`${apiBase}/api/assessment/start?user_id=${encodeURIComponent(userId)}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ language }),
      })
      if (!res.ok) throw new Error(`HTTP ${res.status}`)
      const data = await res.json()
      setQuestions(data.questions)
      setAnswers(new Array(data.questions.length).fill(-1))
      setCurrentIndex(0)
      setPhase('answering')
    } catch (e: any) {
      setError(`加载题目失败：${e.message}`)
      setPhase('profile')
    }
  }

  const selectAnswer = (optionIndex: number) => {
    const newAnswers = [...answers]
    newAnswers[currentIndex] = optionIndex
    setAnswers(newAnswers)
  }

  const goNext = () => {
    if (currentIndex < questions.length - 1) {
      setCurrentIndex(currentIndex + 1)
    }
  }

  const goPrev = () => {
    if (currentIndex > 0) {
      setCurrentIndex(currentIndex - 1)
    }
  }

  const submitAssessment = async () => {
    setPhase('loading')
    try {
      const res = await fetch(`${apiBase}/api/assessment/submit?user_id=${encodeURIComponent(userId)}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ language, answers }),
      })
      if (!res.ok) throw new Error(`HTTP ${res.status}`)
      const data = await res.json()
      setResult(data)

      // 如果有画像，获取定制计划
      if (profile) {
        try {
          const planRes = await fetch(`${apiBase}/api/assessment/plan?user_id=${encodeURIComponent(userId)}`)
          if (planRes.ok) {
            const planData = await planRes.json()
            if (planData.plan && !planData.plan.parse_error) {
              setCustomPlan(planData.plan)
            }
          }
        } catch {
          // 计划获取失败不影响评估结果展示
        }
      }

      setPhase('result')
    } catch (e: any) {
      setError(`提交失败：${e.message}`)
      setPhase('answering')
    }
  }

  const unansweredCount = answers.filter(a => a === -1).length
  const answeredCount = answers.filter(a => a !== -1).length
  const allAnswered = unansweredCount === 0

  const diffLabel = (d: string) => {
    const map: Record<string, string> = { easy: '简单', medium: '中等', hard: '困难' }
    return map[d] || d
  }

  const diffClass = (d: string) => `diff-badge diff-${d}`

  const levelColor = (lvl: string) => {
    const map: Record<string, string> = {
      '入门': 'var(--accent-green)',
      '初级': 'var(--accent-blue)',
      '中级': 'var(--accent-orange)',
      '高级': 'var(--accent-red)',
    }
    return map[lvl] || 'var(--accent-blue)'
  }

  // ========== 渲染：人物画像表单 ==========
  if (phase === 'profile') {
    return (
      <div className="assessment-container">
        <div className="profile-form-section">
          <h2>个人背景信息</h2>
          <p className="profile-subtitle">
            填写以下信息，我们将为你生成专属人物画像并定制学习计划
          </p>

          {error && <div className="profile-error">{error}</div>}

          <div className="profile-form">
            <div className="form-group">
              <label>编程经验</label>
              <textarea
                placeholder="例如：自学 Python 3 个月，写过几个小脚本，了解基本语法但面向对象不熟..."
                value={profileForm.experience}
                onChange={e => setProfileForm({ ...profileForm, experience: e.target.value })}
                rows={3}
              />
            </div>

            <div className="form-row">
              <div className="form-group">
                <label>自评水平</label>
                <select
                  value={profileForm.current_level}
                  onChange={e => setProfileForm({ ...profileForm, current_level: e.target.value })}
                >
                  <option value="">请选择</option>
                  <option value="入门">入门（刚接触编程）</option>
                  <option value="初级">初级（能写简单程序）</option>
                  <option value="中级">中级（能独立完成项目）</option>
                  <option value="高级">高级（能设计架构）</option>
                </select>
              </div>
              <div className="form-group">
                <label>偏好学习风格</label>
                <select
                  value={profileForm.learning_style}
                  onChange={e => setProfileForm({ ...profileForm, learning_style: e.target.value })}
                >
                  <option value="">请选择</option>
                  <option value="动手实践型">动手实践型（喜欢写代码）</option>
                  <option value="理论深入型">理论深入型（喜欢理解原理）</option>
                  <option value="项目驱动型">项目驱动型（通过做项目学习）</option>
                  <option value="视频学习型">视频学习型（看教程学习）</option>
                  <option value="阅读文档型">阅读文档型（读官方文档）</option>
                </select>
              </div>
            </div>

            <div className="form-group">
              <label>学习目标</label>
              <textarea
                placeholder="例如：想系统掌握 Python，能独立开发 Web 后端，未来找一份后端开发工作..."
                value={profileForm.goals}
                onChange={e => setProfileForm({ ...profileForm, goals: e.target.value })}
                rows={2}
              />
            </div>

            <div className="form-row">
              <div className="form-group">
                <label>每周可投入时间</label>
                <select
                  value={profileForm.time_per_week}
                  onChange={e => setProfileForm({ ...profileForm, time_per_week: e.target.value })}
                >
                  <option value="">请选择</option>
                  <option value="少于 3 小时">少于 3 小时</option>
                  <option value="3-6 小时">3-6 小时</option>
                  <option value="6-12 小时">6-12 小时</option>
                  <option value="12 小时以上">12 小时以上</option>
                </select>
              </div>
              <div className="form-group">
                <label>目标语言</label>
                <input type="text" value={language} disabled className="input-disabled" />
              </div>
            </div>

            <div className="form-group">
              <label>补充说明（选填）</label>
              <textarea
                placeholder="任何其他想告诉我们的信息：学习痛点、偏好时间段、已掌握的技术栈..."
                value={profileForm.notes}
                onChange={e => setProfileForm({ ...profileForm, notes: e.target.value })}
                rows={2}
              />
            </div>

            <div className="profile-actions">
              <button
                className="btn-primary"
                onClick={submitProfile}
                disabled={profileLoading}
              >
                {profileLoading ? '正在生成画像...' : '生成画像并开始评估'}
              </button>
              <button className="btn-secondary" onClick={skipProfile}>
                跳过，直接开始评估
              </button>
            </div>
          </div>
        </div>
      </div>
    )
  }

  // ========== 加载中 ==========
  if (phase === 'loading') {
    return (
      <div className="assessment-container">
        <div className="assessment-loading">
          <div className="loading-spinner" />
          <p>{profileLoading ? '正在生成人物画像...' : '正在加载评估题目...'}</p>
        </div>
      </div>
    )
  }

  // ========== 答题 ==========
  if (phase === 'answering') {
    const q = questions[currentIndex]
    return (
      <div className="assessment-container">
        <div className="assessment-quiz">
          <div className="quiz-header">
            <h2>基础评估</h2>
            <div className="quiz-progress">
              <span className="progress-text">第 {currentIndex + 1} / {questions.length} 题</span>
              <span className="progress-answered">已答 {answeredCount} 题</span>
              <div className="progress-bar">
                <div
                  className="progress-fill"
                  style={{ width: `${((currentIndex + 1) / questions.length) * 100}%` }}
                />
              </div>
            </div>
            <div className="quiz-meta">
              <span className={diffClass(q.difficulty)}>{diffLabel(q.difficulty)}</span>
              <span className="topic-badge">{q.topic}</span>
            </div>
          </div>

          <div className="quiz-question">
            <pre>{q.question}</pre>
          </div>

          <div className="quiz-options">
            {q.options.map((opt, i) => (
              <button
                key={i}
                className={`option-btn ${i === 4 ? 'option-unsure' : ''} ${answers[currentIndex] === i ? 'selected' : ''}`}
                onClick={() => selectAnswer(i)}
              >
                <span className="option-marker">{opt.trimStart()[0]}</span>
                <span className="option-text">{opt.replace(/^[A-E]\)\s*/, '')}</span>
              </button>
            ))}
          </div>

          <div className="quiz-actions">
            <button
              className="btn-secondary"
              onClick={goPrev}
              disabled={currentIndex === 0}
            >
              上一题
            </button>
            <span className="nav-hint">{currentIndex + 1} / {questions.length}</span>
            {currentIndex < questions.length - 1 ? (
              <button className="btn-primary" onClick={goNext}>
                下一题
              </button>
            ) : (
              <button
                className="btn-primary btn-submit"
                onClick={submitAssessment}
                disabled={!allAnswered}
              >
                {allAnswered ? '提交评估' : `还有 ${unansweredCount} 题未答`}
              </button>
            )}
          </div>
        </div>
      </div>
    )
  }

  // ========== 结果页 ==========
  if (phase === 'result' && result) {
    const scoreColor = result.score >= 80 ? 'var(--accent-green)' :
      result.score >= 60 ? 'var(--accent-blue)' :
        result.score >= 30 ? 'var(--accent-orange)' : 'var(--accent-red)'

    return (
      <div className="assessment-container">
        <div className="assessment-result">
          <div className="result-header">
            <h2>评估结果</h2>
            <button className="btn-secondary btn-sm" onClick={() => { setPhase('profile'); setProfile(null); setCustomPlan(null); }}>
              重新开始
            </button>
          </div>

          {/* 人物画像卡片 */}
          {profile && (
            <div className="profile-card">
              <h3>人物画像</h3>
              <div className="profile-card-body">
                <div className="profile-summary">{profile.summary}</div>
                <div className="profile-meta-grid">
                  <div className="profile-meta-item">
                    <span className="meta-label">水平</span>
                    <span className="meta-value" style={{ color: levelColor(profile.level) }}>
                      {profile.level}
                    </span>
                  </div>
                  <div className="profile-meta-item">
                    <span className="meta-label">学习风格</span>
                    <span className="meta-value">{profile.style}</span>
                  </div>
                  <div className="profile-meta-item">
                    <span className="meta-label">可用时间</span>
                    <span className="meta-value">{profile.time_budget}</span>
                  </div>
                </div>
                {profile.tags && profile.tags.length > 0 && (
                  <div className="profile-tags">
                    {profile.tags.map((t, i) => (
                      <span key={i} className="profile-tag">{t}</span>
                    ))}
                  </div>
                )}
                <div className="profile-detail-row">
                  {profile.goals && profile.goals.length > 0 && (
                    <div className="profile-detail-col">
                      <span className="detail-label">学习目标</span>
                      <ul className="detail-list">
                        {profile.goals.map((g, i) => <li key={i}>{g}</li>)}
                      </ul>
                    </div>
                  )}
                  {profile.weaknesses && profile.weaknesses.length > 0 && (
                    <div className="profile-detail-col">
                      <span className="detail-label">薄弱环节</span>
                      <ul className="detail-list">
                        {profile.weaknesses.map((w, i) => <li key={i}>{w}</li>)}
                      </ul>
                    </div>
                  )}
                  {profile.strengths && profile.strengths.length > 0 && (
                    <div className="profile-detail-col">
                      <span className="detail-label">优势领域</span>
                      <ul className="detail-list">
                        {profile.strengths.map((s, i) => <li key={i}>{s}</li>)}
                      </ul>
                    </div>
                  )}
                </div>
              </div>
            </div>
          )}

          {/* 分数卡片 */}
          <div className="score-card" style={{ borderColor: scoreColor }}>
            <div className="score-ring" style={{ color: scoreColor }}>
              <span className="score-number">{result.score}</span>
              <span className="score-unit">分</span>
            </div>
            <div className="score-info">
              <div className="level-badge" style={{ background: scoreColor }}>
                {result.level}
              </div>
              <p className="score-detail">
                正确 {result.correct}/{result.total} 题
              </p>
            </div>
          </div>

          <div className="advice-box">
            <p>{result.advice}</p>
          </div>

          {/* 个性化学习计划（定制版优先） */}
          {customPlan && (
            <div className="study-plan">
              <h3>个性化学习计划（AI 定制）</h3>
              <p className="plan-overview">{customPlan.overview}</p>

              {customPlan.weekly_schedule && (
                <div className="weekly-schedule">
                  <span className="schedule-icon">&#x1F4C5;</span>
                  <span>
                    建议 {customPlan.weekly_schedule.sessions_per_week} 次/周，
                    每次 {customPlan.weekly_schedule.minutes_per_session} 分钟 - {customPlan.weekly_schedule.routine}
                  </span>
                </div>
              )}

              {customPlan.priority_topics && customPlan.priority_topics.length > 0 && (
                <div className="priority-topics">
                  <span className="detail-label">优先攻克</span>
                  <div className="topic-chips">
                    {customPlan.priority_topics.map((t, i) => (
                      <span key={i} className="topic-chip">{t}</span>
                    ))}
                  </div>
                </div>
              )}

              <div className="plan-timeline">
                {customPlan.phases.map((p, i) => (
                  <div key={i} className="plan-phase">
                    <div className="plan-phase-header">
                      <span className="plan-phase-num">{p.phase}</span>
                      <div>
                        <h4>{p.title}</h4>
                        <span className="plan-duration">{p.duration}</span>
                        {p.focus && <span className="plan-focus"> · {p.focus}</span>}
                      </div>
                    </div>
                    <ul className="plan-items">
                      {p.items.map((item, j) => (
                        <li key={j}>{item}</li>
                      ))}
                    </ul>
                    {p.resources && p.resources.length > 0 && (
                      <div className="plan-resources">
                        <span className="resource-label">推荐资源：</span>
                        {p.resources.map((r, j) => (
                          <span key={j} className="resource-tag">{r}</span>
                        ))}
                      </div>
                    )}
                  </div>
                ))}
              </div>

              {customPlan.tips && customPlan.tips.length > 0 && (
                <div className="plan-tips">
                  <span className="detail-label">学习建议</span>
                  <ul>
                    {customPlan.tips.map((t, i) => <li key={i}>{t}</li>)}
                  </ul>
                </div>
              )}
            </div>
          )}


          {/* 答题详情 */}
          <details className="result-details">
            <summary>查看答题详情</summary>
            <div className="details-list">
              {result.details.map((d, i) => (
                <div key={d.id} className={`detail-item ${d.is_correct ? 'correct' : 'wrong'}`}>
                  <div className="detail-header">
                    <span className="detail-num">{i + 1}.</span>
                    <span className={diffClass(d.difficulty)}>{diffLabel(d.difficulty)}</span>
                    <span className="topic-badge">{d.topic}</span>
                    <span className={`detail-status ${d.is_unsure ? 'status-unsure' : d.is_correct ? 'status-ok' : 'status-fail'}`}>
                      {d.is_unsure ? '不清楚' : d.is_correct ? '正确' : '错误'}
                    </span>
                  </div>
                  <pre className="detail-question">{d.question}</pre>
                  {!d.is_correct && (
                    <div className="detail-fix">
                      <span>正确答案：{d.correct_label}</span>
                      <p>{d.explanation}</p>
                    </div>
                  )}
                </div>
              ))}
            </div>
          </details>
        </div>
      </div>
    )
  }

  return null
}

export default Assessment
