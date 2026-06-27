"""学习板块服务 — 学习路径 + 知识点内容 + 关联习题"""
from typing import Any
from services.exercise_service import PYTHON_EXERCISES, TOPIC_CONCEPTS
from services.multi_lang_exercises import ALL_EXERCISE_BANKS
from services.multi_lang_lessons import ALL_LANG_LEARNING_PATHS

# ============================================================
# 学习路径 - 按主题组织的知识点
# ============================================================
LEARNING_PATH: list[dict[str, Any]] = [
    # ===== 数据类型 =====
    {
        "topic": "数据类型",
        "topic_concept": TOPIC_CONCEPTS["数据类型"],
        "lessons": [
            {
                "id": "lesson_py_001",
                "title": "数字类型",
                "topic": "数据类型",
                "content": (
                    "Python 中的数字分为三种：整数（int）、浮点数（float）和复数（complex）。"
                    "整数可以是任意大小，不受 32 位或 64 位限制，Python 会自动处理大整数。"
                    "浮点数使用 IEEE 754 双精度标准，存在精度问题——比如 0.1 + 0.2 不一定等于 0.3，"
                    "这是所有语言共有的浮点误差。复数用 a + bj 表示，其中 j 是虚数单位。"
                    "数字类型支持加减乘除、幂运算（**）、取模（%）、整除（//）等常规运算，"
                    "类型转换用 int()、float() 等内置函数。Python 3 中除法 / 总是返回浮点数，整除用 //。"
                ),
                "examples": [
                    "# 整数运算：任意精度，无需担心溢出\na = 2 ** 100  # 1267650600228229401496703205376\nb = 10 // 3    # 3（整除）\nc = 10 % 3     # 1（取模）",
                    "# 浮点数精度问题\nprint(0.1 + 0.2)          # 0.30000000000000004\nprint(round(0.1 + 0.2, 2))  # 0.3（四舍五入解决）",
                    "# 类型转换\nprice = \"19.99\"\nreal_price = float(price)  # 19.99\ncount = int(3.7)           # 3（直接截断，不是四舍五入）"
                ],
                "key_points": [
                    "int 任意精度，float 双精度可能有误差",
                    "普通除法 / 返回 float，整除用 //",
                    "int() 截断小数部分，不是四舍五入",
                ],
            },
            {
                "id": "lesson_py_002",
                "title": "序列类型",
                "topic": "数据类型",
                "content": (
                    "序列类型是 Python 最常用的数据结构，包括字符串（str）、列表（list）、元组（tuple）和范围（range）。"
                    "它们共同的特点是：支持索引访问（从 0 开始）、切片操作 [start:stop:step]、长度 len()、"
                    "成员检查 in/not in，以及 + 拼接、* 重复。列表和元组的区别在于可变性："
                    "列表可以原地修改（增删改），元组创建后不可变。字符串也是不可变序列，"
                    "每次\"修改\"字符串实际上是创建了新对象。理解序列的通用操作，"
                    "可以让你在不同类型间无缝切换，大幅提升编码效率。"
                ),
                "examples": [
                    "# 切片语法 [start:stop:step]\ns = \"Hello Python\"\nprint(s[0:5])    # Hello\nprint(s[::-1])   # nohtyP olleH（反转字符串）",
                    "# 列表 vs 元组\nlst = [1, 2, 3]\ntup = (1, 2, 3)\nlst[0] = 99  # OK\ntup[0] = 99  # TypeError: 元组不可变",
                    "# 序列通用操作\nprint(len(lst))      # 3\nprint(2 in tup)     # True\nprint([1,2] + [3,4])  # [1, 2, 3, 4]"
                ],
                "key_points": [
                    "序列支持索引、切片、len()、in、+、*",
                    "list 可变，tuple 不可变，str 不可变",
                    "切片语法 [start:stop:step]，step 为负可反转",
                ],
            },
            {
                "id": "lesson_py_003",
                "title": "映射与集合类型",
                "topic": "数据类型",
                "content": (
                    "除了序列，Python 还提供了映射（dict）和集合（set）两种核心容器。"
                    "字典 dict 是键值对映射，通过 key 快速查找 value（时间复杂度 O(1)），"
                    "key 必须是不可变类型（字符串、数字、元组）。集合 set 是无序、不重复元素的集合，"
                    "底层也是哈希表，支持并集 |、交集 &、差集 - 等数学运算。"
                    "frozenset 是 set 的不可变版本，可以作为 dict 的 key。"
                    "这两类容器都是可变的（set 和 dict），适合需要快速查找、去重、关联映射的场景。"
                ),
                "examples": [
                    "# 字典操作\nd = {\"name\": \"Alice\", \"age\": 25}\nprint(d[\"name\"])        # Alice\nprint(d.get(\"score\", 0))  # 0（安全取值，不存在用默认值）",
                    "# 集合运算\na = {1, 2, 3}\nb = {2, 3, 4}\nprint(a | b)  # {1, 2, 3, 4}（并集）\nprint(a & b)  # {2, 3}（交集）\nprint(a - b)  # {1}（差集）",
                    "# frozenset 可哈希，能做 dict key\nfs = frozenset([1, 2, 3])\nd = {fs: \"frozen\"}  # OK"
                ],
                "key_points": [
                    "dict 键值对映射，key 必须不可变，查找 O(1)",
                    "set 无序去重，支持集合运算 | & -",
                    "dict.get(key, default) 安全取值，frozenset 可哈希",
                ],
            },
        ],
    },
    # ===== 控制流 =====
    {
        "topic": "控制流",
        "topic_concept": TOPIC_CONCEPTS["控制流"],
        "lessons": [
            {
                "id": "lesson_py_004",
                "title": "条件判断",
                "topic": "控制流",
                "content": (
                    "条件判断让程序根据不同情况执行不同代码。Python 使用 if / elif / else 结构，"
                    "从上到下依次检查条件，只执行第一个为 True 的分支。条件表达式可以是任意值："
                    "数字 0、空字符串 ''、空列表 []、None 被视为 False，其他值视为 True（真值测试）。"
                    "Python 还支持三元表达式 x if cond else y，一行完成简单条件赋值。"
                    "注意 Python 用缩进而非大括号定义代码块，同一级缩进必须一致（通常 4 空格）。"
                    "多个条件可用 and / or / not 组合，利用短路特性优化代码效率。"
                ),
                "examples": [
                    "# 基本 if/elif/else\nscore = 85\nif score >= 90:\n    grade = \"A\"\nelif score >= 80:\n    grade = \"B\"  # 执行这个分支\nelse:\n    grade = \"C\"\nprint(grade)  # B",
                    "# 三元表达式\nage = 20\nstatus = \"成年\" if age >= 18 else \"未成年\"",
                    "# 真值测试\nname = \"\"\nif name:\n    print(name)   # 不会执行，空字符串为 False\nelse:\n    print(\"name 为空\")  # 执行这里"
                ],
                "key_points": [
                    "if/elif/else 从上到下只执行第一个 True 分支",
                    "空值（0、空串、空列表、None）视为 False",
                    "三元表达式 x if cond else y 一行完成条件赋值",
                ],
            },
            {
                "id": "lesson_py_005",
                "title": "for 循环",
                "topic": "控制流",
                "content": (
                    "for 循环是 Python 最常用的循环，用于遍历可迭代对象（列表、字符串、字典、文件等）。"
                    "基本格式是 for item in iterable:。搭配 range(n) 生成 0 到 n-1 的整数序列，"
                    "range(start, stop, step) 可以自定义起止和步长。遍历字典时，默认遍历 key，"
                    "用 .items() 同时获取 key 和 value。循环中 break 立即终止整个循环，"
                    "continue 跳过当前轮进入下一轮。for 循环有一个独特的 else 子句——"
                    "当循环正常结束（未被 break 中断）时执行，常用于搜索场景中未找到的处理。"
                ),
                "examples": [
                    "# 基本遍历\nfruits = [\"apple\", \"banana\", \"cherry\"]\nfor i, fruit in enumerate(fruits):\n    print(f\"{i}: {fruit}\")  # 0: apple, 1: banana, 2: cherry",
                    "# for-else 用法：搜索\nnames = [\"Alice\", \"Bob\", \"Charlie\"]\nfor name in names:\n    if name == \"David\":\n        print(\"找到 David\")\n        break\nelse:\n    print(\"未找到 David\")  # 循环正常结束才执行",
                    "# 遍历字典\nd = {\"a\": 1, \"b\": 2}\nfor k, v in d.items():\n    print(f\"{k} -> {v}\")"
                ],
                "key_points": [
                    "for item in iterable 遍历可迭代对象",
                    "range(n) 生成 0~n-1，range(start,stop,step) 自定义",
                    "for-else：循环正常结束（无 break）执行 else",
                ],
            },
            {
                "id": "lesson_py_006",
                "title": "while 循环",
                "topic": "控制流",
                "content": (
                    "while 循环在条件为 True 时反复执行代码块，适用于循环次数不确定的场景。"
                    "与 for 不同，while 需要手动维护循环变量，忘记更新可能导致死循环。"
                    "常见的模式有：读取文件直到 EOF、轮询等待条件满足、游戏主循环。"
                    "break 和 continue 同样适用。while 也有 else 子句，逻辑与 for-else 一致。"
                    "小心 while True 无限循环——务必在合适的位置用 break 退出。"
                    "编程实践中，能用 for 解决的尽量不用 while，更安全、可读性更好。"
                ),
                "examples": [
                    "# 基本 while 循环\ncount = 0\nwhile count < 5:\n    print(count)\n    count += 1  # 必须手动更新，否则死循环",
                    "# while-else 用法\nn = 10\nwhile n > 0:\n    if n == 5:\n        break\n    n -= 1\nelse:\n    print(\"正常结束\")  # 被 break 中断，不执行",
                    "# 常见模式：用户输入验证\npassword = \"\"\nwhile len(password) < 6:\n    password = input(\"输入密码（至少6位）: \")"
                ],
                "key_points": [
                    "while 条件循环，需手动更新循环变量防死循环",
                    "while-else 同 for-else：正常结束才执行",
                    "能用 for 遍历解决的尽量不用 while",
                ],
            },
        ],
    },
    # ===== 函数 =====
    {
        "topic": "函数",
        "topic_concept": TOPIC_CONCEPTS["函数"],
        "lessons": [
            {
                "id": "lesson_py_007",
                "title": "函数定义与参数",
                "topic": "函数",
                "content": (
                    "函数是组织代码的基本单元，用 def 关键字定义。参数传递是 Python 函数的核心："
                    "位置参数按顺序传入，关键字参数按名称传入，默认参数给参数设默认值。"
                    "*args 将多余位置参数打包为元组，**kwargs 将多余关键字参数打包为字典。"
                    "return 语句返回值（可多个，用逗号分隔，实际返回元组），没有 return 默认返回 None。"
                    "注意：默认参数只在函数定义时求值一次，可变默认参数（如 []）会在多次调用间共享状态，"
                    "这是常见陷阱。推荐用 None 作为默认值，在函数内部判断后再初始化。"
                ),
                "examples": [
                    "# 位置参数 + 默认参数 + 关键字参数\ndef greet(name, greeting=\"Hello\", punctuation=\"!\"):\n    return f\"{greeting}, {name}{punctuation}\"\nprint(greet(\"Alice\"))                    # Hello, Alice!\nprint(greet(\"Bob\", punctuation=\".\"))    # Hello, Bob.",
                    "# *args 和 **kwargs\ndef log_info(level, *msgs, **kwargs):\n    print(f\"[{level}]\", *msgs)\n    for k, v in kwargs.items():\n        print(f\"  {k}: {v}\")\nlog_info(\"INFO\", \"连接成功\", \"开始处理\", user=\"admin\", ip=\"127.0.0.1\")",
                    "# 常见陷阱：可变默认参数\ndef bad_append(item, lst=[]):\n    lst.append(item)\n    return lst\nprint(bad_append(1))  # [1]\nprint(bad_append(2))  # [1, 2]！不是 [2]！"
                ],
                "key_points": [
                    "位置参数按序，关键字参数按名，*args/**kwargs 打包",
                    "默认参数定义时求值一次，可变默认值共享状态是陷阱",
                    "return 可返回多个值（实际是元组），无 return 返回 None",
                ],
            },
            {
                "id": "lesson_py_008",
                "title": "作用域与闭包",
                "topic": "函数",
                "content": (
                    "作用域决定了变量的可见范围，Python 遵循 LEGB 规则：Local（函数内）、Enclosing（外层函数）、"
                    "Global（模块全局）、Built-in（内置）。函数内部可以读取外部变量，但要修改外部变量"
                    "需要使用 global（修改全局变量）或 nonlocal（修改外层函数的变量）声明。"
                    "闭包是函数式编程的重要概念：内层函数引用了外层函数的变量，即使外层函数已返回，"
                    "内层函数仍能\"记住\"这些变量的值。闭包是装饰器的基础，常用于工厂函数、"
                    "回调函数等场景，让你可以创建带有\"记忆\"的函数。"
                ),
                "examples": [
                    "# LEGB 规则示例\nx = \"global\"        # Global\ndef outer():\n    x = \"enclosing\"  # Enclosing\n    def inner():\n        x = \"local\"  # Local\n        print(x)       # local\n    inner()\n    print(x)           # enclosing\nouter()\nprint(x)               # global",
                    "# 闭包：计数器工厂\ndef make_counter(start=0):\n    count = [start]  # 用列表避免 nonlocal\n    def counter():\n        count[0] += 1\n        return count[0]\n    return counter\nc1 = make_counter(10)\nprint(c1())  # 11\nprint(c1())  # 12",
                    "# nonlocal 修改外层变量\ndef outer():\n    x = 10\n    def inner():\n        nonlocal x\n        x += 1\n    inner()\n    print(x)  # 11\nouter()"
                ],
                "key_points": [
                    "LEGB 规则：Local → Enclosing → Global → Built-in",
                    "global 修改全局变量，nonlocal 修改外层函数变量",
                    "闭包=内层函数+外层变量，外层返回后仍可访问",
                ],
            },
            {
                "id": "lesson_py_009",
                "title": "lambda 与高阶函数",
                "topic": "函数",
                "content": (
                    "lambda 关键字可以快速创建匿名函数，语法为 lambda 参数: 表达式。它只能包含单个表达式，"
                    "不能有语句、循环或赋值。lambda 适合作为参数传给高阶函数——接收函数作为参数或返回函数的函数。"
                    "Python 内置的高阶函数有 map（对每个元素应用函数）、filter（筛选满足条件的元素）、"
                    "reduce（累积计算）、sorted（自定义排序 key）。"
                    "虽然 lambda 方便，但如果逻辑复杂，用普通 def 函数更清晰。"
                    "实际开发中，列表推导式通常比 map/filter 更 Pythonic。"
                ),
                "examples": [
                    "# lambda 基本用法\nsquare = lambda x: x ** 2\nprint(square(5))  # 25\n\n# 作为 sorted 的 key\nusers = [{\"name\": \"Alice\", \"age\": 30}, {\"name\": \"Bob\", \"age\": 25}]\nsorted_users = sorted(users, key=lambda u: u[\"age\"])  # 按年龄排序",
                    "# map / filter 示例\nnums = [1, 2, 3, 4, 5]\ndoubled = list(map(lambda x: x * 2, nums))      # [2, 4, 6, 8, 10]\neven = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]",
                    "# 列表推导式更 Pythonic\n# 替代 map:  [x*2 for x in nums]\n# 替代 filter: [x for x in nums if x % 2 == 0]"
                ],
                "key_points": [
                    "lambda 参数: 表达式，只能单表达式，适合作参数",
                    "高阶函数：map、filter、sorted(key=)、reduce",
                    "复杂逻辑用 def，简单场景列表推导式优于 map/filter",
                ],
            },
        ],
    },
    # ===== 列表操作 =====
    {
        "topic": "列表操作",
        "topic_concept": TOPIC_CONCEPTS["列表操作"],
        "lessons": [
            {
                "id": "lesson_py_010",
                "title": "列表基础操作",
                "topic": "列表操作",
                "content": (
                    "列表是 Python 最常用的可变序列容器，用方括号 [ ] 创建。核心操作分为增删改查："
                    "增用 append（末尾加一个元素）、extend（扩展另一个可迭代对象）、insert（指定位置插入）；"
                    "删用 pop（按索引删除并返回）、remove（按值删除第一个匹配项）、clear（清空）；"
                    "改直接用索引赋值；查用 index() 查找位置、count() 统计出现次数。"
                    "列表支持 sort() 原地排序（key 参数自定义排序规则）和 reverse() 反转。"
                    "注意 append 和 extend 的区别：append 把参数当作一个整体元素，extend 把参数的元素逐个加入。"
                ),
                "examples": [
                    "# 增删改查\nfruits = [\"apple\"]\nfruits.append(\"banana\")        # ['apple', 'banana']\nfruits.insert(0, \"cherry\")     # ['cherry', 'apple', 'banana']\nfruits.extend([\"date\", \"fig\"])  # ['cherry', 'apple', 'banana', 'date', 'fig']\npopped = fruits.pop(1)         # popped = 'apple', 列表变['cherry', 'banana', 'date', 'fig']",
                    "# append vs extend\nlst = [1, 2]\nlst.append([3, 4])   # [1, 2, [3, 4]]  —— 整个列表作为一个元素\nlst2 = [1, 2]\nlst2.extend([3, 4])  # [1, 2, 3, 4]   —— 元素逐个加入",
                    "# 排序\nnums = [3, 1, 4, 1, 5, 9]\nnums.sort()                    # [1, 1, 3, 4, 5, 9]（原地排序）\nnums.sort(reverse=True)        # [9, 5, 4, 3, 1, 1]（降序）\nwords = [\"apple\", \"Banana\", \"cherry\"]\nwords.sort(key=str.lower)      # 忽略大小写排序"
                ],
                "key_points": [
                    "append 加一个元素，extend 加多个，insert 指定位置",
                    "pop 按索引删除并返回，remove 按值删除第一个",
                    "sort() 原地排序，key 参数自定义规则，sorted() 返回新列表",
                ],
            },
            {
                "id": "lesson_py_011",
                "title": "列表推导式",
                "topic": "列表操作",
                "content": (
                    "列表推导式（List Comprehension）是 Python 最具特色的语法之一，一行代码生成新列表。"
                    "基本格式：[表达式 for 变量 in 可迭代对象 if 条件]。比传统 for 循环更简洁、优雅、"
                    "通常也更快（C 层面优化）。支持嵌套推导（多层 for）、带 if-else 条件表达式。"
                    "但注意可读性：过于复杂的推导式反而难以理解，此时拆成普通 for 循环更好。"
                    "实际开发中，列表推导式常用于：过滤数据、转换格式、扁平化嵌套列表、"
                    "笛卡尔积组合等场景。掌握它是写出 Pythonic 代码的关键一步。"
                ),
                "examples": [
                    "# 基本列表推导式\nsquares = [x ** 2 for x in range(10)]          # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]\neven_squares = [x**2 for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]",
                    "# if-else 在推导式中的位置\nlabels = [\"even\" if x % 2 == 0 else \"odd\" for x in range(5)]\n# ['even', 'odd', 'even', 'odd', 'even']",
                    "# 嵌套推导：展平二维列表\nmatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]\nflat = [n for row in matrix for n in row]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]"
                ],
                "key_points": [
                    "格式：[表达式 for 变量 in 可迭代对象 if 条件]",
                    "比传统 for 更简洁、更快（C 层优化）",
                    "仅 if 放后面，if-else 放表达式位置，嵌套推导注意可读性",
                ],
            },
        ],
    },
    # ===== 字典操作 =====
    {
        "topic": "字典操作",
        "topic_concept": TOPIC_CONCEPTS["字典操作"],
        "lessons": [
            {
                "id": "lesson_py_012",
                "title": "字典基础操作",
                "topic": "字典操作",
                "content": (
                    "字典是 Python 的核心映射容器，用 {key: value} 创建。key 必须是不可变类型（字符串、数字、"
                    "含不可变元素的元组），value 可以是任意类型。增删改查基本操作：d[key] = value 增/改，"
                    "del d[key] 或 d.pop(key) 删除，len(d) 查看条目数。推荐用 d.get(key, default) 安全取值，"
                    "避免 KeyError。遍历用 d.items()（键值对）、d.keys()（键）、d.values()（值）。"
                    "从 Python 3.7 起，字典保持插入顺序。还支持合并运算符 |（Python 3.9+）和 |= 原地更新。"
                ),
                "examples": [
                    "# 增删改查\nd = {\"name\": \"Alice\", \"age\": 25}\nd[\"city\"] = \"Beijing\"          # 新增/修改\nd.pop(\"age\")                     # 删除并返回 25\nprint(d.get(\"score\", 0))         # 0（安全取值）",
                    "# 遍历字典\nfor k, v in d.items():\n    print(f\"{k}: {v}\")\n# name: Alice\n# city: Beijing",
                    "# 合并字典（Python 3.9+）\nd1 = {\"a\": 1}\nd2 = {\"b\": 2, \"c\": 3}\nmerged = d1 | d2  # {'a': 1, 'b': 2, 'c': 3}"
                ],
                "key_points": [
                    "d[key] 取值可能 KeyError，get(key, default) 更安全",
                    "遍历用 items()、keys()、values()",
                    "Python 3.7+ 字典保持插入顺序，3.9+ 支持 | 合并",
                ],
            },
            {
                "id": "lesson_py_013",
                "title": "字典推导式与高级用法",
                "topic": "字典操作",
                "content": (
                    "字典推导式和列表推导式语法相似：{key_expr: value_expr for item in iterable if condition}。"
                    "适合从列表生成字典、交换键值、过滤字典等场景。高级用法包括：defaultdict（访问不存在的 key 自动创建默认值）、"
                    "Counter（统计元素出现次数）、OrderedDict（从 Python 3.7 起普通 dict 已保持顺序，但 OrderedDict 保留了一些特有方法如 move_to_end）。"
                    "setdefault 方法是 get + 赋值的合体：如果 key 不存在就设置默认值并返回，存在则返回已有值。"
                    "这些工具在数据处理、统计、缓存场景非常实用。"
                ),
                "examples": [
                    "# 字典推导式\nnames = [\"Alice\", \"Bob\", \"Charlie\"]\nname_len = {name: len(name) for name in names}  # {'Alice': 5, 'Bob': 3, 'Charlie': 7}\nevens = {x: x**2 for x in range(10) if x % 2 == 0}  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}",
                    "# defaultdict 用法\nfrom collections import defaultdict\ncounter = defaultdict(int)\nwords = [\"a\", \"b\", \"a\", \"c\", \"b\", \"a\"]\nfor w in words:\n    counter[w] += 1  # 自动初始化为 0\nprint(dict(counter))  # {'a': 3, 'b': 2, 'c': 1}",
                    "# setdefault：有则返回，无则设默认\nd = {}\nd.setdefault(\"count\", 0)  # key 不存在，设为 0\nd[\"count\"] += 1\nd.setdefault(\"count\", 0)  # key 已存在，不作改动\nd[\"count\"] += 1\nprint(d[\"count\"])  # 2"
                ],
                "key_points": [
                    "字典推导式：{key: value for ... if ...}",
                    "defaultdict 自动创建默认值，适合计数和分组",
                    "setdefault 有则返回无则设默认，一行替代 get+赋值",
                ],
            },
        ],
    },
    # ===== 字符串 =====
    {
        "topic": "字符串",
        "topic_concept": TOPIC_CONCEPTS["字符串"],
        "lessons": [
            {
                "id": "lesson_py_014",
                "title": "字符串基础",
                "topic": "字符串",
                "content": (
                    "Python 字符串是不可变的 Unicode 字符序列，用单引号或双引号创建。支持索引 [i] 和切片 [::]。"
                    "常用方法：len() 获取长度，upper()/lower() 大小写转换，strip()/lstrip()/rstrip() 去除空白，"
                    "split(sep) 按分隔符分割为列表，join(iterable) 用分隔符连接列表为字符串，"
                    "replace(old, new) 替换子串，find(sub)/index(sub) 查找子串位置（find 找不到返回 -1，index 抛异常）。"
                    "判断方法：startswith()、endswith()、isdigit()、isalpha() 等。字符串不可变意味着每次\"修改\"都创建新对象，"
                    "频繁拼接大量字符串时用 join() 而非 +，性能差异显著。"
                ),
                "examples": [
                    "# 常用方法\ns = \"  Hello World  \"\nprint(s.strip())                # \"Hello World\"\nprint(s.lower())                # \"  hello world  \"\nprint(s.replace(\"World\", \"Python\"))  # \"  Hello Python  \"",
                    "# split 和 join\ncsv_line = \"apple,banana,cherry\"\nitems = csv_line.split(\",\")     # ['apple', 'banana', 'cherry']\njoined = \" | \".join(items)      # \"apple | banana | cherry\"",
                    "# 高效拼接：join 优于 + in 循环\nwords = [\"a\"] * 10000\n# 推荐：\nresult = \"\".join(words)\n# 避免：\n# result = \"\"\n# for w in words:\n#     result += w  # 每次创建新字符串，O(n^2)"
                ],
                "key_points": [
                    "字符串不可变，支持索引和切片",
                    "split 分割为列表，join 连接为字符串",
                    "大量拼接用 join() 不可以用 + 循环，性能差很多",
                ],
            },
            {
                "id": "lesson_py_015",
                "title": "字符串格式化",
                "topic": "字符串",
                "content": (
                    "Python 有三种字符串格式化方式，推荐程度递减：f-string（Python 3.6+）> str.format() > % 运算符。"
                    "f-string 最简洁直观：f'文本 {表达式}'，表达式可以是任意 Python 代码。"
                    "format() 方法用 {} 占位，支持位置索引和关键字。% 运算符是旧式风格，不建议新代码使用。"
                    "格式规范：{value:^10} 居中对齐宽度 10，{value:.2f} 保留两位小数，{value:,} 千分位分隔。"
                    "实际开发中，f-string 是首选方案，只有模板化场景（格式字符串存储在变量或文件中）才用 format。"
                ),
                "examples": [
                    "# f-string（推荐）\nname = \"Alice\"\nage = 25\nprint(f\"{name} 今年 {age} 岁\")         # Alice 今年 25 岁\nprint(f\"{name=}, {age=}\")              # name='Alice', age=25（调试用法）",
                    "# 格式规范\npi = 3.1415926\nprint(f\"{pi:.2f}\")       # 3.14（保留两位小数）\nprint(f\"{pi:10.2f}\")     # \"      3.14\"（宽度 10 右对齐）\nnum = 1234567\nprint(f\"{num:,}\")         # 1,234,567（千分位）",
                    "# format() 模板化\nTEMPLATE = \"Hello {name}, your score is {score}\"\nprint(TEMPLATE.format(name=\"Bob\", score=95))"
                ],
                "key_points": [
                    "f-string 最简洁：f'{表达式}'，Python 3.6+ 首选",
                    "格式：{:.2f} 两位小数，{:^10} 居中对齐，{:,} 千分位",
                    "模板化场景用 format()，避免 % 运算符",
                ],
            },
        ],
    },
    # ===== 面向对象 =====
    {
        "topic": "面向对象",
        "topic_concept": TOPIC_CONCEPTS["面向对象"],
        "lessons": [
            {
                "id": "lesson_py_016",
                "title": "类与对象",
                "topic": "面向对象",
                "content": (
                    "类是对象的蓝图，用 class 关键字定义，通过类名() 创建实例。__init__ 是构造函数，"
                    "在创建实例时自动调用，用于初始化实例属性。self 指向当前实例本身，是方法的第一个参数。"
                    "实例属性属于每个对象独立持有，类属性在所有实例间共享。"
                    "方法中访问实例属性必须通过 self.attr，否则会访问局部变量或报 NameError。"
                    "面向对象的优势在于将数据（属性）和行为（方法）封装在一起，让代码更模块化、易复用。"
                    "Python 中一切皆对象，int、str、函数都是对象，理解类和对象是进阶的基石。"
                ),
                "examples": [
                    "# 定义类\nclass Dog:\n    species = \"犬科\"  # 类属性，所有实例共享\n\n    def __init__(self, name, age):\n        self.name = name  # 实例属性\n        self.age = age\n\n    def bark(self):\n        return f\"{self.name} says Woof!\"\n\nd1 = Dog(\"旺财\", 3)\nd2 = Dog(\"来福\", 5)\nprint(d1.bark())      # 旺财 says Woof!\nprint(d1.species)     # 犬科\nDog.species = \"犬属\"   # 修改类属性，所有实例受影响\nprint(d2.species)     # 犬属",
                    "# 属性访问控制（约定，非强制）\nclass BankAccount:\n    def __init__(self, owner, balance):\n        self.owner = owner          # 公开属性\n        self._protected = balance   # 受保护的（约定用 _ 前缀）\n        self.__private = 0          # 名称改写为 _BankAccount__private（避免子类冲突）"
                ],
                "key_points": [
                    "class 定义类，__init__ 构造，self 指向实例",
                    "实例属性 self.xxx，类属性共享，通过类名访问",
                    "Python 约定 _protected（保护）、__name（名称改写）",
                ],
            },
            {
                "id": "lesson_py_017",
                "title": "继承与多态",
                "topic": "面向对象",
                "content": (
                    "继承让子类复用父类的属性和方法，用 class Child(Parent) 语法。子类可以重写（override）父类方法，"
                    "用 super() 调用父类同名方法。Python 支持多继承（一个子类继承多个父类），"
                    "方法解析顺序（MRO）用 C3 线性化算法确定，可通过 cls.__mro__ 查看。"
                    "多态指同一接口不同实现：只要对象实现了相同的方法名，就可以互换使用，"
                    "不需要显示的接口定义。Python 的\"鸭子类型\"——\"如果它走路像鸭子，叫起来像鸭子，那它就是鸭子\"——"
                    "是多态的自然体现。isinstance(obj, cls) 检查类型，issubclass(cls, parent) 检查继承关系。"
                ),
                "examples": [
                    "# 继承与重写\nclass Animal:\n    def speak(self):\n        return \"Some sound\"\n\nclass Cat(Animal):\n    def speak(self):\n        return \"Meow\"\n\nclass Dog(Animal):\n    def speak(self):\n        return \"Woof\"\n\nanimals = [Cat(), Dog(), Animal()]\nfor a in animals:\n    print(a.speak())  # Meow, Woof, Some sound（多态）",
                    "# super() 调用父类方法\nclass Parent:\n    def __init__(self, name):\n        self.name = name\n\nclass Child(Parent):\n    def __init__(self, name, age):\n        super().__init__(name)  # 调用父类 __init__\n        self.age = age\nc = Child(\"小明\", 10)\nprint(c.name, c.age)  # 小明 10",
                    "# isinstance 类型检查\nprint(isinstance(c, Child))    # True\nprint(isinstance(c, Parent))   # True（子类实例也是父类实例）\nprint(issubclass(Child, Parent))  # True"
                ],
                "key_points": [
                    "class Child(Parent) 继承，super() 调用父类方法",
                    "多态：相同方法名不同行为，Python 鸭子类型天然支持",
                    "isinstance 检查类型、issubclass 检查继承关系",
                ],
            },
            {
                "id": "lesson_py_018",
                "title": "魔术方法与属性",
                "topic": "面向对象",
                "content": (
                    "魔术方法（Magic Methods / Dunder Methods）是 Python 中双下划线开头结尾的特殊方法，"
                    "让你可以自定义类在特定操作下的行为。最常用的：__str__ 定义 print() 输出、"
                    "__repr__ 定义开发者看到的表示、__len__ 支持 len()、__getitem__ 支持索引访问 [i]、"
                    "__eq__ 定义 == 比较、__lt__ 定义 < 比较等。@property 装饰器把方法伪装成属性访问，"
                    "搭配 @xxx.setter 实现赋值时的校验逻辑。这些机制让自定义类可以像内置类型一样自然使用，"
                    "是 Python 数据模型的核心，也是各种第三方库能如此优雅的原因。"
                ),
                "examples": [
                    "# 常用魔术方法\nclass Book:\n    def __init__(self, title, author, pages):\n        self.title = title\n        self.author = author\n        self.pages = pages\n\n    def __str__(self):\n        return f\"《{self.title}》by {self.author}\"\n\n    def __repr__(self):\n        return f\"Book('{self.title}', '{self.author}', {self.pages})\"\n\n    def __len__(self):\n        return self.pages\n\n    def __eq__(self, other):\n        return self.title == other.title and self.author == other.author\n\nb = Book(\"Python入门\", \"张三\", 300)\nprint(b)       # 《Python入门》by 张三\nprint(len(b))  # 300",
                    "# @property 属性装饰器\nclass Temperature:\n    def __init__(self, celsius):\n        self._celsius = celsius\n\n    @property\n    def fahrenheit(self):\n        return self._celsius * 9 / 5 + 32\n\n    @fahrenheit.setter\n    def fahrenheit(self, value):\n        self._celsius = (value - 32) * 5 / 9\n\nt = Temperature(0)\nprint(t.fahrenheit)  # 32.0（像属性一样访问）\nt.fahrenheit = 212\nprint(t._celsius)    # 100.0"
                ],
                "key_points": [
                    "__str__ 用户友好输出，__repr__ 开发者表示",
                    "__len__、__getitem__、__eq__ 等让对象像内置类型",
                    "@property 方法伪装属性，@setter 实现赋值校验",
                ],
            },
        ],
    },
    # ===== 异常处理 =====
    {
        "topic": "异常处理",
        "topic_concept": TOPIC_CONCEPTS["异常处理"],
        "lessons": [
            {
                "id": "lesson_py_019",
                "title": "try/except 基础",
                "topic": "异常处理",
                "content": (
                    "异常是程序运行时发生的错误。Python 用 try/except 捕获并处理异常，避免程序崩溃。"
                    "基本结构：try 块放可能出错的代码，except 捕获指定异常类型并处理。"
                    "可以捕获多个异常类型用逗号分隔，或用多个 except 分支分别处理不同异常。"
                    "捕获 Exception 可以兜底所有常规异常，但不建议直接 except:（裸捕获会吞掉 KeyboardInterrupt 等系统异常）。"
                    "else 子句在 try 块无异常时执行，finally 无论是否异常都执行（常用于清理资源如关闭文件、释放锁）。"
                ),
                "examples": [
                    "# 基本异常处理\ntry:\n    num = int(input(\"输入数字: \"))\n    result = 10 / num\n    print(f\"结果: {result}\")\nexcept ValueError:\n    print(\"请输入有效数字！\")\nexcept ZeroDivisionError:\n    print(\"除数不能为 0！\")\nexcept Exception as e:\n    print(f\"未知错误: {e}\")",
                    "# else 和 finally\ntry:\n    f = open(\"data.txt\")\nexcept FileNotFoundError:\n    print(\"文件不存在\")\nelse:\n    content = f.read()  # 仅在无异常时执行\n    f.close()\nfinally:\n    print(\"清理完成\")  # 总执行",
                    "# 常见异常类型\n# ValueError: 类型转换失败\n# TypeError: 操作类型不匹配\n# IndexError: 列表索引越界\n# KeyError: 字典 key 不存在\n# AttributeError: 对象属性不存在"
                ],
                "key_points": [
                    "try/except 捕获异常，多个 except 分别处理不同异常",
                    "避免裸 except，至少 except Exception",
                    "else 无异常时执行，finally 始终执行（清理资源）",
                ],
            },
            {
                "id": "lesson_py_020",
                "title": "自定义异常与清理",
                "topic": "异常处理",
                "content": (
                    "自定义异常只需继承 Exception 类，可以添加额外的属性（如错误码、详情信息）。"
                    "用 raise 抛出异常，raise from 可以保留原始异常链（用于异常转换场景）。"
                    "上下文管理器（with 语句）是资源清理的最佳实践：定义 __enter__ 和 __exit__ 方法，"
                    "或者用 contextlib 的 contextmanager 装饰器将生成器转为上下文管理器。"
                    "with 块结束时自动调用 __exit__，即使发生异常也会执行清理，"
                    "完美替代 try/finally 模式，代码更简洁、更安全。"
                    "所有带 close/release 方法的资源（文件、网络连接、锁）都推荐用 with 管理。"
                ),
                "examples": [
                    "# 自定义异常\nclass InsufficientBalanceError(Exception):\n    def __init__(self, balance, amount):\n        self.balance = balance\n        self.amount = amount\n        super().__init__(f\"余额 {balance} 不足，需要 {amount}\")\n\n# raise from 保留异常链\ntry:\n    int(\"abc\")\nexcept ValueError as e:\n    raise AppError(\"输入格式错误\") from e",
                    "# 上下文管理器（with 语句）\nclass ManagedFile:\n    def __init__(self, name):\n        self.name = name\n\n    def __enter__(self):\n        self.file = open(self.name, 'w')\n        return self.file\n\n    def __exit__(self, exc_type, exc_val, exc_tb):\n        self.file.close()\n\nwith ManagedFile(\"test.txt\") as f:\n    f.write(\"Hello\")  # 即使出错也会自动 close",
                    "# contextmanager 装饰器简化\nfrom contextlib import contextmanager\n@contextmanager\ndef managed_file(name):\n    f = open(name, 'w')\n    try:\n        yield f\n    finally:\n        f.close()"
                ],
                "key_points": [
                    "自定义异常继承 Exception，raise 抛出",
                    "raise from 保留异常链，追溯根因",
                    "with 语句自动清理资源，替代 try/finally",
                ],
            },
        ],
    },
    # ===== 文件IO =====
    {
        "topic": "文件IO",
        "topic_concept": TOPIC_CONCEPTS["文件IO"],
        "lessons": [
            {
                "id": "lesson_py_021",
                "title": "文件读写基础",
                "topic": "文件IO",
                "content": (
                    "Python 用 open() 函数打开文件，返回文件对象进行操作。推荐使用 with 语句自动管理文件关闭。"
                    "读操作用 f.read() 一次读取全部内容（适合小文件）、f.readline() 逐行读取、"
                    "f.readlines() 读取所有行返回列表。写操作用 f.write() 写入字符串、f.writelines() 写入字符串列表。"
                    "文件指针控制：f.seek(offset) 移动指针、f.tell() 获取当前指针位置。"
                    "读取大文件时不要用 read() 一次全读，会撑爆内存——用迭代器逐行处理：for line in f:。"
                ),
                "examples": [
                    "# 写文件\nwith open(\"output.txt\", \"w\", encoding=\"utf-8\") as f:\n    f.write(\"第一行\\n\")\n    f.write(\"第二行\\n\")",
                    "# 读文件——三种方式\nwith open(\"output.txt\", \"r\", encoding=\"utf-8\") as f:\n    content = f.read()        # 一次全读\n    # f.seek(0)               # 重置指针才能再读\n    # lines = f.readlines()   # 读所有行为列表",
                    "# 大文件逐行处理\nwith open(\"large_file.txt\", \"r\") as f:\n    for line in f:           # 逐行迭代，内存友好\n        process(line.strip())"
                ],
                "key_points": [
                    "with open(...) as f: 自动关闭，推荐用法",
                    "小文件用 read() 全读，大文件用 for line in f 逐行",
                    "seek() 移动指针，tell() 获取指针位置",
                ],
            },
            {
                "id": "lesson_py_022",
                "title": "文件模式与路径",
                "topic": "文件IO",
                "content": (
                    "open() 的 mode 参数决定了文件打开方式：'r' 只读（默认）、'w' 覆盖写（清空后写入）、"
                    "'a' 追加写、'x' 排他创建（文件已存在则报错）。加上 '+' 表示读写模式如 'r+'（读写）。"
                    "加上 'b' 表示二进制模式如 'rb'、'wb'（用于图片、视频等非文本文件）。"
                    "Python 用 os.path 或 pathlib 操作路径。pathlib.Path 是面向对象的路径管理方式比 os.path 更现代："
                    "Path('a') / 'b' 拼接路径、.exists() 检查存在、.mkdir(parents=True) 递归创建目录、"
                    ".glob('*.py') 匹配文件名、.read_text()/.write_text() 直接读写文本。"
                ),
                "examples": [
                    "# 文件模式\n# 'r' 只读, 'w' 覆盖写, 'a' 追加, 'x' 排他创建\n# 'b' 二进制模式, '+' 读写模式\nwith open(\"data.bin\", \"wb\") as f:\n    f.write(b\"binary data\")",
                    "# pathlib 路径操作（推荐）\nfrom pathlib import Path\np = Path(\"data\") / \"2024\" / \"report.txt\"\nprint(p)                           # data\\2024\\report.txt\np.parent.mkdir(parents=True, exist_ok=True)  # 递归创建目录\np.write_text(\"Hello\")               # 直接写文本\ncontent = p.read_text()             # 直接读文本\nprint(p.exists())                   # True",
                    "# glob 匹配文件\nfor py_file in Path(\".\").glob(\"*.py\"):\n    print(py_file.name)  # 列出所有 .py 文件"
                ],
                "key_points": [
                    "模式：r/w/a/x + b（二进制）+ +（读写）",
                    "pathlib.Path 面向对象路径管理，优于 os.path",
                    "Path('a') / 'b' 拼接，.glob('*.py') 匹配文件",
                ],
            },
        ],
    },
    # ===== 装饰器 =====
    {
        "topic": "装饰器",
        "topic_concept": TOPIC_CONCEPTS["装饰器"],
        "lessons": [
            {
                "id": "lesson_py_023",
                "title": "装饰器原理",
                "topic": "装饰器",
                "content": (
                    "装饰器是一种在不修改原函数代码的前提下，给函数添加额外功能的机制。本质上，装饰器是一个"
                    "接收函数、返回新函数的闭包。@decorator 语法糖等价于 func = decorator(func)。"
                    "最简装饰器结构：外层函数接收 func，内层 wrapper 函数在调用 func 前后执行额外逻辑，"
                    "返回 wrapper。为保留原函数的元信息（__name__、__doc__ 等），务必在 wrapper 上加 @functools.wraps(func)。"
                    "装饰器可以带参数：再加一层函数，参数传给最外层，真正装饰逻辑在中间层。"
                    "常见应用：日志记录、执行计时、权限校验、缓存结果、重试机制等。"
                ),
                "examples": [
                    "# 基本装饰器\nimport functools\nimport time\n\ndef timer(func):\n    @functools.wraps(func)\n    def wrapper(*args, **kwargs):\n        start = time.perf_counter()\n        result = func(*args, **kwargs)\n        elapsed = time.perf_counter() - start\n        print(f\"{func.__name__} took {elapsed:.4f}s\")\n        return result\n    return wrapper\n\n@timer\ndef slow_add(a, b):\n    time.sleep(0.1)\n    return a + b\n\nprint(slow_add(1, 2))  # slow_add took 0.1xxx s \\n# 3",
                    "# 带参数的装饰器（三层结构）\ndef repeat(times):\n    def decorator(func):\n        @functools.wraps(func)\n        def wrapper(*args, **kwargs):\n            for _ in range(times):\n                result = func(*args, **kwargs)\n            return result\n        return wrapper\n    return decorator\n\n@repeat(3)\ndef say_hi():\n    print(\"Hi!\")\nsay_hi()  # 打印 3 次 Hi!"
                ],
                "key_points": [
                    "装饰器 = 接收函数、返回函数的闭包",
                    "@decorator 等价于 func = decorator(func)",
                    "用 @functools.wraps 保留原函数元信息",
                ],
            },
            {
                "id": "lesson_py_024",
                "title": "装饰器进阶",
                "topic": "装饰器",
                "content": (
                    "除了函数装饰器，Python 还支持类装饰器（接收类，返回类或可调用对象），用于注册、修改类行为。"
                    "内置装饰器：@staticmethod（静态方法，无需 self/cls）、@classmethod（类方法，第一个参数为 cls）、"
                    "@property（属性装饰器，方法伪装属性）。装饰器可以叠加——多个装饰器从下往上（最靠近 def 的先执行）。"
                    "常见进阶模式：参数校验装饰器（检查参数类型或范围）、缓存装饰器（如 lru_cache 记忆化）、"
                    "重试装饰器（处理临时错误自动重试）、上下文注入（为函数注入额外上下文）。"
                ),
                "examples": [
                    "# 多个装饰器叠加\n@timer\n@repeat(2)\ndef greet():\n    print(\"Hello\")\ngreet()  # 打印 2 次 Hello，然后输出总耗时",
                    "# 缓存装饰器（内置）\nfrom functools import lru_cache\n\n@lru_cache(maxsize=128)\ndef fib(n):\n    if n < 2:\n        return n\n    return fib(n - 1) + fib(n - 2)\n\nprint(fib(100))  # 秒出结果，无缓存会卡死",
                    "# 类装饰器\ndef add_repr(cls):\n    cls.__repr__ = lambda self: f\"{cls.__name__}(...)\"\n    return cls\n\n@add_repr\nclass User:\n    def __init__(self, name):\n        self.name = name\n\nprint(User(\"Alice\"))  # User(...)"
                ],
                "key_points": [
                    "@staticmethod、@classmethod、@property 是常用内置装饰器",
                    "多个装饰器从下往上执行（近 def 先）",
                    "@lru_cache 最常用的缓存装饰器，适合递归/重复计算",
                ],
            },
        ],
    },
    # ===== 生成器 =====
    {
        "topic": "生成器",
        "topic_concept": TOPIC_CONCEPTS["生成器"],
        "lessons": [
            {
                "id": "lesson_py_025",
                "title": "生成器基础",
                "topic": "生成器",
                "content": (
                    "生成器是一种特殊的迭代器，用 yield 代替 return 的函数叫生成器函数。"
                    "调用生成器函数不会立即执行，而是返回一个生成器对象。每次调用 next()（或在 for 循环中迭代），"
                    "函数执行到 yield 语句，产出值并暂停，下次从暂停处继续。"
                    "生成器的核心优势是惰性计算：不一次性生成所有值，而是按需产出一个值，"
                    "极大节省内存。适合处理大文件、无限序列、数据流等场景。"
                    "send() 方法可以向生成器内部发送值（用作 yield 表达式的返回值），实现双向通信。"
                ),
                "examples": [
                    "# 基本生成器\ndef countdown(n):\n    while n > 0:\n        yield n\n        n -= 1\n\nfor num in countdown(5):\n    print(num, end=\" \")  # 5 4 3 2 1",
                    "# 生成器 vs 列表：内存对比\n# 列表：一次性生成所有元素（占用大量内存）\nbig_list = [x for x in range(10_000_000)]  # 约 80MB\n# 生成器：按需产出（几乎不占内存）\nbig_gen = (x for x in range(10_000_000))   # 常量内存",
                    "# send() 双向通信\ndef echo():\n    while True:\n        received = yield\n        print(f\"收到: {received}\")\n\ng = echo()\nnext(g)        # 启动生成器（推进到第一个 yield）\ng.send(\"Hello\")  # 收到: Hello\ng.send(\"World\")  # 收到: World"
                ],
                "key_points": [
                    "yield 替代 return，函数变为生成器，暂停而非终止",
                    "惰性计算：按需产出，极大节省内存",
                    "send() 向生成器发送值，next() 或 for 迭代取值",
                ],
            },
            {
                "id": "lesson_py_026",
                "title": "生成器表达式",
                "topic": "生成器",
                "content": (
                    "生成器表达式是列表推导式的惰性版本，用圆括号替代方括号：(expr for x in iterable if cond)。"
                    "它返回一个生成器对象，在迭代时才逐个产出值。相比列表推导式，节省内存但只能迭代一次。"
                    "作为函数参数时，如果生成器表达式是唯一参数，可以省略外层圆括号：sum(x*2 for x in range(10))。"
                    "yield from 语法简化了嵌套生成器的代理：yield from iterable 等价于 for item in iterable: yield item，"
                    "而且还能自动处理 send()、throw()、close() 的转发。常用于分层的生成器场景。"
                ),
                "examples": [
                    "# 生成器表达式\nsquares_gen = (x ** 2 for x in range(10))\nprint(type(squares_gen))  # <class 'generator'>\nprint(list(squares_gen))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]\nprint(list(squares_gen))  # []（生成器已耗尽！）",
                    "# 唯一参数时可省略括号\nprint(sum(x**2 for x in range(10)))    # 285\nprint(max(len(w) for w in [\"a\", \"bb\", \"ccc\"]))  # 3",
                    "# yield from 代理子生成器\ndef chain(*iterables):\n    for it in iterables:\n        yield from it  # 代替 for x in it: yield x\n\nprint(list(chain(\"ab\", \"cd\", \"ef\")))  # ['a', 'b', 'c', 'd', 'e', 'f']"
                ],
                "key_points": [
                    "生成器表达式 (expr for x in ...)，惰性，只可迭代一次",
                    "作为唯一函数参数时可省略外层括号",
                    "yield from it 代理子生成器，等价于 for x in it: yield x",
                ],
            },
        ],
    },
    # ===== GIL/并发 =====
    {
        "topic": "GIL/并发",
        "topic_concept": TOPIC_CONCEPTS["GIL/并发"],
        "lessons": [
            {
                "id": "lesson_py_027",
                "title": "GIL 原理",
                "topic": "GIL/并发",
                "content": (
                    "GIL（Global Interpreter Lock，全局解释器锁）是 CPython 的线程安全机制："
                    "同一时刻只允许一个线程执行 Python 字节码。这意味着多线程无法利用多核 CPU "
                    "做真正的并行计算。为什么要有 GIL？因为 CPython 的内存管理（引用计数）不是线程安全的，"
                    "GIL 是最简单的解决方式。需要理解：GIL 影响的是 CPU 密集型任务（计算），"
                    "对 IO 密集型任务（网络请求、文件读写）影响较小——IO 操作时会释放 GIL，允许其他线程运行。"
                    "目前 CPython 团队在逐步优化 GIL 的影响，但短期内不会移除。"
                ),
                "examples": [
                    "# CPU 密集型：多线程反而更慢（GIL 竞争）\nimport threading\nimport time\n\ndef cpu_bound():\n    count = 0\n    for i in range(10_000_000):\n        count += 1\n    return count\n\nstart = time.time()\nt1 = threading.Thread(target=cpu_bound)\nt2 = threading.Thread(target=cpu_bound)\nt1.start(); t2.start()\nt1.join(); t2.join()\nprint(f\"多线程耗时: {time.time() - start:.4f}s\")  # 约等于单线程×2（无加速）",
                    "# IO 密集型：多线程有效（IO 时释放 GIL）\nimport requests\nimport concurrent.futures\n\nurls = [\"https://httpbin.org/delay/1\"] * 5\nwith concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:\n    results = list(ex.map(requests.get, urls))\n# 5 个请求只需约 1 秒（并发 IO）"
                ],
                "key_points": [
                    "GIL 保证同一时刻只有一个线程执行 Python 字节码",
                    "CPU 密集型多线程无加速（甚至更慢），IO 密集型有效",
                    "GIL 源于 CPython 内存管理（引用计数）线程安全问题",
                ],
            },
            {
                "id": "lesson_py_028",
                "title": "多线程与多进程",
                "topic": "GIL/并发",
                "content": (
                    "面对并发需求，Python 提供了多线程（threading）和多进程（multiprocessing）两种方案。"
                    "多线程适合 IO 密集型：线程间共享内存，通信简单，但受 GIL 限制。线程同步工具："
                    "Lock（互斥锁）、RLock（可重入锁）、Semaphore（信号量）、Queue（线程安全队列）。"
                    "多进程适合 CPU 密集型：每个进程有独立的 GIL，真正利用多核。但进程间内存不共享，"
                    "通信需用 Pipe、Queue、共享内存等机制，开销比线程大。"
                    "concurrent.futures 提供统一的线程/进程池接口，常用 ThreadPoolExecutor 和 ProcessPoolExecutor。"
                    "asyncio 是第三种并发方案（协程），适合高并发的网络 IO 场景，后续可深入学习。"
                ),
                "examples": [
                    "# 多线程：ThreadPoolExecutor\nfrom concurrent.futures import ThreadPoolExecutor, as_completed\n\ndef fetch(url):\n    # 模拟 IO 操作\n    time.sleep(0.5)\n    return f\"data from {url}\"\n\nurls = [\"url1\", \"url2\", \"url3\"]\nwith ThreadPoolExecutor(max_workers=3) as executor:\n    futures = {executor.submit(fetch, url): url for url in urls}\n    for future in as_completed(futures):\n        print(future.result())  # 按完成顺序输出",
                    "# 多进程：ProcessPoolExecutor\nfrom concurrent.futures import ProcessPoolExecutor\n\ndef cpu_heavy(n):\n    return sum(i * i for i in range(n))\n\nwith ProcessPoolExecutor() as executor:\n    results = list(executor.map(cpu_heavy, [1_000_000] * 4))\n# 4 个核心并行计算，约等于 1 个的时间"
                ],
                "key_points": [
                    "IO 密集用 threading/ThreadPoolExecutor",
                    "CPU 密集用 multiprocessing/ProcessPoolExecutor",
                    "concurrent.futures 统一接口，简化并发编程",
                ],
            },
        ],
    },
    # ===== 常用库 =====
    {
        "topic": "常用库",
        "topic_concept": TOPIC_CONCEPTS["常用库"],
        "lessons": [
            {
                "id": "lesson_py_029",
                "title": "标准库概览",
                "topic": "常用库",
                "content": (
                    "Python 标准库是 Python 的一大优势——\"开箱即用\"。常用模块：os（操作系统接口，路径/环境变量/进程）、"
                    "sys（解释器参数、标准流、递归深度）、re（正则表达式匹配和替换）、json（JSON 序列化/反序列化）、"
                    "datetime（日期时间处理、时区、时间差计算）、collections（deque 双端队列、Counter 计数器、"
                    "namedtuple 具名元组）、itertools（排列组合、无限迭代器、分组）、functools（偏函数、缓存）、"
                    "random（随机数生成）。多了解标准库能避免重复造轮子，代码也更简洁可靠。"
                ),
                "examples": [
                    "# json 序列化\nimport json\ndata = {\"name\": \"Alice\", \"items\": [1, 2, 3]}\njson_str = json.dumps(data, ensure_ascii=False, indent=2)\nrestored = json.loads(json_str)",
                    "# collections：Counter 统计\nfrom collections import Counter, namedtuple\ncnt = Counter(\"abracadabra\")\nprint(cnt.most_common(3))  # [('a', 5), ('b', 2), ('r', 2)]\n\n# namedtuple：轻量类\nPoint = namedtuple(\"Point\", [\"x\", \"y\"])\np = Point(10, 20)\nprint(p.x, p.y)  # 10 20",
                    "# itertools 高效迭代\nfrom itertools import product, combinations\nprint(list(product(\"AB\", repeat=2)))      # [('A','A'), ('A','B'), ('B','A'), ('B','B')]\nprint(list(combinations(\"ABC\", 2)))       # [('A','B'), ('A','C'), ('B','C')]"
                ],
                "key_points": [
                    "标准库：os、sys、json、re、datetime、random",
                    "collections：deque、Counter、namedtuple、defaultdict",
                    "itertools：产品/排列/组合等高效迭代工具",
                ],
            },
            {
                "id": "lesson_py_030",
                "title": "常用第三方库",
                "topic": "常用库",
                "content": (
                    "Python 的强大离不开丰富的第三方库生态。最常用的：requests（HTTP 请求，简洁优雅，替代 urllib）、"
                    "pandas（数据分析，DataFrame 是 Python 数据分析的事实标准）、numpy（科学计算，高效的数组运算）、"
                    "matplotlib（数据可视化，静态图表绘制）、flask/fastapi（Web 框架，构建 API 服务）、"
                    "sqlalchemy（ORM 框架，数据库操作）、pytest（测试框架，简洁强大）、"
                    "black/isort（代码格式化，统一代码风格）。安装三方库：pip install 包名。"
                    "善用三方库是高效开发的秘诀——不要重复造轮子。"
                ),
                "examples": [
                    "# requests：HTTP 请求\nimport requests\nresp = requests.get(\"https://api.github.com\", timeout=5)\nprint(resp.status_code)  # 200\nprint(resp.json())       # 自动解析 JSON",
                    "# pandas：数据分析\nimport pandas as pd\ndf = pd.DataFrame({\n    \"name\": [\"Alice\", \"Bob\", \"Charlie\"],\n    \"score\": [85, 92, 78]\n})\nprint(df.describe())  # 统计摘要\nprint(df[df[\"score\"] > 80])  # 过滤：score > 80 的行",
                    "# numpy：数组运算\nimport numpy as np\narr = np.array([1, 2, 3, 4, 5])\nprint(arr * 2)          # [2 4 6 8 10]（向量化运算）\nprint(arr[arr > 3])     # [4 5]（布尔索引）"
                ],
                "key_points": [
                    "requests 网络请求、pandas 数据分析、numpy 科学计算",
                    "Flask/FastAPI Web 框架、pytest 测试框架",
                    "pip install 安装，virtualenv/venv 管理虚拟环境",
                ],
            },
        ],
    },
    # ===== 装饰器深入 =====
    {
        "topic": "装饰器深入",
        "topic_concept": TOPIC_CONCEPTS["装饰器深入"],
        "lessons": [
            {
                "id": "lesson_py_031",
                "title": "装饰器高级模式",
                "topic": "装饰器深入",
                "content": (
                    "基础装饰器之后，深入掌握实际工程中常见的高级模式。类装饰器：用类实现装饰器，"
                    "__init__ 接收被装饰对象，__call__ 替代 wrapper 逻辑，适合需要维护状态的场景"
                    "（如计数器、限流器）。带参数的类装饰器在 __init__ 中接收参数。"
                    "装饰器工厂模式：根据条件动态返回不同装饰器，让你可以在运行时决定装饰行为。"
                    "singledispatch 单分派泛函数：根据第一个参数的类型分发到不同实现，"
                    "无需写一长串 isinstance 判断，代码更清晰、可扩展（第三方可注册新类型）。"
                    "实际工程中的经典应用：参数验证装饰器——结合类型注解和运行时校验，"
                    "在函数入口自动检查参数类型和范围；注册表模式——用装饰器自动将函数注册到全局字典，"
                    "常用于插件系统、命令路由；retry 装饰器——处理临时错误自动重试，支持指数退避和最大重试次数。"
                    "理解装饰器的本质是「编译时/导入时元编程」，你就能写出框架级的优雅代码。"
                ),
                "examples": [
                    "# 类装饰器：适用于需要状态的场景\nclass CountCalls:\n    def __init__(self, func):\n        self.func = func\n        self.count = 0\n\n    def __call__(self, *args, **kwargs):\n        self.count += 1\n        print(f\"{self.func.__name__} 被调用 {self.count} 次\")\n        return self.func(*args, **kwargs)\n\n@CountCalls\ndef hello():\n    print(\"Hello\")\n\nhello()  # hello 被调用 1 次\nhello()  # hello 被调用 2 次",
                    "# singledispatch：按类型分发\nfrom functools import singledispatch\n\n@singledispatch\ndef process(arg):\n    raise TypeError(f\"不支持类型 {type(arg)}\")\n\n@process.register(int)\ndef _(arg):\n    return f\"整数: {arg}\"\n\n@process.register(str)\ndef _(arg):\n    return f\"字符串: {arg}\"\n\nprint(process(42))     # 整数: 42\nprint(process(\"hi\"))   # 字符串: hi",
                    "# 注册表模式：装饰器自动注册插件\nplugins = {}\n\ndef register(name):\n    def decorator(func):\n        plugins[name] = func\n        return func\n    return decorator\n\n@register(\"pdf\")\ndef export_pdf(data):\n    return f\"导出 PDF: {data}\"\n\n@register(\"excel\")\ndef export_excel(data):\n    return f\"导出 Excel: {data}\"\n\nprint(plugins[\"pdf\"](\"报表\"))   # 导出 PDF: 报表"
                ],
                "key_points": [
                    "类装饰器用 __call__ 实现，适合需要维护状态的场景",
                    "singledispatch 按第一个参数类型分发，替代冗长 isinstance",
                    "注册表模式用装饰器自动收集函数，常用于插件/路由系统",
                ],
            },
        ],
    },
    # ===== 异步编程 =====
    {
        "topic": "异步编程",
        "topic_concept": TOPIC_CONCEPTS["异步编程"],
        "lessons": [
            {
                "id": "lesson_py_032",
                "title": "asyncio 协程与事件循环",
                "topic": "异步编程",
                "content": (
                    "asyncio 是 Python 异步 I/O 的核心框架，基于「事件循环 + 协程」模型实现单线程高并发。"
                    "协程用 async def 定义，调用协程函数返回一个 coroutine 对象而非立即执行。"
                    "await 关键字挂起当前协程，等待可等待对象（coroutine / Task / Future）完成，"
                    "事件循环在此期间调度其他协程执行。Task 将协程包装为独立任务并发运行，"
                    "asyncio.gather() 并发执行多个协程并收集结果。理解「协作式多任务」的关键："
                    "只有在 await 点才会切换，不会像线程那样随时被抢占，因此没有数据竞争问题，"
                    "但需要注意不要在协程中调用同步阻塞函数（如 requests.get），会阻塞整个事件循环。"
                    "asyncio.run() 是 Python 3.7+ 推荐的主入口，自动创建和管理事件循环。"
                    "实际应用中搭配 aiohttp（异步 HTTP）、aiomysql/asyncpg（异步数据库）构建全异步链路。"
                ),
                "examples": [
                    "# 基本的 async/await\nimport asyncio\n\nasync def fetch_data(url, delay):\n    print(f\"开始请求 {url}\")\n    await asyncio.sleep(delay)  # 模拟 IO 等待\n    print(f\"{url} 完成\")\n    return f\"data from {url}\"\n\nasync def main():\n    # gather 并发执行多个协程\n    results = await asyncio.gather(\n        fetch_data(\"url1\", 2),\n        fetch_data(\"url2\", 1),\n        fetch_data(\"url3\", 3),\n    )\n    print(results)  # 总耗时约 3 秒（最慢的那个），而非 2+1+3=6 秒\n\nasyncio.run(main())",
                    "# Task 手动创建和等待\nasync def main2():\n    task1 = asyncio.create_task(fetch_data(\"A\", 2))\n    task2 = asyncio.create_task(fetch_data(\"B\", 1))\n    # 两个 task 已在后台并发运行\n    r1 = await task1\n    r2 = await task2\n    print(r1, r2)\n\n# asyncio.run(main2())",
                    "# 常见错误：在协程中调用同步阻塞函数\nimport time\nasync def bad_example():\n    time.sleep(2)  # 阻塞整个事件循环！其他协程无法运行\n    # 正确做法：await asyncio.sleep(2)"
                ],
                "key_points": [
                    "async def 定义协程，await 挂起等待，事件循环调度切换",
                    "gather() 并发执行多个协程，create_task() 创建后台任务",
                    "严禁在协程中调用同步阻塞函数，需要「一路 async 到底」",
                ],
            },
        ],
    },
    # ===== 类型系统 =====
    {
        "topic": "类型系统",
        "topic_concept": TOPIC_CONCEPTS["类型系统"],
        "lessons": [
            {
                "id": "lesson_py_033",
                "title": "Type Hints 基础",
                "topic": "类型系统",
                "content": (
                    "Python 3.5+ 引入类型注解，配合 mypy/pyright 实现静态类型检查。"
                    "基础语法：变量注解 var: type，函数签名 def func(arg: type) -> ret_type。"
                    "typing 模块核心类型：Optional[X] 表示 X | None（3.10+ 可直接用 X | None），"
                    "Union[X, Y] 表示 X | Y（3.10+ 直接用 X | Y），Any 表示任意类型（关闭检查），"
                    "List[X]、Dict[K, V]、Tuple[X, ...]、Set[X]（3.9+ 建议用内置 list[X] 等）。"
                    "Callable[[ArgTypes], RetType] 标注函数类型，"
                    "Literal[\"a\", \"b\"] 限定值为特定字面量。"
                    "类型注解不会影响运行时行为（Python 仍是动态语言），"
                    "但能极大提升代码可读性、IDE 智能提示和重构安全性。"
                    "建议新项目从一开始就加类型注解，老项目逐步增量添加。"
                ),
                "examples": [
                    "# 基础类型注解\nfrom typing import Optional, Union, List, Dict\n\ndef get_user(name: str, age: Optional[int] = None) -> Dict[str, Union[str, int]]:\n    result: Dict[str, Union[str, int]] = {\"name\": name}\n    if age is not None:\n        result[\"age\"] = age\n    return result\n\n# Python 3.10+ 更简洁的语法\ndef process(items: list[str], limit: int | None = None) -> dict[str, int]:\n    return {item: len(item) for item in items[:limit]}",
                    "# Callable 标注函数参数\ndef apply(func: Callable[[int, int], int], a: int, b: int) -> int:\n    return func(a, b)\n\nresult = apply(lambda x, y: x + y, 3, 5)  # 8",
                    "# Literal 限定具体值\nfrom typing import Literal\n\ndef set_mode(mode: Literal[\"read\", \"write\", \"append\"]) -> None:\n    print(f\"模式设为 {mode}\")\n\nset_mode(\"read\")    # OK\n# set_mode(\"delete\")  # mypy 会报错"
                ],
                "key_points": [
                    "变量: 类型 / def f(arg: T) -> R 是基础注解语法",
                    "Optional[X] = X|None, Union[X,Y] = X|Y, Callable 标注函数",
                    "类型注解不影响运行时，但提升可读性、IDE 提示和静态检查",
                ],
            },
            {
                "id": "lesson_py_034",
                "title": "泛型与 Protocol",
                "topic": "类型系统",
                "content": (
                    "泛型让你的函数和类可以处理多种类型同时保持类型安全。"
                    "TypeVar 声明类型变量，Generic[T] 定义泛型类。"
                    "例如一个泛型栈 Stack[T]：方法 push(item: T) 和 pop() -> T 能自动推断具体类型，"
                    "mypy 会检查 push(1) 后 pop() 返回 int，不会让你误用为 str。"
                    "Protocol（结构化子类型）是 Python 对「鸭子类型」的形式化："
                    "只要一个类实现了 Protocol 定义的方法签名，就被视为该类型的子类型，"
                    "无需显式继承。这比 ABC 更灵活，符合 Python 哲学。"
                    "TypedDict 标注字典的键值结构，适合 JSON/API 响应等场景。"
                    "Final 标记不可变变量、@final 禁止子类重写方法。"
                    "掌握泛型+Protocol 是写出既灵活又类型安全的大型 Python 项目的关键。"
                ),
                "examples": [
                    "# 泛型类\nfrom typing import TypeVar, Generic\n\nT = TypeVar(\"T\")\n\nclass Stack(Generic[T]):\n    def __init__(self) -> None:\n        self._items: list[T] = []\n\n    def push(self, item: T) -> None:\n        self._items.append(item)\n\n    def pop(self) -> T:\n        return self._items.pop()\n\nint_stack = Stack[int]()\nint_stack.push(1)\nn: int = int_stack.pop()  # mypy 确认类型正确\n# int_stack.push(\"str\")    # mypy 报错",
                    "# Protocol：结构化子类型（静态鸭子类型）\nfrom typing import Protocol\n\nclass Drawable(Protocol):\n    def draw(self) -> str: ...\n\nclass Circle:\n    def draw(self) -> str:\n        return \"○\"\n\nclass Square:\n    def draw(self) -> str:\n        return \"□\"\n\ndef render(shape: Drawable) -> None:\n    print(shape.draw())\n\nrender(Circle())  # OK，无需显式继承 Drawable\nrender(Square())  # OK",
                    "# TypedDict：标注字典结构\nfrom typing import TypedDict\n\nclass User(TypedDict):\n    name: str\n    age: int\n\ndef greet(user: User) -> str:\n    return f\"{user['name']} ({user['age']}岁)\"\n\nalice: User = {\"name\": \"Alice\", \"age\": 25}\nprint(greet(alice))  # Alice (25岁)"
                ],
                "key_points": [
                    "TypeVar + Generic[T] 实现泛型类，保持类型安全",
                    "Protocol 结构化子类型：实现方法签名即子类型，无需继承",
                    "TypedDict 标注字典结构、Final 禁止覆盖、@final 禁止重写",
                ],
            },
        ],
    },
    # ===== 性能优化 =====
    {
        "topic": "性能优化",
        "topic_concept": TOPIC_CONCEPTS["性能优化"],
        "lessons": [
            {
                "id": "lesson_py_035",
                "title": "性能剖析与优化策略",
                "topic": "性能优化",
                "content": (
                    "性能优化第一铁律：先测量，再优化。盲目优化是万恶之源。"
                    "内置 cProfile 做热点分析，定位最耗时的函数；line_profiler 逐行计时，"
                    "精确到每条语句的耗时；memory_profiler 检查内存泄漏和峰值；"
                    "timeit 模块做微基准测试，注意先预热（warmup）消除 JIT/缓存偏差。"
                    "常见优化技巧：①循环中频繁的属性访问和全局变量查找代价高——"
                    "把 obj.attr 缓存为局部变量 local_attr = obj.attr 然后循环中使用；"
                    "②字符串拼接不要用 + 在循环中累加，用 ''.join() 一次性完成；"
                    "③__slots__ 减少实例 __dict__ 的内存开销（每个实例省约 56 字节），"
                    "适合千万级对象场景；④生成器替代列表返回中间结果，降低内存峰值；"
                    "⑤functools.lru_cache 缓存重复计算结果，尤其适合递归和数据库查询结果。"
                    "终极武器：PyPy（JIT 编译，平均提速 3-7 倍，纯 Python 无改动）、"
                    "Cython（编译为 C 扩展）、Numba（JIT 加速数值计算）。"
                ),
                "examples": [
                    "# cProfile 热点分析\nimport cProfile\nimport pstats\n\ndef slow_function():\n    total = 0\n    for i in range(1_000_000):\n        total += i ** 2\n    return total\n\n# profiler = cProfile.Profile()\n# profiler.enable()\n# slow_function()\n# profiler.disable()\n# pstats.Stats(profiler).sort_stats('cumulative').print_stats(10)",
                    "# 优化技巧 1：缓存属性访问\nimport math\nnums = range(1_000_000)\n# 慢：每次循环查找 math.sqrt\nresult1 = [math.sqrt(x) for x in nums]\n# 快：缓存为局部变量\nsqrt = math.sqrt\nresult2 = [sqrt(x) for x in nums]",
                    "# 优化技巧 2：__slots__ 节省内存\nclass PointSlots:\n    __slots__ = ('x', 'y')\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n\nclass PointDict:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n\n# PointSlots 每个实例约 56 字节 vs PointDict 约 152 字节\n# 创建 100 万个 PointSlots 可省约 96 MB 内存"
                ],
                "key_points": [
                    "cProfile 热点分析 + line_profiler 逐行计时 + timeit 微基准",
                    "缓存属性为局部变量、join 替代 + 拼接、__slots__ 省内存",
                    "PyPy/Cython/Numba 是终极武器，先用内置技巧优化再上编译方案",
                ],
            },
        ],
    },
    # ===== 实战项目 =====
    {
        "topic": "实战项目",
        "topic_concept": TOPIC_CONCEPTS["实战项目"],
        "lessons": [
            {
                "id": "lesson_py_036",
                "title": "综合实战",
                "topic": "实战项目",
                "content": (
                    "学完所有知识点后，通过完整项目将技能串联起来，建立从需求到交付的全链路思维。"
                    "推荐三类项目：①命令行工具：argparse 构建可配置的 CLI，rich 美化终端输出，"
                    "click 框架简化命令定义。适合自动化脚本、批量处理、运维工具。"
                    "②REST API 服务：FastAPI 定义路由和模型（Pydantic 自动校验），"
                    "async/await 处理高并发请求，uvicorn 高性能部署，自动生成 Swagger 文档。"
                    "③数据处理管道：pandas 清洗和转换数据，asyncio 并发拉取多个数据源，"
                    "openpyxl 或 xlsxwriter 导出精美 Excel 报表，matplotlib 生成可视化图表。"
                    "项目规范：pyproject.toml 管理依赖（替代 requirements.txt），"
                    "src 布局隔离源码与配置，pytest 编写单元测试和集成测试，"
                    "pre-commit 在 git commit 前自动运行 lint 和格式检查。"
                    "动手完成一个完整项目，比读一百个知识点都有效。"
                ),
                "examples": [
                    "# 命令行工具骨架（click）\nimport click\n\n@click.group()\ndef cli():\n    \"\"\"我的工具箱\"\"\"\n    pass\n\n@cli.command()\n@click.argument('path')\n@click.option('--verbose', '-v', is_flag=True, help='详细输出')\ndef analyze(path: str, verbose: bool):\n    \"\"\"分析指定路径的文件\"\"\"\n    if verbose:\n        click.echo(f\"正在分析 {path}...\")\n    # 核心逻辑\n    click.echo(f\"分析完成: {path}\")\n\nif __name__ == '__main__':\n    cli()",
                    "# FastAPI 最小示例\nfrom fastapi import FastAPI\nfrom pydantic import BaseModel\n\napp = FastAPI()\n\nclass Item(BaseModel):\n    name: str\n    price: float\n\n@app.get(\"/\")\nasync def root():\n    return {\"message\": \"Hello World\"}\n\n@app.post(\"/items\")\nasync def create_item(item: Item):\n    return {\"name\": item.name, \"price_with_tax\": item.price * 1.13}\n\n# 运行：uvicorn main:app --reload\n# 访问 http://127.0.0.1:8000/docs 查看自动生成的 API 文档",
                    "# 项目结构参考\n# myproject/\n# ├── pyproject.toml       # 依赖和配置\n# ├── src/\n# │   └── myproject/\n# │       ├── __init__.py\n# │       ├── cli.py       # 命令行入口\n# │       └── core.py      # 核心逻辑\n# ├── tests/\n# │   └── test_core.py     # pytest 测试\n# └── .pre-commit-config.yaml"
                ],
                "key_points": [
                    "CLI 工具：click/argparse + rich；REST API：FastAPI + Pydantic",
                    "项目规范：pyproject.toml + src 布局 + pytest + pre-commit",
                    "端到端完成一个项目，串联所有知识的最高效方式",
                ],
            },
        ],
    },
]


# ============================================================
# 服务函数
# ============================================================

def get_learning_path(language: str = "python") -> list[dict[str, Any]]:
    """返回按 topic 分组的学习路径（支持多语言）"""
    if language == "python":
        return _python_learning_path()
    else:
        return _generic_learning_path(language)


def _python_learning_path() -> list[dict[str, Any]]:
    """Python 完整学习路径"""
    return [
        {
            "topic": group["topic"],
            "topic_concept": group["topic_concept"],
            "lessons": [
                {
                    "id": les["id"],
                    "title": les["title"],
                    "topic": les["topic"],
                    "key_points": les["key_points"],
                }
                for les in group["lessons"]
            ],
        }
        for group in LEARNING_PATH
    ]


def _generic_learning_path(language: str) -> list[dict[str, Any]]:
    """根据 TOPIC_CONCEPTS 或完整课程数据动态生成非 Python 语言的学习路径"""

    # 优先使用完整课程数据（multi_lang_lessons.py）
    full_path = ALL_LANG_LEARNING_PATHS.get(language)
    if full_path is not None:
        result = []
        for group in full_path:
            result.append({
                "topic": group["topic"],
                "topic_concept": "",
                "lessons": [
                    {
                        "id": les["id"],
                        "title": les["title"],
                        "topic": les["topic"],
                        "key_points": les.get("key_points", []),
                    }
                    for les in group["lessons"]
                ],
            })
        return result

    # 回退：根据 TOPIC_CONCEPTS 动态生成（兼容尚未编写完整课程的语言）
    language_prefix_map = {
        "java":       ("java",       ("Java", "Spring")),
        "javascript": ("js",         ("JS",)),
        "cpp":        ("cpp",        ("C++",)),
        "go":         ("go",         ("Go",)),
        "typescript": ("ts",         ("TypeScript",)),
        "rust":       ("rust",       ("Rust",)),
        "sql":        ("sql",        ("SQL", "JOIN", "聚合", "索引", "安全")),
    }

    entry = language_prefix_map.get(language)
    if entry is None:
        return []  # 不支持的语言返回空

    prefix, topic_prefixes = entry

    result = []
    for topic, concept in TOPIC_CONCEPTS.items():
        matches = False
        for tp in topic_prefixes:
            if topic.startswith(tp):
                matches = True
                break
        if not matches:
            continue

        result.append({
            "topic": topic,
            "topic_concept": concept,
            "lessons": [
                {
                    "id": f"lesson_{prefix}_{topic.replace(' ', '_')}",
                    "title": topic,
                    "topic": topic,
                    "key_points": [concept[:100] + "..." if len(concept) > 100 else concept],
                }
            ],
        })
    return result


def get_lesson(lesson_id: str, language: str = "python") -> dict[str, Any] | None:
    """返回单个知识点的完整内容（支持多语言）"""
    # 1) 先搜索 Python 完整路径
    for group in LEARNING_PATH:
        for les in group["lessons"]:
            if les["id"] == lesson_id:
                return dict(les)

    # 2) 搜索多语言完整课程数据（multi_lang_lessons.py）
    full_path = ALL_LANG_LEARNING_PATHS.get(language)
    if full_path:
        for group in full_path:
            for les in group["lessons"]:
                if les["id"] == lesson_id:
                    return dict(les)

    # 3) 回退：非 Python 语言从动态生成的学习路径中构建基础课程
    if language != "python":
        generic_path = get_learning_path(language)
        for group in generic_path:
            for les in group["lessons"]:
                if les["id"] == lesson_id:
                    return {
                        "id": les["id"],
                        "title": les["title"],
                        "topic": les["topic"],
                        "content": group["topic_concept"],
                        "examples": [],
                        "key_points": les.get("key_points", []),
                    }
    return None


def get_lesson_exercises(lesson_id: str, count: int = 5, language: str = "python") -> list[dict[str, Any]]:
    """根据语言从习题库筛选与知识点所属 topic 相同的题目，返回不含 answer 的习题列表"""
    lesson = get_lesson(lesson_id)
    if not lesson:
        return []

    bank = ALL_EXERCISE_BANKS.get(language, PYTHON_EXERCISES)
    topic = lesson["topic"]
    filtered = [q for q in bank if q["topic"] == topic]

    remaining = [q for q in bank if q not in filtered]
    import random
    if len(filtered) < count:
        needed = count - len(filtered)
        if remaining:
            extra = random.sample(remaining, min(needed, len(remaining)))
            filtered = filtered + extra

    selected = filtered[:count]
    random.shuffle(selected)

    # 去掉 answer 字段，附上概念解释
    return [
        {**{k: v for k, v in q.items() if k != "answer"}, "concept": TOPIC_CONCEPTS.get(q["topic"], "")}
        for q in selected
    ]
