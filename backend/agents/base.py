from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import os
from typing import List, Dict, Optional


class BaseAgent:
    """Agent 基类，封装 LLM 调用和通用逻辑"""

    def __init__(
        self,
        name: str,
        system_prompt: str,
        model: Optional[str] = None,
        temperature: float = 0.7
    ):
        self.name = name
        self.system_prompt = system_prompt

        # 支持本地 Ollama 和云端 API 双通道
        api_base = os.getenv("LLM_API_BASE", "http://localhost:11434/v1")
        api_key = os.getenv("LLM_API_KEY", "ollama")

        self.llm = ChatOpenAI(
            model=model or os.getenv("LLM_MODEL", "qwen2.5-coder:7b"),
            base_url=api_base,
            api_key=api_key,
            temperature=temperature,
            streaming=True
        )

    def _build_messages(self, history: List[Dict[str, str]], current: str):
        """构建消息列表"""
        messages = [SystemMessage(content=self.system_prompt)]
        for msg in history:
            if msg["role"] == "user":
                messages.append(HumanMessage(content=msg["content"]))
            elif msg["role"] == "assistant":
                messages.append(AIMessage(content=msg["content"]))
        messages.append(HumanMessage(content=current))
        return messages

    async def stream(self, history: List[Dict[str, str]], current: str):
        """流式调用 LLM"""
        messages = self._build_messages(history, current)
        async for chunk in self.llm.astream(messages):
            if chunk.content:
                yield chunk.content

    async def invoke(self, history: List[Dict[str, str]], current: str) -> str:
        """非流式调用 LLM"""
        messages = self._build_messages(history, current)
        result = await self.llm.ainvoke(messages)
        return result.content
