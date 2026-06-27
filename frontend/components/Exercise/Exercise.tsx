import React, { useState } from 'react'
import './Exercise.css'

interface ExerciseQuestion {
  id: string
  question: string
  options: string[]
  difficulty: string
  topic: string
  concept?: string
}

interface ExerciseDetail {
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

interface ExerciseResult {
  score: number
  correct: number
  total: number
  details: ExerciseDetail[]
  difficulty_stats: Record<string, { total: number; correct: number }>
  topic_stats: Record<string, { total: number; correct: number }>
}

interface ExerciseProps {
  backendPort: number
  language: string
  userId: string
}

const TOPICS = [
  '全部', '数据类型', '控制流', '函数', '列表操作', '字典操作',
  '字符串', '面向对象', '异常处理', '文件IO', '装饰器', '生成器',
  'GIL/并发', '常用库',
]

const DIFFICULTIES = [
  { value: 'all', label: '全部' },
  { value: 'easy', label: '简单' },
  { value: 'medium', label: '中等' },
  { value: 'hard', label: '困难' },
]

type Phase = 'selecting' | 'answering' | 'result'

const Exercise: React.FC<ExerciseProps> = ({ backendPort, language, userId }) => {
  const [phase, setPhase] = useState<Phase>('selecting')
  const [questions, setQuestions] = useState<ExerciseQuestion[]>([])
  const [answers, setAnswers] = useState<number[]>([])
  const [currentIndex, setCurrentIndex] = useState(0)
  const [result, setResult] = useState<ExerciseResult | null>(null)
  const [error, setError] = useState('')

  // 选题参数
  const [selTopic, setSelTopic] = useState('全部')
  const [selDifficulty, setSelDifficulty] = useState('all')
  const [selCountInput, setSelCountInput] = useState('10')
  const [loading, setLoading] = useState(false)
  const [showConcept, setShowConcept] = useState(false)

  // ===== 阶段1：选题 =====
  const startExercise = async () => {
    setLoading(true)
    setError('')
    try {
      const count = Math.max(1, Math.min(50, parseInt(selCountInput) || 10))
      const body: any = { language, count }
      if (selTopic !== '全部') body.topic = selTopic
      if (selDifficulty !== 'all') body.difficulty = selDifficulty

      const res = await fetch(`http://127.0.0.1:${backendPort}/api/exercises/start`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body),
      })
      if (!res.ok) throw new Error(`HTTP ${res.status}`)
      const data = await res.json()
      setQuestions(data.questions)
      setAnswers(new Array(data.questions.length).fill(-1))
      setCurrentIndex(0)
      setPhase('answering')
    } catch (e: any) {
      setError(`加载题目失败：${e.message}`)
    } finally {
      setLoading(false)
    }
  }

  // ===== 阶段2：答题 =====
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

  const submitExercise = async () => {
    setLoading(true)
    try {
      const answersDict: Record<string, number> = {}
      questions.forEach((q, i) => {
        if (answers[i] !== -1) {
          answersDict[q.id] = answers[i]
        }
      })
      const res = await fetch(`http://127.0.0.1:${backendPort}/api/exercises/submit`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ language, answers: answersDict, user_id: userId }),
      })
      if (!res.ok) throw new Error(`HTTP ${res.status}`)
      const data = await res.json()
      setResult(data)
      setPhase('result')
    } catch (e: any) {
      setError(`提交失败：${e.message}`)
    } finally {
      setLoading(false)
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

  // ===== 阶段1 渲染：选题 =====
  if (phase === 'selecting') {
    return (
      <div className="exercise-container">
        <div className="exercise-select">
          <h2>习题练习</h2>
          <p className="select-desc">选择题量和范围，开始针对性练习</p>

          {error && <div className="select-error">{error}</div>}

          <div className="select-group">
            <label>主题筛选</label>
            <div className="topic-grid">
              {TOPICS.map(t => (
                <button
                  key={t}
                  className={`topic-chip ${selTopic === t ? 'active' : ''}`}
                  onClick={() => setSelTopic(t)}
                >
                  {t}
                </button>
              ))}
            </div>
          </div>

          <div className="select-group">
            <label>难度筛选</label>
            <div className="diff-btn-group">
              {DIFFICULTIES.map(d => (
                <button
                  key={d.value}
                  className={`diff-btn ${selDifficulty === d.value ? 'active' : ''}`}
                  onClick={() => setSelDifficulty(d.value)}
                >
                  {d.label}
                </button>
              ))}
            </div>
          </div>

          <div className="select-group">
            <label>题量</label>
            <div className="count-group">
              <input
                type="number"
                className="count-input"
                min={1}
                max={50}
                value={selCountInput}
                onChange={e => setSelCountInput(e.target.value)}
                onBlur={() => {
                  const v = parseInt(selCountInput)
                  if (!selCountInput || v < 1) setSelCountInput('1')
                  else if (v > 50) setSelCountInput('50')
                }}
              />
              <span className="count-unit">题</span>
            </div>
          </div>

          <button
            className="btn-primary btn-start"
            onClick={startExercise}
            disabled={loading}
          >
            {loading ? '加载中...' : '开始练习'}
          </button>
        </div>
      </div>
    )
  }

  if (loading && phase === 'answering') {
    return (
      <div className="exercise-container">
        <div className="exercise-loading">
          <div className="loading-spinner" />
          <p>正在加载题目...</p>
        </div>
      </div>
    )
  }

  // ===== 阶段2 渲染：答题 =====
  if (phase === 'answering') {
    const q = questions[currentIndex]
    return (
      <div className="exercise-container">
        <div className="exercise-quiz">
          <div className="quiz-header">
            <h2>习题练习</h2>
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
              {q.concept && (
                <button
                  className={`concept-toggle ${showConcept ? 'active' : ''}`}
                  onClick={() => setShowConcept(!showConcept)}
                  title="查看概念解释"
                >
                  {showConcept ? '隐藏概念' : '查看概念'}
                </button>
              )}
            </div>
            {showConcept && q.concept && (
              <div className="concept-panel">
                <div className="concept-label">{q.topic} 是什么？</div>
                <p className="concept-text">{q.concept}</p>
              </div>
            )}
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
                onClick={submitExercise}
                disabled={!allAnswered}
              >
                {allAnswered ? '提交练习' : `还有 ${unansweredCount} 题未答`}
              </button>
            )}
          </div>
        </div>
      </div>
    )
  }

  // ===== 阶段3 渲染：结果 =====
  if (phase === 'result' && result) {
    const scoreColor = result.score >= 80 ? 'var(--accent-green)' :
      result.score >= 60 ? 'var(--accent-blue)' :
        result.score >= 30 ? 'var(--accent-orange)' : 'var(--accent-red)'

    const diffOrder = ['easy', 'medium', 'hard']
    const diffLabelMap: Record<string, string> = { easy: '简单', medium: '中等', hard: '困难' }

    return (
      <div className="exercise-container">
        <div className="exercise-result">
          <div className="result-header">
            <h2>练习结果</h2>
            <div className="result-header-actions">
              <button className="btn-secondary btn-sm" onClick={() => { setPhase('selecting'); setResult(null) }}>返回选题</button>
              <button className="btn-primary btn-sm" onClick={startExercise}>再来一组</button>
            </div>
          </div>

          {/* 分数卡片 */}
          <div className="score-card" style={{ borderColor: scoreColor }}>
            <div className="score-ring" style={{ color: scoreColor }}>
              <span className="score-number">{result.score}</span>
              <span className="score-unit">分</span>
            </div>
            <div className="score-info">
              <p className="score-detail">
                正确 {result.correct}/{result.total} 题
              </p>
            </div>
          </div>

          {/* 按难度统计 */}
          {Object.keys(result.difficulty_stats).length > 0 && (
            <div className="stats-section">
              <h3>按难度统计</h3>
              <div className="stats-grid">
                {diffOrder.map(diff => {
                  const s = result.difficulty_stats[diff]
                  if (!s) return null
                  const pct = s.total > 0 ? Math.round(s.correct / s.total * 100) : 0
                  return (
                    <div key={diff} className="stat-item">
                      <span className={`diff-badge diff-${diff}`}>{diffLabelMap[diff] || diff}</span>
                      <span className="stat-bar-wrap">
                        <span className="stat-bar" style={{ width: `${pct}%`, background: diff === 'easy' ? 'var(--accent-green)' : diff === 'medium' ? 'var(--accent-orange)' : 'var(--accent-red)' }} />
                      </span>
                      <span className="stat-num">{s.correct}/{s.total}</span>
                    </div>
                  )
                })}
              </div>
            </div>
          )}

          {/* 按主题统计 */}
          {Object.keys(result.topic_stats).length > 0 && (
            <div className="stats-section">
              <h3>按主题统计</h3>
              <div className="stats-grid">
                {Object.entries(result.topic_stats).map(([topic, s]) => {
                  const pct = s.total > 0 ? Math.round(s.correct / s.total * 100) : 0
                  const barColor = pct >= 80 ? 'var(--accent-green)' : pct >= 50 ? 'var(--accent-orange)' : 'var(--accent-red)'
                  return (
                    <div key={topic} className="stat-item">
                      <span className="stat-topic-label">{topic}</span>
                      <span className="stat-bar-wrap">
                        <span className="stat-bar" style={{ width: `${pct}%`, background: barColor }} />
                      </span>
                      <span className="stat-num">{s.correct}/{s.total}</span>
                    </div>
                  )
                })}
              </div>
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
                  {!d.is_correct && !d.is_unsure && (
                    <div className="detail-fix">
                      <span>正确答案：{d.correct_label}</span>
                      <p>{d.explanation}</p>
                    </div>
                  )}
                  {d.is_unsure && (
                    <div className="detail-fix detail-unsure">
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

export default Exercise
