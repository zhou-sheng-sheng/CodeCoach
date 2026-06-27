import React, { useState, useEffect } from 'react'
import './StudyPlan.css'

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

interface PlanPhase {
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

interface PlanData {
  overview: string
  priority_topics: string[]
  phases: PlanPhase[]
  weekly_schedule: WeeklySchedule
  tips: string[]
}

interface StudyPlanProps {
  backendPort: number
  language: string
  userId: string
}

type ViewMode = 'loading' | 'no_assessment' | 'assessing' | 'plan'

const StudyPlan: React.FC<StudyPlanProps> = ({ backendPort, language, userId }) => {
  const [mode, setMode] = useState<ViewMode>('loading')
  const [result, setResult] = useState<AssessmentResult | null>(null)
  const [planData, setPlanData] = useState<PlanData | null>(null)
  const [questions, setQuestions] = useState<Question[]>([])
  const [answers, setAnswers] = useState<number[]>([])
  const [currentIndex, setCurrentIndex] = useState(0)
  const [error, setError] = useState('')

  // 组件挂载或语言切换时检查是否有评估结果
  useEffect(() => {
    checkLatestAssessment()
  }, [language])

  const checkLatestAssessment = async () => {
    setMode('loading')
    setError('')
    setPlanData(null)
    try {
      // 并行请求：评估结果 + 学习计划
      const [latestRes, planRes] = await Promise.all([
        fetch(`http://127.0.0.1:${backendPort}/api/assessment/latest?language=${language}&user_id=${encodeURIComponent(userId)}`),
        fetch(`http://127.0.0.1:${backendPort}/api/assessment/plan?language=${language}&user_id=${encodeURIComponent(userId)}`).catch(() => null)
      ])

      if (!latestRes.ok) throw new Error(`HTTP ${latestRes.status}`)
      const latestData = await latestRes.json()
      if (latestData.status === 'not_taken') {
        setMode('no_assessment')
        return
      }

      setResult(latestData)
      setMode('plan')

      // 解析学习计划（可能因无画像而不可用）
      if (planRes && planRes instanceof Response && planRes.ok) {
        const planJson = await planRes.json()
        if (planJson.plan && typeof planJson.plan === 'object' && planJson.plan.phases) {
          setPlanData(planJson.plan as PlanData)
        }
      }
    } catch (e: any) {
      setError(`加载失败：${e.message}`)
      setMode('no_assessment')
    }
  }

  const startAssessment = async () => {
    setMode('loading')
    setError('')
    try {
      const res = await fetch(`http://127.0.0.1:${backendPort}/api/assessment/start?language=${encodeURIComponent(language)}&user_id=${encodeURIComponent(userId)}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ language })
      })
      if (!res.ok) throw new Error(`HTTP ${res.status}`)
      const data = await res.json()
      setQuestions(data.questions)
      setAnswers(new Array(data.questions.length).fill(-1))
      setCurrentIndex(0)
      setMode('assessing')
    } catch (e: any) {
      setError(`加载题目失败：${e.message}`)
      setMode('no_assessment')
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
    setMode('loading')
    try {
      const res = await fetch(`http://127.0.0.1:${backendPort}/api/assessment/submit`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ language, answers, user_id: userId })
      })
      if (!res.ok) throw new Error(`HTTP ${res.status}`)
      const data = await res.json()
      setResult(data)
      setMode('plan')
    } catch (e: any) {
      setError(`提交失败：${e.message}`)
      setMode('assessing')
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

  // ============ 加载中 ============
  if (mode === 'loading') {
    return (
      <div className="studyplan-container">
        <div className="studyplan-loading">
          <div className="loading-spinner" />
          <p>正在加载...</p>
        </div>
      </div>
    )
  }

  // ============ 模式1: 未评估 → 提示卡片 ============
  if (mode === 'no_assessment') {
    return (
      <div className="studyplan-container">
        <div className="studyplan-hint">
          <div className="hint-card">
            <div className="hint-icon">
              <svg width="48" height="48" viewBox="0 0 48 48" fill="none">
                <rect x="4" y="4" width="40" height="40" rx="8" stroke="#a371f7" strokeWidth="2" fill="none" />
                <circle cx="18" cy="18" r="4" stroke="#a371f7" strokeWidth="2" fill="none" />
                <path d="M30 18h8M34 14v8" stroke="#a371f7" strokeWidth="2" strokeLinecap="round" />
                <path d="M6 38l10-12 8 6 10-12 8 18H6z" stroke="#a371f7" strokeWidth="2" fill="none" />
                <circle cx="14" cy="34" r="2" fill="#a371f7" />
                <circle cx="34" cy="26" r="2" fill="#a371f7" />
              </svg>
            </div>
            <h2>请先完成基础评估</h2>
            <p className="hint-desc">
              完成基础评估后，系统将根据你的水平生成个性化学习计划
            </p>
            <button className="btn-start-assessment" onClick={startAssessment}>
              开始评估
            </button>
            {error && <p className="hint-error">{error}</p>}
          </div>
        </div>
      </div>
    )
  }

  // ============ 模式2: 评估中 → 答题界面 ============
  if (mode === 'assessing' && questions.length > 0) {
    const q = questions[currentIndex]
    return (
      <div className="studyplan-container">
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
          {error && <p className="quiz-error">{error}</p>}
        </div>
      </div>
    )
  }

  // ============ 模式3: 显示学习计划 ============
  if (mode === 'plan' && result) {
    const scoreColor = result.score >= 80 ? 'var(--accent-green)' :
      result.score >= 60 ? 'var(--accent-blue)' :
        'var(--accent-orange)'

    return (
      <div className="studyplan-container">
        <div className="studyplan-result">
          <div className="result-header">
            <h2>学习计划</h2>
          </div>

          {/* 评估概况 */}
          <div className="score-card" style={{ borderColor: scoreColor }}>
            <div className="score-ring" style={{ color: scoreColor }}>
              <span className="score-number">{result.score}</span>
              <span className="score-unit">分</span>
            </div>
            <div className="score-info">
              <div className="level-badge" style={{ background: scoreColor }}>
                {result.level}
              </div>
              <p className="score-detail">正确 {result.correct}/{result.total} 题</p>
            </div>
          </div>

          <div className="advice-box">
            <p>{result.advice}</p>
          </div>

          {/* 个性化学习计划 */}
          {planData && (
            <div className="plan-sections">
              {/* 计划概述 */}
              {planData.overview && (
                <div className="plan-section">
                  <h3 className="plan-section-title">计划概述</h3>
                  <p className="plan-overview-text">{planData.overview}</p>
                </div>
              )}

              {/* 重点主题 */}
              {planData.priority_topics && planData.priority_topics.length > 0 && (
                <div className="plan-section">
                  <h3 className="plan-section-title">优先攻克</h3>
                  <div className="topic-tags">
                    {planData.priority_topics.map((t, i) => (
                      <span key={i} className="priority-tag">{t}</span>
                    ))}
                  </div>
                </div>
              )}

              {/* 阶段计划 */}
              {planData.phases && planData.phases.length > 0 && (
                <div className="plan-section">
                  <h3 className="plan-section-title">阶段计划</h3>
                  <div className="phases-list">
                    {planData.phases.map((phase) => (
                      <div key={phase.phase} className="phase-card">
                        <div className="phase-header">
                          <span className="phase-number">阶段 {phase.phase}</span>
                          <span className="phase-title">{phase.title}</span>
                          <span className="phase-duration">{phase.duration}</span>
                        </div>
                        <p className="phase-focus">{phase.focus}</p>
                        {phase.items && phase.items.length > 0 && (
                          <ul className="phase-items">
                            {phase.items.map((item, i) => (
                              <li key={i}>{item}</li>
                            ))}
                          </ul>
                        )}
                        {phase.resources && phase.resources.length > 0 && (
                          <div className="phase-resources">
                            <span className="resources-label">推荐资源：</span>
                            {phase.resources.map((r, i) => (
                              <span key={i} className="resource-tag">{r}</span>
                            ))}
                          </div>
                        )}
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* 每周安排 */}
              {planData.weekly_schedule && (
                <div className="plan-section">
                  <h3 className="plan-section-title">学习节奏</h3>
                  <div className="schedule-card">
                    <div className="schedule-stats">
                      <div className="schedule-stat">
                        <span className="stat-value">{planData.weekly_schedule.sessions_per_week}</span>
                        <span className="stat-label">次/周</span>
                      </div>
                      <div className="schedule-stat">
                        <span className="stat-value">{planData.weekly_schedule.minutes_per_session}</span>
                        <span className="stat-label">分钟/次</span>
                      </div>
                    </div>
                    {planData.weekly_schedule.routine && (
                      <p className="schedule-routine">{planData.weekly_schedule.routine}</p>
                    )}
                  </div>
                </div>
              )}

              {/* 学习建议 */}
              {planData.tips && planData.tips.length > 0 && (
                <div className="plan-section">
                  <h3 className="plan-section-title">学习建议</h3>
                  <ul className="tips-list">
                    {planData.tips.map((tip, i) => (
                      <li key={i} className="tip-item">{tip}</li>
                    ))}
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

export default StudyPlan
