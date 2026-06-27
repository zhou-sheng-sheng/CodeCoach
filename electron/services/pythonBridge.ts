import { spawn, ChildProcess } from 'child_process'
import http from 'http'
import path from 'path'
import fs from 'fs'

export class PythonBridge {
  private process: ChildProcess | null = null
  private port: number = 18080
  private running: boolean = false

  /**
   * 逐级探测可用的 Python 解释器，避免依赖 PATH。
   * 先用 fs.existsSync 检查常用路径，再用 spawn 验证。
   */
  private async findPython(log: (msg: string) => void): Promise<string> {
    // 候选路径：本地 AppData > C 盘常见位置
    const localAppData = process.env.LOCALAPPDATA || ''
    const appData = process.env.APPDATA || ''
    const candidates = [
      path.join(localAppData, 'Programs', 'Python', 'Python311', 'python.exe'),
      path.join(localAppData, 'Programs', 'Python', 'Python312', 'python.exe'),
      path.join(localAppData, 'Programs', 'Python', 'Python313', 'python.exe'),
      'C:\\Python311\\python.exe',
      'C:\\Python312\\python.exe',
      'C:\\Python313\\python.exe',
      'D:\\Python312\\python.exe',
      'D:\\Python\\python.exe',
      path.join(appData, 'Tencent', 'Marvis', 'runtime', 'python311', 'python.exe'),
      'python', // 最后回退到 PATH
    ]

    for (const candidate of candidates) {
      if (candidate === 'python') {
        log('[PythonBridge] Trying PATH: python')
        return 'python'
      }
      if (fs.existsSync(candidate)) {
        log('[PythonBridge] Found: ' + candidate)
        return candidate
      }
    }

    throw new Error('No Python interpreter found. Please install Python 3.11+ from https://python.org')
  }

  async start(backendDir: string): Promise<void> {
    const alreadyRunning = await this.healthCheck()
    if (alreadyRunning) {
      console.log('[PythonBridge] Using existing backend')
      this.running = true
      return
    }

    // 日志：如果写文件失败就只用 console
    let logStream: fs.WriteStream | null = null
    const log = (msg: string) => {
      console.log(msg)
      if (logStream) {
        try { logStream.write(`[${new Date().toISOString()}] ${msg}\n`) } catch {}
      }
    }

    try {
      const logPath = path.join(backendDir, 'startup.log')
      logStream = fs.createWriteStream(logPath, { flags: 'a' })
    } catch {
      log('[PythonBridge] Cannot write startup.log, using console only')
    }

    log('[PythonBridge] Starting backend, dir=' + backendDir)

    let pythonPath: string
    try {
      pythonPath = await this.findPython(log)
    } catch (err: any) {
      logStream?.end()
      throw err
    }

    return new Promise((resolve, reject) => {
      this.process = spawn(pythonPath, [
        '-m', 'uvicorn', 'main:app',
        '--host', '127.0.0.1',
        '--port', String(this.port),
      ], {
        cwd: backendDir,
        stdio: ['pipe', 'pipe', 'pipe'],
        windowsHide: true,
        env: { ...process.env, PYTHONUNBUFFERED: '1', PYTHONIOENCODING: 'utf-8', PYTHONLEGACYWINDOWSSTDIO: 'utf-8' },
      })

      let settled = false
      const settle = (ok: boolean, reason?: string) => {
        if (settled) return
        settled = true
        try { if (logStream?.writable) { logStream.end() } } catch {}
        if (ok) {
          if (logStream?.writable) { log('[PythonBridge] Backend started successfully') }
          resolve()
        } else {
          if (logStream?.writable) { log('[PythonBridge] Backend start failed: ' + (reason || 'timeout')) }
          reject(new Error(reason || 'Backend start timeout'))
        }
      }

      this.process.stdout?.on('data', (data: Buffer) => {
        const msg = data.toString().trim()
        if (msg) log('[Python stdout] ' + msg)
        if (msg.includes('Uvicorn running') || msg.includes('Application startup complete')) {
          this.running = true
          settle(true)
        }
      })

      this.process.stderr?.on('data', (data: Buffer) => {
        const msg = data.toString().trim()
        if (msg) log('[Python stderr] ' + msg)
        if (msg.includes('Uvicorn running') || msg.includes('Application startup complete')) {
          this.running = true
          settle(true)
        }
      })

      this.process.on('error', (err) => {
        settle(false, 'spawn error: ' + err.message)
      })

      this.process.on('exit', (code) => {
        log(`[PythonBridge] Process exited with code ${code}`)
        this.running = false
        if (!settled) {
          settle(false, `process exited with code ${code}`)
        }
      })

      // 后端初始化较慢（ChromaDB + Agent 初始化 ~11s），设 30s 超时
      setTimeout(() => settle(false, 'timeout after 30s'), 30000)
    })
  }

  stop(): void {
    if (this.process) {
      this.process.kill('SIGTERM')
      this.process = null
      this.running = false
    }
  }

  isRunning(): boolean {
    return this.running
  }

  getPort(): number {
    return this.port
  }

  async healthCheck(): Promise<boolean> {
    return new Promise((resolve) => {
      const req = http.get(`http://127.0.0.1:${this.port}/health`, (res) => {
        resolve(res.statusCode === 200)
      })
      req.on('error', () => resolve(false))
      req.setTimeout(3000, () => {
        req.destroy()
        resolve(false)
      })
    })
  }
}
