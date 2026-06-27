"""多语言评估题库 — Java / JavaScript / C++ / Go"""

from typing import Any

MULTI_LANG_QUESTION_BANK: dict[str, list[dict[str, Any]]] = {
    "java": [
        {
            "id": "java_q1",
            "question": "Java 中，以下哪个是基本数据类型？",
            "options": ["A) String", "B) Integer", "C) int", "D) ArrayList", "E) 我不清楚"],
            "answer": 2, "difficulty": "easy", "topic": "Java基础",
            "explanation": "int 是 Java 的 8 种基本类型之一。String 和 Integer 是引用类型。"
        },
        {
            "id": "java_q2",
            "question": "以下代码输出什么？\nString s1 = new String(\"hello\");\nString s2 = new String(\"hello\");\nSystem.out.println(s1 == s2);",
            "options": ["A) true", "B) false", "C) 编译错误", "D) 运行时错误", "E) 我不清楚"],
            "answer": 1, "difficulty": "easy", "topic": "Java基础",
            "explanation": "== 比较引用地址，new 创建了两个不同对象，比较内容应用 s1.equals(s2)。"
        },
        {
            "id": "java_q3",
            "question": "以下代码输出什么？\nint[] arr = {1, 2, 3};\nint[] arr2 = arr;\narr2[0] = 99;\nSystem.out.println(arr[0]);",
            "options": ["A) 1", "B) 99", "C) 编译错误", "D) 运行时错误", "E) 我不清楚"],
            "answer": 1, "difficulty": "easy", "topic": "Java基础",
            "explanation": "arr2 = arr 使两个引用指向同一个数组对象，修改 arr2[0] 会影响 arr[0]。"
        },
        {
            "id": "java_q4",
            "question": "以下关于 ArrayList 和 LinkedList 的说法正确的是？",
            "options": ["A) ArrayList 底层是链表，LinkedList 底层是数组", "B) ArrayList 随机访问快，LinkedList 插入删除快", "C) ArrayList 和 LinkedList 都实现了 Set 接口", "D) LinkedList 比 ArrayList 更省内存", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "Java集合",
            "explanation": "ArrayList 底层是动态数组，随机访问 O(1)；LinkedList 底层是双向链表，插入删除 O(1)（已知位置）。"
        },
        {
            "id": "java_q5",
            "question": "HashMap 的底层数据结构是？",
            "options": ["A) 数组", "B) 链表", "C) 数组+链表+红黑树（JDK 8+）", "D) 平衡二叉树", "E) 我不清楚"],
            "answer": 2, "difficulty": "medium", "topic": "Java集合",
            "explanation": "JDK 8 中 HashMap 底层是数组+链表+红黑树。当链表长度 >= 8 且数组容量 >= 64 时，链表转为红黑树。"
        },
        {
            "id": "java_q6",
            "question": "以下关于 Java 继承的说法正确的是？",
            "options": ["A) Java 支持多继承", "B) 子类可以访问父类的 private 成员", "C) 子类构造方法必须先调用父类构造方法", "D) final 修饰的类可以被继承", "E) 我不清楚"],
            "answer": 2, "difficulty": "medium", "topic": "Java OOP",
            "explanation": "子类构造方法隐式或显式调用父类构造方法（super()），确保父类先初始化。"
        },
        {
            "id": "java_q7",
            "question": "以下代码输出什么？\ntry { int[] arr = {1,2}; System.out.println(arr[2]); }\ncatch (ArrayIndexOutOfBoundsException e) { System.out.println(\"Error\"); }\nfinally { System.out.println(\"Done\"); }",
            "options": ["A) Error", "B) Done", "C) Error Done", "D) 编译错误", "E) 我不清楚"],
            "answer": 2, "difficulty": "easy", "topic": "Java异常",
            "explanation": "arr[2] 越界触发异常，catch 打印 Error，finally 始终执行打印 Done。"
        },
        {
            "id": "java_q8",
            "question": "以下哪个是启动新线程的正确方式？",
            "options": ["A) new Thread().run()", "B) new Thread(task).start()", "C) task.run()", "D) Thread.start(task)", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "Java并发",
            "explanation": "必须调用 start() 启动新线程，直接调用 run() 只在当前线程执行。"
        },
        {
            "id": "java_q9",
            "question": "synchronized 代码块可以指定任意对象作为锁。这个说法？",
            "options": ["A) 正确", "B) 错误（只能用 this）", "C) 错误（只能用 Class 对象）", "D) 错误（synchronized 不支持代码块）", "E) 我不清楚"],
            "answer": 0, "difficulty": "medium", "topic": "Java并发",
            "explanation": "synchronized(obj) { ... } 可指定任意对象作为锁。方法中：静态方法锁 Class，实例方法锁 this。"
        },
        {
            "id": "java_q10",
            "question": "Spring Boot 内嵌了哪个 Web 服务器？",
            "options": ["A) Apache HTTPD", "B) Nginx", "C) Tomcat", "D) IIS", "E) 我不清楚"],
            "answer": 2, "difficulty": "medium", "topic": "Spring Boot",
            "explanation": "Spring Boot 默认内嵌 Tomcat，也可替换为 Jetty 或 Undertow。"
        },
    ],
    "javascript": [
        {
            "id": "js_q1",
            "question": "以下代码输出什么？\nconsole.log(typeof null);",
            "options": ["A) \"null\"", "B) \"undefined\"", "C) \"object\"", "D) \"number\"", "E) 我不清楚"],
            "answer": 2, "difficulty": "easy", "topic": "JS基础",
            "explanation": "typeof null 返回 \"object\" 是 JavaScript 的历史 Bug。"
        },
        {
            "id": "js_q2",
            "question": "以下代码输出什么？\nvar a = 1;\nfunction foo() { console.log(a); var a = 2; }\nfoo();",
            "options": ["A) 1", "B) 2", "C) undefined", "D) ReferenceError", "E) 我不清楚"],
            "answer": 2, "difficulty": "medium", "topic": "JS基础",
            "explanation": "var 有变量提升（hoisting），函数内 var a 被提升到函数顶部但值为 undefined。"
        },
        {
            "id": "js_q3",
            "question": "以下代码输出什么？\nconsole.log(0.1 + 0.2 === 0.3);",
            "options": ["A) true", "B) false", "C) undefined", "D) 报错", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "JS基础",
            "explanation": "浮点数精度问题：0.1 + 0.2 = 0.30000000000000004。"
        },
        {
            "id": "js_q4",
            "question": "以下代码输出什么？\nconst p = new Promise(r => r(1));\np.then(v => console.log(v));\nconsole.log(2);",
            "options": ["A) 1 2", "B) 2 1", "C) 1", "D) 2", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "JS异步",
            "explanation": "Promise.then 是微任务，在主线程同步代码执行完后才执行，所以先输出 2，再输出 1。"
        },
        {
            "id": "js_q5",
            "question": "async 函数总是返回 Promise。这个说法？",
            "options": ["A) 正确", "B) 错误（取决于返回值）", "C) 错误（async 返回原始值）", "D) 错误（async 不返回值）", "E) 我不清楚"],
            "answer": 0, "difficulty": "medium", "topic": "JS异步",
            "explanation": "async 函数总是返回 Promise，return 1 等价于 return Promise.resolve(1)。"
        },
        {
            "id": "js_q6",
            "question": "以下代码输出什么？\nconst obj = { a: 1, foo() { console.log(this.a); } };\nobj.foo();",
            "options": ["A) 1", "B) undefined", "C) window", "D) 报错", "E) 我不清楚"],
            "answer": 0, "difficulty": "easy", "topic": "JS原型与this",
            "explanation": "obj.foo() 调用时 this 指向 obj，所以 this.a = 1。"
        },
        {
            "id": "js_q7",
            "question": "以下代码输出什么？\n[1, 2, 3].map(x => x * 2).filter(x => x > 3);",
            "options": ["A) [4, 6]", "B) [2, 4, 6]", "C) [4]", "D) 报错", "E) 我不清楚"],
            "answer": 0, "difficulty": "easy", "topic": "JS基础",
            "explanation": "map 将每个元素乘2得 [2,4,6]，filter 筛选 >3 得 [4,6]。"
        },
        {
            "id": "js_q8",
            "question": "ES6 的 import/export 支持 Tree Shaking。这个说法？",
            "options": ["A) 正确", "B) 错误（import 不支持）", "C) 错误（只支持 CommonJS）", "D) 错误（Node.js 不支持 import）", "E) 我不清楚"],
            "answer": 0, "difficulty": "medium", "topic": "JS模块",
            "explanation": "ESM 的 import/export 是静态声明，打包工具可进行 Tree Shaking 移除未引用代码。"
        },
        {
            "id": "js_q9",
            "question": "以下代码输出什么？\nconsole.log([] == ![]);",
            "options": ["A) true", "B) false", "C) undefined", "D) 报错", "E) 我不清楚"],
            "answer": 0, "difficulty": "hard", "topic": "JS基础",
            "explanation": "![] 转为 false，[] == false 类型转换：[] 先转 \"\" 再转 0，false 转 0，所以 0 == 0 为 true。"
        },
        {
            "id": "js_q10",
            "question": "以下哪个是 JavaScript 的事件循环顺序？",
            "options": ["A) 宏任务 → 微任务 → 渲染", "B) 微任务 → 宏任务 → 渲染", "C) 同步代码 → 微任务 → 宏任务", "D) 宏任务 → 微任务 → 同步代码", "E) 我不清楚"],
            "answer": 2, "difficulty": "medium", "topic": "JS异步",
            "explanation": "事件循环：同步代码 → 清空微任务队列 → 取一个宏任务 → 清空微任务 → 循环。"
        },
    ],
    "cpp": [
        {
            "id": "cpp_q1",
            "question": "以下代码输出什么？\nint a = 10;\nint &ref = a;\nref = 20;\ncout << a;",
            "options": ["A) 10", "B) 20", "C) 编译错误", "D) 运行时错误", "E) 我不清楚"],
            "answer": 1, "difficulty": "easy", "topic": "C++基础",
            "explanation": "引用 ref 是 a 的别名，修改 ref 就是修改 a，所以输出 20。"
        },
        {
            "id": "cpp_q2",
            "question": "以下代码输出什么？\nint x = 5;\nint *p = &x;\ncout << *p;",
            "options": ["A) 地址值", "B) 5", "C) 编译错误", "D) 运行时错误", "E) 我不清楚"],
            "answer": 1, "difficulty": "easy", "topic": "C++基础",
            "explanation": "*p 解引用指针，获取 p 指向地址的值，即 x 的值 5。"
        },
        {
            "id": "cpp_q3",
            "question": "以下关于 vector 的说法正确的是？",
            "options": ["A) vector 底层是链表", "B) push_back 总是 O(1)", "C) 扩容时可能使所有迭代器失效", "D) vector 不支持随机访问", "E) 我不清楚"],
            "answer": 2, "difficulty": "medium", "topic": "C++STL",
            "explanation": "vector 底层是连续数组，扩容时重新分配内存，导致所有迭代器/指针/引用失效。"
        },
        {
            "id": "cpp_q4",
            "question": "unique_ptr 可以被拷贝。这个说法？",
            "options": ["A) 正确", "B) 错误（独占所有权，只能移动）", "C) 错误（可以被拷贝）", "D) 错误（unique_ptr 不是智能指针）", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "C++内存管理",
            "explanation": "unique_ptr 独占资源所有权，不可拷贝（删除拷贝构造），只能通过 std::move 转移所有权。"
        },
        {
            "id": "cpp_q5",
            "question": "以下代码有什么问题？\nBase *p = new Derived();\ndelete p;  // Base 析构函数非 virtual",
            "options": ["A) 内存泄漏", "B) 只调用 Base 析构，Derived 析构不被调用", "C) 编译错误", "D) 正常运行", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "C++多态",
            "explanation": "基类析构函数非 virtual 时，delete 基类指针只调用基类析构，Derived 部分不被析构。"
        },
        {
            "id": "cpp_q6",
            "question": "const 成员函数可以调用非 const 成员函数。这个说法？",
            "options": ["A) 正确", "B) 错误（不能调用非 const 函数）", "C) 正确（只要不修改成员）", "D) 取决于编译器", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "C++基础",
            "explanation": "const 成员函数不能调用非 const 成员函数，因为非 const 函数可能修改对象状态。"
        },
        {
            "id": "cpp_q7",
            "question": "RAII 的核心思想是？",
            "options": ["A) 垃圾回收", "B) 利用对象生命周期自动管理资源", "C) 引用计数", "D) 手动内存管理", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "C++内存管理",
            "explanation": "RAII（资源获取即初始化）：将资源生命周期绑定到对象生命周期，构造时获取、析构时释放。"
        },
        {
            "id": "cpp_q8",
            "question": "以下代码输出什么？\nvector<int> v = {1,2,3};\nfor (auto it = v.rbegin(); it != v.rend(); ++it)\n    cout << *it << ' ';",
            "options": ["A) 1 2 3", "B) 3 2 1", "C) 编译错误", "D) 运行时错误", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "C++STL",
            "explanation": "rbegin()/rend() 是反向迭代器，从末尾向开头遍历，输出 3 2 1。"
        },
        {
            "id": "cpp_q9",
            "question": "以下关于模板的说法正确的是？",
            "options": ["A) 模板代码在运行时动态生成", "B) 模板在编译期展开，可能导致代码膨胀", "C) 模板只适用于类", "D) 模板不能用于函数", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "C++基础",
            "explanation": "C++ 模板在编译期展开（模板实例化），每种类型组合都生成一份代码，可能导致二进制体积增大。"
        },
        {
            "id": "cpp_q10",
            "question": "以下关于移动语义的说法正确的是？",
            "options": ["A) std::move 移动数据并销毁源对象", "B) std::move 只是类型转换（转右值引用）", "C) 移动构造函数自动生成", "D) 移动后源对象必须为 null", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "C++基础",
            "explanation": "std::move 本质上是 static_cast<T&&>，不移动任何数据，只是将左值转为右值引用以便调用移动构造函数。"
        },
    ],
    "go": [
        {
            "id": "go_q1",
            "question": "以下代码输出什么？\ns := []int{1, 2, 3}\ns = append(s, 4)\nprintln(len(s))",
            "options": ["A) 3", "B) 4", "C) 编译错误", "D) 运行时错误", "E) 我不清楚"],
            "answer": 1, "difficulty": "easy", "topic": "Go基础",
            "explanation": "append 向切片追加元素，len(s) 返回切片当前长度 4。"
        },
        {
            "id": "go_q2",
            "question": "以下代码输出什么？\nm := map[string]int{\"a\": 1, \"b\": 2}\nv, ok := m[\"c\"]\nprintln(ok)",
            "options": ["A) true", "B) false", "C) 1", "D) 编译错误", "E) 我不清楚"],
            "answer": 1, "difficulty": "easy", "topic": "Go基础",
            "explanation": "访问 map 不存在的 key 时，ok 为 false，v 为值类型的零值。"
        },
        {
            "id": "go_q3",
            "question": "以下代码输出什么？\ndefer fmt.Println(\"first\")\ndefer fmt.Println(\"second\")\nfmt.Println(\"main\")",
            "options": ["A) first second main", "B) main first second", "C) main second first", "D) 编译错误", "E) 我不清楚"],
            "answer": 2, "difficulty": "easy", "topic": "Go defer",
            "explanation": "defer 按 LIFO（后进先出）顺序执行，先输出 main，再 second，最后 first。"
        },
        {
            "id": "go_q4",
            "question": "以下代码有什么问题？\nch := make(chan int)\nch <- 1\nprintln(<-ch)",
            "options": ["A) 死锁：无缓冲 channel 发送会阻塞", "B) 编译错误", "C) 正常运行输出 1", "D) 运行时 panic", "E) 我不清楚"],
            "answer": 0, "difficulty": "medium", "topic": "Go并发",
            "explanation": "无缓冲 channel 的发送操作会阻塞直到有接收者，主 goroutine 在 ch <- 1 处死锁。"
        },
        {
            "id": "go_q5",
            "question": "以下代码输出什么？\nvar i interface{} = 42\nv, ok := i.(string)\nfmt.Println(v, ok)",
            "options": ["A) 42 true", "B) \"\" false", "C) panic", "D) 编译错误", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "Go接口与错误",
            "explanation": "类型断言 i.(string) 失败，v 为 string 零值 \"\"，ok 为 false。"
        },
        {
            "id": "go_q6",
            "question": "goroutine 的初始栈大小大约是多少？",
            "options": ["A) 1MB", "B) 2KB", "C) 8KB", "D) 与操作系统线程相同", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "Go并发",
            "explanation": "goroutine 初始栈约 2KB（可动态扩容），远小于操作系统线程（通常 1MB+）。"
        },
        {
            "id": "go_q7",
            "question": "以下代码输出什么？\nfunc double(x int) (result int) {\n    defer func() { result *= 2 }()\n    return x\n}\nfmt.Println(double(5))",
            "options": ["A) 5", "B) 10", "C) 0", "D) 编译错误", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "Go defer",
            "explanation": "命名返回值 result，defer 在 return 之后修改 result，所以最终返回 10。"
        },
        {
            "id": "go_q8",
            "question": "Go 的错误处理惯例是？",
            "options": ["A) try-catch", "B) 返回 (result, error)，调用方检查 if err != nil", "C) throw 异常", "D) 全局错误码", "E) 我不清楚"],
            "answer": 1, "difficulty": "easy", "topic": "Go接口与错误",
            "explanation": "Go 惯例：函数返回 (T, error)，调用方检查 if err != nil。Go 没有 try-catch。"
        },
        {
            "id": "go_q9",
            "question": "Go 的接口实现方式是？",
            "options": ["A) 显式声明 implements", "B) 隐式实现（鸭子类型）", "C) 通过继承", "D) 通过宏", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "Go接口与错误",
            "explanation": "Go 接口隐式实现：只要类型实现了接口的所有方法，就自动实现了该接口，无需显式声明。"
        },
        {
            "id": "go_q10",
            "question": "以下关于 Go Modules 的说法正确的是？",
            "options": ["A) go.mod 文件记录依赖信息", "B) Go 使用 npm 管理依赖", "C) go.mod 是自动生成不可手动编辑", "D) Go 不支持模块化", "E) 我不清楚"],
            "answer": 0, "difficulty": "easy", "topic": "Go工程化",
            "explanation": "Go Modules 使用 go.mod 文件声明模块路径和依赖版本，go.sum 记录校验和。"
        },
    ],
    "python": [
        {
            "id": "py_assess_q1",
            "question": "Python 中，以下哪个不是合法的变量名？",
            "options": ["A) _name", "B) name_1", "C) 1name", "D) Name", "E) 我不清楚"],
            "answer": 2, "difficulty": "easy", "topic": "Python基础",
            "explanation": "Python 变量名不能以数字开头。_name、name_1、Name 都是合法变量名。"
        },
        {
            "id": "py_assess_q2",
            "question": "以下代码输出什么？\nprint(type([]) == list)",
            "options": ["A) False", "B) True", "C) list", "D) 报错", "E) 我不清楚"],
            "answer": 1, "difficulty": "easy", "topic": "Python基础",
            "explanation": "type([]) 返回 <class 'list'>，与 list 比较为 True。"
        },
        {
            "id": "py_assess_q3",
            "question": "以下哪个方法可以去除字符串首尾空格？",
            "options": ["A) str.ltrim()", "B) str.strip()", "C) str.trim()", "D) str.remove()", "E) 我不清楚"],
            "answer": 1, "difficulty": "easy", "topic": "字符串操作",
            "explanation": "strip() 去除首尾空白字符，lstrip() 去左侧，rstrip() 去右侧。Python 没有 trim() 方法。"
        },
        {
            "id": "py_assess_q4",
            "question": "以下代码输出什么？\nprint([1, 2, 3] + [4, 5])",
            "options": ["A) [1, 2, 3, [4, 5]]", "B) [1, 2, 3, 4, 5]", "C) [5, 7, 8]", "D) 报错", "E) 我不清楚"],
            "answer": 1, "difficulty": "easy", "topic": "列表操作",
            "explanation": "列表的 + 运算符将两个列表拼接为新列表。"
        },
        {
            "id": "py_assess_q5",
            "question": "以下关于 Python 元组 (tuple) 的说法正确的是？",
            "options": ["A) 元组可变", "B) 元组不可变，不可被修改", "C) 元组不支持索引", "D) 元组不能包含不同类型", "E) 我不清楚"],
            "answer": 1, "difficulty": "easy", "topic": "数据类型",
            "explanation": "tuple 是不可变序列，创建后不能修改元素。但元组内的可变对象（如列表）其内容可修改。"
        },
        {
            "id": "py_assess_q6",
            "question": "以下代码输出什么？\na = [1, 2, 3, 4, 5]\nprint(a[::2])",
            "options": ["A) [1, 2, 3, 4, 5]", "B) [1, 3, 5]", "C) [2, 4]", "D) [5, 4, 3, 2, 1]", "E) 我不清楚"],
            "answer": 1, "difficulty": "easy", "topic": "列表操作",
            "explanation": "切片 a[::2] 从头到尾步长为 2，取索引 0、2、4 即 [1, 3, 5]。"
        },
        {
            "id": "py_assess_q7",
            "question": "Python 中 lambda 表达式的作用是？",
            "options": ["A) 定义多行函数", "B) 创建匿名函数（单表达式函数）", "C) 创建类", "D) 导入模块", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "函数",
            "explanation": "lambda 创建匿名函数，只能包含单个表达式。常用于 sorted() 的 key 参数、map/filter 等。"
        },
        {
            "id": "py_assess_q8",
            "question": "以下代码输出什么？\nprint(set([1, 2, 2, 3, 3, 3]))",
            "options": ["A) [1, 2, 3]", "B) {1, 2, 3}", "C) [1, 2, 2, 3, 3, 3]", "D) 报错", "E) 我不清楚"],
            "answer": 1, "difficulty": "easy", "topic": "数据类型",
            "explanation": "set() 自动去重，返回 {1, 2, 3}。花括号表示 set 类型。"
        },
        {
            "id": "py_assess_q9",
            "question": "以下哪个操作会修改原列表？",
            "options": ["A) [1,2,3] + [4]", "B) [x*2 for x in [1,2,3]]", "C) lst.append(4)", "D) lst[1:3]", "E) 我不清楚"],
            "answer": 2, "difficulty": "medium", "topic": "列表操作",
            "explanation": "append() 原地修改列表。+ 和列表推导式、切片都返回新列表，不修改原列表。"
        },
        {
            "id": "py_assess_q10",
            "question": "以下代码输出什么？\nimport copy\na = [1, [2, 3]]\nb = copy.deepcopy(a)\nb[1][0] = 9\nprint(a[1][0])",
            "options": ["A) 9", "B) 2", "C) 3", "D) 报错", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "数据类型",
            "explanation": "deepcopy 创建完全独立的副本，嵌套列表也被复制。修改 b 不影响 a，a[1][0] 仍为 2。"
        },
    ],
    "typescript": [
        {
            "id": "ts_assess_q1",
            "question": "TypeScript 中 any 类型的含义是？",
            "options": ["A) 表示任意类型，关闭该变量的类型检查", "B) 表示字符串类型", "C) 表示对象类型", "D) 表示 null 类型", "E) 我不清楚"],
            "answer": 0, "difficulty": "easy", "topic": "TypeScript基础",
            "explanation": "any 类型绕过类型检查，该变量可赋任意值并调用任意方法，失去 TypeScript 的保护。应尽量使用 unknown 或具体类型。"
        },
        {
            "id": "ts_assess_q2",
            "question": "以下代码编译结果是什么？\nconst nums: number[] = [1, 2, 3];\nnums.push('hello');",
            "options": ["A) 正常运行，数组变为 [1,2,3,'hello']", "B) 运行时错误", "C) 编译错误：类型 'string' 不能赋给 'number'", "D) undefined", "E) 我不清楚"],
            "answer": 2, "difficulty": "easy", "topic": "TypeScript基础",
            "explanation": "number[] 类型约束数组元素必须为 number，push('hello') 传入 string 会导致 TypeScript 编译错误。"
        },
        {
            "id": "ts_assess_q3",
            "question": "以下关于 readonly 修饰符的说法正确的是？",
            "options": ["A) readonly 属性在运行时不可修改", "B) readonly 仅在编译时检查，防止属性被赋值", "C) readonly 与 const 完全相同", "D) readonly 只能用于数组", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "类型系统",
            "explanation": "readonly 是编译时约束，阻止对属性重新赋值。运行时 JavaScript 中仍可修改。const 用于变量，readonly 用于属性。"
        },
        {
            "id": "ts_assess_q4",
            "question": "以下泛型约束 `<T extends HasLength>` 的含义是？",
            "options": ["A) T 必须是 HasLength 的子类", "B) T 必须具有 HasLength 定义的属性/方法", "C) T 必须是 HasLength 的实例", "D) 以上都不对", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "泛型",
            "explanation": "extends 在泛型中是类型约束（type constraint），要求 T 满足 HasLength 的结构（结构化类型系统）。"
        },
        {
            "id": "ts_assess_q5",
            "question": "以下关于 as const 断言的说法正确的是？",
            "options": ["A) as const 将对象/数组的所有属性设为 readonly，类型收窄为字面量", "B) as const 将变量转换为常量", "C) as const 是运行时断言", "D) as const 只能在函数中使用", "E) 我不清楚"],
            "answer": 0, "difficulty": "medium", "topic": "类型系统",
            "explanation": "as const 将宽类型收窄为具体字面量类型：如 ['a','b'] 推为 readonly ['a','b'] 而非 string[]。"
        },
        {
            "id": "ts_assess_q6",
            "question": "never 类型的典型用途是？",
            "options": ["A) 表示永远不会发生的类型（如抛出异常/死循环函数返回类型、穷举检查）", "B) 等同于 void", "C) 等同于 any", "D) 表示可能为 null", "E) 我不清楚"],
            "answer": 0, "difficulty": "medium", "topic": "类型系统",
            "explanation": "never 表示永不存在的值类型。用于：①永无返回的函数（throw/死循环）；②switch 穷举检查确保处理所有 case。"
        },
        {
            "id": "ts_assess_q7",
            "question": "Pick<T, K> 工具类型的作用是？",
            "options": ["A) 从 T 中选择指定属性 K 构造新类型", "B) 从 T 中排除指定属性", "C) 将 T 的所有属性变为可选", "D) 将 T 的所有属性变为只读", "E) 我不清楚"],
            "answer": 0, "difficulty": "medium", "topic": "工具类型",
            "explanation": "Pick<User, 'id' | 'name'> 从 User 类型中仅选取 id 和 name 两属性。Omit 相反是排除。"
        },
        {
            "id": "ts_assess_q8",
            "question": "以下关于类型守卫（Type Guard）的说法正确的是？",
            "options": ["A) typeof 和 instanceof 是内置类型守卫，可缩小联合类型范围", "B) 类型守卫只能在 if 语句中使用", "C) 类型守卫是运行时检查，不影响 TypeScript 编译", "D) 自定义类型守卫使用 isGuard 关键字", "E) 我不清楚"],
            "answer": 0, "difficulty": "medium", "topic": "类型系统",
            "explanation": "typeof/instanceof/in 以及自定义 `arg is Type` 返回类型的函数都是类型守卫，帮助 TS 在分支中缩小类型。"
        },
        {
            "id": "ts_assess_q9",
            "question": "tsconfig.json 中 outDir 的作用是？",
            "options": ["A) 指定源文件目录", "B) 指定编译后的 JS 文件输出目录", "C) 指定第三方包目录", "D) 指定 TypeScript 安装路径", "E) 我不清楚"],
            "answer": 1, "difficulty": "easy", "topic": "工程配置",
            "explanation": "outDir 指定 tsc 编译产出 .js 文件的目录。rootDir 指定源文件根目录。"
        },
        {
            "id": "ts_assess_q10",
            "question": "以下代码输出什么？\ntype A = { x: number };\ntype B = { y: string };\ntype C = A & B;\n// C 类型的结构是？",
            "options": ["A) { x: number } | { y: string }（联合）", "B) { x: number; y: string }（交叉/合并）", "C) never", "D) 编译错误", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "类型系统",
            "explanation": "& 是交叉类型（Intersection），合并所有属性。C 类型同时具有 x 和 y。| 是联合类型。"
        },
    ],
    "rust": [
        {
            "id": "rust_assess_q1",
            "question": "Rust 中，以下哪个是创建可变变量的正确方式？",
            "options": ["A) let x = 5", "B) let mut x = 5", "C) var x = 5", "D) mut x = 5", "E) 我不清楚"],
            "answer": 1, "difficulty": "easy", "topic": "Rust基础",
            "explanation": "Rust 变量默认不可变，用 mut 关键字声明可变变量。let mut x = 5 创建可变变量 x。"
        },
        {
            "id": "rust_assess_q2",
            "question": "以下代码是否有问题？\nlet r;\n{\n    let x = 5;\n    r = &x;\n}\nprintln!(\"{}\", r);",
            "options": ["A) 正常运行输出 5", "B) 编译错误：x 的生命周期不够长", "C) 运行时错误", "D) 输出 0", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "生命周期",
            "explanation": "r 引用了 x，但 x 在内部块结束后被释放，r 成为悬垂引用。Rust 编译器会拒绝此代码。"
        },
        {
            "id": "rust_assess_q3",
            "question": "Rust 中 unwrap() 方法的作用是？",
            "options": ["A) 将 Option/Result 的包装打开，遇到 None/Err 时 panic", "B) 安全地获取值，不会 panic", "C) 仅用于 String 类型", "D) 将值转为字符串", "E) 我不清楚"],
            "answer": 0, "difficulty": "easy", "topic": "错误处理",
            "explanation": "unwrap() 提取 Some/Ok 中的值，若为 None/Err 则 panic。推荐用 ?、match 或 unwrap_or() 等安全替代。"
        },
        {
            "id": "rust_assess_q4",
            "question": "Rust 中 struct 和 enum 的区别是？",
            "options": ["A) 完全相同", "B) struct 是乘积类型（同时拥有多个字段），enum 是和类型（同一时刻只取一个变体）", "C) enum 不能包含数据", "D) struct 不能有方法", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "Rust基础",
            "explanation": "struct 组合多个字段（AND 关系）。enum 定义多个变体（OR 关系），每个变体可携带不同类型的数据。"
        },
        {
            "id": "rust_assess_q5",
            "question": "以下关于 Rust 模块系统的说法正确的是？",
            "options": ["A) Rust 没有模块系统", "B) mod 声明模块，use 引入路径，pub 控制可见性", "C) 每个文件只能有一个 mod", "D) use 和 import 是相同的", "E) 我不清楚"],
            "answer": 1, "difficulty": "easy", "topic": "模块系统",
            "explanation": "mod 定义模块，use 引入路径以简化使用，pub 使项对外可见（默认私有）。一个文件可包含多个 mod。"
        },
        {
            "id": "rust_assess_q6",
            "question": "Rust 中 clone() 和 Copy trait 的区别是？",
            "options": ["A) 完全相同", "B) Copy 是隐式的按位复制（编译器自动调用）；Clone 是显式的深拷贝，需要调用 .clone()", "C) Copy 适用于所有类型", "D) Clone 是自动的", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "所有权",
            "explanation": "Copy trait 的类型在赋值时自动按位复制而不移动所有权（如 i32、bool）。Clone 需显式调用 .clone() 做深拷贝。"
        },
        {
            "id": "rust_assess_q7",
            "question": "Rust 中 `use std::collections::HashMap` 的作用是？",
            "options": ["A) 创建一个 HashMap", "B) 将 HashMap 引入当前作用域，之后可直接使用 HashMap", "C) 导出 HashMap", "D) 删除 HashMap", "E) 我不清楚"],
            "answer": 1, "difficulty": "easy", "topic": "模块系统",
            "explanation": "use 语句将外部路径引入作用域，之后可直接用 HashMap 代替 std::collections::HashMap。类似 Python 的 from ... import。"
        },
        {
            "id": "rust_assess_q8",
            "question": "Rust 中 ? 运算符的作用是？",
            "options": ["A) 三元运算符（条件表达式）", "B) 传播错误：遇到 Err 则提前返回 Err，否则提取 Ok 中的值", "C) 表示可选参数", "D) 等同于 unwrap()", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "错误处理",
            "explanation": "? 是错误传播语法糖：作用于 Result 时，Ok 提取值继续，Err 提前返回。作用于 Option 时类似。"
        },
        {
            "id": "rust_assess_q9",
            "question": "Rust 中线程间共享数据的安全方式是？",
            "options": ["A) 直接共享可变引用", "B) Arc<Mutex<T>>（原子引用计数 + 互斥锁）", "C) 全局变量", "D) 不需要安全方式", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "并发",
            "explanation": "Arc<Mutex<T>> 允许多线程安全共享数据：Arc 多线程引用计数，Mutex 内部可变性确保互斥访问。"
        },
        {
            "id": "rust_assess_q10",
            "question": "Rust 的 cargo build --release 与 cargo build 的区别是？",
            "options": ["A) 完全相同", "B) --release 启用编译器优化，生成运行更快的二进制（编译时间更长）", "C) --release 只用于测试", "D) --release 跳过编译直接运行", "E) 我不清楚"],
            "answer": 1, "difficulty": "easy", "topic": "工程化",
            "explanation": "cargo build --release 启用优化（-O），产物在 target/release/ 目录，体积更小运行更快。debug 模式（默认）包含调试信息不优化。"
        },
    ],
    "sql": [
        {
            "id": "sql_assess_q1",
            "question": "SQL 中 SELECT DISTINCT 的作用是？",
            "options": ["A) 选择所有列", "B) 去除结果集中的重复行", "C) 按某列排序", "D) 选择指定的表", "E) 我不清楚"],
            "answer": 1, "difficulty": "easy", "topic": "基础查询",
            "explanation": "DISTINCT 关键字去重，返回唯一值。例如 SELECT DISTINCT city FROM users 返回不重复的城市。"
        },
        {
            "id": "sql_assess_q2",
            "question": "ORDER BY 默认的排序方式是？",
            "options": ["A) 降序 DESC", "B) 升序 ASC", "C) 随机", "D) 按主键", "E) 我不清楚"],
            "answer": 1, "difficulty": "easy", "topic": "基础查询",
            "explanation": "ORDER BY 默认升序 ASC。ORDER BY salary DESC 显式指定降序。"
        },
        {
            "id": "sql_assess_q3",
            "question": "SQL 中 LIMIT 10 OFFSET 20 的含义是？",
            "options": ["A) 跳过前10行取20行", "B) 跳过前20行取10行", "C) 取前10行", "D) 取20到30行", "E) 我不清楚"],
            "answer": 1, "difficulty": "easy", "topic": "基础查询",
            "explanation": "OFFSET 20 跳过前20行，LIMIT 10 取10行。拿到的行是第21到30行。常用于分页。"
        },
        {
            "id": "sql_assess_q4",
            "question": "以下哪个是 SQL 中主键（PRIMARY KEY）的特性？",
            "options": ["A) 可以为 NULL", "B) 唯一且不为 NULL", "C) 允许重复值", "D) 自动递增", "E) 我不清楚"],
            "answer": 1, "difficulty": "easy", "topic": "约束",
            "explanation": "主键必须满足 UNIQUE + NOT NULL。一张表只能有一个主键，但主键可由多列组成（复合主键）。"
        },
        {
            "id": "sql_assess_q5",
            "question": "以下 SQL 查询输出什么？\nSELECT * FROM A\nLEFT JOIN B ON A.id = B.a_id\nWHERE B.a_id IS NULL;",
            "options": ["A) A 和 B 的交集", "B) A 中有但 B 中没有匹配的记录", "C) A 和 B 的全部记录", "D) B 中所有记录", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "JOIN",
            "explanation": "LEFT JOIN ... WHERE B.a_id IS NULL 找出 A 中存在但 B 中无匹配的行，即求差集。"
        },
        {
            "id": "sql_assess_q6",
            "question": "以下哪个 SQL 语句用于给表添加一列？",
            "options": ["A) ADD COLUMN email VARCHAR(100) TO users", "B) ALTER TABLE users ADD COLUMN email VARCHAR(100)", "C) INSERT COLUMN INTO users", "D) MODIFY TABLE users ADD email", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "DDL",
            "explanation": "ALTER TABLE 用于修改表结构，ADD COLUMN 添加列，DROP COLUMN 删除列，MODIFY COLUMN 修改列定义。"
        },
        {
            "id": "sql_assess_q7",
            "question": "外键（FOREIGN KEY）的作用是？",
            "options": ["A) 加速查询", "B) 维护引用完整性，确保子表值在主表中存在", "C) 自动生成 ID", "D) 创建索引", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "约束",
            "explanation": "外键约束确保子表中的外键列的值必须在主表的主键列中存在（或为 NULL）。维护数据引用完整性。"
        },
        {
            "id": "sql_assess_q8",
            "question": "以下关于 UNION 和 UNION ALL 的说法正确的是？",
            "options": ["A) 完全相同", "B) UNION 去重（自动 DISTINCT），UNION ALL 不去重", "C) UNION ALL 去重", "D) UNION 比 UNION ALL 快", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "基础查询",
            "explanation": "UNION 合并结果并去除重复行。UNION ALL 保留所有行（包括重复），性能更好。如果确定无重复应优先用 UNION ALL。"
        },
        {
            "id": "sql_assess_q9",
            "question": "SQL 中 `WHERE EXISTS (subquery)` 的作用是？",
            "options": ["A) 检查子查询是否返回至少一行", "B) 检查子查询是否返回 NULL", "C) 等同于 WHERE ... IN (...)", "D) 删除子查询结果", "E) 我不清楚"],
            "answer": 0, "difficulty": "medium", "topic": "子查询",
            "explanation": "EXISTS 检查子查询是否返回至少一行记录。返回 true/false，通常比 IN 效率更高（找到第一行即停止）。"
        },
        {
            "id": "sql_assess_q10",
            "question": "数据库范式化（Normalization）的主要目的是？",
            "options": ["A) 提高查询速度", "B) 减少数据冗余和更新异常", "C) 增加数据冗余", "D) 使表结构更复杂", "E) 我不清楚"],
            "answer": 1, "difficulty": "medium", "topic": "数据库设计",
            "explanation": "范式化通过分解表来消除数据冗余、避免插入/更新/删除异常。实践中常在 3NF 和适度反范式化之间平衡。"
        },
    ],

}