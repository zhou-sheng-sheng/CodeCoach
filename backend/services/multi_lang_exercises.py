"""多语言习题库 — Java / JavaScript / C++ / Go"""

from typing import Any

# ===== Java 习题库 (10道) =====
JAVA_EXERCISES: list[dict[str, Any]] = [
    {
        "id": "java_q1",
        "question": "Java 中，以下哪个是基本数据类型？",
        "options": ["A) String", "B) Integer", "C) int", "D) ArrayList", "E) 我不清楚"],
        "answer": 2, "difficulty": "easy", "topic": "Java基础",
        "explanation": "int 是 Java 的 8 种基本类型之一。String 和 Integer 是引用类型（类），ArrayList 是集合类。"
    },
    {
        "id": "java_q2",
        "question": "以下代码输出什么？\nString s1 = new String(\"hello\");\nString s2 = new String(\"hello\");\nSystem.out.println(s1 == s2);",
        "options": ["A) true", "B) false", "C) 编译错误", "D) 运行时错误", "E) 我不清楚"],
        "answer": 1, "difficulty": "easy", "topic": "Java基础",
        "explanation": "== 比较引用地址，new 创建了两个不同对象，所以 s1 == s2 为 false。比较内容应用 s1.equals(s2)。"
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
        "explanation": "子类构造方法隐式或显式调用父类构造方法（super()），确保父类先初始化。Java 不支持多继承，final 类不可被继承。"
    },
    {
        "id": "java_q7",
        "question": "以下代码输出什么？\ntry {\n    int[] arr = {1, 2};\n    System.out.println(arr[2]);\n} catch (ArrayIndexOutOfBoundsException e) {\n    System.out.println(\"Error\");\n} finally {\n    System.out.println(\"Done\");\n}",
        "options": ["A) Error", "B) Done", "C) Error Done", "D) 编译错误", "E) 我不清楚"],
        "answer": 2, "difficulty": "easy", "topic": "Java异常",
        "explanation": "arr[2] 越界触发异常，被 catch 捕获打印 Error，finally 块始终执行打印 Done。"
    },
    {
        "id": "java_q8",
        "question": "以下哪个方法可以正确启动一个新线程？",
        "options": ["A) new Thread().run()", "B) new Thread(myTask).start()", "C) myTask.run()", "D) Thread.start(myTask)", "E) 我不清楚"],
        "answer": 1, "difficulty": "medium", "topic": "Java并发",
        "explanation": "必须调用 start() 才会启动新线程；直接调用 run() 只会在当前线程执行。"
    },
    {
        "id": "java_q9",
        "question": "以下关于 synchronized 的说法正确的是？",
        "options": ["A) synchronized 方法锁的是 Class 对象", "B) synchronized 代码块可以指定锁对象", "C) synchronized 只保证可见性", "D) synchronized 对性能无影响", "E) 我不清楚"],
        "answer": 1, "difficulty": "medium", "topic": "Java并发",
        "explanation": "synchronized 代码块可以指定任意对象作为锁。synchronized 方法中，静态方法锁 Class，实例方法锁 this。"
    },
    {
        "id": "java_q10",
        "question": "以下关于 Spring Boot 的说法正确的是？",
        "options": ["A) @RestController 返回视图名称", "B) @Autowired 是 JDK 内置注解", "C) Spring Boot 内嵌了 Tomcat 服务器", "D) application.yml 不能替代 application.properties", "E) 我不清楚"],
        "answer": 2, "difficulty": "medium", "topic": "Spring Boot",
        "explanation": "Spring Boot 内嵌 Tomcat（也可换 Jetty），无需外部部署。@RestController 返回 JSON（@ResponseBody）。"
    },
    {
        "id": "java_q11",
        "question": "以下关于 Lambda 的说法正确的是？\nList<Integer> list = Arrays.asList(1,2,3);\nlist.stream().filter(x -> x > 1).forEach(System.out::println);",
        "options": ['A) 编译错误，filter 不支持 Lambda', 'B) 输出 2 换行 3', 'C) 输出 1 2 3', 'D) 输出 [2, 3]', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "Java Lambda",
        "explanation": "Stream.filter 接受 Predicate Lambda（x -> x > 1），过滤掉 1 后 forEach 输出 2 和 3（分两行）。",
    },
    {
        "id": "java_q12",
        "question": "以下代码中，方法引用的等价 Lambda 是？\nlist.forEach(System.out::println);",
        "options": ['A) list.forEach(x -> System.out.println(x))', 'B) list.forEach(x -> x.println())', 'C) list.forEach(System.out)', 'D) list.forEach(x -> println(x))', 'E) 我不清楚'],
        "answer": 0,
        "difficulty": "easy",
        "topic": "Java Lambda",
        "explanation": "System.out::println 是实例方法引用，等价于 x -> System.out.println(x)。",
    },
    {
        "id": "java_q13",
        "question": "以下关于泛型的说法正确的是？",
        "options": ['A) 泛型在运行时保留完整类型信息', 'B) ? extends T 表示可以写入任意 T 的子类型', 'C) ? super T 适用于消费者（写入），? extends T 适用于生产者（读取）', 'D) 泛型只能用于集合', 'E) 我不清楚'],
        "answer": 2,
        "difficulty": "medium",
        "topic": "Java泛型",
        "explanation": "PECS 原则：Producer Extends（读取），Consumer Super（写入）。extends 上界只读，super 下界可写。",
    },
    {
        "id": "java_q14",
        "question": "以下代码为何编译错误？\nList<String> list = new ArrayList<>();\nlist.add(\"hello\");\nString s = (String) list.get(0);  // OK\nList<Object> objList = list;  // 编译错误",
        "options": ['A) List<String> 不是 List<Object> 的子类型（泛型不变）', 'B) ArrayList 不能赋值给 List', 'C) String 不能强转 Object', 'D) 泛型不支持 add 方法', 'E) 我不清楚'],
        "answer": 0,
        "difficulty": "medium",
        "topic": "Java泛型",
        "explanation": "Java 泛型是不变的（invariant）：List<String> 不是 List<Object> 的子类型。若需要协变，用 List<? extends Object>。",
    },
    {
        "id": "java_q15",
        "question": "以下代码的正确用途是？\ntry (BufferedReader br = new BufferedReader(new FileReader(\"test.txt\"))) {\n    String line;\n    while ((line = br.readLine()) != null) {\n        System.out.println(line);\n    }\n}",
        "options": ['A) 写入文件', 'B) 逐行读取文件并自动关闭资源', 'C) 复制文件', 'D) 编译错误', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "easy",
        "topic": "Java IO",
        "explanation": "try-with-resources（Java 7+）自动关闭 AutoCloseable 资源。BufferedReader.readLine() 逐行读取文本文件。",
    },
    {
        "id": "java_q16",
        "question": "字节流和字符流的关键区别是？",
        "options": ['A) 没有区别，只是命名不同', 'B) 字节流 InputStream/OutputStream 处理二进制，字符流 Reader/Writer 处理文本并自动处理编码', 'C) 字节流比字符流更快', 'D) 字符流不支持文件操作', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "easy",
        "topic": "Java IO",
        "explanation": "字节流以 byte 为单位处理二进制数据；字符流以 char 为单位，内置编码转换（如 UTF-8），适合文本。",
    },
    {
        "id": "java_q17",
        "question": "@Override 注解的作用是？",
        "options": ['A) 编译器检查该方法是否正确重写了父类/接口方法', 'B) 强制子类必须重写该方法', 'C) 运行时代替父类方法', 'D) 没有实际作用，仅文档用途', 'E) 我不清楚'],
        "answer": 0,
        "difficulty": "easy",
        "topic": "Java注解",
        "explanation": "@Override 让编译器验证方法签名是否确实覆盖了父类/接口方法。若签名不匹配会报编译错误，防止意外重载。",
    },
    {
        "id": "java_q18",
        "question": "以下自定义注解的正确定义是？",
        "options": ['A) annotation MyAnno { String value(); }', 'B) @interface MyAnno { String value() default ""; }', 'C) @annotation MyAnno { String value; }', 'D) interface @MyAnno { String value(); }', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "Java注解",
        "explanation": "自定义注解使用 @interface 关键字定义，成员以无参方法声明，可用 default 设定默认值。",
    },

]

# ===== JavaScript 习题库 (8道) =====
JS_EXERCISES: list[dict[str, Any]] = [
    {
        "id": "js_q1",
        "question": "以下代码输出什么？\nconsole.log(typeof null);",
        "options": ["A) \"null\"", "B) \"undefined\"", "C) \"object\"", "D) \"number\"", "E) 我不清楚"],
        "answer": 2, "difficulty": "easy", "topic": "JS基础",
        "explanation": "typeof null 返回 \"object\" 是 JavaScript 的历史 Bug，实际上 null 是原始类型。"
    },
    {
        "id": "js_q2",
        "question": "以下代码输出什么？\nvar a = 1;\nfunction foo() {\n    console.log(a);\n    var a = 2;\n}\nfoo();",
        "options": ["A) 1", "B) 2", "C) undefined", "D) ReferenceError", "E) 我不清楚"],
        "answer": 2, "difficulty": "medium", "topic": "JS基础",
        "explanation": "var 有变量提升（hoisting），函数内 var a 被提升到函数顶部但值为 undefined，所以输出 undefined。"
    },
    {
        "id": "js_q3",
        "question": "以下代码输出什么？\nconsole.log(0.1 + 0.2 === 0.3);",
        "options": ["A) true", "B) false", "C) undefined", "D) 报错", "E) 我不清楚"],
        "answer": 1, "difficulty": "medium", "topic": "JS基础",
        "explanation": "浮点数精度问题：0.1 + 0.2 = 0.30000000000000004，所以 === 比较返回 false。"
    },
    {
        "id": "js_q4",
        "question": "以下代码输出什么？\nconst p = new Promise((resolve) => {\n    resolve(1);\n});\np.then(v => console.log(v));\nconsole.log(2);",
        "options": ["A) 1 2", "B) 2 1", "C) 1", "D) 2", "E) 我不清楚"],
        "answer": 1, "difficulty": "medium", "topic": "JS异步",
        "explanation": "Promise.then 是微任务，在主线程同步代码执行完后才执行，所以先输出 2，再输出 1。"
    },
    {
        "id": "js_q5",
        "question": "以下代码输出什么？\nasync function foo() {\n    return 1;\n}\nconsole.log(foo() instanceof Promise);",
        "options": ["A) true", "B) false", "C) undefined", "D) 报错", "E) 我不清楚"],
        "answer": 0, "difficulty": "medium", "topic": "JS异步",
        "explanation": "async 函数总是返回 Promise，return 1 等价于 return Promise.resolve(1)。"
    },
    {
        "id": "js_q6",
        "question": "以下代码输出什么？\nfunction foo() {\n    console.log(this.a);\n}\nconst obj = { a: 1, foo };\nconst a = 2;\nobj.foo();",
        "options": ["A) 1", "B) 2", "C) undefined", "D) 报错", "E) 我不清楚"],
        "answer": 0, "difficulty": "medium", "topic": "JS原型与this",
        "explanation": "obj.foo() 调用时 this 指向 obj，所以 this.a = obj.a = 1。"
    },
    {
        "id": "js_q7",
        "question": "以下代码输出什么？\nconst arr = [1, 2, 3];\nconst result = arr.map(x => x * 2).filter(x => x > 3);\nconsole.log(result);",
        "options": ["A) [4, 6]", "B) [2, 4, 6]", "C) [4]", "D) 报错", "E) 我不清楚"],
        "answer": 0, "difficulty": "easy", "topic": "JS基础",
        "explanation": "map 将每个元素乘2得 [2,4,6]，filter 筛选 >3 得 [4,6]。"
    },
    {
        "id": "js_q8",
        "question": "以下关于 ES6 import/export 的说法正确的是？",
        "options": ["A) import 是 CommonJS 规范的一部分", "B) export default 只能用于函数", "C) import 支持 Tree Shaking 优化", "D) Node.js 不支持 import", "E) 我不清楚"],
        "answer": 2, "difficulty": "medium", "topic": "JS模块",
        "explanation": "ESM 的 import/export 是静态声明，打包工具可进行 Tree Shaking（移除未引用代码）。Node.js 12+ 通过 .mjs 或 type:module 支持。"
    },
    {
        "id": "js_q9",
        "question": "以下代码输出什么？\nfunction createCounter() {\n    let count = 0;\n    return function() { return ++count; };\n}\nconst c1 = createCounter();\nconst c2 = createCounter();\nconsole.log(c1(), c1(), c2());",
        "options": ['A) 1 2 1', 'B) 1 2 3', 'C) 1 1 1', 'D) 0 1 1', 'E) 我不清楚'],
        "answer": 0,
        "difficulty": "medium",
        "topic": "JS闭包",
        "explanation": "每次调用 createCounter() 创建独立闭包。c1 闭包内 count 从 0→1→2，c2 有独立的 count 从 0→1。",
    },
    {
        "id": "js_q10",
        "question": "以下代码输出什么？\nfor (var i = 0; i < 3; i++) {\n    setTimeout(() => console.log(i), 0);\n}",
        "options": ['A) 0 1 2', 'B) 3 3 3', 'C) 0 0 0', 'D) undefined undefined undefined', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "JS闭包",
        "explanation": "var 没有块级作用域，循环后 i=3。setTimeout 回调执行时访问的是同一个 i（值为 3），输出 3 3 3。用 let 可修复。",
    },
    {
        "id": "js_q11",
        "question": "以下 DOM 操作中，哪个能正确获取 id=\"app\" 的元素？",
        "options": ["A) document.querySelector('#app')", "B) document.getElementById('app')", 'C) A 和 B 都可以', "D) document.getElement('#app')", 'E) 我不清楚'],
        "answer": 2,
        "difficulty": "easy",
        "topic": "JS DOM",
        "explanation": "getElementById 通过 id 获取单个元素，querySelector 支持 CSS 选择器（#app 即按 id 选择），两者都可。",
    },
    {
        "id": "js_q12",
        "question": "事件委托（Event Delegation）的优势是？",
        "options": ['A) 只能减少内存使用', 'B) 动态添加的子元素也能响应事件，且只需父级一个监听器', 'C) 比直接绑定更快', 'D) 不需要 event 对象', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "JS DOM",
        "explanation": "事件委托利用事件冒泡，父元素监听事件，通过 event.target 判断目标子元素。优势：减少监听器数量，动态元素无需重新绑定。",
    },
    {
        "id": "js_q13",
        "question": "以下代码输出什么？\nconsole.log(1);\nsetTimeout(() => console.log(2), 0);\nPromise.resolve().then(() => console.log(3));\nconsole.log(4);",
        "options": ['A) 1 4 3 2', 'B) 1 4 2 3', 'C) 1 2 3 4', 'D) 1 3 2 4', 'E) 我不清楚'],
        "answer": 0,
        "difficulty": "medium",
        "topic": "JS事件循环",
        "explanation": "同步代码先执行（1,4），然后清空微任务（Promise.then 输出 3），最后宏任务（setTimeout 输出 2）。",
    },
    {
        "id": "js_q14",
        "question": "以下代码输出什么？\nasync function foo() { console.log(2); }\nconsole.log(1);\nfoo();\nconsole.log(3);",
        "options": ['A) 1 2 3', 'B) 1 3 2', 'C) 2 1 3', 'D) 3 1 2', 'E) 我不清楚'],
        "answer": 0,
        "difficulty": "easy",
        "topic": "JS事件循环",
        "explanation": "async 函数在第一个 await 之前是同步执行的。foo() 没有 await，所以同步输出 1 2 3。",
    },
    {
        "id": "js_q15",
        "question": "以下代码输出什么？\nwindow.onerror = () => console.log('caught');\nsetTimeout(() => { throw new Error('async'); }, 0);",
        "options": ['A) caught', 'B) Uncaught Error（未被捕获）', 'C) undefined', 'D) null', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "JS错误处理",
        "explanation": "window.onerror 只能捕获同步执行中抛出的错误。异步回调（setTimeout）中的错误不会被 onerror 捕获，需在回调内部 try-catch。",
    },
    {
        "id": "js_q16",
        "question": "以下代码输出什么？\nPromise.reject('error')\n    .catch(e => { console.log(e); return 'recovered'; })\n    .then(v => console.log(v));",
        "options": ['A) error', 'B) error 换行 recovered', 'C) recovered', 'D) UnhandledPromiseRejection', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "JS错误处理",
        "explanation": ".catch 捕获 reject 并返回 'recovered'，后续 .then 收到恢复后的值输出 'recovered'。",
    },
    {
        "id": "js_q17",
        "question": "localStorage 和 sessionStorage 的关键区别是？",
        "options": ['A) localStorage 只能存字符串', 'B) sessionStorage 在标签页关闭后清除，localStorage 持久化', 'C) sessionStorage 容量更大', 'D) localStorage 会随 HTTP 请求发送到服务器', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "easy",
        "topic": "JS存储",
        "explanation": "localStorage 数据持久化直到手动清除；sessionStorage 仅在当前会话（标签页）有效，关闭后清除。两者都只存字符串，不随请求发送。",
    },
    {
        "id": "js_q18",
        "question": "以下哪个方案适合存储大量结构化数据？",
        "options": ['A) Cookie', 'B) localStorage', 'C) IndexedDB', 'D) sessionStorage', 'E) 我不清楚'],
        "answer": 2,
        "difficulty": "medium",
        "topic": "JS存储",
        "explanation": "IndexedDB 是客户端 NoSQL 数据库，支持索引、事务、大容量存储。Cookie 4KB，localStorage 5-10MB 且只存字符串。",
    },
    {
        "id": "js_q19",
        "question": "以下代码使用了哪种设计模式？\nconst singleton = (function() {\n    let instance;\n    function create() { return { name: 'singleton' }; }\n    return { getInstance() { if (!instance) instance = create(); return instance; } };\n})();",
        "options": ['A) 工厂模式', 'B) 单例模式（Singleton）', 'C) 观察者模式', 'D) 策略模式', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "JS设计模式",
        "explanation": "IIFE 闭包隐藏 instance，getInstance 保证只有一个实例——这是单例模式的典型实现。",
    },
    {
        "id": "js_q20",
        "question": "观察者模式（Observer/Pub-Sub）的核心思想是？",
        "options": ['A) 所有对象直接互相调用', 'B) 主题维护订阅者列表，状态变化时通知所有订阅者', 'C) 只有一个实例', 'D) 用工厂创建对象', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "easy",
        "topic": "JS设计模式",
        "explanation": "观察者模式：Subject 持有 Observer 列表，状态变化时调用 observer.update()。JS 中 addEventListener、EventEmitter 都是此模式。",
    },

]

# ===== C++ 习题库 (8道) =====
CPP_EXERCISES: list[dict[str, Any]] = [
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
        "question": "以下关于 unique_ptr 的说法正确的是？",
        "options": ["A) unique_ptr 可以被拷贝", "B) unique_ptr 可以被多个指针共享", "C) unique_ptr 独占所有权，不可拷贝只能移动", "D) unique_ptr 不需要手动 delete", "E) 我不清楚"],
        "answer": 2, "difficulty": "medium", "topic": "C++内存管理",
        "explanation": "unique_ptr 独占资源所有权，不可拷贝（删除拷贝构造），只能通过 std::move 转移所有权。"
    },
    {
        "id": "cpp_q5",
        "question": "以下代码有什么问题？\nBase *p = new Derived();\ndelete p;  // Base 析构函数非 virtual",
        "options": ["A) 内存泄漏", "B) 只调用 Base 析构，Derived 析构不被调用", "C) 编译错误", "D) 正常运行", "E) 我不清楚"],
        "answer": 1, "difficulty": "medium", "topic": "C++多态",
        "explanation": "基类析构函数非 virtual 时，delete 基类指针只调用基类析构，Derived 部分不被析构，导致资源泄漏。"
    },
    {
        "id": "cpp_q6",
        "question": "以下关于 const 的说法正确的是？",
        "options": ["A) const int* p 表示指针本身不可改", "B) int* const p 表示指向的值不可改", "C) const 成员函数不能修改成员变量", "D) constexpr 是运行时常量", "E) 我不清楚"],
        "answer": 2, "difficulty": "medium", "topic": "C++基础",
        "explanation": "const int* p（底层 const）指向的值不可改；int* const p（顶层 const）指针不可改；constexpr 是编译期常量。"
    },
    {
        "id": "cpp_q7",
        "question": "以下关于 RAII 的说法正确的是？",
        "options": ["A) RAII 是 C++ 的垃圾回收机制", "B) RAII 利用对象生命周期自动管理资源", "C) RAII 仅适用于内存管理", "D) RAII 会降低程序性能", "E) 我不清楚"],
        "answer": 1, "difficulty": "medium", "topic": "C++内存管理",
        "explanation": "RAII（资源获取即初始化）：将资源生命周期绑定到对象生命周期，构造时获取、析构时释放。适用于内存、文件、锁等。"
    },
    {
        "id": "cpp_q8",
        "question": "以下关于 Lambda 的说法正确的是？\nauto f = [](int a, int b) { return a + b; };",
        "options": ["A) 正确，返回类型自动推导", "B) 错误，必须显式指定返回类型", "C) 错误，Lambda 不能赋值给 auto", "D) 错误，Lambda 不能有参数", "E) 我不清楚"],
        "answer": 0, "difficulty": "easy", "topic": "Lambda",
        "explanation": "Lambda 表达式返回值类型可自动推导（只有一条 return 语句时），可赋值给 auto。"
    },
    {
        "id": "cpp_q9",
        "question": "以下代码输出什么？\ntemplate<typename T>\nT max(T a, T b) { return a > b ? a : b; }\ncout << max(3, 5) << ' ' << max(2.5, 1.8);",
        "options": ['A) 5 2.5', 'B) 5 2', 'C) 5 1.8', 'D) 编译错误', 'E) 我不清楚'],
        "answer": 0,
        "difficulty": "easy",
        "topic": "C++模板",
        "explanation": "编译器根据实参自动推导模板参数 T（int 和 double），分别实例化两个 max 函数。输出 5 和 2.5。",
    },
    {
        "id": "cpp_q10",
        "question": "模板特化（Template Specialization）的作用是？",
        "options": ['A) 让模板运行更快', 'B) 为特定类型提供不同于通用模板的实现', 'C) 限制模板只能用于某些类型', 'D) 自动推导模板参数', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "C++模板",
        "explanation": "模板特化（template<> 全特化/偏特化）为特定类型提供定制实现，如对 bool 类型的 vector 做位压缩优化。",
    },
    {
        "id": "cpp_q11",
        "question": "std::mutex 配合 lock_guard 的好处是？",
        "options": ['A) 性能更高', 'B) RAII 自动释放锁，防止忘记 unlock 导致死锁', 'C) 支持递归锁', 'D) 可跨进程同步', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "C++并发",
        "explanation": "lock_guard 在构造时 lock，析构时 unlock。利用 RAII 确保异常安全，不会因忘记 unlock 而死锁。",
    },
    {
        "id": "cpp_q12",
        "question": "std::atomic 的主要优势是？",
        "options": ['A) 无需加锁即可实现线程安全的读-改-写操作', 'B) 比 std::mutex 总是更慢', 'C) 只能用于整数类型', 'D) 自动管理线程生命周期', 'E) 我不清楚'],
        "answer": 0,
        "difficulty": "medium",
        "topic": "C++并发",
        "explanation": "std::atomic 通过 CPU 原子指令（如 CAS）实现无锁线程安全操作，避免 mutex 的开销和竞争。适用于简单共享变量。",
    },
    {
        "id": "cpp_q13",
        "question": "std::move() 的作用是？",
        "options": ['A) 移动对象在内存中的位置', 'B) 将左值强制转换为右值引用，触发移动语义', 'C) 删除对象', 'D) 复制对象', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "C++Move",
        "explanation": "std::move 本质是 static_cast<T&&>，将左值转为右值引用。本身不移动任何东西，只是让编译器选择移动构造/赋值而非拷贝。",
    },
    {
        "id": "cpp_q14",
        "question": "以下代码中 std::move 后 v1 的状态是？\nstd::vector<int> v1 = {1,2,3};\nstd::vector<int> v2 = std::move(v1);",
        "options": ['A) v1 仍然是 {1,2,3}', 'B) v1 为空但处于有效但未定义状态（通常为空）', 'C) 编译错误', 'D) v1 和 v2 共享相同数据', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "C++Move",
        "explanation": "移动后，v2 接管 v1 的内部指针，v1 变为空（标准库保证移动后处于有效但未指定状态，可安全赋新值或析构）。",
    },
    {
        "id": "cpp_q15",
        "question": "以下代码输出什么？\nvoid foo() noexcept { throw 1; }\ntry {\n    foo();\n} catch (...) {\n    cout << \"caught\";\n}",
        "options": ['A) caught', 'B) std::terminate() 被调用', 'C) 编译错误', 'D) 正常运行不抛异常', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "C++异常",
        "explanation": "noexcept 函数中抛出异常会直接调用 std::terminate() 终止程序，不会展开栈，不会被 catch 捕获。",
    },
    {
        "id": "cpp_q16",
        "question": "以下代码是否有问题？\nstruct A { ~A() noexcept(false) { throw 1; } };\nvoid f() { A a; throw 2; }",
        "options": ['A) 没问题', 'B) 双重异常导致 std::terminate()——析构函数在栈展开时抛异常', 'C) 只捕获到 1', 'D) 只捕获到 2', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "hard",
        "topic": "C++异常",
        "explanation": "栈展开时先抛 2，然后销毁局部对象 a。A 的析构又抛 1，导致两个未处理异常并存，触发 std::terminate()。析构函数不应抛出异常。",
    },
    {
        "id": "cpp_q17",
        "question": "以下 Lambda 捕获方式中，哪个使得 Lambda 内部可以修改捕获的变量？\nint x = 10;\nauto f = [?]() { x = 20; };",
        "options": ['A) [x]', 'B) [&x]', 'C) [=]', 'D) 无法通过捕获让 Lambda 修改外部变量', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "easy",
        "topic": "C++Lambda",
        "explanation": "[&x] 引用捕获，Lambda 内修改 x 会直接修改外部变量。[=] 值捕获默认不可修改，加 mutable 后可在副本上修改。",
    },
    {
        "id": "cpp_q18",
        "question": "以下泛型 Lambda 的正确写法是？",
        "options": ['A) auto f = [](auto a, auto b) { return a + b; };', 'B) auto f = [](T a, T b) { return a + b; };', 'C) auto f<T> = [](T a, T b) { return a + b; };', 'D) C++11 不支持泛型 Lambda', 'E) 我不清楚'],
        "answer": 0,
        "difficulty": "easy",
        "topic": "C++Lambda",
        "explanation": "C++14 起支持泛型 Lambda：参数类型用 auto，编译器生成模板化的 operator()。C++11 不支持。",
    },
    {
        "id": "cpp_q19",
        "question": "以下代码使用了哪种惯用法？\nclass MyClass {\n    struct Impl;  // forward declare\n    std::unique_ptr<Impl> pImpl;\npublic:\n    MyClass();\n    ~MyClass();\n    void doSomething();\n};",
        "options": ['A) Singleton', 'B) PIMPL（Pointer to Implementation）', 'C) Factory Method', 'D) Observer', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "C++设计模式",
        "explanation": "PIMPL 将实现细节隐藏在 .cpp 文件中，减少头文件依赖，缩短编译时间，保持 ABI 兼容性。",
    },
    {
        "id": "cpp_q20",
        "question": "CRTP（Curiously Recurring Template Pattern）的主要用途是？",
        "options": ['A) 运行时多态', 'B) 编译时多态（静态分发），避免虚函数开销', 'C) 创建线程安全单例', 'D) 工厂模式', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "C++设计模式",
        "explanation": "CRTP：template<class Derived> class Base; class Derived : public Base<Derived>。基类通过 static_cast<Derived*>(this) 在编译时调用子类方法，零开销多态。",
    },

]

# ===== Go 习题库 (8道) =====
GO_EXERCISES: list[dict[str, Any]] = [
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
        "explanation": "访问 map 不存在的 key 时，ok 为 false，v 为值类型的零值（int 的零值是 0）。"
    },
    {
        "id": "go_q3",
        "question": "以下代码输出什么？\ndefer fmt.Println(\"first\")\ndefer fmt.Println(\"second\")\nfmt.Println(\"main\")",
        "options": ["A) first second main", "B) main first second", "C) main second first", "D) 编译错误", "E) 我不清楚"],
        "answer": 2, "difficulty": "easy", "topic": "Go defer",
        "explanation": "defer 按 LIFO（后进先出）顺序执行，所以先输出 main，再 second，最后 first。"
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
        "question": "以下关于 goroutine 的说法正确的是？",
        "options": ["A) goroutine 是操作系统线程", "B) goroutine 由 Go 运行时调度，栈初始约 2KB", "C) goroutine 间共享内存不需同步", "D) go func() 会阻塞等待执行完成", "E) 我不清楚"],
        "answer": 1, "difficulty": "medium", "topic": "Go并发",
        "explanation": "goroutine 是轻量级用户态线程，由 Go runtime 调度，初始栈约 2KB（可动态扩容）。"
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
        "question": "以下关于 Go error 处理的说法正确的是？",
        "options": ["A) Go 使用 try-catch 处理异常", "B) 函数返回 (result, error)，调用方必须检查 error", "C) panic 可以完全替代 error", "D) error 是内置的关键字", "E) 我不清楚"],
        "answer": 1, "difficulty": "easy", "topic": "Go接口与错误",
        "explanation": "Go 惯例：函数返回 (T, error)，调用方检查 if err != nil。Go 没有 try-catch。"
    },
    {
        "id": "go_q9",
        "question": "Go 中单元测试函数的命名规则是？",
        "options": ['A) 任意命名，在 test 目录下', 'B) 函数名以 Test 开头，如 TestAdd，文件以 _test.go 结尾', 'C) 函数名以 test 开头', 'D) 需要实现 Test 接口', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "easy",
        "topic": "Go测试",
        "explanation": "Go 测试函数必须在 *_test.go 文件中，函数签名 func TestXxx(t *testing.T)，go test 自动发现并运行。",
    },
    {
        "id": "go_q10",
        "question": "Go 基准测试（Benchmark）的写法是？",
        "options": ['A) func TestBench(b *testing.B) {}', 'B) func BenchmarkXxx(b *testing.B) { for i:=0; i<b.N; i++ { ... } }', 'C) func bench(b *testing.T) {}', 'D) go test -bench 不需要特殊函数', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "Go测试",
        "explanation": "基准测试函数以 Benchmark 开头，参数 *testing.B。b.N 由框架自动调整以保证稳定测量。go test -bench=. 运行。",
    },
    {
        "id": "go_q11",
        "question": "context.Context 应该如何使用？",
        "options": ['A) 存储在 struct 中供后续使用', 'B) 作为函数第一个参数传递，贯穿整个请求链', 'C) 使用全局 context.Background() 即可', 'D) context 可以替代 error', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "Go Context",
        "explanation": "Go 官方建议 Context 作为函数第一个参数（ctx context.Context），不应存储在 struct 中，应贯穿函数调用链。",
    },
    {
        "id": "go_q12",
        "question": "context.WithTimeout 的作用是？",
        "options": ['A) 设置 goroutine 栈大小', 'B) 创建带超时的 context，超时后 ctx.Done() channel 关闭', 'C) 设置 HTTP 响应头', 'D) 延缓函数执行', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "Go Context",
        "explanation": "WithTimeout 返回在指定时间后自动取消的 Context。常用于数据库查询、HTTP 请求等需要超时控制的场景。",
    },
    {
        "id": "go_q13",
        "question": "以下代码输出什么？\nvar x int = 42\nfmt.Println(reflect.TypeOf(x).Kind())",
        "options": ['A) int', 'B) reflect.Int', 'C) compile error', 'D) 42', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "Go反射",
        "explanation": "TypeOf(x).Kind() 返回 reflect.Int（Kind 是 reflect 包的常量）。Name() 返回 \"int\"，Kind() 返回 reflect.Int。",
    },
    {
        "id": "go_q14",
        "question": "使用反射修改值时，必须传入什么？",
        "options": ['A) 值本身', 'B) 指向值的指针，并通过 Elem() 获取可寻址的 Value', 'C) interface{} 类型', 'D) 反射不能修改值', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "Go反射",
        "explanation": "要修改值，必须传入指针：reflect.ValueOf(&x).Elem().SetInt(100)。元素必须是可寻址的（CanSet() 返回 true）。",
    },
    {
        "id": "go_q15",
        "question": "Go 垃圾回收器的特点是什么？",
        "options": ['A) 需要手动调用 GC', 'B) 并发三色标记-清除，低延迟（目标 <1ms STW）', 'C) 引用计数方式', 'D) Go 没有自动 GC', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "Go GC",
        "explanation": "Go GC 是并发三色标记-清除，目标极低 STW（<1ms）。GOGC 环境变量控制 GC 触发频率（默认 100，即堆翻倍时触发）。",
    },
    {
        "id": "go_q16",
        "question": "逃逸分析（Escape Analysis）的作用是？",
        "options": ['A) 检测内存泄漏', 'B) 编译器判断变量是否"逃逸"到堆上——优先分配在栈上减少 GC 压力', 'C) 优化 goroutine 调度', 'D) 检测并发冲突', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "Go GC",
        "explanation": "逃逸分析决定变量分配位置：能在栈上的不分配堆（函数返回即回收）。go build -gcflags='-m' 查看逃逸分析结果。",
    },
    {
        "id": "go_q17",
        "question": "以下代码启动的 HTTP 服务器默认行为是？\nhttp.HandleFunc(\"/hello\", func(w http.ResponseWriter, r *http.Request) {\n    fmt.Fprintf(w, \"Hello\")\n})\nhttp.ListenAndServe(\":8080\", nil)",
        "options": ['A) 监听 8080 端口，GET /hello 返回 Hello', 'B) 编译错误', 'C) 只支持 HTTPS', 'D) 需要手动处理每个 TCP 连接', 'E) 我不清楚'],
        "answer": 0,
        "difficulty": "easy",
        "topic": "Go网络编程",
        "explanation": "http.HandleFunc 注册路由处理函数，ListenAndServe 启动 HTTP 服务器（默认 net/http 为每个连接分配 goroutine）。",
    },
    {
        "id": "go_q18",
        "question": "Go HTTP 中间件的标准签名是？",
        "options": ['A) func(next func) func', 'B) func(http.Handler) http.Handler', 'C) func(http.Request, http.Response)', 'D) func(http.ResponseWriter, *http.Request, next)', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "Go网络编程",
        "explanation": "标准中间件模式：接收 http.Handler 并返回 http.Handler，可链式组合。如日志中间件 func(next http.Handler) http.Handler。",
    },
    {
        "id": "go_q19",
        "question": "Functional Options 模式解决什么问题？",
        "options": ['A) 并发问题', 'B) 提供清晰的 API 来配置复杂对象，避免长参数列表', 'C) 替换 interface', 'D) 减少编译时间', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "Go设计模式",
        "explanation": "Functional Options：type Option func(*Config)；func WithTimeout(d time.Duration) Option。NewServer(WithTimeout(5s), WithPort(8080))，灵活且向后兼容。",
    },
    {
        "id": "go_q20",
        "question": "Go 中依赖注入的惯用方式是？",
        "options": ['A) 必须使用 DI 框架（如 wire）', 'B) 通过接口+构造函数手动注入，Wire 工具生成胶水代码', 'C) 使用全局变量', 'D) Go 不支持依赖注入', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "Go设计模式",
        "explanation": "Go 推崇显式依赖注入：接口定义依赖，构造函数接收并保存。google/wire 是编译时 DI 代码生成工具，无运行时反射开销。",
    },

]


# ===== TypeScript 习题库 (10道) =====
TYPESCRIPT_EXERCISES: list[dict[str, Any]] = [
    {
        "id": "ts_q1",
        "question": "TypeScript 中，以下哪个是正确的类型注解？",
        "options": ["A) let name: string = 42", "B) let name: string = 'hello'", "C) let name = string", "D) string name = 'hello'", "E) 我不清楚"],
        "answer": 1, "difficulty": "easy", "topic": "TypeScript基础",
        "explanation": "TypeScript 类型注解格式为 `变量名: 类型 = 值`。B 正确，A 中 string 类型不能赋 number。"
    },
    {
        "id": "ts_q2",
        "question": "以下代码输出什么？\ninterface User { name: string; age?: number }\nconst u: User = { name: 'Alice' };\nconsole.log(u.age);",
        "options": ["A) 0", "B) null", "C) undefined", "D) 编译错误", "E) 我不清楚"],
        "answer": 2, "difficulty": "easy", "topic": "TypeScript基础",
        "explanation": "age 带 ? 表示可选属性，未提供时值为 undefined。"
    },
    {
        "id": "ts_q3",
        "question": "以下关于 TypeScript 和 JavaScript 关系的描述正确的是？",
        "options": ["A) TypeScript 是 JavaScript 的超集", "B) TypeScript 与 JavaScript 完全不兼容", "C) TypeScript 是 JavaScript 的替代品，不能与 JS 混合使用", "D) TypeScript 需要浏览器原生支持", "E) 我不清楚"],
        "answer": 0, "difficulty": "easy", "topic": "TypeScript基础",
        "explanation": "TypeScript 是 JavaScript 的超集，所有合法的 JS 代码都是合法的 TS 代码。TS 编译为 JS 后在任何 JS 引擎运行。"
    },
    {
        "id": "ts_q4",
        "question": "以下泛型函数定义正确的是？",
        "options": ["A) function first<T>(arr: T[]): T { return arr[0] }", "B) function first(arr: T[]): T { return arr[0] }", "C) function first<T>(arr): T { return arr[0] }", "D) function T first(arr: T[]) { return arr[0] }", "E) 我不清楚"],
        "answer": 0, "difficulty": "medium", "topic": "泛型",
        "explanation": "泛型在函数名后用 <T> 声明，参数类型可引用 T。A 正确：接收 T[] 返回 T。"
    },
    {
        "id": "ts_q5",
        "question": "以下类型工具中，哪个可以将所有属性变为可选？",
        "options": ["A) Required<T>", "B) Partial<T>", "C) Pick<T, K>", "D) Readonly<T>", "E) 我不清楚"],
        "answer": 1, "difficulty": "medium", "topic": "工具类型",
        "explanation": "Partial<T> 将 T 的所有属性变为可选（?）。Required 相反变为必填，Pick 选择部分属性，Readonly 变为只读。"
    },
    {
        "id": "ts_q6",
        "question": "以下关于 enum 的说法正确的是？",
        "options": ["A) TypeScript 不支持枚举", "B) enum 只能在类内部定义", "C) 默认从 0 开始自增，可手动赋值", "D) enum 的值只能是字符串", "E) 我不清楚"],
        "answer": 2, "difficulty": "medium", "topic": "TypeScript基础",
        "explanation": "TypeScript enum 默认从 0 开始自增，支持数字和字符串枚举，可手动赋值。"
    },
    {
        "id": "ts_q7",
        "question": "以下关于 type 和 interface 的区别正确的是？",
        "options": ["A) interface 可以声明合并，type 不能", "B) type 可以被 extends，interface 不能", "C) type 只能定义对象类型", "D) interface 可以定义联合类型", "E) 我不清楚"],
        "answer": 0, "difficulty": "medium", "topic": "类型系统",
        "explanation": "interface 支持声明合并（同名的自动合并），type 不行。type 可定义联合/交叉/元组等复杂类型。两者都可以 extends。"
    },
    {
        "id": "ts_q8",
        "question": "以下代码中，为什么会报错？\nconst obj = { a: 1, b: 'hello' };\nconsole.log(obj.c);",
        "options": ["A) obj 没有 c 属性", "B) TypeScript 推导 obj 的类型为 { a: number; b: string }，c 不在其类型中", "C) 不能在 console.log 中使用点号", "D) 需要使用方括号语法 obj['c']", "E) 我不清楚"],
        "answer": 1, "difficulty": "easy", "topic": "TypeScript基础",
        "explanation": "TypeScript 基于赋值自动推导对象类型。推导出的类型 { a: number; b: string } 不含 c，访问 c 会报编译错误。"
    },
    {
        "id": "ts_q9",
        "question": "以下代码输出什么？\ntype Status = 'loading' | 'success' | 'error';\nfunction handle(s: Status) {\n  switch (s) {\n    case 'loading': return 1;\n    case 'success': return 2;\n    case 'error': return 3;\n  }\n}\nconsole.log(handle('success'));",
        "options": ["A) 1", "B) 2", "C) 3", "D) 编译错误", "E) 我不清楚"],
        "answer": 1, "difficulty": "easy", "topic": "类型系统",
        "explanation": "Status 是字面量联合类型，handle 入参 'success' 匹配 case 'success' 返回 2。穷举检查确保覆盖所有分支。"
    },
    {
        "id": "ts_q10",
        "question": "tsconfig.json 中 'strict' 选项的作用是？",
        "options": ["A) 只启用一种严格检查", "B) 启用所有严格类型检查选项（strictNullChecks、noImplicitAny 等）", "C) 使 TypeScript 变为 JavaScript", "D) 禁止使用 any 类型", "E) 我不清楚"],
        "answer": 1, "difficulty": "medium", "topic": "工程配置",
        "explanation": "strict: true 是推荐配置，一次性启用 strictNullChecks、noImplicitAny、strictFunctionTypes 等所有严格检查选项。"
    },
    {
        "id": "ts_q11",
        "question": "以下类装饰器的作用是？\nfunction sealed(constructor: Function) {\n    Object.seal(constructor);\n    Object.seal(constructor.prototype);\n}\n@sealed\nclass MyClass {}",
        "options": ['A) 让类不可继承', 'B) 密封类和原型，阻止添加/删除属性', 'C) 使类变为单例', 'D) 编译错误', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "TypeScript装饰器",
        "explanation": "类装饰器接收构造函数。@sealed 在类定义时执行 Object.seal，阻止运行时添加或删除属性。",
    },
    {
        "id": "ts_q12",
        "question": "TypeScript 装饰器需要哪个 tsconfig 选项？",
        "options": ['A) strict: true', 'B) experimentalDecorators: true', 'C) emitDecoratorMetadata: true（虽然常一起用，但仅此还不够）', 'D) allowJs: true', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "easy",
        "topic": "TypeScript装饰器",
        "explanation": "装饰器是实验性特性，需在 tsconfig.json 中设置 experimentalDecorators: true（emitDecoratorMetadata 可选，用于元数据反射）。",
    },
    {
        "id": "ts_q13",
        "question": "以下关于 namespace 的说法正确的是？",
        "options": ['A) namespace 是现代 TS 推荐的组织方式', 'B) namespace 将相关代码封装，避免全局命名冲突', 'C) namespace 等同于 import/export', 'D) namespace 只能用于声明文件', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "TypeScript命名空间",
        "explanation": "namespace 是内部模块，可嵌套和拆分。现代项目更推荐 ES Module（import/export），但 namespace 在声明文件（.d.ts）中仍常用。",
    },
    {
        "id": "ts_q14",
        "question": "以下如何正确使用命名空间中的类型？\nnamespace Utils {\n    export interface Result { success: boolean; data: string; }\n}",
        "options": ['A) let r: Result = {}', 'B) let r: Utils.Result = {}', 'C) let r: Utils::Result = {}', "D) import { Result } from 'Utils'", 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "easy",
        "topic": "TypeScript命名空间",
        "explanation": "命名空间通过 export 对外暴露，外部使用 NamespaceName.ExportedName 引用。Utils.Result 是正确的访问方式。",
    },
    {
        "id": "ts_q15",
        "question": "条件类型 infer 关键字的作用是？\ntype ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;",
        "options": ['A) 推断函数返回类型', 'B) 在条件类型中提取并推导类型变量', 'C) 类型断言', 'D) 运行时类型检查', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "TypeScript高级类型",
        "explanation": "infer 在条件类型的 extends 子句中声明一个待推断的类型变量。ReturnType<T> 提取函数类型的返回值类型。",
    },
    {
        "id": "ts_q16",
        "question": "unknown 和 any 的主要区别是？",
        "options": ['A) unknown 是安全的：操作前必须类型守卫；any 跳过类型检查', 'B) 完全相同', 'C) unknown 只能用于 async 函数', 'D) any 比 unknown 更安全', 'E) 我不清楚'],
        "answer": 0,
        "difficulty": "easy",
        "topic": "TypeScript高级类型",
        "explanation": "unknown 是类型安全的 top type：不能直接赋值给其他类型（除 unknown/any），调用方法/访问属性前必须类型守卫。any 关闭所有检查。",
    },
    {
        "id": "ts_q17",
        "question": "以下 async 函数的正确返回类型是？\nasync function fetchUser(id: number) {\n    const res = await fetch(`/api/user/${id}`);\n    return res.json();\n}",
        "options": ['A) Promise<Response>', 'B) Promise<unknown>，因为 res.json() 返回 any', 'C) Promise<any>，因为 res.json() 默认返回 any', 'D) 编译错误', 'E) 我不清楚'],
        "answer": 2,
        "difficulty": "medium",
        "topic": "TypeScript异步",
        "explanation": "res.json() 的默认类型签名是 Promise<any>。实际应声明泛型：fetchUser<T>(id:number): Promise<T> 或 await res.json() as User。",
    },
    {
        "id": "ts_q18",
        "question": "TypeScript 中 try-catch 捕获的错误类型是？",
        "options": ['A) Error', 'B) unknown（从 TS 4.0 起）', 'C) any', 'D) never', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "TypeScript异步",
        "explanation": "TS 4.0+ 的 catch 子句中 error 类型为 unknown（useUnknownInCatchVariables 默认开启），需要 instanceof 检查或类型守卫。",
    },
    {
        "id": "ts_q19",
        "question": "以下代码使用了哪种模式？\ninterface Animal { speak(): string; }\nclass Dog implements Animal { speak() { return 'Woof'; } }\nclass AnimalFactory {\n    static create(type: 'dog' | 'cat'): Animal {\n        if (type === 'dog') return new Dog();\n        return new Cat();\n    }\n}",
        "options": ['A) 单例模式', 'B) 工厂模式（Factory Pattern）', 'C) 装饰器模式', 'D) 观察者模式', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "easy",
        "topic": "TypeScript设计模式",
        "explanation": "工厂模式：通过工厂方法创建对象，隐藏实例化逻辑。利用 TypeScript 的 discriminated union 确保编译时安全。",
    },
    {
        "id": "ts_q20",
        "question": "Discriminated Union 的核心要素是？",
        "options": ['A) 所有类型共享一个公共字面量属性（tag），switch 穷举', 'B) 使用 class 继承', 'C) 使用 any 类型', 'D) 运行时 instanceof 检查', 'E) 我不清楚'],
        "answer": 0,
        "difficulty": "medium",
        "topic": "TypeScript设计模式",
        "explanation": "Discriminated Union 通过字面量类型作为判别字段（如 type: 'success' | 'error'），TS 可在 switch 中自动缩窄类型，实现穷举检查。",
    },
    {
        "id": "ts_q21",
        "question": "vitest 相比 Jest 的主要优势是？",
        "options": ['A) 只支持 TypeScript', 'B) 原生 Vite 支持，开箱即用 TS，速度更快', 'C) 不支持 Mock', 'D) 需要单独的类型定义', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "TypeScript测试",
        "explanation": "vitest 与 Vite 共用配置和转换管道，原生 TypeScript 支持无需额外配置（如 ts-jest），HMR 加速开发体验。",
    },
    {
        "id": "ts_q22",
        "question": "TypeScript 中测试类型的最佳方式是？",
        "options": ['A) 只依靠 Jest 类型检查', 'B) 使用 expect-type 或 tsd 进行编译时类型断言', 'C) 使用 console.log(typeof x)', 'D) TypeScript 不需要类型测试', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "TypeScript测试",
        "explanation": "expect-type 和 tsd 专为编译时类型测试设计。如 expectTypeOf(fn).toMatchTypeOf<(x: number) => string>()，在编译期验证类型。",
    },

]


# ===== Rust 习题库 (10道) =====
RUST_EXERCISES: list[dict[str, Any]] = [
    {
        "id": "rust_q1",
        "question": "Rust 中，以下代码是否有问题？\nlet s1 = String::from(\"hello\");\nlet s2 = s1;\nprintln!(\"{}\", s1);",
        "options": ["A) 正常输出 hello", "B) 编译错误：s1 的所有权已转移给 s2", "C) 运行时错误", "D) 输出两个 hello", "E) 我不清楚"],
        "answer": 1, "difficulty": "easy", "topic": "所有权",
        "explanation": "String 在堆上分配，s2 = s1 发生所有权转移（move），s1 失效。之后再使用 s1 导致编译错误。"
    },
    {
        "id": "rust_q2",
        "question": "Rust 中 &T 和 &mut T 的主要区别是？",
        "options": ["A) 无区别", "B) &T 是不可变引用，&mut T 是可变引用；同一作用域可有多个 &T 但只能有一个 &mut T", "C) &T 比 &mut T 更快", "D) &mut T 不能被函数返回", "E) 我不清楚"],
        "answer": 1, "difficulty": "easy", "topic": "借用",
        "explanation": "Rust 引用规则：同一时刻可有多个不可变引用(&T) 或 一个可变引用(&mut T)，两者不能共存。这保证了数据竞争安全。"
    },
    {
        "id": "rust_q3",
        "question": "以下关于 Option<T> 的说法正确的是？",
        "options": ["A) Option 是 Rust 的异常类型", "B) Option 表示一个值可能存在（Some）或不存在（None），用于替代 null", "C) Option 只能用于数字类型", "D) Option 会自动展开", "E) 我不清楚"],
        "answer": 1, "difficulty": "easy", "topic": "枚举与模式匹配",
        "explanation": "Option<T> 是 Rust 标准库的枚举：Some(T) 包含值，None 表示无值。通过 match 或 unwrap()/? 等处理。Rust 没有 null。"
    },
    {
        "id": "rust_q4",
        "question": "以下代码输出什么？\nlet x = 5;\nmatch x {\n    1 => println!(\"one\"),\n    2..=4 => println!(\"small\"),\n    _ => println!(\"other\"),\n}",
        "options": ["A) one", "B) small", "C) other", "D) 编译错误", "E) 我不清楚"],
        "answer": 2, "difficulty": "easy", "topic": "枚举与模式匹配",
        "explanation": "match 模式匹配：x=5 不匹配 1 和 2..=4（2到4），进入通配符 _（other）。"
    },
    {
        "id": "rust_q5",
        "question": "Rust 中处理潜在错误的惯用方式是？",
        "options": ["A) try-catch 异常", "B) Result<T, E> 枚举，配合 ? 运算符传播错误", "C) 使用全局错误码", "D) 忽略错误", "E) 我不清楚"],
        "answer": 1, "difficulty": "medium", "topic": "错误处理",
        "explanation": "Rust 用 Result<T, E>（Ok(T) 成功 / Err(E) 失败）处理可恢复错误。? 运算符自动传播 Err。不可恢复错误用 panic!。"
    },
    {
        "id": "rust_q6",
        "question": "Rust 中 Trait 的作用是什么？",
        "options": ["A) 类似 Java 的 class，定义数据结构", "B) 定义共享行为（方法集合），类型可以实现多个 Trait", "C) Trait 只能用于泛型", "D) Trait 是 Rust 的包管理工具", "E) 我不清楚"],
        "answer": 1, "difficulty": "medium", "topic": "特征(Trait)",
        "explanation": "Trait 定义一组方法签名，类似接口。类型通过 impl TraitName for TypeName 实现 Trait。泛型约束常用 trait bound（T: Trait）。"
    },
    {
        "id": "rust_q7",
        "question": "以下关于 Vec<T> 的说法正确的是？",
        "options": ["A) Vec 大小在编译时确定", "B) Vec::push() 返回新的 Vec", "C) Vec 是动态数组，可增长，元素存储在堆上", "D) Vec 不能包含 String", "E) 我不清楚"],
        "answer": 2, "difficulty": "easy", "topic": "数据结构",
        "explanation": "Vec<T> 是 Rust 的动态数组，可增长（push），元素在堆上连续存储。数组 [T; N] 大小编译时确定，栈上存储。"
    },
    {
        "id": "rust_q8",
        "question": "Rust 中 Box<T> 的用途是什么？",
        "options": ["A) 创建线程", "B) 在堆上分配数据，常用于递归类型或大对象", "C) 加密数据", "D) 包管理工具", "E) 我不清楚"],
        "answer": 1, "difficulty": "medium", "topic": "智能指针",
        "explanation": "Box<T> 将数据分配在堆上，栈上只存指针。用于：①递归类型（如链表）；②大对象避免栈溢出；③trait object（Box<dyn Trait>）。"
    },
    {
        "id": "rust_q9",
        "question": "以下代码中，为什么需要标注生命周期？\nfn longest<'a>(x: &'a str, y: &'a str) -> &'a str {\n    if x.len() > y.len() { x } else { y }\n}",
        "options": ["A) 编译器无法确定返回的引用来自 x 还是 y", "B) 生命周期标注只是为了文档", "C) 这是可选的语法糖", "D) Rust 不支持这种函数", "E) 我不清楚"],
        "answer": 0, "difficulty": "hard", "topic": "生命周期",
        "explanation": "当函数返回引用时，编译器需要知道返回值与哪个输入参数的生命周期关联。'a 标注表示返回值的生命周期与 x、y 中较短者一致。"
    },
    {
        "id": "rust_q10",
        "question": "Rust 中使用 Cargo 创建新项目的命令是？",
        "options": ["A) cargo new my_project", "B) rustc new my_project", "C) npm init", "D) cargo init", "E) 我不清楚"],
        "answer": 0, "difficulty": "easy", "topic": "工程化",
        "explanation": "cargo new my_project 创建新项目（含 src/main.rs 和 Cargo.toml）。cargo build 编译、cargo run 运行、cargo test 测试。"
    },
    {
        "id": "rust_q11",
        "question": "以下声明宏的输出是？\nmacro_rules! my_vec {\n    ($($x:expr),*) => {\n        {\n            let mut v = Vec::new();\n            $(v.push($x);)*\n            v\n        }\n    };\n}\nlet v = my_vec![1, 2, 3];",
        "options": ['A) 编译错误，宏语法有误', 'B) v = [1, 2, 3]（Vec<i32>）', 'C) v = [1, 2, 3]（数组）', 'D) v = []', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "Rust宏",
        "explanation": "$($x:expr),* 匹配逗号分隔的表达式，$(v.push($x);)* 为每个匹配项展开 push 语句。结果 v = vec![1,2,3]。",
    },
    {
        "id": "rust_q12",
        "question": "#[derive(Debug)] 属于哪类宏？",
        "options": ['A) 声明宏（macro_rules!）', 'B) 过程宏中的派生宏（Derive Macro）', 'C) 属性宏', 'D) 函数式过程宏', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "easy",
        "topic": "Rust宏",
        "explanation": "derive 宏是过程宏的一种，自动为类型实现指定 trait（如 Debug）。编译器在 #[derive(Debug)] 处调用 proc_macro_derive 生成实现代码。",
    },
    {
        "id": "rust_q13",
        "question": "以下代码中，.await 的作用是？\nasync fn fetch_data() -> String { \"data\".into() }\nasync fn main_component() {\n    let result = fetch_data().await;\n}",
        "options": ['A) 阻塞当前线程直到 Future 完成', 'B) 暂停当前 Future，将控制权交还运行时，等 fetch_data 完成后恢复', 'C) 创建新线程执行 fetch_data', 'D) 立即返回 Future', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "Rust异步",
        "explanation": ".await 不阻塞线程。它将当前 Future 挂起并注册到运行时，待 fetch_data 完成后再恢复执行。多个 .await 可交替执行。",
    },
    {
        "id": "rust_q14",
        "question": "Rust async 需要哪个运行时？",
        "options": ['A) 内置，无需第三方', 'B) tokio 或 async-std（Rust 标准库只提供 Future trait，不提供运行时）', 'C) libuv', 'D) Go runtime', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "Rust异步",
        "explanation": "Rust 标准库只定义了 Future trait 和 async/await 语法，不提供运行时。需要 tokio（最流行）或 async-std 等第三方运行时来调度和执行 Future。",
    },
    {
        "id": "rust_q15",
        "question": "unsafe 代码块的作用是？",
        "options": ['A) 关闭所有安全检查，包括借用检查', 'B) 允许五类受限操作：裸指针解引用、调用 unsafe 函数、访问静态可变变量、实现 unsafe trait、访问 union 字段', 'C) 提升运行性能', 'D) 绕过所有权系统任意修改值', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "Rust Unsafe",
        "explanation": "unsafe 块不会关闭借用检查。它仅解锁上述五类能力。通常将 unsafe 封装在安全抽象内（如 Vec 内部 unsafe，对外安全 API）。",
    },
    {
        "id": "rust_q16",
        "question": "FFI（Foreign Function Interface）调用 C 函数为什么需要 unsafe？",
        "options": ['A) 为了性能', 'B) C 函数无法被 Rust 编译器验证安全性（内存安全、线程安全等）', 'C) C 代码比 Rust 危险', 'D) 不需要 unsafe', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "Rust Unsafe",
        "explanation": "Rust 编译器无法检查 C 代码的内存安全性，调用外部函数（extern \"C\" fn）被视为 unsafe 操作，需在 unsafe 块中进行。",
    },
    {
        "id": "rust_q17",
        "question": "Rust 中如何运行单元测试？",
        "options": ['A) cargo run --test', 'B) cargo test', 'C) rustc --test', 'D) cargo check', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "easy",
        "topic": "Rust测试",
        "explanation": "cargo test 编译并运行所有测试（单元测试、集成测试、文档测试）。cargo test test_name 筛选特定测试。",
    },
    {
        "id": "rust_q18",
        "question": "should_panic 属性的作用是？\n#[test]\n#[should_panic]\nfn test_overflow() { panic!(); }",
        "options": ['A) 标记测试应被忽略', 'B) 断言测试会 panic，如果没 panic 则测试失败', 'C) 禁止测试 panic', 'D) 运行时处理 panic', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "easy",
        "topic": "Rust测试",
        "explanation": "#[should_panic] 标记期望 panic 的测试。若函数正常返回（未 panic），测试失败。可加 expected 参数匹配 panic 消息。",
    },
    {
        "id": "rust_q19",
        "question": "pub(crate) 的可见性范围是？",
        "options": ['A) 所有模块', 'B) 仅当前 crate（包）内部', 'C) 仅父模块', 'D) 仅当前文件', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "Rust模块系统",
        "explanation": "pub(crate) 让项在定义它的 crate 内任意位置可见，但 crate 外部不可见。pub(super) 仅父模块可见，pub(in path) 指定路径可见。",
    },
    {
        "id": "rust_q20",
        "question": "use 语句的作用是？",
        "options": ['A) 导入外部 crate', 'B) 将路径引入当前作用域，避免重复写完整路径', 'C) 声明模块', 'D) 导出符号', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "easy",
        "topic": "Rust模块系统",
        "explanation": "use 将路径缩短到当前作用域：use std::collections::HashMap 后可直接用 HashMap。use ... as 可重命名，pub use 可再导出。",
    },
    {
        "id": "rust_q21",
        "question": "以下代码使用了哪种惯用模式？\nstruct Meters(u32);\nimpl Meters {\n    fn new(value: u32) -> Self { Meters(value) }\n    fn value(&self) -> u32 { self.0 }\n}",
        "options": ['A) Strategy', 'B) Newtype 模式：用元组结构体包装基本类型增加类型安全', 'C) Builder', 'D) Singleton', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "Rust设计模式",
        "explanation": "Newtype 模式通过包装类型（Meters(u32)）创建新的类型标识，防止误用（不会把米当成秒）。零运行时开销。",
    },
    {
        "id": "rust_q22",
        "question": "Rust 中如何为外部类型实现自定义 Trait？",
        "options": ['A) 直接 impl MyTrait for Vec<i32> {}', 'B) 使用 Newtype 模式包装外部类型，然后为包装类型实现 Trait（孤儿规则）', 'C) 使用 unsafe', 'D) 无法实现', 'E) 我不清楚'],
        "answer": 1,
        "difficulty": "medium",
        "topic": "Rust设计模式",
        "explanation": "孤儿规则：不能为外部类型实现外部 trait。用 Newtype 包装外部类型，然后为包装类型实现 trait，通过 Deref/DerefMut 获得原始类型行为。",
    },

]


# ===== SQL 习题库 (10道) =====
SQL_EXERCISES: list[dict[str, Any]] = [
    {
        "id": "sql_q1",
        "question": "以下 SQL 查询的作用是？\nSELECT COUNT(*) FROM users WHERE age > 18;",
        "options": ["A) 列出所有年龄大于18的用户", "B) 统计年龄大于18的用户数量", "C) 删除年龄大于18的用户", "D) 更新年龄大于18的用户", "E) 我不清楚"],
        "answer": 1, "difficulty": "easy", "topic": "基础查询",
        "explanation": "COUNT(*) 是聚合函数，返回符合条件的行数而非具体数据。"
    },
    {
        "id": "sql_q2",
        "question": "INNER JOIN 和 LEFT JOIN 的区别是？",
        "options": ["A) 完全相同", "B) INNER JOIN 只返回匹配行；LEFT JOIN 返回左表所有行，右表无匹配填 NULL", "C) LEFT JOIN 比 INNER JOIN 快", "D) INNER JOIN 只在 MySQL 可用", "E) 我不清楚"],
        "answer": 1, "difficulty": "easy", "topic": "JOIN",
        "explanation": "INNER JOIN 只返回两表匹配的行。LEFT JOIN 以左表为准，右表无匹配时填充 NULL。RIGHT JOIN 反之。"
    },
    {
        "id": "sql_q3",
        "question": "以下哪个 SQL 语句可以删除表中所有行但不删除表结构？",
        "options": ["A) DROP TABLE users", "B) DELETE FROM users", "C) TRUNCATE TABLE users", "D) B 和 C 都可以", "E) 我不清楚"],
        "answer": 3, "difficulty": "easy", "topic": "数据操作",
        "explanation": "DELETE FROM users 和 TRUNCATE TABLE users 都清空数据。TRUNCATE 更快（不可回滚），DELETE 可回滚。DROP TABLE 删除整张表。"
    },
    {
        "id": "sql_q4",
        "question": "以下查询输出什么？\nSELECT * FROM orders\nWHERE order_date BETWEEN '2024-01-01' AND '2024-12-31';",
        "options": ["A) 2024年之前的所有订单", "B) 2024年全年的订单（含1月1日和12月31日）", "C) 2024年1月到11月的订单", "D) 报错", "E) 我不清楚"],
        "answer": 1, "difficulty": "easy", "topic": "基础查询",
        "explanation": "BETWEEN 包含边界值，'2024-01-01' 和 '2024-12-31' 都包含在内。"
    },
    {
        "id": "sql_q5",
        "question": "以下 SQL 查询有什么问题？\nSELECT department, COUNT(*) FROM employees;",
        "options": ["A) 语法完全正确", "B) 缺少 GROUP BY department", "C) 不能使用 COUNT(*)", "D) FROM 拼写错误", "E) 我不清楚"],
        "answer": 1, "difficulty": "medium", "topic": "聚合函数",
        "explanation": "SELECT 中同时含普通列（department）和聚合函数（COUNT）时，必须用 GROUP BY department 分组，否则大多数数据库会报错。"
    },
    {
        "id": "sql_q6",
        "question": "HAVING 和 WHERE 的区别是？",
        "options": ["A) 完全相同", "B) WHERE 筛选原始行，HAVING 筛选分组后的聚合结果", "C) HAVING 可以替代 WHERE", "D) HAVING 只能用于子查询", "E) 我不清楚"],
        "answer": 1, "difficulty": "medium", "topic": "聚合函数",
        "explanation": "WHERE 在 GROUP BY 之前筛选行，HAVING 在 GROUP BY 之后筛选分组。HAVING 可使用聚合函数，WHERE 不能。"
    },
    {
        "id": "sql_q7",
        "question": "以下哪个 SQL 语句用于创建索引？",
        "options": ["A) ADD INDEX idx_name ON users(name)", "B) CREATE INDEX idx_name ON users(name)", "C) MAKE INDEX idx_name ON users(name)", "D) INDEX idx_name ON users(name)", "E) 我不清楚"],
        "answer": 1, "difficulty": "medium", "topic": "索引",
        "explanation": "CREATE INDEX idx_name ON table(column) 创建索引。索引加速 WHERE/JOIN/ORDER BY 查询，但会降低写入性能。"
    },
    {
        "id": "sql_q8",
        "question": "事务的 ACID 属性中，'I' 代表什么？",
        "options": ["A) Integrity（完整性）", "B) Isolation（隔离性）", "C) Index（索引）", "D) Instant（即时）", "E) 我不清楚"],
        "answer": 1, "difficulty": "medium", "topic": "事务",
        "explanation": "ACID：Atomicity（原子性）、Consistency（一致性）、Isolation（隔离性）、Durability（持久性）。"
    },
    {
        "id": "sql_q9",
        "question": "以下 SQL 查询的作用是？\nSELECT department, AVG(salary) as avg_sal\nFROM employees\nGROUP BY department\nHAVING AVG(salary) > 5000;",
        "options": ["A) 列出所有部门", "B) 找出平均薪资超过5000的部门及其平均薪资", "C) 计算全公司平均薪资", "D) 删除薪资低于5000的员工", "E) 我不清楚"],
        "answer": 1, "difficulty": "medium", "topic": "聚合函数",
        "explanation": "GROUP BY 按部门分组，AVG 计算每组的平均薪资，HAVING 过滤出平均薪资 > 5000 的组。"
    },
    {
        "id": "sql_q10",
        "question": "以下关于 SQL 注入的说法正确的是？",
        "options": ["A) SQL 注入无法防御", "B) 使用参数化查询（Prepared Statement）可有效防止 SQL 注入", "C) 只在 MySQL 中需要关注 SQL 注入", "D) 拼接 SQL 字符串最安全", "E) 我不清楚"],
        "answer": 1, "difficulty": "medium", "topic": "安全性",
        "explanation": "参数化查询（预编译语句）将 SQL 结构与数据分离，阻止恶意输入被解析为 SQL 代码，是最有效的防注入手段。"
    },
    {
        "id": "sql_q11",
        "question": "事务的原子性（Atomicity）意味着什么？",
        "options": ["A) 事务可以与其他事务并发执行", "B) 事务中的所有操作要么全部成功，要么全部回滚", "C) 事务执行后数据满足所有约束", "D) 事务提交后永久保存", "E) 我不清楚"],
        "answer": 1, "difficulty": "easy", "topic": "SQL事务",
        "explanation": "原子性（A of ACID）：事务是不可分割的最小单元。若事务中任何一步失败，已执行的操作自动回滚到事务开始前状态。"
    },
    {
        "id": "sql_q12",
        "question": "在 MySQL InnoDB 中，默认事务隔离级别是？",
        "options": ["A) READ UNCOMMITTED（读未提交）", "B) READ COMMITTED（读已提交）", "C) REPEATABLE READ（可重复读）", "D) SERIALIZABLE（串行化）", "E) 我不清楚"],
        "answer": 2, "difficulty": "medium", "topic": "SQL事务",
        "explanation": "MySQL InnoDB 默认 REPEATABLE READ，通过 MVCC + Next-Key Lock 在一定程度上防止幻读。PostgreSQL 默认 READ COMMITTED。"
    },
    {
        "id": "sql_q13",
        "question": "以下关于视图的语句，哪个是正确的？",
        "options": ["A) CREATE VIEW active_users AS SELECT * FROM users WHERE status = 'active'", "B) VIEW active_users AS SELECT * FROM users", "C) CREATE active_users VIEW AS SELECT * FROM users", "D) CREATE VIEW active_users { SELECT * FROM users WHERE status = 'active' }", "E) 我不清楚"],
        "answer": 0, "difficulty": "easy", "topic": "SQL视图",
        "explanation": "CREATE VIEW view_name AS SELECT ... 是标准语法。视图是虚拟表，查询时动态执行其 SELECT 语句。"
    },
    {
        "id": "sql_q14",
        "question": "物化视图（Materialized View）和普通视图的区别是？",
        "options": ["A) 没有区别", "B) 物化视图存储查询结果的物理副本，查询更快但需手动刷新数据", "C) 物化视图不支持 SELECT", "D) 物化视图只能有 1 列", "E) 我不清楚"],
        "answer": 1, "difficulty": "medium", "topic": "SQL视图",
        "explanation": "普通视图每次访问时动态执行查询。物化视图预计算并存储结果（物理表），查询直接返回快照数据，适合汇总报表。"
    },
    {
        "id": "sql_q15",
        "question": "存储过程相比直接执行多条 SQL 的优势是？",
        "options": ["A) 只能用于 MySQL", "B) 预编译提升性能、减少网络传输、封装业务逻辑、权限控制", "C) 存储过程总是比直接 SQL 快", "D) 不需要数据库", "E) 我不清楚"],
        "answer": 1, "difficulty": "easy", "topic": "SQL存储过程",
        "explanation": "存储过程在服务器端预编译并缓存执行计划，一次调用可执行多条 SQL，减少网络往返。还可在存储过程内封装权限校验逻辑。"
    },
    {
        "id": "sql_q16",
        "question": "MySQL 中定义存储过程的基本语法是？",
        "options": ["A) CREATE PROC name AS ...", "B) CREATE PROCEDURE name(params) BEGIN ... END", "C) FUNCTION name RETURN ...", "D) PROCEDURE name IS ...", "E) 我不清楚"],
        "answer": 1, "difficulty": "medium", "topic": "SQL存储过程",
        "explanation": "MySQL 存储过程：CREATE PROCEDURE name(IN param1 INT, OUT param2 VARCHAR) BEGIN ... END。用 CALL name(...) 调用。"
    },
    {
        "id": "sql_q17",
        "question": "以下查询输出什么？\nSELECT name, score, RANK() OVER (ORDER BY score DESC) as rnk\nFROM students;",
        "options": ["A) 每行一个排名，同分不同名", "B) 每行一个排名，同分同名且后续排名跳过（如 1,2,2,4）", "C) 只有一行结果", "D) 编译错误", "E) 我不清楚"],
        "answer": 1, "difficulty": "medium", "topic": "SQL窗口函数",
        "explanation": "RANK() 窗口函数按 score DESC 降序排名。同分同名，下一名跳过（如 1,2,2,4）。DENSE_RANK() 不跳过，ROW_NUMBER() 同分不同名。"
    },
    {
        "id": "sql_q18",
        "question": "窗口函数中 PARTITION BY 的作用是？",
        "options": ["A) 过滤行", "B) 将结果集按指定列分组，窗口函数在每组内独立计算", "C) 排序", "D) 合并结果集", "E) 我不清楚"],
        "answer": 1, "difficulty": "medium", "topic": "SQL窗口函数",
        "explanation": "PARTITION BY 类似 GROUP BY 但不合并行。窗口函数在每个分区内独立计算。如 ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) 在每个部门内排名。"
    },
]

# 按语言汇总所有习题库
ALL_EXERCISE_BANKS: dict[str, list[dict[str, Any]]] = {
    "python": [],  # 留空：由 exercise_service.py 的 PYTHON_EXERCISES 兜底
    "java": JAVA_EXERCISES,
    "javascript": JS_EXERCISES,
    "typescript": TYPESCRIPT_EXERCISES,
    "cpp": CPP_EXERCISES,
    "go": GO_EXERCISES,
    "rust": RUST_EXERCISES,
    "sql": SQL_EXERCISES,
}