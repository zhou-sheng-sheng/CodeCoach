"""分级题库 — 按难度和主题检索习题的向量库"""
import uuid
from rag.embedder import embedder
from rag.store import get_collection, EXERCISE_BANK_COLLECTION as COLLECTION_NAME


class ExerciseBank:
    """分级习题向量检索引擎"""

    def __init__(self):
        self.collection = get_collection(COLLECTION_NAME)

    def add(self, exercises: list[dict]):
        """批量添加习题"""
        texts = [ex["text"] for ex in exercises]
        metadatas = [
            {
                "difficulty": ex.get("difficulty", "medium"),
                "topic": ex.get("topic", ""),
                "language": ex.get("language", "python"),
                "exercise_type": ex.get("exercise_type", "code_writing"),
            }
            for ex in exercises
        ]
        ids = [str(uuid.uuid4()) for _ in texts]
        embeddings = embedder.embed(texts)
        self.collection.add(documents=texts, metadatas=metadatas, embeddings=embeddings, ids=ids)
        return ids

    def search(
        self,
        query: str,
        k: int = 5,
        difficulty: str | None = None,
        topic: str | None = None,
    ) -> list[dict]:
        """按条件检索习题"""
        query_embedding = embedder.embed_query(query)

        where_filter = {}
        if difficulty:
            where_filter["difficulty"] = difficulty
        if topic:
            where_filter["topic"] = topic

        # ChromaDB 要求多条件时用 $and
        if len(where_filter) > 1:
            where_filter = {"$and": [{k: v} for k, v in where_filter.items()]}

        kwargs = {"query_embeddings": [query_embedding], "n_results": k}
        if where_filter:
            kwargs["where"] = where_filter

        results = self.collection.query(**kwargs)

        out = []
        if results["ids"] and results["ids"][0]:
            for i, doc_id in enumerate(results["ids"][0]):
                out.append({
                    "id": doc_id,
                    "content": results["documents"][0][i],
                    "metadata": results["metadatas"][0][i] if results["metadatas"] else {},
                    "distance": results["distances"][0][i] if results["distances"] else 0,
                })
        return out

    def count(self) -> int:
        return self.collection.count()

    def reset(self):
        try:
            self.collection._client.delete_collection(name=COLLECTION_NAME)
        except Exception:
            pass
        self.collection = get_collection(COLLECTION_NAME)


# 种子习题
SEED_EXERCISES = [
    {
        "text": "【Python·简单】写一个函数 is_palindrome(s)，判断字符串是否为回文（忽略大小写和空格）。例：'A man a plan a canal Panama' → True",
        "difficulty": "easy", "topic": "字符串处理", "language": "python", "exercise_type": "code_writing"
    },
    {
        "text": "【Python·中等】实现一个函数 flatten(arr)，将任意嵌套的列表展平为一维列表。例：flatten([1, [2, [3, 4], 5], 6]) → [1, 2, 3, 4, 5, 6]",
        "difficulty": "medium", "topic": "递归", "language": "python", "exercise_type": "code_writing"
    },
    {
        "text": "【Python·困难】实现一个 LRU 缓存类 LRUCache(capacity)，支持 get(key) 和 put(key, value) 操作，均要求 O(1) 时间复杂度。使用 OrderedDict 或 哈希表+双向链表。",
        "difficulty": "hard", "topic": "数据结构", "language": "python", "exercise_type": "code_writing"
    },
    {
        "text": "【通用·中等】以下代码有什么问题？\ndef add_item(item, lst=[]):\n    lst.append(item)\n    return lst\n请解释原因并给出修复方案。",
        "difficulty": "medium", "topic": "Python陷阱", "language": "python", "exercise_type": "debugging"
    },
    {
        "text": "【Python·简单】以下列表推导式的结果是什么？\n[x for x in range(10) if x % 2 == 0]\nA) [0,2,4,6,8]  B) [1,3,5,7,9]  C) [0,1,2,3,4,5,6,7,8,9]  D) Error",
        "difficulty": "easy", "topic": "列表推导式", "language": "python", "exercise_type": "multiple_choice"
    },
    {
        "text": "【算法·中等】给定一个整数数组 nums 和目标值 target，找出数组中和为 target 的两个数的索引。假设只有一组解。请用 O(n) 时间复杂度的解法。",
        "difficulty": "medium", "topic": "哈希表", "language": "python", "exercise_type": "code_writing"
    },
    {
        "text": "【Python·中等】审查以下代码：\ndef divide_by(numbers, divisor):\n    return [n / divisor for n in numbers]\n指出潜在问题并给出改进方案。",
        "difficulty": "medium", "topic": "错误处理", "language": "python", "exercise_type": "code_review"
    },
    {
        "text": "【Python·简单】用 Python 写一个函数，接收一个字符串并返回出现频率最高的字符及其次数。如果有多个字符频率相同，返回第一个遇到的。",
        "difficulty": "easy", "topic": "字典", "language": "python", "exercise_type": "code_writing"
    },
    {
        "text": "【Python·中等】实现装饰器 @retry(max_attempts=3)，使被装饰函数在抛出指定异常时自动重试，超过最大次数才抛出异常。",
        "difficulty": "medium", "topic": "装饰器", "language": "python", "exercise_type": "code_writing"
    },
    {
        "text": "【算法·困难】给定字符串 s 和单词字典 wordDict，判断 s 是否可以由字典中的单词拼接而成。同一单词可多次使用。例：s='leetcode', wordDict=['leet','code'] → True",
        "difficulty": "hard", "topic": "动态规划", "language": "python", "exercise_type": "code_writing"
    },
    {
        "text": "【JavaScript·中等】解释以下代码的输出并说明原因：\nfor (var i = 0; i < 3; i++) {\n  setTimeout(() => console.log(i), 100);\n}\n如何修复使其输出 0, 1, 2？",
        "difficulty": "medium", "topic": "闭包", "language": "javascript", "exercise_type": "code_review"
    },
    {
        "text": "【Python·简单】以下哪个选项是正确的字典创建方式？\nA) d = {}  B) d = dict()  C) d = {1: 'a', 2: 'b'}  D) 以上都是",
        "difficulty": "easy", "topic": "字典", "language": "python", "exercise_type": "multiple_choice"
    },
    {
        "text": "【Python·中等】创建一个生成器函数 fibonacci(n)，生成前 n 个斐波那契数。使用 yield 实现惰性求值。",
        "difficulty": "medium", "topic": "生成器", "language": "python", "exercise_type": "code_writing"
    },
    {
        "text": "【Python·困难】实现一个线程安全的单例模式类。需要考虑多线程环境下的懒加载。",
        "difficulty": "hard", "topic": "设计模式", "language": "python", "exercise_type": "code_writing"
    },
    {
        "text": "【SQL·中等】给定 employees(salary) 表，写 SQL 查询找出第二高的薪水。如果没有第二高，返回 null。",
        "difficulty": "medium", "topic": "SQL", "language": "sql", "exercise_type": "code_writing"
    },
    # ===== Java 习题 (5+) =====
    {
        "text": "【Java·简单】以下代码输出什么？\nString s1 = \"hello\";\nString s2 = \"hello\";\nSystem.out.println(s1 == s2);\nA) true  B) false  C) 报错  D) 不确定",
        "difficulty": "easy", "topic": "字符串", "language": "java", "exercise_type": "multiple_choice"
    },
    {
        "text": "【Java·简单】写一个方法 public static int sum(int[] arr)，计算整数数组所有元素之和并返回。如果数组为空返回 0。",
        "difficulty": "easy", "topic": "数组", "language": "java", "exercise_type": "code_writing"
    },
    {
        "text": "【Java·中等】以下代码有什么问题？\npublic class Test {\n    public static void main(String[] args) {\n        ArrayList list = new ArrayList();\n        list.add(\"hello\");\n        list.add(123);\n        String s = (String) list.get(1);\n    }\n}\n请指出问题并给出修复方案。",
        "difficulty": "medium", "topic": "泛型", "language": "java", "exercise_type": "debugging"
    },
    {
        "text": "【Java·中等】实现一个线程安全的懒汉单例模式类 Singleton，包含 private 构造方法和 public static 获取实例的方法。",
        "difficulty": "medium", "topic": "设计模式", "language": "java", "exercise_type": "code_writing"
    },
    {
        "text": "【Java·困难】解释 HashMap 的 put 方法底层原理：包括 hash 计算、数组索引定位、链表/红黑树转换条件，以及 JDK 7 和 JDK 8 在并发环境下的区别。",
        "difficulty": "hard", "topic": "HashMap", "language": "java", "exercise_type": "code_writing"
    },
    {
        "text": "【Java·中等】以下关于 equals 和 hashCode 的说法正确的是？\nA) 重写 equals 可以不重写 hashCode\nB) equals 相等的两个对象 hashCode 必须相等\nC) hashCode 相等的两个对象 equals 必须相等\nD) 以上都不对",
        "difficulty": "medium", "topic": "equals与hashCode", "language": "java", "exercise_type": "multiple_choice"
    },
    # ===== C++ 习题 (5+) =====
    {
        "text": "【C++·简单】以下代码输出什么？\nint a = 10;\nint &ref = a;\nref = 20;\nstd::cout << a;\nA) 10  B) 20  C) 报错  D) 不确定",
        "difficulty": "easy", "topic": "引用", "language": "cpp", "exercise_type": "multiple_choice"
    },
    {
        "text": "【C++·简单】写一个函数 std::vector<int> filterEven(const std::vector<int>& nums)，返回只包含偶数的 vector。",
        "difficulty": "easy", "topic": "STL", "language": "cpp", "exercise_type": "code_writing"
    },
    {
        "text": "【C++·中等】以下代码存在什么问题？\nclass Base {\npublic:\n    ~Base() { std::cout << \"Base dtor\\n\"; }\n};\nclass Derived : public Base {\npublic:\n    ~Derived() { std::cout << \"Derived dtor\\n\"; }\n};\nBase* p = new Derived();\ndelete p;\n请指出问题并修复。",
        "difficulty": "medium", "topic": "虚析构函数", "language": "cpp", "exercise_type": "debugging"
    },
    {
        "text": "【C++·中等】实现一个模板函数 template<typename T> T maxOfThree(T a, T b, T c)，返回三个参数中的最大值。",
        "difficulty": "medium", "topic": "模板", "language": "cpp", "exercise_type": "code_writing"
    },
    {
        "text": "【C++·困难】解释 unique_ptr、shared_ptr 和 weak_ptr 的区别和使用场景，以及 std::move 在智能指针转移所有权中的作用。为什么 weak_ptr 可以解决 shared_ptr 循环引用问题？",
        "difficulty": "hard", "topic": "智能指针", "language": "cpp", "exercise_type": "code_writing"
    },
    {
        "text": "【C++·中等】以下代码输出什么？\nstd::vector<int> v = {1, 2, 3};\nv.push_back(4);\nstd::cout << v.capacity();\nA) 3  B) 4  C) 6  D) 不确定（取决于实现）",
        "difficulty": "medium", "topic": "vector", "language": "cpp", "exercise_type": "multiple_choice"
    },
    # ===== Go 习题 (5+) =====
    {
        "text": "【Go·简单】以下代码输出什么？\npackage main\nfunc main() {\n    s := []int{1, 2, 3}\n    s = append(s, 4)\n    println(len(s))\n}\nA) 3  B) 4  C) 报错  D) 不确定",
        "difficulty": "easy", "topic": "切片", "language": "go", "exercise_type": "multiple_choice"
    },
    {
        "text": "【Go·简单】写一个函数 func factorial(n int) int，使用循环计算 n 的阶乘。如果 n < 0 返回 -1 表示错误。",
        "difficulty": "easy", "topic": "函数", "language": "go", "exercise_type": "code_writing"
    },
    {
        "text": "【Go·中等】以下代码有什么问题？\nfunc main() {\n    ch := make(chan int)\n    ch <- 1\n    fmt.Println(<-ch)\n}\n请解释死锁原因并给出两种修复方案。",
        "difficulty": "medium", "topic": "Channel", "language": "go", "exercise_type": "debugging"
    },
    {
        "text": "【Go·中等】写一个并发安全的计数器类型 SafeCounter，包含 Inc() 和 Value() 方法，支持多个 goroutine 同时递增和读取。",
        "difficulty": "medium", "topic": "并发", "language": "go", "exercise_type": "code_writing"
    },
    {
        "text": "【Go·困难】解释 Go 中 nil interface 和 nil 指针的区别。以下代码中，err 是否为 nil？\nfunc getError() error {\n    var p *MyError = nil\n    return p\n}\nfunc main() {\n    err := getError()\n    fmt.Println(err == nil)\n}\n为什么？",
        "difficulty": "hard", "topic": "接口", "language": "go", "exercise_type": "code_writing"
    },
    {
        "text": "【Go·中等】以下关于 defer 的说法正确的是？\nA) defer 语句在函数开始时执行\nB) 多个 defer 按声明顺序执行\nC) defer 在 return 之后、函数返回前执行\nD) 多个 defer 按后进先出（LIFO）顺序执行",
        "difficulty": "medium", "topic": "defer", "language": "go", "exercise_type": "multiple_choice"
    },
    # ===== TypeScript 习题种子 =====
    {
        "text": "【TypeScript·简单】写一个 TypeScript 接口 User 包含 id(number)、name(string)、email?(可选string)。然后写一个函数 getUserName 接收 User 返回 name。",
        "difficulty": "easy", "topic": "接口", "language": "typescript", "exercise_type": "code_writing"
    },
    {
        "text": "【TypeScript·简单】使用 TypeScript 枚举定义 HTTP 状态：OK=200, NotFound=404, ServerError=500。写函数 getStatusText 返回对应的字符串描述。",
        "difficulty": "easy", "topic": "枚举", "language": "typescript", "exercise_type": "code_writing"
    },
    {
        "text": "【TypeScript·中等】实现一个泛型函数 first<T>(arr: T[]): T | undefined，返回数组第一个元素。若空数组返回 undefined。",
        "difficulty": "medium", "topic": "泛型", "language": "typescript", "exercise_type": "code_writing"
    },
    {
        "text": "【TypeScript·中等】类型体操：写一个 MyPick<T, K extends keyof T> 类型，从 T 中选取指定属性 K。不使用内置 Pick。",
        "difficulty": "medium", "topic": "类型体操", "language": "typescript", "exercise_type": "code_writing"
    },
    {
        "text": "【TypeScript·中等】以下代码有什么问题？\nfunction printId(id: number | string) {\n  console.log(id.toUpperCase());\n}\n请修复，使用类型守卫确保安全访问。",
        "difficulty": "medium", "topic": "类型守卫", "language": "typescript", "exercise_type": "debugging"
    },
    {
        "text": "【TypeScript·困难】实现一个 DeepReadonly<T> 类型，将对象类型的所有嵌套属性递归设为 readonly。",
        "difficulty": "hard", "topic": "类型体操", "language": "typescript", "exercise_type": "code_writing"
    },
    {
        "text": "【TypeScript·中等】以下选项哪个正确描述了 Tuple（元组）？\nA) 定长且每位置类型固定  B) 等同于数组  C) 不支持类型标注  D) 运行时与数组不同",
        "difficulty": "medium", "topic": "元组", "language": "typescript", "exercise_type": "multiple_choice"
    },
    {
        "text": "【TypeScript·中等】实现工具类型 MyOmit<T, K extends keyof T>，从 T 中排除指定属性 K。提示：Pick + Exclude 组合。",
        "difficulty": "medium", "topic": "工具类型", "language": "typescript", "exercise_type": "code_writing"
    },
    {
        "text": "【TypeScript·简单】以下代码中 name 的类型是什么？\nconst arr = ['Alice', 'Bob', 'Charlie'] as const;\ntype Name = typeof arr[number];\nA) string  B) 'Alice' | 'Bob' | 'Charlie'  C) readonly string[]  D) any",
        "difficulty": "easy", "topic": "类型推导", "language": "typescript", "exercise_type": "multiple_choice"
    },
    {
        "text": "【TypeScript·中等】写一个函数 mergeObjects，使用泛型接收两个对象参数并返回它们的交叉类型合并结果。",
        "difficulty": "medium", "topic": "泛型", "language": "typescript", "exercise_type": "code_writing"
    },
    # ===== Rust 习题种子 =====
    {
        "text": "【Rust·简单】写一个函数 fn is_even(n: i32) -> bool，判断整数是否为偶数。",
        "difficulty": "easy", "topic": "函数", "language": "rust", "exercise_type": "code_writing"
    },
    {
        "text": "【Rust·简单】写一个函数 fn sum_vec(v: &Vec<i32>) -> i32，计算向量中所有元素的和。",
        "difficulty": "easy", "topic": "集合", "language": "rust", "exercise_type": "code_writing"
    },
    {
        "text": "【Rust·中等】实现一个函数 fn find_max<T: PartialOrd>(slice: &[T]) -> Option<&T>，返回切片中的最大元素引用。",
        "difficulty": "medium", "topic": "泛型与Trait", "language": "rust", "exercise_type": "code_writing"
    },
    {
        "text": "【Rust·中等】以下代码有什么问题？\nlet mut v = vec![1, 2, 3];\nlet first = &v[0];\nv.push(4);\nprintln!(\"{}\", first);\n请解释为什么编译错误并给出修复方案。",
        "difficulty": "medium", "topic": "借用检查", "language": "rust", "exercise_type": "debugging"
    },
    {
        "text": "【Rust·中等】写一个函数 fn word_count(text: &str) -> HashMap<&str, u32>，统计字符串中每个单词出现的次数。",
        "difficulty": "medium", "topic": "HashMap", "language": "rust", "exercise_type": "code_writing"
    },
    {
        "text": "【Rust·困难】实现一个简单的线程池 ThreadPool，支持创建固定数量工作线程并通过 channel 分发任务。",
        "difficulty": "hard", "topic": "并发", "language": "rust", "exercise_type": "code_writing"
    },
    {
        "text": "【Rust·中等】以下关于 String 和 &str 的说法正确的是？\nA) String 可变、堆分配；&str 是不可变引用  B) &str 可变  C) String 和 &str 完全相同  D) &str 是 String 的缩写",
        "difficulty": "medium", "topic": "字符串", "language": "rust", "exercise_type": "multiple_choice"
    },
    {
        "text": "【Rust·中等】实现 trait Summary { fn summarize(&self) -> String; } 并为 struct Article 和 Tweet 实现该 trait。",
        "difficulty": "medium", "topic": "Trait", "language": "rust", "exercise_type": "code_writing"
    },
    {
        "text": "【Rust·简单】以下哪个是创建新 Vec<i32> 的正确方式？\nA) let v: Vec<i32> = Vec::new()  B) let v = vec![1, 2, 3]  C) let v = Vec::from([1, 2, 3])  D) 以上都是",
        "difficulty": "easy", "topic": "Vec", "language": "rust", "exercise_type": "multiple_choice"
    },
    {
        "text": "【Rust·困难】使用 Rust 的通道（channel）实现生产者-消费者模式：一个线程生成 0..10，另一个线程接收并打印。",
        "difficulty": "hard", "topic": "并发", "language": "rust", "exercise_type": "code_writing"
    },
    # ===== SQL 习题种子 =====
    {
        "text": "【SQL·简单】写一个 SQL 查询，从 employees 表中选择所有部门为 'Engineering' 的员工姓名和薪资，按薪资降序排列。",
        "difficulty": "easy", "topic": "基础查询", "language": "sql", "exercise_type": "code_writing"
    },
    {
        "text": "【SQL·简单】写一个 SQL 查询创建 users 表：id 主键自增、name 不为空、email 唯一、created_at 默认当前时间戳。",
        "difficulty": "easy", "topic": "DDL", "language": "sql", "exercise_type": "code_writing"
    },
    {
        "text": "【SQL·中等】给定 departments(id,name) 和 employees(id,name,salary,dept_id)，写 SQL 查询每个部门的名称和平均薪资，按平均薪资降序。",
        "difficulty": "medium", "topic": "JOIN与聚合", "language": "sql", "exercise_type": "code_writing"
    },
    {
        "text": "【SQL·中等】写一个 SQL 查询找出 employees 表中薪资高于所在部门平均薪资的员工（子查询/窗口函数均可用）。",
        "difficulty": "medium", "topic": "子查询", "language": "sql", "exercise_type": "code_writing"
    },
    {
        "text": "【SQL·中等】以下查询有什么问题？\nSELECT name, MAX(salary) FROM employees;\nA) 正确  B) 缺少 GROUP BY  C) MAX 不能用于 SELECT  D) salary 必须索引",
        "difficulty": "medium", "topic": "聚合函数", "language": "sql", "exercise_type": "multiple_choice"
    },
    {
        "text": "【SQL·困难】使用窗口函数为 employees 表中每个部门的员工按薪资降序排名（并列排名不跳号），取每个部门前 3 名。",
        "difficulty": "hard", "topic": "窗口函数", "language": "sql", "exercise_type": "code_writing"
    },
    {
        "text": "【SQL·中等】写一个 SQL 查询删除 orders 表中所有重复记录（相同 customer_id 和 order_date），保留每组中 id 最小的那条。",
        "difficulty": "medium", "topic": "数据操作", "language": "sql", "exercise_type": "code_writing"
    },
    {
        "text": "【SQL·简单】以下哪个 SQL 注入防护方法最有效？\nA) 转义用户输入  B) 参数化查询/预编译语句  C) 校验输入长度  D) 使用 HTTPS",
        "difficulty": "easy", "topic": "安全性", "language": "sql", "exercise_type": "multiple_choice"
    },
    {
        "text": "【SQL·中等】写一个 SQL 查询为 orders 表的 customer_id 和 order_date 列创建复合索引。并说明索引使用的最左前缀原则。",
        "difficulty": "medium", "topic": "索引", "language": "sql", "exercise_type": "code_writing"
    },
    {
        "text": "【SQL·中等】写一个 SQL 事务：将账户 A 的余额减少 100，账户 B 增加 100。需要保证原子性（要么全成功要么全回滚）。",
        "difficulty": "medium", "topic": "事务", "language": "sql", "exercise_type": "code_writing"
    },
]


exercise_bank = ExerciseBank()
