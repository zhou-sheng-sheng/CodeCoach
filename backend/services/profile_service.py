"""人物画像服务 — 画像生成、向量化、知识库匹配、个性化学习计划"""
import json
import os
from agents.base import BaseAgent

PROFILE_SYSTEM_PROMPT = """你是一个编程学习评估专家。根据用户提供的个人背景信息，生成一份结构化的人物画像 JSON。

## 输出格式（严格 JSON，不含任何额外文字）
{
  "level": "入门/初级/中级/高级",
  "tags": ["主题标签1", "主题标签2", ...],
  "goals": ["学习目标1", "学习目标2", ...],
  "time_budget": "可用时间描述",
  "style": "偏好的学习风格",
  "weaknesses": ["薄弱点1", "薄弱点2", ...],
  "strengths": ["优势1", "优势2", ...],
  "summary": "一段简洁的人物概述"
}

## 字段说明
- level: 根据描述的编程经验、知识面综合判断
- tags: 3-5 个关键词标签，如 Python、Web开发、数据结构
- goals: 用户明确或隐含的学习目标，1-3 条
- time_budget: 用户能投入的学习时间
- style: 如"动手实践型"、"理论深入型"、"项目驱动型"
- weaknesses: 推测的薄弱环节，2-4 条
- strengths: 推测的优势领域，2-4 条
- summary: 50 字以内的人物概述

## 注意
- 所有文本使用中文
- tags 使用英文技术术语
- 保证 JSON 可被直接解析"""


PLAN_SYSTEM_PROMPT = """你是一个编程学习规划专家。根据用户的人物画像、答题评估结果和知识库匹配结果，生成一份个性化学习计划。

## 输出格式（严格 JSON，不含任何额外文字）
{
  "overview": "计划概述（100字以内）",
  "priority_topics": ["重点主题1", "重点主题2", ...],
  "phases": [
    {
      "phase": 1,
      "title": "阶段标题",
      "duration": "预计时间",
      "focus": "阶段重点",
      "items": ["具体学习项1", "具体学习项2", ...],
      "resources": ["推荐资源1", "推荐资源2"]
    }
  ],
  "weekly_schedule": {
    "sessions_per_week": 3,
    "minutes_per_session": 60,
    "routine": "每周学习节奏描述"
  },
  "tips": ["学习建议1", "学习建议2"]
}

## 规划原则
- 结合人物画像的 level 设定难度梯度
- 重点攻克 weaknesses 中列出的薄弱点
- 匹配知识库中检索到的相关知识点
- phases 通常 3-5 个阶段，循序渐进
- weekly_schedule 根据 time_budget 合理分配
- 考虑用户偏好的学习风格"""


class ProfileService:
    """人物画像服务"""

    def __init__(self):
        self.profile_agent = BaseAgent(
            name="profile_generator",
            system_prompt=PROFILE_SYSTEM_PROMPT,
            temperature=0.3
        )
        self.plan_agent = BaseAgent(
            name="plan_generator",
            system_prompt=PLAN_SYSTEM_PROMPT,
            temperature=0.5
        )

    async def generate_profile(self, background: dict) -> dict:
        """
        根据用户背景信息生成结构化人物画像

        Args:
            background: {
                "experience": "编程经验描述",
                "current_level": "自评水平",
                "goals": "学习目标",
                "time_per_week": "每周可用时间",
                "learning_style": "学习风格偏好",
                "languages_known": ["已知语言"],
                "target_language": "目标语言",
                "notes": "补充说明"
            }
        """
        prompt = self._build_profile_prompt(background)
        result = await self.profile_agent.invoke([], prompt)
        profile = self._parse_json(result)
        return profile

    async def generate_plan(
        self,
        profile: dict,
        assessment_result: dict,
        knowledge_matches: list[dict]
    ) -> dict:
        """结合画像、评估结果和知识库匹配生成个性化学习计划"""
        prompt = self._build_plan_prompt(profile, assessment_result, knowledge_matches)
        result = await self.plan_agent.invoke([], prompt)
        plan = self._parse_json(result)
        return plan

    def _build_profile_prompt(self, bg: dict) -> str:
        parts = []
        parts.append("请根据以下用户背景信息生成人物画像 JSON：")
        if bg.get("experience"):
            parts.append(f"- 编程经验：{bg['experience']}")
        if bg.get("current_level"):
            parts.append(f"- 自评水平：{bg['current_level']}")
        if bg.get("goals"):
            parts.append(f"- 学习目标：{bg['goals']}")
        if bg.get("time_per_week"):
            parts.append(f"- 每周可用时间：{bg['time_per_week']}")
        if bg.get("learning_style"):
            parts.append(f"- 偏好学习风格：{bg['learning_style']}")
        if bg.get("languages_known"):
            parts.append(f"- 已知编程语言：{', '.join(bg['languages_known'])}")
        if bg.get("target_language"):
            parts.append(f"- 目标学习语言：{bg['target_language']}")
        if bg.get("notes"):
            parts.append(f"- 补充说明：{bg['notes']}")
        return "\n".join(parts)

    def _build_plan_prompt(
        self,
        profile: dict,
        assessment: dict,
        knowledge: list[dict]
    ) -> str:
        parts = []
        parts.append("请根据以下信息生成个性化学习计划 JSON：\n")

        parts.append("## 人物画像")
        parts.append(json.dumps(profile, ensure_ascii=False, indent=2))

        parts.append("\n## 答题评估结果")
        assess_summary = {
            "score": assessment.get("score"),
            "level": assessment.get("level"),
            "weak_topics": assessment.get("weak_topics", []),
            "topic_stats": assessment.get("topic_stats", {}),
        }
        parts.append(json.dumps(assess_summary, ensure_ascii=False, indent=2))

        if knowledge:
            parts.append("\n## 知识库匹配结果")
            kb_items = []
            for k in knowledge[:10]:
                kb_items.append(f"- [{k.get('metadata', {}).get('topic', '通用')}] {k.get('content', '')[:100]}")
            parts.append("\n".join(kb_items))

        return "\n".join(parts)

    def _parse_json(self, raw: str) -> dict:
        """从 LLM 输出中提取 JSON 对象"""
        raw = raw.strip()
        # 尝试直接解析
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            pass

        # 尝试提取 ```json ... ``` 代码块
        if "```" in raw:
            for marker in ["```json", "```"]:
                if marker in raw:
                    start = raw.index(marker) + len(marker)
                    end = raw.index("```", start) if "```" in raw[start:] else len(raw)
                    try:
                        return json.loads(raw[start:end].strip())
                    except json.JSONDecodeError:
                        continue

        # 尝试找 { ... }
        brace_start = raw.find("{")
        brace_end = raw.rfind("}")
        if brace_start >= 0 and brace_end > brace_start:
            try:
                return json.loads(raw[brace_start:brace_end + 1])
            except json.JSONDecodeError:
                pass

        # 兜底：返回原始文本
        return {"raw_output": raw, "parse_error": True}


profile_service = ProfileService()
