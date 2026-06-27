import { app, BrowserWindow, ipcMain } from 'electron'
import path from 'path'
import { PythonBridge } from './services/pythonBridge'

let mainWindow: BrowserWindow | null = null
let pythonBridge: PythonBridge | null = null

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1400,
    height: 900,
    minWidth: 1024,
    minHeight: 680,
    title: '编程AI陪练',
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,
      nodeIntegration: false
    },
    show: true
  })

  if (process.env.VITE_DEV_SERVER_URL) {
    mainWindow.loadURL(process.env.VITE_DEV_SERVER_URL)
  } else {
    mainWindow.loadFile(path.join(__dirname, '../dist/index.html'))
  }

  // 注入 fetch 拦截器，将 /api/* 请求代理到 Python 后端
  mainWindow.webContents.on('did-finish-load', () => {
    mainWindow?.webContents.executeJavaScript(`
      (function() {
        var port = 18080;
        var origFetch = window.fetch.bind(window);
        window.fetch = function(url, opts) {
          if (typeof url === 'string' && url.indexOf('/api/') === 0) {
            url = 'http://127.0.0.1:' + port + url;
          }
          return origFetch(url, opts);
        };
      })();
    `).catch(() => {});
  })

  mainWindow.on('closed', () => {
    mainWindow = null
  })
}

function getBackendDir(): string {
  if (app.isPackaged) {
    // 打包环境：backend 作为 extraResources 放在 resources 目录下
    return path.join(process.resourcesPath, 'backend')
  }
  // 开发环境：相对于 main.ts 的路径
  return path.join(__dirname, '..', '..', 'backend')
}

async function startBackend() {
  const backendDir = getBackendDir()
  console.log('[Main] Backend directory:', backendDir)
  pythonBridge = new PythonBridge()
  try {
    await pythonBridge.start(backendDir)
    console.log('[Main] Python backend started')
  } catch (err) {
    console.error('[Main] Failed to start Python backend:', err)
  }
}

function stopBackend() {
  if (pythonBridge) {
    pythonBridge.stop()
    pythonBridge = null
  }
}

// IPC handlers
ipcMain.handle('backend:status', () => {
  return pythonBridge?.isRunning() ?? false
})

ipcMain.handle('backend:port', () => {
  return pythonBridge?.getPort() ?? null
})

app.whenReady().then(async () => {
  await startBackend()
  createWindow()

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow()
    }
  })
})

app.on('window-all-closed', () => {
  stopBackend()
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('before-quit', () => {
  stopBackend()
})
