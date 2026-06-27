import React, { useState, useEffect } from 'react'
import './Learn.css'

// ===== 类型定义 =====

interface KeyPoint {
  key_points: string[]
}

interface LessonSummary {
  id: string
  title: string
  topic: string
  key_points: string[]
}

interface TopicGroup {
  topic: string
  topic_concept: string
  lessons: LessonSummary[]
}

interface LearningPathData {
  topics: TopicGroup[]
}

interface LessonDetail {
  id: string
  title: string
  topic: string
  content: string
  examples: string[]
  key_points: string[]
}

interface LessonData {
  lesson: LessonDetail
}

// 复用 Exercise 的题目类型
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

// ===== 组件接口 =====

interface LearnProps {
  backendPort: number
  language: string
}

// ===== 阶段类型 =====

type Phase = 'path' | 'learning' | 'exercising' | 'result'

const Learn: React.FC<LearnProps> = ({ backendPort, language }) => {
  const [phase, setPhase] = useState<Phase>('path')

  // 学习路径数据
  const [topics, setTopics] = useState<TopicGroup[]>([])
  const [expandedTopic, setExpandedTopic] = useState<string | null>(null)
  const [pathLoading, setPathLoading] = useState(true)
  const [pathError, setPathError] = useState('')

  // 当前知识点
  const [currentLesson, setCurrentLesson] = useState<LessonDetail | null>(null)

  // 练习题数据（复用 Exercise 的交互逻辑）
  const [questions, setQuestions] = useState<ExerciseQuestion[]>([])
  const [answers, setAnswers] = useState<number[]>([])
  const [currentIndex, setCurrentIndex] = useState(0)
  const [result, setResult] = useState<ExerciseResult | null>(null)
  const [exerciseLoading, setExerciseLoading] = useState(false)
  const [exerciseError, setExerciseError] = useState('')

  const [showConcept, setShowConcept] = useState(false)

  // ===== 加载学习路径 =====
  useEffect(() => {
    const fetchPath = async () => {
      try {
        const res = await fetch(`http://127.0.0.1:${backendPort}/api/learn/path?language=${language}`)
        if (!res.ok) throw new Error(`HTTP ${res.status}`)
        const data: LearningPathData = await res.json()
        setTopics(data.topics)
        if (data.topics.length > 0) {
          setExpandedTopic(data.topics[0].topic)
        }
      } catch (e: any) {
        setPathError(`加载学习路径失败：${e.message}`)
      } finally {
        setPathLoading(false)
      }
    }
    fetchPath()
  }, [backendPort, language])

  // ===== 选择知识点 =====
  const selectLesson = async (lessonId: string) => {
    try {
      const res = await fetch(`http://127.0.0.1:${backendPort}/api/learn/lesson/${lessonId}?language=${language}`)
      if (!res.ok) throw new Error(`HTTP ${res.status}`)
      const data: LessonData = await res.json()
      setCurrentLesson(data.lesson)
      setPhase('learning')
    } catch (e: any) {
      setPathError(`加载知识点失败: ${e.message}`)
    }
  }

  // ===== 开始练习 =====
  const startExercises = async () => {
    if (!currentLesson) return
    setExerciseLoading(true)
    setExerciseError('')
    try {
      const res = await fetch(
        `http://127.0.0.1:${backendPort}/api/learn/exercises/${currentLesson.id}`,
        {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ count: 5, language }),
        }
      )
      if (!res.ok) throw new Error(`HTTP ${res.status}`)
      const data = await res.json()
      if (data.questions.length === 0) {
        setExerciseError('该知识点暂无相关练习题')
        return
      }
      setQuestions(data.questions)
      setAnswers(new Array(data.questions.length).fill(-1))
      setCurrentIndex(0)
      setResult(null)
      setPhase('exercising')
    } catch (e: any) {
      setExerciseError(`加载题目失败：${e.message}`)
    } finally {
      setExerciseLoading(false)
    }
  }

  // ===== 答题逻辑 =====
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
    setExerciseLoading(true)
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
        body: JSON.stringify({ language, answers: answersDict }),
      })
      if (!res.ok) throw new Error(`HTTP ${res.status}`)
      const data: ExerciseResult = await res.json()
      setResult(data)
      setPhase('result')
    } catch (e: any) {
      setExerciseError(`提交失败：${e.message}`)
    } finally {
      setExerciseLoading(false)
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

  // ===== 返回学习路径 =====
  const backToPath = () => {
    setCurrentLesson(null)
    setQuestions([])
    setAnswers([])
    setResult(null)
    setPhase('path')
  }

  // ===== 阶段1：学习路径总览 =====
  if (phase === 'path') {
    if (pathLoading) {
      return (
        <div className="learn-container">
          <div className="learn-loading">
            <div className="loading-spinner" />
            <p>正在加载学习路径...</p>
          </div>
        </div>
      )
    }

    return (
      <div className="learn-container">
        <div className="learn-path">
          <h2 className="learn-title">学习板块</h2>
          <p className="learn-subtitle">先学后练，按主题系统掌握 Python 核心知识</p>

          {pathError && <div className="learn-error">{pathError}</div>}

          <div className="learn-layout">
            {/* 左侧：主题列表 */}
            <aside className="learn-topics-sidebar">
              <h3>主题</h3>
              <div className="topic-list">
                {topics.map(tg => (
                  <button
                    key={tg.topic}
                    className={`topic-btn ${expandedTopic === tg.topic ? 'active' : ''}`}
                    onClick={() => setExpandedTopic(expandedTopic === tg.topic ? null : tg.topic)}
                  >
                    <span className="topic-btn-name">{tg.topic}</span>
                    <span className="topic-btn-count">{tg.lessons.length} 节</span>
                  </button>
                ))}
              </div>
            </aside>

            {/* 右侧：知识点列表 */}
            <main className="learn-lessons-area">
              {expandedTopic && (() => {
                const active = topics.find(t => t.topic === expandedTopic)
                if (!active) return null
                return (
                  <div className="lessons-topic-group">
                    <div className="lesson-topic-header">
                      <h3>{active.topic}</h3>
                    </div>
                    <div className="topic-concept-card">
                      <div className="concept-label">本主题概览</div>
                      <p className="concept-text">{active.topic_concept}</p>
                    </div>
                    <div className="lessons-grid">
                      {active.lessons.map(les => (
                        <button
                          key={les.id}
                          className="lesson-card"
                          onClick={() => selectLesson(les.id)}
                        >
                          <div className="lesson-card-header">
                            <span className="lesson-card-title">{les.title}</span>
                          </div>
                          <div className="lesson-card-points">
                            {les.key_points.map((kp, i) => (
                              <span key={i} className="kp-tag">{kp}</span>
                            ))}
                          </div>
                        </button>
                      ))}
                    </div>
                  </div>
                )
              })()}
              {!expandedTopic && (
                <div className="lessons-empty">
                  <p>请从左侧选择一个主题开始学习</p>
                </div>
              )}
            </main>
          </div>
        </div>
      </div>
    )
  }

  // ===== 阶段2：知识点学习 =====
  if (phase === 'learning' && currentLesson) {
    return (
      <div className="learn-container">
        <div className="learn-detail">
          {/* 顶部导航 */}
          <div className="learn-detail-nav">
            <button className="btn-text" onClick={backToPath}>
              &larr; 返回学习路径
            </button>
            <span className="topic-badge">{currentLesson.topic}</span>
          </div>

          <h2 className="learn-detail-title">{currentLesson.title}</h2>

          {/* 内容区 */}
          <div className="content-section">
            <pre className="content-text">{currentLesson.content}</pre>
          </div>

          {/* 代码示例 */}
          <div className="examples-section">
            <h3>代码示例</h3>
            {currentLesson.examples.map((ex, i) => (
              <div key={i} className="code-block">
                <div className="code-block-header">示例 {i + 1}</div>
                <pre className="code-content"><code>{ex}</code></pre>
              </div>
            ))}
          </div>

          {/* 关键要点 */}
          <div className="keypoints-section">
            <h3>关键要点</h3>
            <ul className="keypoints-list">
              {currentLesson.key_points.map((kp, i) => (
                <li key={i} className="keypoint-item">{kp}</li>
              ))}
            </ul>
          </div>

          {/* 底部操作 */}
          <div className="learn-detail-actions">
            <button className="btn-secondary" onClick={backToPath}>返回学习路径</button>
            <button
              className="btn-primary"
              onClick={startExercises}
              disabled={exerciseLoading}
            >
              {exerciseLoading ? '加载中...' : '开始练习'}
            </button>
          </div>
          {exerciseError && <div className="learn-error">{exerciseError}</div>}
        </div>
      </div>
    )
  }

  // ===== 阶段3：练习题答题 =====
  if (phase === 'exercising') {
    const q = questions[currentIndex]
    return (
      <div className="learn-container">
        <div className="learn-exercise">
          <div className="learn-detail-nav">
            <button className="btn-text" onClick={backToPath}>
              &larr; 返回学习路径
            </button>
            <span className="topic-badge">
              {currentLesson?.topic || ''} 练习
            </span>
          </div>

          <div className="quiz-header">
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
          {exerciseError && <div className="learn-error">{exerciseError}</div>}
        </div>
      </div>
    )
  }

  // ===== 阶段4：练习结果 =====
  if (phase === 'result' && result) {
    const scoreColor = result.score >= 80 ? 'var(--accent-green)' :
      result.score >= 60 ? 'var(--accent-blue)' :
        result.score >= 30 ? 'var(--accent-orange)' : 'var(--accent-red)'

    const diffOrder = ['easy', 'medium', 'hard']
    const diffLabelMap: Record<string, string> = { easy: '简单', medium: '中等', hard: '困难' }

    return (
      <div className="learn-container">
        <div className="learn-result">
          <div className="result-header">
            <h2>练习结果</h2>
            <div className="result-header-actions">
              <button className="btn-secondary btn-sm" onClick={backToPath}>继续学习</button>
              <button className="btn-primary btn-sm" onClick={() => { setPhase('exercising'); startExercises() }}>再来一组</button>
            </div>
          </div>

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

export default Learn
