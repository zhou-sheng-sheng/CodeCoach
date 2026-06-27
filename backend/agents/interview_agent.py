"""面试Agent — 模拟技术面试（算法 / 系统设计 / 行为面试）"""
import json
import random
import time
import re
from dataclasses import dataclass, field
from typing import Any, Optional
from services.achievement import record_interview

# ─── 面试题目库 ───────────────────────────────────────────

ALGORITHM_QUESTIONS = [
    {
        "id": "algo_001",
        "title": "两数之和",
        "difficulty": "easy",
        "question": "给定一个整数数组 nums 和一个目标值 target，请找出数组中和为目标值的两个数的下标。假设每个输入只有一个解，且同一个元素不能使用两次。请用 Python 实现。",
        "topics": ["数组", "哈希表"],
        "follow_ups": [
            "你的解法时间复杂度是多少？能优化到 O(n) 吗？",
            "如果数组已经排序，你能用双指针做到 O(n) 吗？",
            "如果要求返回所有可能的组合（不限于两个数），你会怎么做？",
        ],
    },
    {
        "id": "algo_002",
        "title": "反转链表",
        "difficulty": "easy",
        "question": "给你单链表的头节点 head，请反转链表并返回反转后的链表。请用 Python 实现（可以假设已有 ListNode 类）。",
        "topics": ["链表", "迭代/递归"],
        "follow_ups": [
            "你能同时给出迭代和递归两种解法吗？",
            "两种方法的空间复杂度分别是多少？",
            "如果要反转链表的一部分（第 m 到第 n 个节点）呢？",
        ],
    },
    {
        "id": "algo_003",
        "title": "有效的括号",
        "difficulty": "easy",
        "question": "给定一个只包含 '('、')'、'{'、'}'、'['、']' 的字符串 s，判断字符串是否有效。有效需满足：左括号必须用相同类型的右括号闭合，且左括号必须以正确的顺序闭合。",
        "topics": ["栈", "字符串"],
        "follow_ups": [
            "时间复杂度是多少？",
            "如果括号类型扩展到更多种（如 < >），你的代码需要怎样修改？",
            "能否不借助栈来实现？",
        ],
    },
    {
        "id": "algo_004",
        "title": "最长无重复子串",
        "difficulty": "medium",
        "question": "给定一个字符串 s，请找出其中不含有重复字符的最长子串的长度。例如 s='abcabcbb' 输出 3（'abc'）。请用 Python 实现。",
        "topics": ["滑动窗口", "哈希表"],
        "follow_ups": [
            "你的解法时间复杂度是多少？空间复杂度呢？",
            "如果要求返回最长子串本身（而非长度），怎么改？",
            "如果字符集很小（如只有小写字母），有更优解吗？",
        ],
    },
    {
        "id": "algo_005",
        "title": "二叉树的层序遍历",
        "difficulty": "medium",
        "question": "给你二叉树的根节点 root，返回其节点值的层序遍历（即逐层从左到右访问所有节点）。请用 Python 实现。",
        "topics": ["二叉树", "BFS", "队列"],
        "follow_ups": [
            "如果要求之字形遍历（Z 字形）呢？",
            "能否用 DFS 实现层序遍历？",
            "你的空间复杂度是多少？",
        ],
    },
    {
        "id": "algo_006",
        "title": "LRU 缓存",
        "difficulty": "medium",
        "question": "设计一个 LRU（最近最少使用）缓存。实现 LRUCache 类：get(key) 获取值（不存在返回 -1），put(key, value) 插入或更新。缓存容量固定，超出时淘汰最久未使用的。要求 get 和 put 都是 O(1)。",
        "topics": ["设计", "哈希表", "双向链表"],
        "follow_ups": [
            "为什么需要双向链表而不是单向链表？",
            "如果改成 LFU（最不经常使用）策略，怎么实现？",
            "Python 的 OrderedDict 能如何简化这个实现？",
        ],
    },
    {
        "id": "algo_007",
        "title": "合并 K 个升序链表",
        "difficulty": "hard",
        "question": "给你一个链表数组，每个链表都已按升序排列。请将所有链表合并到一个升序链表中并返回。请用 Python 实现。",
        "topics": ["堆", "分治", "链表"],
        "follow_ups": [
            "用最小堆和两两合并两种方案，复杂度各是多少？",
            "如果链表数量非常大（百万级）怎么办？",
            "能否用归并排序的思路来做？",
        ],
    },
]

SYSTEM_DESIGN_QUESTIONS = [
    {
        "id": "sys_001",
        "title": "设计短链接系统",
        "difficulty": "medium",
        "scenario": "设计一个类似 TinyURL 的短链接服务。用户输入长 URL，系统返回一个短链接；访问短链接时跳转到原始 URL。请考虑：短码生成策略、存储方案、高并发处理、过期策略。",
        "guide": [
            "先估算一下 QPS 和数据量：假设日活千万，每天生成百万短链接，读写比约 10:1",
            "短码生成：可以用什么算法？自增 ID + Base62 编码，还是哈希？各自的优缺点？",
            "存储选型：关系型数据库还是 NoSQL？为什么？",
            "高并发：缓存策略是什么？读写分离怎么做？",
            "扩展性：如果要支持自定义短码、统计分析，架构需要怎样调整？",
        ],
    },
    {
        "id": "sys_002",
        "title": "设计即时通讯系统",
        "difficulty": "hard",
        "scenario": "设计一个类似微信的即时通讯系统，支持一对一聊天、群聊、消息已读/未读状态。请考虑消息可靠性、实时性、存储方案和扩展性。",
        "guide": [
            "消息如何实时推送？长连接（WebSocket）还是轮询？",
            "消息可靠性：如何保证消息不丢失、不重复？",
            "离线消息怎么处理？用户上线后如何同步？",
            "群聊消息如何高效分发？写扩散还是读扩散？",
            "存储：消息表如何设计？历史消息如何归档？",
        ],
    },
]

BEHAVIORAL_QUESTIONS = [
    {
        "id": "bhv_001",
        "title": "项目冲突处理",
        "question": "请描述一次你在团队项目中遇到技术分歧的经历。你是如何处理分歧的？最终结果如何？请用 STAR 法则回答。",
        "follow_ups": [
            "你当时为什么坚持自己的方案？技术理由是什么？",
            "如果再来一次，你会怎么处理？",
            "你觉得技术决策中，什么情况下应该妥协？",
        ],
    },
    {
        "id": "bhv_002",
        "title": "失败经历",
        "question": "请分享一次你在编程/项目中的失败经历。你从中学到了什么？之后如何改进的？",
        "follow_ups": [
            "这个失败对团队造成了什么影响？",
            "你是如何发现问题的？主动发现的还是别人指出的？",
            "之后你建立了什么机制来防止类似问题？",
        ],
    },
    {
        "id": "bhv_003",
        "title": "快速学习",
        "question": "请描述一次你需要快速学习一门新技术/新语言来完成任务的经历。你的学习策略是什么？花了多长时间？结果如何？",
        "follow_ups": [
            "你是如何评估一门新技术是否值得引入项目的？",
            "学习过程中遇到了什么困难？怎么克服的？",
            "你如何平衡快速上手和深入理解？",
        ],
    },
    {
        "id": "bhv_004",
        "title": "代码质量",
        "question": "你如何看待代码质量？请分享一次你主动提升代码质量的经历，包括你采取的措施和结果。",
        "follow_ups": [
            "Code Review 中你最关注什么？",
            "你会如何说服一个不重视代码质量的同事？",
            "技术债务：什么时候该还，什么时候可以接受？",
        ],
    },
]

INTERVIEW_TYPES = {
    "algorithm": {"label": "算法面试", "time_per_question": 900, "question_count": 3},
    "system_design": {"label": "系统设计面试", "time_per_question": 1200, "question_count": 1},
    "behavioral": {"label": "行为面试", "time_per_question": 600, "question_count": 3},
}


# ─── 状态机 ──────────────────────────────────────────────

@dataclass
class InterviewSession:
    session_id: str
    interview_type: str
    language: str
    questions: list[dict] = field(default_factory=list)
    current_q_index: int = 0
    phase: str = "idle"          # idle | asking | waiting_answer | follow_up | scoring | done
    follow_up_index: int = 0
    answers: list[dict] = field(default_factory=list)
    scores: list[dict] = field(default_factory=list)
    started_at: float = 0.0
    user_id: str = "default"


# ─── Agent ───────────────────────────────────────────────

class InterviewAgent:
    """面试Agent — 管理面试状态，协调 LLM 生成追问和评分"""

    def __init__(self):
        self._sessions: dict[str, InterviewSession] = {}

    # ── 会话管理 ──────────────────────────────────────

    def create_session(self, interview_type: str, language: str, user_id: str = "default") -> InterviewSession:
        import uuid
        sid = str(uuid.uuid4())[:8]

        # 选题
        if interview_type == "algorithm":
            pool = ALGORITHM_QUESTIONS
        elif interview_type == "system_design":
            pool = SYSTEM_DESIGN_QUESTIONS
        else:
            pool = BEHAVIORAL_QUESTIONS

        count = INTERVIEW_TYPES.get(interview_type, {}).get("question_count", 3)
        questions = random.sample(pool, min(count, len(pool)))

        session = InterviewSession(
            session_id=sid,
            interview_type=interview_type,
            language=language,
            questions=questions,
            phase="idle",
            started_at=time.time(),
            user_id=user_id,
        )
        self._sessions[sid] = session
        return session

    def get_session(self, session_id: str) -> Optional[InterviewSession]:
        return self._sessions.get(session_id)

    # ── 面试流程 ──────────────────────────────────────

    def start_question(self, session_id: str) -> dict:
        """面试官出题"""
        s = self._sessions.get(session_id)
        if not s:
            return {"error": "会话不存在"}

        if s.current_q_index >= len(s.questions):
            s.phase = "done"
            return {"phase": "done", "message": "所有题目已完成"}

        q = s.questions[s.current_q_index]
        s.phase = "waiting_answer"
        s.follow_up_index = 0

        meta = INTERVIEW_TYPES.get(s.interview_type, {})

        return {
            "phase": "asking",
            "question_index": s.current_q_index + 1,
            "total_questions": len(s.questions),
            "question_id": q["id"],
            "title": q.get("title", ""),
            "question": q.get("question", q.get("scenario", "")),
            "topics": q.get("topics", []),
            "difficulty": q.get("difficulty", ""),
            "time_limit": meta.get("time_per_question", 900),
            "session_id": session_id,
        }

    def evaluate_answer(self, session_id: str, answer: str) -> dict:
        """评估用户作答 + 自动追问"""
        s = self._sessions.get(session_id)
        if not s:
            return {"error": "会话不存在"}

        q = s.questions[s.current_q_index]

        # 记录答案
        s.answers.append({
            "question_id": q["id"],
            "question": q.get("question", q.get("scenario", "")),
            "answer": answer,
            "timestamp": time.time(),
        })

        # 系统设计面试：用 LLM 生成追问
        if s.interview_type == "system_design":
            return self._generate_system_design_followup(s, q, answer)

        # 算法 / 行为面试：预置追问
        follow_ups = q.get("follow_ups", [])
        if s.follow_up_index < len(follow_ups):
            fu = follow_ups[s.follow_up_index]
            s.follow_up_index += 1
            s.phase = "follow_up"
            return {
                "phase": "follow_up",
                "follow_up": fu,
                "follow_up_index": s.follow_up_index,
                "total_follow_ups": len(follow_ups),
                "session_id": session_id,
            }
        else:
            # 追问完毕，进行评分
            return self._score_and_next(session_id)

    def answer_follow_up(self, session_id: str, answer: str) -> dict:
        """用户回答追问后的处理"""
        s = self._sessions.get(session_id)
        if not s:
            return {"error": "会话不存在"}

        q = s.questions[s.current_q_index]

        # 记录回答
        s.answers.append({
            "question_id": q["id"],
            "question": f"[追问{s.follow_up_index}]（原题：{q.get('title', '')}）",
            "answer": answer,
            "timestamp": time.time(),
        })

        # 继续追问或评分
        follow_ups = q.get("follow_ups", [])
        if s.follow_up_index < len(follow_ups):
            fu = follow_ups[s.follow_up_index]
            s.follow_up_index += 1
            s.phase = "follow_up"
            return {
                "phase": "follow_up",
                "follow_up": fu,
                "follow_up_index": s.follow_up_index,
                "total_follow_ups": len(follow_ups),
                "session_id": session_id,
            }
        else:
            return self._score_and_next(session_id)

    def skip_follow_ups(self, session_id: str) -> dict:
        """跳过追问，直接进入评分"""
        return self._score_and_next(session_id)

    def _score_and_next(self, session_id: str) -> dict:
        """评分当前题 → 进入下一题或结束"""
        s = self._sessions.get(session_id)
        if not s:
            return {"error": "会话不存在"}

        q = s.questions[s.current_q_index]

        # 模拟评分（正式版可用 LLM 评分）
        score = self._mock_score(q)
        s.scores.append({
            "question_id": q["id"],
            "title": q.get("title", ""),
            "score": score["score"],
            "comment": score["comment"],
            "strengths": score.get("strengths", []),
            "weaknesses": score.get("weaknesses", []),
        })

        s.current_q_index += 1

        if s.current_q_index >= len(s.questions):
            s.phase = "done"
            return self._generate_report(session_id)

        # 展示当前题评分，准备下一题
        return {
            "phase": "scored",
            "scores": s.scores,
            "session_id": session_id,
        }

    def _mock_score(self, q: dict) -> dict:
        """基于题目难度生成模拟评分（正式版替换为 LLM 评分）"""
        diff_map = {"easy": (70, 90), "medium": (55, 80), "hard": (40, 70)}
        lo, hi = diff_map.get(q.get("difficulty", "medium"), (50, 75))
        score = random.randint(lo, hi)

        if score >= 80:
            comment = "回答清晰，核心思路正确，对复杂度有较好理解。"
            strengths = ["逻辑清晰", "核心思路正确"]
            weaknesses = ["可以补充边界条件讨论"]
        elif score >= 60:
            comment = "基本方向正确，但部分细节表述不够精准，需要加强深入理解。"
            strengths = ["方向正确", "有基本思路"]
            weaknesses = ["细节不够精准", "缺少复杂度分析"]
        else:
            comment = "思路不够清晰，核心概念理解有偏差，建议加强基础复习。"
            strengths = ["有尝试回答"]
            weaknesses = ["核心概念理解偏差", "缺少结构化思维"]

        return {"score": score, "comment": comment, "strengths": strengths, "weaknesses": weaknesses}

    def _generate_report(self, session_id: str) -> dict:
        """生成面试报告"""
        s = self._sessions.get(session_id)
        if not s:
            return {"error": "会话不存在"}

        scores = s.scores
        if not scores:
            return {"phase": "done", "message": "无评分数据", "session_id": session_id}

        avg_score = sum(x["score"] for x in scores) / len(scores)

        if avg_score >= 80:
            level = "优秀"
            summary = "你在本次模拟面试中表现优秀，展现了扎实的技术功底和清晰的表达能力。继续保持！"
        elif avg_score >= 60:
            level = "良好"
            summary = "你展现了基本的技术能力，但在深度和细节上还有提升空间。建议针对薄弱环节加强训练。"
        else:
            level = "需要提升"
            summary = "本次面试暴露出一些基础薄弱环节。建议根据以下分析进行针对性复习，再次练习。"

        all_weaknesses: list[str] = []
        all_strengths: list[str] = []
        for sc in scores:
            all_strengths.extend(sc.get("strengths", []))
            all_weaknesses.extend(sc.get("weaknesses", []))

        return {
            "phase": "report",
            "session_id": session_id,
            "interview_type": s.interview_type,
            "interview_type_label": INTERVIEW_TYPES.get(s.interview_type, {}).get("label", s.interview_type),
            "total_questions": len(s.questions),
            "average_score": round(avg_score),
            "level": level,
            "summary": summary,
            "scores": scores,
            "strengths": list(set(all_strengths))[:5],
            "weaknesses": list(set(all_weaknesses))[:5],
            "duration_seconds": int(time.time() - s.started_at),
            "new_achievements": record_interview(avg_score, s.interview_type, s.user_id),
        }

    def _generate_system_design_followup(self, s: InterviewSession, q: dict, answer: str) -> dict:
        """系统设计面试：根据回答用 LLM 生成追问（带 fallback）"""
        # 先检查是否有预置追问
        follow_ups = q.get("follow_ups", [])
        if s.follow_up_index < len(follow_ups):
            fu = follow_ups[s.follow_up_index]
            s.follow_up_index += 1
            s.phase = "follow_up"
            return {
                "phase": "follow_up",
                "follow_up": fu,
                "follow_up_index": s.follow_up_index,
                "total_follow_ups": len(follow_ups),
                "session_id": s.session_id,
            }

        # 没有更多预置追问 → 评分推进
        return self._score_and_next(s.session_id)

    def get_next(self, session_id: str) -> dict:
        """获取下一题（评分后调用）"""
        s = self._sessions.get(session_id)
        if not s:
            return {"error": "会话不存在"}
        if s.phase == "done":
            return self._generate_report(session_id)
        return self.start_question(session_id)


interview_agent = InterviewAgent()
