import { contextBridge, ipcRenderer } from 'electron'

contextBridge.exposeInMainWorld('electronAPI', {
  getBackendStatus: () => ipcRenderer.invoke('backend:status'),
  getBackendPort: () => ipcRenderer.invoke('backend:port'),
  platform: process.platform
})
