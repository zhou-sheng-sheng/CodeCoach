import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import electron from 'vite-plugin-electron'
import electronRenderer from 'vite-plugin-electron-renderer'
import path from 'path'

export default defineConfig(({ command }) => ({
  // 构建时使用相对路径，确保 Electron loadFile 能正确解析静态资源
  base: command === 'build' ? './' : '/',
  plugins: [
    react(),
    electron([
      {
        entry: '../electron/main.ts',
        vite: {
          build: {
            outDir: 'dist-electron',
            rollupOptions: {
              external: ['electron']
            }
          }
        }
      },
      {
        entry: '../electron/preload.ts',
        vite: {
          build: {
            outDir: 'dist-electron'
          }
        }
      }
    ]),
    electronRenderer()
  ],
  root: 'frontend',
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'frontend')
    }
  },
  server: {
    port: 5173
  }
}))
