import React, { useEffect, useState, useCallback } from 'react'
import './Dashboard.css'

interface DashboardProps {
  backendPort: number
  language: string
  userId: string
  onNavigate?: (view: string) => void
}

interface DashboardData {
  has_assessment: boolean
  assessment: AssessmentData | null
  errors: ErrorsData
  summary: SummaryData
}

interface AssessmentData {
  score: number
  level: string
  advice: string
  correct: number
  total: number
  topic_stats: Record<string, { total: number; correct: number }>
  difficulty_stats: Record<string, { total: number; correct: number }>
  weak_topics: string[]
}

interface ErrorsData {
  total_errors: number
  total_attempts: number
  by_topic: Record<string, { count: number; attempts: number }>
  by_difficulty: Record<string, { count: number; attempts: number }>
  most_wrong: MostWrongItem[]
}

interface MostWrongItem {
  question_id: string
  question: string
  topic: string
  error_count: number
}

interface SummaryData {
  overall_level: string
  total_topics: number
  mastered_topics: number
  weakest_topics: string[]
  recommendation: string
}

const LEVEL_CLASS_MAP: Record<string, string> = {
  '入门': 'level-beginner',
  '初级': 'level-junior',
  '中级': 'level-mid',
  '高级': 'level-senior',
}

const Dashboard: React.FC<DashboardProps> = ({ backendPort, language, userId, onNavigate }) => {
  const [data, setData] = useState<DashboardData | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  const fetchData = useCallback(async () => {
    setLoading(true)
    setError(null)
    try {
      const resp = await fetch(`http://127.0.0.1:${backendPort}/api/dashboard?language=${language}&user_id=${encodeURIComponent(userId)}`)
      if (!resp.ok) {
        throw new Error(`HTTP ${resp.status}`)
      }
      const json = await resp.json()
      setData(json)
    } catch (e: any) {
      setError(e.message || '无法加载看板数据')
    } finally {
      setLoading(false)
    }
  }, [backendPort, language])

  useEffect(() => {
    fetchData()
  }, [fetchData])

  if (loading) {
    return (
      <div className="dashboard-container">
        <div className="dashboard-loading">
          <div className="loading-spinner" />
          <p>加载看板数据...</p>
        </div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="dashboard-container">
        <div className="dashboard-error">
          <div className="error-icon">!</div>
          <p>加载失败：{error}</p>
          <button className="btn-retry" onClick={fetchData}>重试</button>
        </div>
      </div>
    )
  }

  if (!data) {
    return null
  }

  // Empty state
  if (!data.has_assessment) {
    return (
      <div className="dashboard-container">
        <div className="dashboard-header">
          <h2>数据看板</h2>
          <button className="btn-refresh" onClick={fetchData}>刷新</button>
        </div>
        <div className="dashboard-empty">
          <div className="empty-icon">
            <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
              <path d="M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
          </div>
          <h3>暂无评估数据</h3>
          <p>完成基础评估后，这里将展示你的学习数据</p>
          {onNavigate && (
            <button className="btn-go-assess" onClick={() => onNavigate('assessment')}>去评估</button>
          )}
        </div>
      </div>
    )
  }

  const { assessment, errors: errStats, summary } = data
  const scorePct = assessment ? Math.round((assessment.correct / assessment.total) * 100) : 0

  const sortedTopics = Object.entries(assessment?.topic_stats || {})
    .sort(([, a], [, b]) => {
      const ra = a.total > 0 ? a.correct / a.total : 0
      const rb = b.total > 0 ? b.correct / b.total : 0
      return ra - rb
    })

  return (
    <div className="dashboard-container">
      {/* Header */}
      <div className="dashboard-header">
        <h2>数据看板</h2>
        <button className="btn-refresh" onClick={fetchData}>刷新</button>
      </div>

      {/* Row 1: Overview Cards */}
      <div className="dashboard-grid overview-grid">
        <div className="card card-score">
          <div className="card-label">评估成绩</div>
          <div className="score-main">
            <span className="score-number">{assessment?.score ?? 0}</span>
            <span className="score-unit">分</span>
          </div>
          <span className={`level-badge ${LEVEL_CLASS_MAP[assessment?.level ?? ''] || ''}`}>
            {assessment?.level ?? '未知'}
          </span>
          <div className="score-sub">{assessment?.correct ?? 0}/{assessment?.total ?? 0} 正确</div>
        </div>

        <div className="card card-errors">
          <div className="card-label">错题统计</div>
          <div className="stat-big">{errStats.total_errors}</div>
          <div className="stat-sub">累计错误次数</div>
        </div>

        <div className="card card-mastery">
          <div className="card-label">主题掌握</div>
          <div className="stat-big">
            {summary.mastered_topics}<span className="stat-unit">/{summary.total_topics}</span>
          </div>
          <div className="stat-sub">已掌握主题</div>
        </div>

        <div className="card card-progress">
          <div className="card-label">薄弱环节</div>
          <div className="stat-big">{summary.weakest_topics?.length ?? 0}</div>
          <div className="stat-sub">待强化主题</div>
        </div>
      </div>

      {/* Row 2: Topic Mastery */}
      <div className="card section-card">
        <h3 className="section-title">主题掌握度</h3>
        <div className="topic-mastery-list">
          {sortedTopics.map(([topic, stats]) => {
            const rate = stats.total > 0 ? (stats.correct / stats.total) * 100 : 0
            const colorClass = rate >= 80 ? 'bar-green' : rate >= 50 ? 'bar-orange' : 'bar-red'
            return (
              <div key={topic} className="topic-row">
                <span className="topic-name">{topic}</span>
                <div className="topic-bar-track">
                  <div
                    className={`topic-bar-fill ${colorClass}`}
                    style={{ width: `${Math.max(rate, 3)}%` }}
                  />
                </div>
                <span className="topic-rate">{rate.toFixed(0)}%</span>
              </div>
            )
          })}
          {sortedTopics.length === 0 && (
            <div className="empty-row">暂无主题数据</div>
          )}
        </div>
      </div>

      {/* Row 3: Most Wrong TOP 5 */}
      {errStats.most_wrong && errStats.most_wrong.length > 0 && (
        <div className="card section-card">
          <h3 className="section-title">高频错题 TOP {Math.min(errStats.most_wrong.length, 5)}</h3>
          <table className="error-table">
            <thead>
              <tr>
                <th>#</th>
                <th>题目</th>
                <th>主题</th>
                <th>错误次数</th>
              </tr>
            </thead>
            <tbody>
              {errStats.most_wrong.slice(0, 5).map((item, idx) => (
                <tr key={item.question_id || idx}>
                  <td className="rank-cell">{idx + 1}</td>
                  <td className="question-cell">
                    {item.question ? item.question.slice(0, 30) + (item.question.length > 30 ? '...' : '') : '—'}
                  </td>
                  <td>{item.topic || '—'}</td>
                  <td>
                    <span className="error-badge">{item.error_count}</span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {/* Summary recommendation */}
      <div className="summary-bar">
        <span className="summary-icon">&#9432;</span>
        <span className="summary-text">{summary.recommendation}</span>
      </div>
    </div>
  )
}

export default Dashboard
