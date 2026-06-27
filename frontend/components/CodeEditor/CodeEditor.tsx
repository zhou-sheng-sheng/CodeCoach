import React, { useState, useEffect } from 'react'
import './CodeEditor.css'

interface CodeEditorProps {
  language?: string
  initialCode?: string
  readOnly?: boolean
  onRun?: (code: string, language: string) => void
  onCodeChange?: (code: string) => void
  backendPort?: number
  userId?: string
}

const LANGUAGE_TEMPLATES: Record<string, string> = {
  python: `# Python 代码
def solution():
    # 在这里编写你的代码
    pass

if __name__ == '__main__':
    solution()
`,
  javascript: `// JavaScript 代码
function solution() {
  // 在这里编写你的代码
}

solution();
`,
  typescript: `// TypeScript 代码
function solution(): void {
  // 在这里编写你的代码
}

solution();
`,
  java: `// Java 代码
public class Main {
    public static void main(String[] args) {
        // 在这里编写你的代码
    }
}
`,
  go: `// Go 代码
package main

import "fmt"

func main() {
    // 在这里编写你的代码
    fmt.Println("Hello, World!")
}
`,
  rust: `// Rust 代码
fn main() {
    // 在这里编写你的代码
    println!("Hello, World!");
}
`,
  cpp: `// C++ 代码
#include <iostream>
using namespace std;

int main() {
    // 在这里编写你的代码
    return 0;
}
`,
  c: `// C 代码
#include <stdio.h>

int main() {
    // 在这里编写你的代码
    return 0;
}
`,
}

const LANG_LABEL: Record<string, string> = {
  python: 'Python',
  javascript: 'JavaScript',
  typescript: 'TypeScript',
  java: 'Java',
  go: 'Go',
  rust: 'Rust',
  cpp: 'C++',
  c: 'C',
}

interface RunResult {
  success: boolean
  stdout: string
  stderr: string
  error?: string
  timed_out: boolean
  exit_code: number
}

const CodeEditor: React.FC<CodeEditorProps> = ({
  language: initialLang = 'python',
  initialCode = '',
  readOnly = false,
  onRun,
  onCodeChange,
  backendPort = 18080,
  userId = 'default',
}) => {
  const [lang, setLang] = useState(initialLang)
  const [code, setCode] = useState(initialCode || LANGUAGE_TEMPLATES[initialLang] || '')
  const [output, setOutput] = useState('')
  const [running, setRunning] = useState(false)
  const [result, setResult] = useState<RunResult | null>(null)

  // 响应外部 language prop 变化（如左侧菜单切换语言）
  useEffect(() => {
    setLang(initialLang)
    const isTemplate = Object.values(LANGUAGE_TEMPLATES).includes(code)
    if (isTemplate) {
      const template = LANGUAGE_TEMPLATES[initialLang]
      if (template) setCode(template)
    }
    // initialLang 变化时同步，code 仅用于判断是否为模板
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [initialLang])

  const handleCodeChange = (val: string) => {
    setCode(val)
    if (onCodeChange) onCodeChange(val)
  }

  const handleRun = async () => {
    if (running) return
    setRunning(true)
    setOutput('')
    setResult(null)

    if (onRun) {
      onRun(code, lang)
      setRunning(false)
      return
    }

    try {
      const res = await fetch(`http://127.0.0.1:${backendPort}/api/sandbox/run`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code, language: lang, stdin: '', user_id: userId || 'default' }),
      })
      const data: RunResult = await res.json()
      setResult(data)
      if (data.success) {
        setOutput(data.stdout || '(无输出)')
      } else {
        setOutput(data.stderr || data.error || '运行失败')
      }
    } catch (e: any) {
      setResult({ success: false, stdout: '', stderr: `请求失败：${e.message}`, timed_out: false, exit_code: -1 })
      setOutput(`请求失败：${e.message}`)
    } finally {
      setRunning(false)
    }
  }

  const lineCount = code.split('\n').length

  return (
    <div className="code-editor-container">
      {/* 工具栏 */}
      <div className="ce-toolbar">
        <span className="ce-lang-label">{LANG_LABEL[lang] || lang}</span>
        <div className="ce-toolbar-right">
          <span className="ce-line-count">{lineCount} 行</span>
          <button
            className="btn-primary btn-run"
            onClick={handleRun}
            disabled={running || readOnly}
          >
            {running ? '运行中...' : '▶ 运行'}
          </button>
        </div>
      </div>

      {/* 编辑器区域 */}
      <div className="ce-editor-area">
        <div className="ce-line-numbers">
          {code.split('\n').map((_, i) => (
            <span key={i} className="ce-line-num">{i + 1}</span>
          ))}
        </div>
        <textarea
          className="ce-textarea"
          value={code}
          onChange={e => handleCodeChange(e.target.value)}
          readOnly={readOnly}
          spellCheck={false}
          onKeyDown={e => {
            if (e.key === 'Tab') {
              e.preventDefault()
              const target = e.target as HTMLTextAreaElement
              const start = target.selectionStart
              const end = target.selectionEnd
              const newCode = code.slice(0, start) + '    ' + code.slice(end)
              handleCodeChange(newCode)
              // 恢复光标位置
              requestAnimationFrame(() => {
                target.selectionStart = target.selectionEnd = start + 4
              })
            }
          }}
        />
      </div>

      {/* 输出区域 */}
      {(output || result) && (
        <div className={`ce-output ${result?.success ? 'output-ok' : 'output-err'}`}>
          <div className="ce-output-header">
            <span className="ce-output-label">
              {result?.success ? '运行结果' : '输出'}
            </span>
            {result && (
              <span className="ce-output-status">
                退出码: {result.exit_code}
                {result.timed_out && ' | 超时'}
              </span>
            )}
          </div>
          <pre className="ce-output-content">{output}</pre>
        </div>
      )}
    </div>
  )
}

export default CodeEditor
