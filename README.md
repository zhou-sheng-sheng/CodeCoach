---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: 8c47871f2c029bd7b1c052905e8cf0de_3475907a722611f1b2f55254006c9bbf
    ReservedCode1: mRLvIAAE9Lk78gP4uBdyArWDGsB0zNZ7CD7V5FdMU0Rx80bik+fpoWyf+1y738YqxOW2YdYIrXq7yjYEhsbSmQ3gYGzBpiyqXnytEge+kh8+7yWY4ZU2nUNGq9cCOwFrjxWIkG/UJ/0AfP5Idlgz3gdxVPve7RAJs/67KNvNK2AE3/oBzta/NuER9iE=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: 8c47871f2c029bd7b1c052905e8cf0de_3475907a722611f1b2f55254006c9bbf
    ReservedCode2: mRLvIAAE9Lk78gP4uBdyArWDGsB0zNZ7CD7V5FdMU0Rx80bik+fpoWyf+1y738YqxOW2YdYIrXq7yjYEhsbSmQ3gYGzBpiyqXnytEge+kh8+7yWY4ZU2nUNGq9cCOwFrjxWIkG/UJ/0AfP5Idlgz3gdxVPve7RAJs/67KNvNK2AE3/oBzta/NuER9iE=
---

# 编程AI陪练系统 — 安装与运行说明

AI 学习陪练系统：5 智能体协作（评估 / 教学 / 习题 / 陪练 / 面试）+ RAG 检索增强（ChromaDB）+ DeepSeek LLM + 阿里百炼 Embedding + Electron 桌面应用

---

## 前置要求

- Node.js 18+（推荐 20 LTS）
- Python 3.10+（推荐 3.11）
- npm 9+
- Git（可选，用于克隆仓库）

---

## 安装步骤

### 1. 克隆仓库

```bash
git clone https://github.com/zhou-sheng-sheng/编程AI陪练系统.git
cd 编程AI陪练系统
```

### 2. 安装前端依赖

```bash
npm install
```

### 3. 安装后端依赖

```bash
cd backend
pip install -r requirements.txt
cd ..
```

### 4. 配置环境变量

在项目根目录创建 `.env` 文件（参考 `.env.example`）：

```env
# DeepSeek LLM
DEEPSEEK_API_KEY=your_deepseek_api_key
DEEPSEEK_BASE_URL=https://api.deepseek.com/v1

# 阿里百炼 Embedding
DASHSCOPE_API_KEY=your_dashscope_api_key
```

### 5. 初始化知识库

```bash
cd backend
python seed_data.py
cd ..
```

---

## 运行方式

### 开发模式（推荐）

**终端 1 — 启动后端**

```bash
.\start_backend.ps1
```

后端运行在 http://localhost:18080

**终端 2 — 启动前端 + Electron**

```bash
.\start-frontend-v2.ps1
```

前端 Vite 运行在 http://localhost:5173，Electron 窗口自动打开。

### 生产模式（打包安装程序）

```bash
npm run electron:build
```

打包输出在 `release\` 目录。

---

## 接口文档

后端启动后访问：http://localhost:18080/docs

---

## 技术栈

| 层 | 技术 |
|---|------|
| 桌面壳 | Electron 28+ |
| 前端 | React 18 + TypeScript + Monaco Editor + Vite |
| 后端 | Python 3.11 + FastAPI |
| AI 编排 | LangChain + LangGraph |
| 向量数据库 | ChromaDB |
| 关系数据库 | SQLite（SQLAlchemy） |
| LLM | DeepSeek（deepseek-chat） |
| Embedding | 阿里百炼 DashScope（text-embedding-v3） |

---

## 功能模块

- **AI 陪练** — 多轮对话，辅导编程问题
- **学习计划** — 能力评估 → LLM 生成个性化学习路径
- **知识点学习** — 多语言教材库，结构化教学
- **习题练习** — AI 出题 + 即时批改
- **基础评估** — 10 题定级测试
- **模拟面试** — 算法 + 系统设计实战
- **数据看板** — 学习进度、正确率、成就统计
- **错题本** — 自动收录，分类回顾
- **笔记** — 学习笔记管理
- **沙箱** — Monaco Editor 在线编码

