"""AgentOrchestrator — 意图路由 + RAG 上下文增强"""
import re
import asyncio
from agents.coach_agent import CoachAgent
from agents.review_agent import ReviewAgent
from rag.knowledge_base import knowledge_base
from rag.user_memory import user_memory


LANG_LABELS = {
    "python": "Python",
    "javascript": "JavaScript",
    "typescript": "TypeScript",
    "java": "Java",
    "go": "Go",
    "rust": "Rust",
    "cpp": "C++",
    "sql": "SQL",
}


def _language_prompt(language: str) -> str:
    label = LANG_LABELS.get(language, language)
    return (
        f"[系统指令] 用户当前正在学习 **{label}** 编程语言。"
        f"请将所有解释、概念讲解和代码示例优先围绕 {label} 展开。"
        "如果用户问的是该语言相关的语法、最佳实践、常见坑点、标准库等，请深入解答。"
    )


class AgentOrchestrator:
    def __init__(self):
        self.coach = CoachAgent()
        self.reviewer = ReviewAgent()

        self._review_keywords = [
            "审查", "review", "检查这段代码", "帮我看下这段代码",
            "代码审查", "帮我审查", "代码review", "审阅",
            "看看这段代码有什么问题", "这段代码有什么毛病",
            "review一下", "帮忙review"
        ]

    def _detect_intent(self, message: str) -> str:
        msg = message.lower()
        for kw in self._review_keywords:
            if kw.lower() in msg:
                return "review"
        if re.search(r"```[\s\S]*?```", message):
            return "review"
        if re.search(r"\.(py|js|ts|tsx|jsx|java|go|rs|cpp|c|h)\b", msg):
            if any(kw in msg for kw in ["报错", "错误", "error", "bug", "改", "修", "检查", "看"]):
                return "review"
        return "coach"

    async def _retrieve_context(self, message: str, language: str = "") -> str:
        kb_ctx = await asyncio.to_thread(knowledge_base.search_as_context, message, 6)
        # 优先匹配当前语言的条目
        if language and kb_ctx:
            lang_label = LANG_LABELS.get(language, language)
            blocks = kb_ctx.split("\n\n")
            matched = [b for b in blocks if lang_label.lower() in b.lower()]
            if matched:
                kb_ctx = "\n\n".join(matched[:3])
            else:
                kb_ctx = "\n\n".join(blocks[:3])
        mem_ctx = await asyncio.to_thread(user_memory.get_profile_context, "default")

        parts = []
        if kb_ctx:
            parts.append(f"## 参考知识\n{kb_ctx}")
        if mem_ctx:
            parts.append(mem_ctx)

        if not parts:
            return ""
        return "\n\n---\n" + "\n\n".join(parts) + "\n---\n"

    async def route(self, history: list[dict], message: str, language: str = "python"):
        intent = self._detect_intent(message)

        if intent == "review":
            code_match = re.search(r"```[\w]*\n([\s\S]*?)```", message)
            lang_match = re.search(r"```(\w+)", message)
            if code_match:
                code = code_match.group(1).strip()
                code_lang = lang_match.group(1) if lang_match else language
                async for chunk in self.reviewer.review(code, code_lang, history):
                    yield chunk
            else:
                async for chunk in self.reviewer.review(message, language, history):
                    yield chunk
        else:
            ctx = await self._retrieve_context(message, language)
            lang_prompt = _language_prompt(language)
            enhanced_message = lang_prompt + "\n\n" + message + ctx if ctx else message
            async for chunk in self.coach.chat(history, enhanced_message):
                yield chunk


orchestrator = AgentOrchestrator()
