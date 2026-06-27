"""基础评估服务 — 按语言出题 + 自动评分 + 等级判定 + 学习建议"""

from services.question_generator import generate_assessment, get_question_by_id
from services.error_book import record_error
from typing import Any

# 评分等级划分
LEVEL_RULES = [
    (0, 30, "入门", "建议从基础语法、变量类型、控制流开始系统学习"),
    (30, 60, "初级", "基础不牢固，建议重点攻克核心概念（函数、类、异常处理）"),
    (60, 80, "中级", "基础扎实，可以进阶到设计模式、算法优化、项目实战"),
    (80, 101, "高级", "基础优秀，建议深入系统设计、源码阅读、开源贡献"),
]

# 各语言评估题库（10 题/语言，覆盖不同难度和主题）
ASSESSMENT_BANK: dict[str, list[dict[str, Any]]] = {
    "python": [
        {
            "id": "py_q1",
            "question": "Python 中，以下哪个是可变数据类型？",
            "options": ["A) int", "B) str", "C) list", "D) tuple", "E) 我不清楚"],
            "answer": 2,
            "difficulty": "easy",
            "topic": "数据类型",
            "explanation": "list 是可变类型，可以原地修改。int、str、tuple 都是不可变类型。"
        },
        {
            "id": "py_q2",
            "question": "以下代码输出什么？\nprint(3 * 'ab')",
            "options": ["A) 'ababab'", "B) '3ab'", "C) 报错", "D) 'ab3'", "E) 我不清楚"],
            "answer": 0,
            "difficulty": "easy",
            "topic": "字符串操作",
            "explanation": "Python 中字符串与整数相乘表示重复：'ab' * 3 = 'ababab'。"
        },
        {
            "id": "py_q3",
            "question": "下面哪个是正确的列表推导式？",
            "options": [
                "A) [x for x in range(5)]",
                "B) [for x in range(5): x]",
                "C) (x for x in range(5))",
                "D) {x for x in range(5)}",
                "E) 我不清楚"
            ],
            "answer": 0,
            "difficulty": "easy",
            "topic": "列表推导式",
            "explanation": "A 是列表推导式返回 list。C 是生成器表达式返回 generator。D 是集合推导式。"
        },
        {
            "id": "py_q4",
            "question": "以下代码的输出是什么？\ndef f(a, lst=[]):\n    lst.append(a)\n    return lst\nprint(f(1))\nprint(f(2))",
            "options": [
                "A) [1] 和 [2]",
                "B) [1] 和 [1, 2]",
                "C) 报错",
                "D) [1, 2] 和 [1, 2]",
                "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "medium",
            "topic": "Python陷阱",
            "explanation": "Python 的默认参数只在函数定义时求值一次，所以 lst 在多次调用间共享。第一次返回 [1]，第二次返回 [1, 2]。"
        },
        {
            "id": "py_q5",
            "question": "Python 中 @staticmethod 和 @classmethod 的区别是？",
            "options": [
                "A) 没有区别",
                "B) staticmethod 不接收类引用，classmethod 接收 cls 参数",
                "C) staticmethod 更快",
                "D) classmethod 不能被子类继承",
                "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "medium",
            "topic": "装饰器",
            "explanation": "@staticmethod 不自动传递任何隐式参数；@classmethod 自动传递类本身作为第一个参数 cls。"
        },
        {
            "id": "py_q6",
            "question": "Python 中 __init__ 和 __new__ 的执行顺序是？",
            "options": [
                "A) __init__ 先执行",
                "B) __new__ 先执行，然后 __init__",
                "C) 同时执行",
                "D) 取决于类定义",
                "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "medium",
            "topic": "面向对象",
            "explanation": "__new__ 负责创建实例（分配内存），__init__ 负责初始化实例。所以 __new__ 先执行。"
        },
        {
            "id": "py_q7",
            "question": "以下哪个操作的时间复杂度是 O(1)？",
            "options": [
                "A) 在列表末尾 append",
                "B) 在列表头部 insert",
                "C) 在列表中查找元素",
                "D) 对列表排序",
                "E) 我不清楚"
            ],
            "answer": 0,
            "difficulty": "medium",
            "topic": "时间复杂度",
            "explanation": "list.append 是均摊 O(1)。insert(0) 需要移动所有元素是 O(n)，查找是 O(n)，排序是 O(n log n)。"
        },
        {
            "id": "py_q8",
            "question": "asyncio 的核心概念是什么？",
            "options": [
                "A) 多线程并行",
                "B) 事件循环驱动的协程调度",
                "C) 多进程通信",
                "D) 信号量同步",
                "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "hard",
            "topic": "异步编程",
            "explanation": "asyncio 基于事件循环（event loop），使用协程实现协作式多任务，适用于 I/O 密集型场景。"
        },
        {
            "id": "py_q9",
            "question": "Python 中 GIL（全局解释器锁）的影响是什么？",
            "options": [
                "A) 禁止使用多线程",
                "B) CPU 密集型任务多线程无法利用多核",
                "C) 影响异步 I/O 性能",
                "D) 所有 Python 代码只能串行执行",
                "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "hard",
            "topic": "GIL",
            "explanation": "GIL 确保同一时刻只有一个线程执行 Python 字节码，CPU 密集型任务用多线程无法加速。I/O 密集型不受明显影响。"
        },
        {
            "id": "py_q10",
            "question": "Python 中如何实现一个线程安全的单例？",
            "options": [
                "A) 使用全局变量",
                "B) 使用模块级别实例",
                "C) 在 __new__ 中加锁控制",
                "D) B 和 C 都可以",
                "E) 我不清楚"
            ],
            "answer": 3,
            "difficulty": "hard",
            "topic": "设计模式",
            "explanation": "模块级别导入时天然线程安全（最简单）。在 __new__ 中加 threading.Lock 也可以实现懒加载式线程安全单例。"
        },
    ],
    "javascript": [
        {
            "id": "js_q1", "question": "typeof null 的结果是？",
            "options": ["A) 'null'", "B) 'object'", "C) 'undefined'", "D) 'boolean'", "E) 我不清楚"],
            "answer": 1, "difficulty": "easy", "topic": "类型系统",
            "explanation": "这是 JavaScript 的历史遗留 bug，typeof null 返回 'object'。"
        },
        {
            "id": "js_q2", "question": "以下哪个方法可以将 JSON 字符串转为对象？",
            "options": ["A) JSON.stringify()", "B) JSON.parse()", "C) JSON.convert()", "D) JSON.toObject()", "E) 我不清楚"],
            "answer": 1, "difficulty": "easy", "topic": "JSON",
            "explanation": "JSON.parse() 将 JSON 字符串解析为 JavaScript 对象。stringify 是反向操作。"
        },
        {
            "id": "js_q3", "question": "let 和 var 的主要区别是什么？",
            "options": [
                "A) 没有区别",
                "B) let 有块级作用域，var 是函数作用域",
                "C) let 不能被重新赋值",
                "D) var 更快",
                "E) 我不清楚"
            ],
            "answer": 1, "difficulty": "easy", "topic": "变量声明",
            "explanation": "let 和 const 有块级作用域（{}），var 只有函数作用域，且存在变量提升问题。"
        },
        {
            "id": "js_q4", "question": "以下代码输出什么？\nconsole.log(0.1 + 0.2 === 0.3)",
            "options": ["A) true", "B) false", "C) undefined", "D) 报错", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "浮点数",
            "explanation": "JavaScript 使用 IEEE 754 浮点数，0.1 + 0.2 = 0.30000000000000004 ≠ 0.3。"
        },
        {
            "id": "js_q5", "question": "Promise 的三种状态是？",
            "options": [
                "A) start / running / end",
                "B) pending / fulfilled / rejected",
                "C) open / in-progress / closed",
                "D) begin / success / fail",
                "E) 我不清楚"
            ],
            "answer": 1, "difficulty": "medium", "topic": "Promise",
            "explanation": "Promise 只有三种状态：pending（等待）、fulfilled（成功）、rejected（失败），且状态不可逆。"
        },
        {
            "id": "js_q6", "question": "事件循环中，微任务和宏任务的执行顺序是？",
            "options": [
                "A) 宏任务优先",
                "B) 微任务优先，每个宏任务后清空微任务队列",
                "C) 交替执行",
                "D) 随机顺序",
                "E) 我不清楚"
            ],
            "answer": 1, "difficulty": "medium", "topic": "事件循环",
            "explanation": "每次执行一个宏任务后，会清空微任务队列（Promise.then/catch/finally、MutationObserver 等）。"
        },
        {
            "id": "js_q7", "question": "以下哪个是闭包的正确描述？",
            "options": [
                "A) 函数内部定义的变量",
                "B) 函数可以访问其外部作用域的变量，即使外部函数已返回",
                "C) 匿名函数",
                "D) 箭头函数",
                "E) 我不清楚"
            ],
            "answer": 1, "difficulty": "medium", "topic": "闭包",
            "explanation": "闭包（Closure）是函数 + 其词法环境的组合，允许内部函数访问外部函数变量。"
        },
        {
            "id": "js_q8", "question": "== 和 === 的区别是？",
            "options": [
                "A) 完全相同",
                "B) == 会类型转换再比较，=== 不会",
                "C) === 会类型转换再比较，== 不会",
                "D) === 比较引用，== 比较值",
                "E) 我不清楚"
            ],
            "answer": 1, "difficulty": "easy", "topic": "运算符",
            "explanation": "== 允许类型强制转换（'5' == 5 为 true），=== 严格比较值和类型（'5' === 5 为 false）。"
        },
        {
            "id": "js_q9", "question": "async/await 是基于什么实现的语法糖？",
            "options": ["A) Callback", "B) Promise + Generator", "C) setTimeout", "D) XMLHttpRequest", "E) 我不清楚"],
            "answer": 1, "difficulty": "hard", "topic": "异步编程",
            "explanation": "async/await 是 Promise + Generator 的语法糖，async 函数始终返回 Promise。"
        },
        {
            "id": "js_q10", "question": "以下哪个操作会导致内存泄漏？",
            "options": [
                "A) 使用 let 声明变量",
                "B) 未清除的 setInterval + 闭包引用",
                "C) 使用箭头函数",
                "D) 使用 const",
                "E) 我不清楚"
            ],
            "answer": 1, "difficulty": "hard", "topic": "内存管理",
            "explanation": "未清除的定时器持有闭包引用，阻止垃圾回收。此外，DOM 引用未释放、全局变量滥用也是常见原因。"
        },
    ],
}


def get_assessment(language: str, count: int = 10) -> list[dict[str, Any]]:
    """获取指定语言的评估题目（随机 count 道），去掉 answer 字段"""
    return generate_assessment(language, count)


def grade_assessment(language: str, answers: list[int], question_ids: list[str] | None = None) -> dict[str, Any]:
    """根据用户答案评分并返回等级与学习建议"""
    # 通过 question_generator 获取完整题目（含 answer）
    questions: list[dict] = []
    if question_ids:
        for qid in question_ids:
            q = get_question_by_id(language, qid)
            if q:
                questions.append(q)

    if not questions:
        return {
            "score": 0, "correct": 0, "unsure": 0, "total": 0,
            "level": "", "advice": "无题目可评分",
            "details": [], "weak_topics": [],
            "error_recorded": 0, "language": language,
        }

    if len(answers) != len(questions):
        answers = (answers + [0] * len(questions))[:len(questions)]

    correct = 0
    unsure_count = 0
    details = []
    error_recorded = 0

    for i, q in enumerate(questions):
        user_ans = answers[i] if i < len(answers) else -1
        is_unsure = user_ans == 4  # E) 我不清楚
        if is_unsure:
            unsure_count += 1
        is_correct = (not is_unsure) and (user_ans == q["answer"])
        if is_correct:
            correct += 1

        detail = {
            "id": q["id"],
            "question": q["question"],
            "user_answer": user_ans,
            "correct_answer": q["answer"],
            "correct_label": q["options"][q["answer"]] if q["answer"] < len(q["options"]) else "未知",
            "is_correct": is_correct,
            "is_unsure": is_unsure,
            "explanation": q["explanation"],
            "difficulty": q["difficulty"],
            "topic": q["topic"],
        }
        details.append(detail)

        # 错题记录：做错 且 非"我不清楚"
        if not is_correct and not is_unsure:
            record_error(language, q)
            error_recorded += 1

    score = int(correct / len(questions) * 100)

    # 判定等级
    level_name = ""
    level_advice = ""
    for lo, hi, name, advice in LEVEL_RULES:
        if lo <= score < hi:
            level_name = name
            level_advice = advice
            break

    # 按难度统计正确率
    difficulty_stats = {}
    topic_stats = {}
    for d in details:
        diff = d["difficulty"]
        if diff not in difficulty_stats:
            difficulty_stats[diff] = {"total": 0, "correct": 0}
        difficulty_stats[diff]["total"] += 1
        if d["is_correct"]:
            difficulty_stats[diff]["correct"] += 1

        topic = d["topic"]
        if topic not in topic_stats:
            topic_stats[topic] = {"total": 0, "correct": 0}
        topic_stats[topic]["total"] += 1
        if d["is_correct"]:
            topic_stats[topic]["correct"] += 1

    # 生成弱项列表
    weak_topics = [
        t for t, s in topic_stats.items()
        if s["correct"] < s["total"]
    ]

    return {
        "score": score,
        "correct": correct,
        "unsure": unsure_count,
        "total": len(questions),
        "level": level_name,
        "advice": level_advice,
        "details": details,
        "topic_stats": topic_stats,
        "difficulty_stats": difficulty_stats,
        "weak_topics": weak_topics,
        "error_recorded": error_recorded,
        "language": language,
    }

