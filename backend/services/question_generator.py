"""出题人服务 — 独立出题模块，题库管理与随机抽题"""

import random
from typing import Any

from .multi_lang_assessment import MULTI_LANG_QUESTION_BANK

# ============================================================
# Python 题库（50 道，覆盖 13 个主题）
# 难度分布：easy ≈25、medium ≈15、hard ≈10
# id 格式：py_q1 ~ py_q50（保留 py_q1~py_q10 向后兼容）
# ============================================================

QUESTION_BANK: dict[str, list[dict[str, Any]]] = {
    "python": [
        # ==================== 数据类型（easy ×3, medium ×1） ====================
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
            "id": "py_q11",
            "question": "以下哪个表达式的值为 True？",
            "options": [
                "A) type(42) == float",
                "B) isinstance(True, int)",
                "C) type([]) == tuple",
                "D) type({}) == list",
                "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "easy",
            "topic": "数据类型",
            "explanation": "Python 中 bool 是 int 的子类，所以 isinstance(True, int) 返回 True。"
        },
        {
            "id": "py_q12",
            "question": "以下代码输出什么？\nx = {1, 2, 2, 3}\nprint(x)",
            "options": [
                "A) {1, 2, 2, 3}",
                "B) {1, 2, 3}",
                "C) [1, 2, 3]",
                "D) 报错",
                "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "easy",
            "topic": "数据类型",
            "explanation": "set 自动去重，重复的 2 被合并为 1 个，输出为 {1, 2, 3}。"
        },
        {
            "id": "py_q13",
            "question": "以下哪个关于 frozenset 的描述是正确的？",
            "options": [
                "A) frozenset 可以用 add() 添加元素",
                "B) frozenset 是可哈希的，可作为 dict 的 key",
                "C) frozenset 和 set 完全相同",
                "D) frozenset 是有序的",
                "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "medium",
            "topic": "数据类型",
            "explanation": "frozenset 是不可变集合，因此可哈希，可以作为 dict 的 key 或 set 的元素。set 是可变的，不可哈希。"
        },

        # ==================== 控制流（easy ×2, medium ×1） ====================
        {
            "id": "py_q14",
            "question": "以下代码输出什么？\nfor i in range(3):\n    if i == 1:\n        continue\n    print(i, end=' ')",
            "options": [
                "A) 0 1 2",
                "B) 0 2",
                "C) 1",
                "D) 0",
                "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "easy",
            "topic": "控制流",
            "explanation": "continue 跳过当前迭代的后续代码进入下一轮，i==1 时不打印，所以输出 0 2。"
        },
        {
            "id": "py_q15",
            "question": "以下代码输出什么？\nfor i in range(3):\n    pass\nprint(i)",
            "options": [
                "A) 0",
                "B) 2",
                "C) 3",
                "D) NameError",
                "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "easy",
            "topic": "控制流",
            "explanation": "Python 的 for 循环变量在循环结束后仍然存在于作用域中，值为最后一次迭代的值 2。"
        },
        {
            "id": "py_q16",
            "question": "以下关于 for-else 的说法哪个正确？",
            "options": [
                "A) else 块在循环每次迭代后都执行",
                "B) else 块只在循环正常结束（未被 break 打断）时执行",
                "C) else 块永远不会执行",
                "D) for-else 语法不存在",
                "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "medium",
            "topic": "控制流",
            "explanation": "Python 的 for-else / while-else 中，else 块仅在循环正常结束（未被 break 跳出）时执行，常用于查找后未找到的场景。"
        },

        # ==================== 函数（easy ×2, medium ×1, hard ×1） ====================
        {
            "id": "py_q17",
            "question": "以下代码输出什么？\ndef add(a, b=3):\n    return a + b\nprint(add(5))",
            "options": [
                "A) 8", "B) 5", "C) 报错（缺少参数）",
                "D) 3", "E) 我不清楚"
            ],
            "answer": 0,
            "difficulty": "easy",
            "topic": "函数",
            "explanation": "b 有默认值 3，add(5) 等价于 add(5, 3)，返回 8。"
        },
        {
            "id": "py_q18",
            "question": "以下代码输出什么？\ndef f(*args):\n    return sum(args)\nprint(f(1, 2, 3, 4))",
            "options": [
                "A) 1", "B) 10", "C) (1, 2, 3, 4)",
                "D) 报错", "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "easy",
            "topic": "函数",
            "explanation": "*args 将位置参数打包为元组 (1, 2, 3, 4)，sum() 求和得 10。"
        },
        {
            "id": "py_q19",
            "question": "以下代码输出什么？\ndef f(**kwargs):\n    return kwargs.get('x', 0)\nprint(f(x=10, y=20))",
            "options": [
                "A) 0", "B) 10", "C) {'x': 10, 'y': 20}",
                "D) 报错", "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "medium",
            "topic": "函数",
            "explanation": "**kwargs 把关键字参数打包为字典，kwargs.get('x', 0) 获取 key 'x' 的值 10。"
        },
        {
            "id": "py_q20",
            "question": "以下代码输出什么？\ndef outer():\n    x = 5\n    def inner():\n        nonlocal x\n        x = 10\n    inner()\n    return x\nprint(outer())",
            "options": [
                "A) 5", "B) 10", "C) SyntaxError",
                "D) UnboundLocalError", "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "hard",
            "topic": "函数",
            "explanation": "nonlocal 声明表示 x 不是 inner 的局部变量，而是外层函数 outer 的变量，修改会影响到 outer 中的 x，所以返回 10。"
        },

        # ==================== 列表操作（easy ×2, medium ×1） ====================
        {
            "id": "py_q21",
            "question": "以下代码输出什么？\nlst = [1, 2, 3]\nlst.append([4, 5])\nprint(len(lst))",
            "options": [
                "A) 3", "B) 4", "C) 5",
                "D) 报错", "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "easy",
            "topic": "列表操作",
            "explanation": "append 将 [4, 5] 作为一个整体元素加入，lst 变为 [1, 2, 3, [4, 5]]，长度为 4。"
        },
        {
            "id": "py_q22",
            "question": "以下代码输出什么？\nlst = [1, 2, 3]\nlst.extend([4, 5])\nprint(len(lst))",
            "options": [
                "A) 3", "B) 4", "C) 5",
                "D) 6", "E) 我不清楚"
            ],
            "answer": 2,
            "difficulty": "easy",
            "topic": "列表操作",
            "explanation": "extend 将可迭代对象中的每个元素逐一加入列表，lst 变为 [1, 2, 3, 4, 5]，长度为 5。"
        },
        {
            "id": "py_q23",
            "question": "以下代码输出什么？\nlst = [1, 2, 3, 4, 5]\nprint(lst[1:4:2])",
            "options": [
                "A) [1, 3]", "B) [2, 4]", "C) [2, 3, 4]",
                "D) [1, 4]", "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "medium",
            "topic": "列表操作",
            "explanation": "切片 lst[start:stop:step] 即 lst[1:4:2] 从索引 1 开始到 4（不含），步长 2，取出 lst[1]=2 和 lst[3]=4。"
        },

        # ==================== 字典操作（easy ×2, medium ×1） ====================
        {
            "id": "py_q24",
            "question": "以下代码输出什么？\nd = {'a': 1, 'b': 2}\nprint(d.get('c', 0))",
            "options": [
                "A) None", "B) 0", "C) KeyError",
                "D) 'c'", "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "easy",
            "topic": "字典操作",
            "explanation": "dict.get(key, default) 在 key 不存在时返回 default 值而不抛出异常，所以返回 0。"
        },
        {
            "id": "py_q25",
            "question": "以下代码输出什么？\nd1 = {'a': 1}\nd2 = {'b': 2}\nprint({**d1, **d2})",
            "options": [
                "A) {'a': 1, 'b': 2}", "B) [('a', 1), ('b', 2)]",
                "C) 报错", "D) {'a': 1}", "E) 我不清楚"
            ],
            "answer": 0,
            "difficulty": "easy",
            "topic": "字典操作",
            "explanation": "** 解包运算符可以合并字典，{**d1, **d2} 等价于 {'a': 1, 'b': 2}。如有重复 key，后面的覆盖前面。"
        },
        {
            "id": "py_q26",
            "question": "以下代码输出什么？\nd = {'x': 1, 'y': 2, 'z': 3}\nresult = [(k, v) for k, v in d.items() if v > 1]\nprint(result)",
            "options": [
                "A) {'y': 2, 'z': 3}",
                "B) [('y', 2), ('z', 3)]",
                "C) ('y', 2), ('z', 3)",
                "D) [('y', 2), ('z', 3), ('x', 1)]",
                "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "medium",
            "topic": "字典操作",
            "explanation": "字典推导式结合条件过滤，取出 v > 1 的键值对组成元组列表。"
        },

        # ==================== 字符串（easy ×2, medium ×1） ====================
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
            "id": "py_q27",
            "question": "以下代码输出什么？\ns = 'hello world'\nprint(s.split('o'))",
            "options": [
                "A) ['hell', ' w', 'rld']",
                "B) ['hell', 'w', 'rld']",
                "C) ['hello', 'world']",
                "D) 'hell w rld'",
                "E) 我不清楚"
            ],
            "answer": 0,
            "difficulty": "easy",
            "topic": "字符串操作",
            "explanation": "split('o') 以 'o' 为分隔符分割，'hello world' 中包含两个 'o'，结果为 ['hell', ' w', 'rld']。"
        },
        {
            "id": "py_q28",
            "question": "以下哪个方法可以判断一个字符串是否全由数字组成？",
            "options": [
                "A) str.isalpha()",
                "B) str.isdigit()",
                "C) str.isnumeric()",
                "D) B 和 C 都可以",
                "E) 我不清楚"
            ],
            "answer": 3,
            "difficulty": "medium",
            "topic": "字符串操作",
            "explanation": "isdigit() 和 isnumeric() 都能判断是否全为数字字符。isnumeric 范围更广（包括中文数字等），isdigit 仅限 0-9。"
        },

        # ==================== 面向对象（easy ×1, medium ×2, hard ×1） ====================
        {
            "id": "py_q29",
            "question": "以下关于 __init__ 方法的描述哪个是正确的？",
            "options": [
                "A) __init__ 用于创建实例",
                "B) __init__ 是类的构造器，用于初始化实例属性",
                "C) 每个类必须定义 __init__",
                "D) __init__ 在类被定义时自动调用",
                "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "easy",
            "topic": "面向对象",
            "explanation": "__init__ 是初始化方法（不是构造器，构造器是 __new__），在实例创建后自动调用，用于设置实例属性的初始值。"
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
            "id": "py_q30",
            "question": "以下关于 super() 的描述哪个是正确的？",
            "options": [
                "A) super() 只能调用直接父类的方法",
                "B) super() 按 MRO（方法解析顺序）查找下一个类的方法",
                "C) super() 等价于 self.__parent__",
                "D) super() 只能在 __init__ 中使用",
                "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "hard",
            "topic": "面向对象",
            "explanation": "super() 按照 MRO（Method Resolution Order）线性顺序查找下一个类，在多重继承中保证每个父类方法只调用一次。"
        },
        {
            "id": "py_q31",
            "question": "以下代码输出什么？\nclass A:\n    def __getattr__(self, name):\n        return name.upper()\na = A()\nprint(a.hello)",
            "options": [
                "A) AttributeError",
                "B) 'HELLO'",
                "C) 'hello'",
                "D) None",
                "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "hard",
            "topic": "面向对象",
            "explanation": "__getattr__ 仅在常规属性查找失败时被调用。a.hello 不存在，触发 __getattr__('hello')，返回 'HELLO'。"
        },

        # ==================== 异常处理（easy ×1, medium ×2） ====================
        {
            "id": "py_q32",
            "question": "以下代码输出什么？\ntry:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print('A')\nfinally:\n    print('B')",
            "options": [
                "A) A", "B) B", "C) A 换行 B",
                "D) 不输出", "E) 我不清楚"
            ],
            "answer": 2,
            "difficulty": "easy",
            "topic": "异常处理",
            "explanation": "except 捕获 ZeroDivisionError 打印 'A'，finally 块无论是否发生异常都会执行，打印 'B'。"
        },
        {
            "id": "py_q33",
            "question": "以下代码输出什么？\ntry:\n    raise ValueError('err')\nexcept Exception as e:\n    print(type(e).__name__)",
            "options": [
                "A) Exception", "B) ValueError",
                "C) 'err'", "D) TypeError", "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "medium",
            "topic": "异常处理",
            "explanation": "ValueError 是 Exception 的子类，except Exception 可以捕获它，type(e).__name__ 返回 'ValueError'。"
        },
        {
            "id": "py_q34",
            "question": "以下关于 raise from 的说法哪个正确？",
            "options": [
                "A) raise from 用于抛出多个异常",
                "B) raise X from Y 将 Y 设为 X 的 __cause__，形成异常链",
                "C) raise from 语法不存在",
                "D) raise from 等价于 raise",
                "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "medium",
            "topic": "异常处理",
            "explanation": "raise X from Y 设置 X.__cause__ = Y，形成异常链。捕获异常后转化时用此语法保留原始异常信息。"
        },

        # ==================== 文件IO（easy ×1, medium ×1） ====================
        {
            "id": "py_q35",
            "question": "使用 with open('file.txt', 'r') as f 的好处是什么？",
            "options": [
                "A) 自动关闭文件，即使发生异常",
                "B) 文件读取更快",
                "C) 无需指定文件名",
                "D) 可以同时读写",
                "E) 我不清楚"
            ],
            "answer": 0,
            "difficulty": "easy",
            "topic": "文件IO",
            "explanation": "with 语句使用上下文管理器，确保文件在代码块结束后自动关闭，即使发生异常也会执行 __exit__ 关闭文件。"
        },
        {
            "id": "py_q36",
            "question": "以下哪个模式可以以二进制方式写入文件？",
            "options": [
                "A) 'w'", "B) 'wb'", "C) 'w+'",
                "D) 'bw'", "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "easy",
            "topic": "文件IO",
            "explanation": "'wb' 表示二进制写模式（write binary），适合写入图片、音频等非文本数据。'w' 是文本模式。'w+' 是可读写模式。"
        },

        # ==================== 装饰器（easy ×1, medium ×1, hard ×1） ====================
        {
            "id": "py_q37",
            "question": "以下哪个是装饰器的本质？",
            "options": [
                "A) 一种特殊语法，只有 @ 符号",
                "B) 一个接收函数并返回新函数的高阶函数",
                "C) 一种类定义方式",
                "D) 一种模块导入方式",
                "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "easy",
            "topic": "装饰器",
            "explanation": "装饰器本质上是一个高阶函数：接收一个函数作为参数，返回一个新函数（通常包装了原函数的功能）。"
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
            "id": "py_q38",
            "question": "以下代码输出什么？\ndef dec(func):\n    def wrapper(*a, **kw):\n        return func(*a, **kw) * 2\n    return wrapper\n@dec\ndef add(x, y):\n    return x + y\nprint(add(3, 4))",
            "options": [
                "A) 7", "B) 14", "C) 报错",
                "D) 3", "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "hard",
            "topic": "装饰器",
            "explanation": "@dec 等价于 add = dec(add)。wrapper 调用原 add(3, 4) 得 7，再 * 2 得 14。"
        },

        # ==================== 生成器（easy ×1, medium ×1, hard ×1） ====================
        {
            "id": "py_q39",
            "question": "以下代码中 g 是什么类型？\ng = (x**2 for x in range(5))",
            "options": [
                "A) list", "B) tuple", "C) generator",
                "D) set", "E) 我不清楚"
            ],
            "answer": 2,
            "difficulty": "easy",
            "topic": "生成器",
            "explanation": "圆括号 (x**2 for x in range(5)) 是生成器表达式，创建的是 generator 对象，惰性求值，内存高效。"
        },
        {
            "id": "py_q40",
            "question": "以下代码输出什么？\ndef gen():\n    yield 1\n    yield 2\n    yield 3\ng = gen()\nprint(sum(g))",
            "options": [
                "A) 0", "B) 6", "C) 报错",
                "D) 1", "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "medium",
            "topic": "生成器",
            "explanation": "sum() 可以消费任何可迭代对象，包括生成器。gen() 逐个 yield 1、2、3，sum 遍历它们得到 6。"
        },
        {
            "id": "py_q41",
            "question": "yield from 的作用是什么？",
            "options": [
                "A) 与 yield 完全相同",
                "B) 将迭代委托给另一个生成器/可迭代对象",
                "C) 终止生成器",
                "D) 并发执行多个生成器",
                "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "hard",
            "topic": "生成器",
            "explanation": "yield from iterable 把迭代委托给子生成器，自动处理 send/throw/close，是生成器间的双向通道。"
        },

        # ==================== GIL/并发（easy ×1, medium ×1, hard ×1） ====================
        {
            "id": "py_q42",
            "question": "Python 中 threading 和 asyncio 的主要适用场景分别是什么？",
            "options": [
                "A) threading 适合 I/O 密集、asyncio 适合 CPU 密集",
                "B) asyncio 适合 I/O 密集、threading 适合 CPU 密集",
                "C) 两者都适合 I/O 密集，asyncio 单线程无锁开销",
                "D) 两者完全相同",
                "E) 我不清楚"
            ],
            "answer": 2,
            "difficulty": "easy",
            "topic": "GIL/并发",
            "explanation": "GIL 下 threading 的 CPU 密集任务无法利用多核。asyncio 单线程协程切换，适合高并发 I/O，无锁竞争。"
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
            "topic": "GIL/并发",
            "explanation": "GIL 确保同一时刻只有一个线程执行 Python 字节码，CPU 密集型任务用多线程无法加速。I/O 密集型不受明显影响。"
        },
        {
            "id": "py_q43",
            "question": "以下关于 multiprocessing 的说法哪个正确？",
            "options": [
                "A) multiprocessing 受 GIL 限制，无法利用多核",
                "B) 每个进程有独立 Python 解释器和 GIL，可以真正并行",
                "C) multiprocessing 比 threading 更轻量",
                "D) multiprocessing 不能共享数据",
                "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "hard",
            "topic": "GIL/并发",
            "explanation": "multiprocessing 创建独立进程，每个进程有自己的 Python 解释器和 GIL，可以实现真正的多核并行，但进程间通信开销比线程大。"
        },

        # ==================== 常用库（easy ×1, medium ×1, hard ×1） ====================
        {
            "id": "py_q44",
            "question": "以下哪个是 Python 标准库中用于处理 JSON 的模块？",
            "options": [
                "A) yaml", "B) json", "C) xml",
                "D) pickle", "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "easy",
            "topic": "常用库",
            "explanation": "json 是 Python 标准库中用于编码和解码 JSON 数据的模块，提供 json.dumps() 和 json.loads() 等方法。"
        },
        {
            "id": "py_q45",
            "question": "以下代码的作用是什么？\nfrom collections import defaultdict\nd = defaultdict(int)\nd['a'] += 1",
            "options": [
                "A) 报 KeyError",
                "B) 自动为不存在的 key 创建默认值（int 的默认值为 0）",
                "C) 创建普通字典",
                "D) 将 'a' 的值设为 1",
                "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "medium",
            "topic": "常用库",
            "explanation": "defaultdict(int) 在访问不存在的 key 时自动调用 int() 返回 0，所以 d['a'] += 1 等价于 d['a'] = 0 + 1 = 1。"
        },
        {
            "id": "py_q46",
            "question": "itertools.chain 的作用是什么？",
            "options": [
                "A) 将一个可迭代对象拆分为多个",
                "B) 将多个可迭代对象串联为一个迭代器",
                "C) 对可迭代对象排序",
                "D) 过滤可迭代对象",
                "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "hard",
            "topic": "常用库",
            "explanation": "itertools.chain(*iterables) 将多个可迭代对象串联，依次产出每个可迭代对象的元素，常用于合并遍历多个序列。"
        },

        # ==================== 列表推导式（easy ×1, medium ×1） ====================
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
            "topic": "列表操作",
            "explanation": "A 是列表推导式返回 list。C 是生成器表达式返回 generator。D 是集合推导式。"
        },
        {
            "id": "py_q47",
            "question": "以下代码输出什么？\nmatrix = [[1,2,3], [4,5,6]]\nflat = [x for row in matrix for x in row if x % 2 == 0]\nprint(flat)",
            "options": [
                "A) [1, 3, 5]", "B) [2, 4, 6]",
                "C) [1, 2, 3, 4, 5, 6]", "D) []",
                "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "medium",
            "topic": "列表操作",
            "explanation": "嵌套列表推导式先遍历 matrix 的每一行，再遍历每行的每个元素，过滤出偶数：2、4、6。"
        },

        # ==================== Python陷阱（medium ×1） ====================
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
            "topic": "函数",
            "explanation": "Python 的默认参数只在函数定义时求值一次，所以 lst 在多次调用间共享。第一次返回 [1]，第二次返回 [1, 2]。"
        },

        # ==================== 时间复杂度（medium ×1） ====================
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
            "topic": "常用库",
            "explanation": "list.append 是均摊 O(1)。insert(0) 需要移动所有元素是 O(n)，查找是 O(n)，排序是 O(n log n)。"
        },

        # ==================== 异步编程/设计模式（hard ×2） ====================
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
            "topic": "GIL/并发",
            "explanation": "asyncio 基于事件循环（event loop），使用协程实现协作式多任务，适用于 I/O 密集型场景。"
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
            "topic": "面向对象",
            "explanation": "模块级别导入时天然线程安全（最简单）。在 __new__ 中加 threading.Lock 也可以实现懒加载式线程安全单例。"
        },

        # ==================== 补充：其他覆盖主题的题目 ====================
        {
            "id": "py_q48",
            "question": "以下代码输出什么？\na = [1, 2, 3]\nb = a\nb.append(4)\nprint(a)",
            "options": [
                "A) [1, 2, 3]", "B) [1, 2, 3, 4]",
                "C) [1, 2, 3, 4, 4]",
                "D) 报错", "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "easy",
            "topic": "数据类型",
            "explanation": "b = a 是引用传递，b 和 a 指向同一个列表对象。b.append(4) 同时修改了 a，a 变为 [1, 2, 3, 4]。"
        },
        {
            "id": "py_q49",
            "question": "以下代码输出什么？\nx = [1, 2, 3]\ny = x.copy()\ny[0] = 99\nprint(x[0])",
            "options": [
                "A) 1", "B) 99", "C) 报错",
                "D) None", "E) 我不清楚"
            ],
            "answer": 0,
            "difficulty": "easy",
            "topic": "数据类型",
            "explanation": "x.copy() 创建浅拷贝，y 是独立的新列表。修改 y 不影响 x，x[0] 仍为 1。"
        },
        {
            "id": "py_q50",
            "question": "以下代码输出什么？\nresult = all([True, True, False])\nprint(result)",
            "options": [
                "A) True", "B) False", "C) [True, True, False]",
                "D) 报错", "E) 我不清楚"
            ],
            "answer": 1,
            "difficulty": "easy",
            "topic": "函数",
            "explanation": "all() 在可迭代对象所有元素为 True 时返回 True，否则返回 False。列表中有 False，所以返回 False。"
        },
    ],
}

# 合并多语言评估题库
for lang, questions in MULTI_LANG_QUESTION_BANK.items():
    if lang not in QUESTION_BANK:
        QUESTION_BANK[lang] = questions
    else:
        QUESTION_BANK[lang].extend(questions)

# ============================================================
# 辅助函数
# ============================================================

def _shuffle_and_strip(questions: list[dict]) -> list[dict]:
    """去除 answer 字段后返回"""
    return [
        {k: v for k, v in q.items() if k != "answer"}
        for q in questions
    ]


# ============================================================
# 公开 API
# ============================================================

def generate_assessment(language: str = "python", count: int = 10) -> list[dict]:
    """
    从题库中随机抽取 count 道题，确保：
    - 每次调用结果不同（随机打乱）
    - 尽量覆盖不同 topic（先按 topic 分组，每组抽题，再合并打乱）
    - 返回不含 answer 字段的题目列表
    """
    bank = QUESTION_BANK.get(language)
    if not bank:
        bank = QUESTION_BANK.get("python", [])

    if len(bank) <= count:
        return _shuffle_and_strip(bank)

    # 按 topic 分组
    topic_groups: dict[str, list[dict]] = {}
    for q in bank:
        topic_groups.setdefault(q["topic"], []).append(q)

    topics = list(topic_groups.keys())
    random.shuffle(topics)

    selected: dict[str, dict] = {}  # 用 dict 按 id 去重

    # 阶段一：从每个 topic 至少取一道
    per_topic = max(1, count // len(topics))
    for topic in topics:
        pool = topic_groups[topic]
        random.shuffle(pool)
        for q in pool[:per_topic]:
            selected[q["id"]] = q

    # 阶段二：不足 count 则从剩余题目中随机补足
    if len(selected) < count:
        remaining = [q for q in bank if q["id"] not in selected]
        random.shuffle(remaining)
        needed = count - len(selected)
        for q in remaining[:needed]:
            selected[q["id"]] = q

    # 阶段三：合并后随机打乱，取前 count 道
    result = list(selected.values())
    random.shuffle(result)
    return _shuffle_and_strip(result[:count])


def get_question_by_id(language: str, question_id: str) -> dict | None:
    """根据 ID 获取完整题目（含 answer）"""
    bank = QUESTION_BANK.get(language)
    if not bank:
        return None
    for q in bank:
        if q["id"] == question_id:
            return dict(q)
    return None


def get_topics(language: str) -> list[str]:
    """获取该语言所有主题列表"""
    bank = QUESTION_BANK.get(language)
    if not bank:
        return []
    seen = []
    for q in bank:
        if q["topic"] not in seen:
            seen.append(q["topic"])
    return seen


def get_question_count(language: str) -> int:
    """获取题库总题数"""
    bank = QUESTION_BANK.get(language)
    return len(bank) if bank else 0
