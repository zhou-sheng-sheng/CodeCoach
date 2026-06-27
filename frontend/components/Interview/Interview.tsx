import React, { useState, useEffect, useRef, useCallback } from 'react'
import './Interview.css'

interface InterviewType {
  key: string
  label: string
  description: string
  icon: string
}

interface QuestionData {
  phase: string
  question_index?: number
  total_questions?: number
  question_id?: string
  title?: string
  question?: string
  topics?: string[]
  difficulty?: string
  time_limit?: number
  session_id: string
  follow_up?: string
  follow_up_index?: number
  total_follow_ups?: number
  scores?: ScoreItem[]
}

interface ScoreItem {
  question_id: string
  title: string
  score: number
  comment: string
  strengths: string[]
  weaknesses: string[]
}

interface ReportData {
  phase: string
  session_id: string
  interview_type_label: string
  total_questions: number
  average_score: number
  level: string
  summary: string
  scores: ScoreItem[]
  strengths: string[]
  weaknesses: string[]
  duration_seconds: number
}

interface InterviewProps {
  backendPort: number
  language: string
  userId: string
}

type Phase = 'select' | 'ready' | 'asking' | 'waiting' | 'follow_up' | 'scored' | 'report'

const Interview: React.FC<InterviewProps> = ({ backendPort, language, userId }) => {
  const [phase, setPhase] = useState<Phase>('select')
  const [types, setTypes] = useState<InterviewType[]>([])
  const [selType, setSelType] = useState('algorithm')
  const [sessionId, setSessionId] = useState('')
  const [current, setCurrent] = useState<QuestionData | null>(null)
  const [answer, setAnswer] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const [report, setReport] = useState<ReportData | null>(null)
  const [timeLeft, setTimeLeft] = useState(0)
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null)

  // 加载面试类型
  useEffect(() => {
    fetch(`http://127.0.0.1:${backendPort}/api/interview/types`)
      .then(r => r.json())
      .then(d => setTypes(d.types || []))
      .catch(() => {})
  }, [backendPort])

  // 计时器
  const startTimer = useCallback((seconds: number) => {
    setTimeLeft(seconds)
    if (timerRef.current) clearInterval(timerRef.current)
    timerRef.current = setInterval(() => {
      setTimeLeft(prev => {
        if (prev <= 1) {
          if (timerRef.current) clearInterval(timerRef.current)
          return 0
        }
        return prev - 1
      })
    }, 1000)
  }, [])

  const stopTimer = useCallback(() => {
    if (timerRef.current) {
      clearInterval(timerRef.current)
      timerRef.current = null
    }
  }, [])

  useEffect(() => {
    return () => stopTimer()
  }, [stopTimer])

  const formatTime = (s: number) => {
    const m = Math.floor(s / 60)
    const sec = s % 60
    return `${m}:${sec.toString().padStart(2, '0')}`
  }

  // 开始面试
  const startInterview = async () => {
    setLoading(true)
    setError('')
    try {
      const res = await fetch(`http://127.0.0.1:${backendPort}/api/interview/start`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ interview_type: selType, language, user_id: userId }),
      })
      const data = await res.json()
      if (data.error) { setError(data.error); return }
      setSessionId(data.session_id)
      setCurrent(data)

      if (data.phase === 'asking' && data.time_limit) {
        startTimer(data.time_limit)
        setPhase('waiting')
      }
    } catch (e: any) {
      setError(`启动失败：${e.message}`)
    } finally {
      setLoading(false)
    }
  }

  // 提交回答
  const submitAnswer = async () => {
    if (!answer.trim()) return
    setLoading(true)
    setError('')
    stopTimer()

    try {
      const res = await fetch(`http://127.0.0.1:${backendPort}/api/interview/answer`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ session_id: sessionId, answer }),
      })
      const data = await res.json()
      if (data.error) { setError(data.error); return }

      setAnswer('')

      if (data.phase === 'follow_up') {
        setCurrent(data)
        setPhase('follow_up')
      } else if (data.phase === 'scored') {
        setCurrent(data)
        setPhase('scored')
      } else if (data.phase === 'report') {
        setReport(data)
        setPhase('report')
      }
    } catch (e: any) {
      setError(`提交失败：${e.message}`)
    } finally {
      setLoading(false)
    }
  }

  // 跳过追问
  const skipFollowUps = async () => {
    setLoading(true)
    stopTimer()
    try {
      const res = await fetch(`http://127.0.0.1:${backendPort}/api/interview/skip`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ session_id: sessionId }),
      })
      const data = await res.json()
      if (data.phase === 'scored') {
        setCurrent(data)
        setPhase('scored')
      } else if (data.phase === 'report') {
        setReport(data)
        setPhase('report')
      }
    } catch (e: any) {
      setError(`操作失败：${e.message}`)
    } finally {
      setLoading(false)
    }
  }

  // 下一题
  const nextQuestion = async () => {
    setLoading(true)
    try {
      const res = await fetch(`http://127.0.0.1:${backendPort}/api/interview/next`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ session_id: sessionId }),
      })
      const data = await res.json()
      if (data.phase === 'asking') {
        setCurrent(data)
        if (data.time_limit) startTimer(data.time_limit)
        setPhase('waiting')
      } else if (data.phase === 'report') {
        setReport(data)
        setPhase('report')
      }
    } catch (e: any) {
      setError(`操作失败：${e.message}`)
    } finally {
      setLoading(false)
    }
  }

  // 重新开始
  const reset = () => {
    stopTimer()
    setPhase('select')
    setCurrent(null)
    setReport(null)
    setAnswer('')
    setSessionId('')
    setError('')
  }

  const diffLabel = (d: string) => {
    const map: Record<string, string> = { easy: '简单', medium: '中等', hard: '困难' }
    return map[d] || d
  }

  const diffClass = (d: string) => `diff-badge diff-${d}`

  // ── 选择面试类型 ──
  if (phase === 'select') {
    return (
      <div className="interview-container">
        <div className="interview-select">
          <h2>模拟面试</h2>
          <p className="select-desc">选择面试类型，AI 模拟真实面试场景</p>

          {error && <div className="select-error">{error}</div>}

          <div className="interview-type-cards">
            {types.map(t => (
              <button
                key={t.key}
                className={`type-card ${selType === t.key ? 'active' : ''}`}
                onClick={() => setSelType(t.key)}
              >
                <div className="type-icon">
                  {t.icon === 'code' && <span>&#128187;</span>}
                  {t.icon === 'architecture' && <span>&#127959;</span>}
                  {t.icon === 'people' && <span>&#128101;</span>}
                </div>
                <div className="type-info">
                  <h3>{t.label}</h3>
                  <p>{t.description}</p>
                </div>
              </button>
            ))}
          </div>

          <button
            className="btn-primary btn-start"
            onClick={startInterview}
            disabled={loading}
          >
            {loading ? '准备中...' : '开始面试'}
          </button>
        </div>
      </div>
    )
  }

  // ── 答题中 ──
  if ((phase === 'waiting' || phase === 'follow_up') && current) {
    const isFollowUp = phase === 'follow_up'

    return (
      <div className="interview-container">
        <div className="interview-room">
          <div className="room-header">
            <div className="room-meta">
              <h2>{isFollowUp ? '追问' : `第 ${current.question_index} / ${current.total_questions} 题`}</h2>
              {!isFollowUp && current.topics && (
                <div className="room-tags">
                  {current.topics.map((t: string) => (
                    <span key={t} className="topic-tag">{t}</span>
                  ))}
                  {current.difficulty && (
                    <span className={diffClass(current.difficulty)}>{diffLabel(current.difficulty)}</span>
                  )}
                </div>
              )}
            </div>
            {!isFollowUp && (
              <div className={`room-timer ${timeLeft < 60 ? 'timer-warn' : ''}`}>
                {formatTime(timeLeft)}
              </div>
            )}
          </div>

          <div className="room-question">
            <div className="question-label">
              {isFollowUp ? '面试官追问' : current.title ? `${current.title}` : '面试题目'}
            </div>
            <pre className="question-text">
              {isFollowUp ? current.follow_up : current.question}
            </pre>
          </div>

          {isFollowUp && (
            <div className="follow-up-hint">
              追问 {current.follow_up_index}/{current.total_follow_ups}
            </div>
          )}

          <div className="room-answer">
            <textarea
              className="answer-input"
              placeholder={isFollowUp
                ? '输入你的回答...'
                : '在此作答（输入代码或文字描述）...'
              }
              value={answer}
              onChange={e => setAnswer(e.target.value)}
              rows={10}
              disabled={loading}
            />
          </div>

          <div className="room-actions">
            <button
              className="btn-primary"
              onClick={submitAnswer}
              disabled={loading || !answer.trim()}
            >
              {loading ? '提交中...' : '提交回答'}
            </button>
            {isFollowUp && (
              <button
                className="btn-secondary"
                onClick={skipFollowUps}
                disabled={loading}
              >
                跳过追问
              </button>
            )}
          </div>
        </div>
      </div>
    )
  }

  // ── 评分展示 ──
  if (phase === 'scored' && current) {
    const scores = current.scores || []
    const lastScore = scores[scores.length - 1]

    return (
      <div className="interview-container">
        <div className="interview-scored">
          <h2>本题评分</h2>

          {lastScore && (
            <div className="scored-card">
              <div className="scored-ring" style={{
                color: lastScore.score >= 80 ? 'var(--accent-green)'
                  : lastScore.score >= 60 ? 'var(--accent-blue)'
                  : 'var(--accent-red)'
              }}>
                <span className="scored-number">{lastScore.score}</span>
                <span className="scored-unit">分</span>
              </div>
              <div className="scored-info">
                <p className="scored-comment">{lastScore.comment}</p>
                {lastScore.strengths && lastScore.strengths.length > 0 && (
                  <div className="scored-strengths">
                    <span className="label-positive">优点</span>
                    {lastScore.strengths.map((s: string) => (
                      <span key={s} className="chip-positive">{s}</span>
                    ))}
                  </div>
                )}
                {lastScore.weaknesses && lastScore.weaknesses.length > 0 && (
                  <div className="scored-weaknesses">
                    <span className="label-negative">待改进</span>
                    {lastScore.weaknesses.map((w: string) => (
                      <span key={w} className="chip-negative">{w}</span>
                    ))}
                  </div>
                )}
              </div>
            </div>
          )}

          <button
            className="btn-primary"
            onClick={nextQuestion}
            disabled={loading}
          >
            {loading ? '加载中...' : '下一题'}
          </button>
        </div>
      </div>
    )
  }

  // ── 面试报告 ──
  if (phase === 'report' && report) {
    const avgColor = report.average_score >= 80 ? 'var(--accent-green)'
      : report.average_score >= 60 ? 'var(--accent-blue)'
      : 'var(--accent-red)'

    return (
      <div className="interview-container">
        <div className="interview-report">
          <div className="report-header">
            <h2>面试报告</h2>
            <span className="report-type">{report.interview_type_label}</span>
          </div>

          <div className="report-summary-card" style={{ borderColor: avgColor }}>
            <div className="report-score-ring" style={{ color: avgColor }}>
              <span className="report-score-num">{report.average_score}</span>
              <span className="report-score-label">平均分</span>
            </div>
            <div className="report-summary-info">
              <h3>评级：{report.level}</h3>
              <p>{report.summary}</p>
              <div className="report-meta">
                <span>共 {report.total_questions} 题</span>
                <span>耗时 {Math.floor(report.duration_seconds / 60)} 分钟</span>
              </div>
            </div>
          </div>

          {/* 优劣分析 */}
          {(report.strengths.length > 0 || report.weaknesses.length > 0) && (
            <div className="report-analysis">
              {report.strengths.length > 0 && (
                <div className="analysis-block">
                  <h4>优势</h4>
                  <div className="analysis-chips">
                    {report.strengths.map(s => <span key={s} className="chip-positive">{s}</span>)}
                  </div>
                </div>
              )}
              {report.weaknesses.length > 0 && (
                <div className="analysis-block">
                  <h4>待改进</h4>
                  <div className="analysis-chips">
                    {report.weaknesses.map(w => <span key={w} className="chip-negative">{w}</span>)}
                  </div>
                </div>
              )}
            </div>
          )}

          {/* 各题评分详情 */}
          <div className="report-details">
            <h3>各题评分详情</h3>
            {report.scores.map((s, i) => (
              <div key={s.question_id} className="detail-card">
                <div className="detail-header">
                  <span className="detail-num">第 {i + 1} 题</span>
                  <span className="detail-title">{s.title}</span>
                  <span className="detail-score" style={{ color: s.score >= 80 ? 'var(--accent-green)' : s.score >= 60 ? 'var(--accent-blue)' : 'var(--accent-red)' }}>
                    {s.score} 分
                  </span>
                </div>
                <p className="detail-comment">{s.comment}</p>
              </div>
            ))}
          </div>

          <button className="btn-primary" onClick={reset}>
            再来一次
          </button>
        </div>
      </div>
    )
  }

  return null
}

export default Interview
