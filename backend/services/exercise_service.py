"""习题练习服务 — 按条件筛选题目 + 提交评分"""
import random
from typing import Any

from .multi_lang_exercises import ALL_EXERCISE_BANKS

# 主题概念定义（每个主题的简明解释）
TOPIC_CONCEPTS: dict[str, str] = {
    # Python 主题
    "数据类型": "Python 变量有多种类型：int（整数）、float（小数）、str（字符串）、list（列表）、tuple（元组）、dict（字典）、set（集合）、bool（布尔）。核心要区分「可变类型」（list、dict、set，内容可改）和「不可变类型」（int、float、str、tuple，内容不能改）。这直接影响赋值、传参和哈希行为。",
    "控制流": "决定代码走哪个分支、循环多少次。if/elif/else 做条件判断（从上到下只执行第一个 True 的分支），for 遍历可迭代对象，while 在条件为 True 时反复执行。break 跳出循环，continue 跳过当前轮，else 子句在循环正常结束时触发。",
    "函数": "用 def 定义的可复用代码块，接收参数并返回结果。参数有位置参数、关键字参数、默认值、*args（变长位置）、**kwargs（变长关键字）。函数内部变量默认局部作用域，要修改外部变量需用 global/nonlocal。lambda 可写单行匿名函数。",
    "列表操作": "列表 [ ] 是 Python 最常用的可变序列。核心操作：索引 [i]、切片 [start:stop:step]、append/pop/insert/remove 增删元素、sort/reverse 排序、extend 合并。列表推导式 [x for x in ... if ...] 能一行生成新列表，是 Python 的标志性语法。",
    "字典操作": "字典 {key: value} 是键值对映射，通过 key 快速查找 value（O(1)）。key 必须是不可变类型（字符串、数字、元组）。常用方法：get(key, default) 安全取值、items()/keys()/values() 遍历、update() 合并、字典推导式批量构造。",
    "字符串": "字符串是不可变的 Unicode 字符序列。支持索引 [i] 和切片 [::]。常用操作：len()、upper()/lower()、strip() 去空格、split() 分割为列表、join() 拼接、replace() 替换、find() 查找、f'{变量}' 格式化（f-string），这是最推荐的格式化方式。",
    "面向对象": "用 class 定义类，封装数据（属性）和行为（方法）。__init__ 是构造函数，self 指向实例自身。三大特性：封装（隐藏内部实现）、继承（子类复用父类代码）、多态（不同类实现相同接口）。__str__/__repr__ 定义打印格式，@property 把方法伪装成属性。",
    "异常处理": "try/except 捕获运行时错误，避免程序崩溃。try 块放可能出错的代码，except 捕获指定异常类型，finally 无论是否异常都执行（常用于释放资源），else 在无异常时执行。raise 手动抛出异常，可自定义异常类继承 Exception。",
    "文件IO": "open() 打开文件，模式：'r' 读、'w' 覆盖写、'a' 追加、'rb'/'wb' 二进制读写。推荐 with open(...) as f: 语法，自动关闭文件无需 f.close()。读：f.read() 全读、f.readline() 逐行、f.readlines() 读为列表。写：f.write()。",
    "装饰器": "不修改函数代码的前提下给函数加功能。本质是「接收函数、返回新函数」的闭包。@decorator 语法糖等价于 func = decorator(func)。常见用途：日志、计时、权限校验、缓存。内置装饰器有 @staticmethod、@classmethod、@property。",
    "生成器": "用 yield 代替 return 的函数叫生成器。特点是「惰性计算」——不一次性生成所有值，而是每次调用 next() 产出一个值，省内存。适合处理大文件、无限序列。生成器表达式 (x for x in ...) 是列表推导式的惰性版本。",
    "GIL/并发": "GIL（全局解释器锁）是 CPython 的机制，保证同一时刻只有一个线程执行 Python 字节码。所以多线程无法利用多核做 CPU 密集型计算。应对：CPU 密集用 multiprocessing 多进程；IO 密集仍可用 threading 或更高效的 asyncio 协程。",
    "常用库": "Python 标准库（os 系统操作、sys 解释器参数、re 正则、json 序列化、datetime 日期时间、collections 高级容器）和常用第三方库（requests 网络请求、pandas 数据分析、numpy 科学计算）。善用库大幅提升效率，无需重复造轮子。",
    "装饰器深入": "在基础装饰器之上深入：带参数的类装饰器、装饰器工厂模式（根据条件返回不同装饰器）、singledispatch 单分派泛函数、参数验证装饰器（利用类型注解运行时校验）、注册表模式（用装饰器自动注册插件）、retry 重试装饰器（指数退避）。理解装饰器本质是「在编译时/导入时执行的元编程」，让你写出更灵活、可组合的框架级代码。",
    "异步编程": "asyncio 是 Python 的异步 I/O 框架，基于事件循环（Event Loop）和协程（coroutine）。async def 定义协程，await 挂起等待可等待对象。Task 并发执行协程，gather() 聚合多个协程结果。aiohttp 异步 HTTP 客户端，aiomysql/asyncpg 异步数据库驱动。异步代码必须「一路 async 到底」，避免混用同步阻塞调用。与线程/进程模型不同，asyncio 是单线程协作式并发，适合高并发 I/O 场景（Web 服务器、爬虫、实时通信）。",
    "类型系统": "Python 3.5+ 支持类型注解（Type Hints），结合 mypy/pyright 做静态类型检查。基础注解：变量: 类型、函数参数和返回值标注。typing 模块提供：Optional[X]（X 或 None）、Union[X, Y]（X | Y, 3.10+）、List[X]/Dict[K,V]（3.9+ 用内置 list[X]）、Callable[[Args], Ret] 标注函数类型、Protocol（结构化子类型/鸭子类型的形式化）、TypedDict（标注字典结构）、Literal（限定具体值）。泛型：TypeVar 声明类型变量，Generic[T] 实现泛型类，让你的代码既灵活又类型安全。",
    "性能优化": "Python 性能优化方法论：①先测量再优化——cProfile/profile 做热点分析，line_profiler 逐行计时，memory_profiler 检查内存泄漏，timeit 做微基准测试。②常见瓶颈：循环中频繁属性访问（缓存为局部变量）、字符串 + 拼接（改用 join）、全局变量查找（放局部命名空间）。③进阶手段：__slots__ 减少对象内存、生成器替代列表减少峰值内存、functools.lru_cache 避免重复计算、PyPy JIT 编译器提速。④终极方案：Cython 编译为 C 扩展、Numba JIT 加速数值计算。",
    "实战项目": "综合运用所学构建完整项目：①命令行工具（argparse 参数解析 + rich 美化输出 + click 框架），适合脚本、运维工具。②REST API 服务（FastAPI + Pydantic 模型 + async/await + uvicorn 部署），自动生成 OpenAPI 文档。③数据处理管道（pandas 清洗 + asyncio 并发拉取 + openpyxl 导出报表）。项目结构规范：pyproject.toml 管理依赖、src 布局、pytest 测试覆盖、pre-commit 代码质量检查。完整项目帮你串联所有知识，建立从需求到交付的全链路思维。",
    # Java 主题
    "Java基础": "Java 是静态强类型语言，变量先声明后使用。8 种基本类型：byte/short/int/long/float/double/char/boolean。引用类型存地址。自动装箱/拆箱允许基本类型与包装类（Integer/Long/Double）互转。String 不可变，频繁拼接用 StringBuilder。",
    "Java集合": "Java 集合框架：Collection 接口下分 List（有序可重复）、Set（无序不可重复）、Queue（队列）。Map（键值对）独立体系。常用实现类：ArrayList（数组实现，随机访问快）、LinkedList（双向链表，增删快）、HashSet/HashMap（哈希表，O(1)）、TreeSet/TreeMap（红黑树，有序）。",
    "Java OOP": "Java 面向对象：封装（private + getter/setter）、继承（extends 单继承，super 调用父类）、多态（父类引用指向子类对象，方法重写 @Override 实现运行时多态）。抽象类（abstract）和接口（interface）定义契约，Java 8+ 接口支持 default/static 方法。",
    "Java异常": "Java 异常分 Error（不可恢复）和 Exception（可处理）。RuntimeException 为非受检异常（空指针、数组越界），其余 Exception 为受检异常（必须 try-catch 或 throws）。try-catch-finally 中 finally 保证执行。try-with-resources 自动关闭资源。",
    "Java并发": "Java 多线程：Thread 类或 Runnable 接口创建线程。synchronized 关键字保证互斥访问（对象锁/类锁），volatile 保证可见性。wait/notify 用于线程通信。java.util.concurrent 提供线程池、ConcurrentHashMap、CountDownLatch 等高级工具。",
    "Spring Boot": "Spring Boot 简化 Spring 应用开发：自动配置（@EnableAutoConfiguration）、起步依赖（starter）、内嵌 Tomcat。@RestController + @RequestMapping 构建 REST API，@Autowired 依赖注入，@Transactional 声明式事务管理。",
    # JavaScript 主题
    "JS基础": "JavaScript 是动态弱类型语言。var（函数作用域，变量提升）、let/const（块级作用域，TDZ 暂时死区）。7 种原始类型：string/number/boolean/null/undefined/symbol/bigint，外加 object。typeof null === 'object' 是历史 Bug。",
    "JS异步": "JavaScript 单线程事件循环。异步方案演进：回调函数 → Promise（三种状态 pending/fulfilled/rejected）→ async/await（语法糖）。微任务（Promise.then）优先于宏任务（setTimeout）。",
    "JS原型与this": "JavaScript 原型链实现继承：每个对象有 [[Prototype]]。this 由调用方式决定而非定义时。箭头函数不绑定 this，继承外层。call/apply/bind 显式绑定 this。",
    "JS模块": "CommonJS（Node.js，require/module.exports）与 ESM（ES6，import/export）。ESM 静态分析支持 Tree Shaking。npm 包管理，package.json 中 type: module 启用 ESM。",
    # C++ 主题
    "C++基础": "C++ 是静态类型、编译型语言，支持面向对象和泛型编程。基本类型：int/float/double/char/bool。指针（*存储地址）和引用（&别名）是核心概念。const 声明常量，constexpr 编译期求值。现代 C++（C++11/14/17/20）推荐智能指针和 auto 推导。",
    "C++STL": "C++ STL 六大组件：容器（vector/list/map/set/unordered_map）、算法（sort/find/transform）、迭代器、适配器（stack/queue）、函数对象、分配器。vector 连续内存动态扩容，map 红黑树有序键值对，unordered_map 哈希表 O(1) 查找。",
    "C++内存管理": "C++ 手动内存管理：new/delete 分配/释放堆内存。RAII（资源获取即初始化）：利用对象生命周期自动管理资源。智能指针：unique_ptr（独占）、shared_ptr（引用计数共享）、weak_ptr（不影响计数，解决循环引用）。",
    "C++多态": "C++ 编译时多态（函数/运算符重载、模板）与运行时多态（virtual 虚函数）。虚函数通过 vtable 实现动态绑定。纯虚函数（=0）定义抽象类。基类析构函数应为 virtual。",
    # Go 主题
    "Go基础": "Go 是静态类型、编译型语言，语法简洁。:= 短变量声明，类型可推断。没有类和继承，通过 struct 组合和 interface 隐式实现达到多态。多返回值，惯例 (result, error)。gofmt 统一代码格式。",
    "Go并发": "goroutine 是轻量级线程（go func()），channel 用于 goroutine 通信。无缓冲 channel 同步阻塞，有缓冲 channel 异步。select 多路监听。sync.Mutex/WaitGroup/Once 提供同步原语。CSP 哲学：通过通信共享内存。",
    "Go接口与错误": "Go 接口隐式实现（鸭子类型），空接口 any/interface{} 接受任意类型。类型断言 x.(T) 和类型选择 switch x.(type)。error 是内置接口，函数返回 (T, error)，调用方必须检查。defer + recover 处理 panic。",
    "Go工程化": "Go Modules（go mod）管理依赖。标准布局：/cmd（入口）、/internal（私有）、/pkg（公共）。Context 传递 deadline/取消信号/请求值。内置 testing 包支持单元测试（go test），Table-Driven Tests 是最佳实践。",
    # TypeScript 主题
    "TypeScript基础": "TypeScript 是 JavaScript 的超集，添加了静态类型系统。核心类型：string/number/boolean/array/tuple/enum/any/unknown/void/never。类型注解用冒号 `let name: string`。接口（interface）和类型别名（type）定义对象结构。联合类型 `|` 和交叉类型 `&` 组合多种类型，类型推断减少显式标注。",
    "TypeScript类型系统": "TypeScript 类型系统的进阶特性：泛型（Generics）让函数/类/接口支持多种类型，`<T>` 语法；类型守卫（typeof/instanceof/in 收窄类型）；条件类型 `T extends U ? X : Y`；映射类型 `{ [K in keyof T]: ... }` 批量转换属性；工具类型 Partial/Required/Pick/Omit 简化常见转换。",
    "TypeScript泛型": "泛型让代码在保持类型安全的同时具备灵活性。泛型函数 `function identity<T>(arg: T): T`、泛型接口、泛型约束 `T extends Lengthwise` 限制类型参数。泛型在 React 中广泛应用（useState<Type>、Props 类型化）。infer 关键字在条件类型中推断类型变量。",
    "TypeScript工程化": "TypeScript 项目配置 tsconfig.json：target/module/strict/paths。声明文件 .d.ts 为 JS 库提供类型。DefinitelyTyped（@types/xxx）社区类型库。与构建工具集成：Vite/Webpack 的 ts-loader。ESLint + typescript-eslint 代码规范，tsc --noEmit 类型检查。",
    # Rust 主题
    "Rust基础": "Rust 是系统级语言，零成本抽象 + 内存安全（无 GC）。变量默认不可变（let），可变用 let mut。所有权（Ownership）是核心：每个值有唯一所有者，离开作用域自动释放。借用（Borrowing）：&T 不可变引用、&mut T 可变引用，同一时刻只能有一个可变引用或多个不可变引用。",
    "Rust所有权": "Rust 所有权规则：1) 每个值有唯一所有者；2) 所有权可通过赋值/传参/返回值移动（move）；3) 离开作用域时值被 drop。Copy trait 的类型（整数/bool 等）赋值时自动复制而非移动。引用不转移所有权，Rc/Arc 实现多所有者共享。生命周期（Lifetime）标注确保引用有效。",
    "Rust特性": "Trait 定义共享行为，类似其他语言的接口。`impl Trait for Type` 为类型实现 trait。derive 宏自动实现 Debug/Clone/Copy 等常见 trait。泛型约束 `fn foo<T: Trait>` 限定类型参数。trait 对象 `Box<dyn Trait>` 实现动态分发。关联类型、默认实现、supertrait 等高级特性。",
    "Rust并发": "Rust 通过类型系统保证线程安全：Send trait（可跨线程转移所有权）、Sync trait（可跨线程共享引用）。std::thread::spawn 创建线程，move 闭包转移所有权。Mutex<T> 互斥锁 + Arc 多线程共享，RwLock 读写锁。Channel（mpsc）线程间消息传递，遵循「共享内存靠锁，消息传递靠 Channel」原则。",
    # SQL 主题
    "SQL基础": "SQL（Structured Query Language）是关系数据库标准语言。DDL：CREATE（建表）、ALTER（修改表）、DROP（删表）；DML：SELECT（查询）、INSERT（插入）、UPDATE（更新）、DELETE（删除）。数据类型：INT/VARCHAR/DATE/BOOLEAN/DECIMAL。主键（PRIMARY KEY）唯一标识行，外键（FOREIGN KEY）关联表间关系。",
    "SQL查询": "SELECT 语句核心：SELECT 列名 FROM 表名 WHERE 条件 ORDER BY 排序列 ASC/DESC LIMIT 限制条数。WHERE 支持 =、<>、>、<、BETWEEN、LIKE（%通配）、IN、IS NULL。聚合函数：COUNT/SUM/AVG/MAX/MIN 配合 GROUP BY 分组统计，HAVING 过滤分组结果。DISTINCT 去重。",
    "JOIN与子查询": "JOIN 连接多表查询：INNER JOIN 取交集、LEFT JOIN 保留左表所有行、RIGHT JOIN 保留右表、FULL JOIN 全连接。ON 指定连接条件。子查询：SELECT 中的标量子查询、FROM 子查询、WHERE 中的关联子查询，EXISTS/NOT EXISTS 检查存在性。UNION 合并结果集（自动去重），UNION ALL 不去重。",
    "聚合函数": "SQL 聚合函数对一组行计算单个结果。COUNT(*) 统计行数、SUM(列) 求和、AVG(列) 平均值、MAX/MIN 最大最小值。必须配合 GROUP BY 使用，分组后每组的聚合结果。HAVING 子句过滤分组（与 WHERE 区别：WHERE 过滤原始行，HAVING 过滤分组结果）。窗口函数（OVER/PARTITION BY/RANK）实现分组内排序和累计。",
    "索引与性能": "索引加速查询（B-Tree 默认），类似书的目录。CREATE INDEX 创建索引，主键自动建索引。适合高频查询列和 WHERE/JOIN/ORDER BY 列，但索引会降低 INSERT/UPDATE/DELETE 性能且占用额外空间。EXPLAIN 分析查询执行计划。复合索引遵循最左前缀原则。避免 SELECT *，合理使用 LIMIT 减少数据传输。",
    "安全性": "SQL 注入是最常见的安全漏洞：恶意用户通过输入拼接 SQL 语句执行非授权操作。防御手段：参数化查询（Prepared Statement）将 SQL 结构与数据分离，ORM 框架（SQLAlchemy/Hibernate）自动处理。最小权限原则：应用账号只授予必要权限。敏感数据加密存储，定期备份。",
    "SQL事务": "事务（Transaction）是一组不可分割的数据库操作，要么全部成功，要么全部回滚。ACID 属性：原子性（Atomicity，全或无）、一致性（Consistency，事务前后数据满足约束）、隔离性（Isolation，并发事务互不干扰）、持久性（Durability，提交后永久保存）。BEGIN/START TRANSACTION 开始，COMMIT 提交，ROLLBACK 回滚。隔离级别：读未提交/读已提交/可重复读/串行化，解决脏读、不可重复读、幻读问题。",
    "SQL视图": "视图（View）是基于 SQL 查询的虚拟表，不存储数据，每次访问动态执行定义它的 SELECT 语句。CREATE VIEW name AS SELECT ... 创建视图。用途：简化复杂查询（封装多表 JOIN）、权限控制（只暴露部分列）、逻辑数据独立性（底层表变更不影响上层应用）。MATERIALIZED VIEW（物化视图）存储查询结果的物理副本，适合报表加速但需手动刷新。",
    "SQL存储过程": "存储过程（Stored Procedure）是预编译的 SQL 代码块，存储在数据库服务器端。CREATE PROCEDURE name(params) BEGIN ... END 定义。优势：减少网络传输（一次调用执行多条 SQL）、预编译提升性能、封装业务逻辑、安全权限控制。Cursor 逐行处理结果集。函数（Function）与存储过程的区别：函数必须有返回值，可在 SELECT 中调用；存储过程通过 OUT 参数返回数据。",
    "SQL窗口函数": "窗口函数（Window Function）在结果集的行组（窗口）上执行聚合计算，但不合并行（保留原始行数）。语法：func() OVER (PARTITION BY 列 ORDER BY 列)。常用函数：ROW_NUMBER() 行号、RANK() 跳跃排名（同值同排名后续跳过）、DENSE_RANK() 连续排名、LAG/LEAD 前/后行值。用途：Top-N 查询、累计求和（SUM OVER）、移动平均、同比环比计算。窗口函数与 GROUP BY 的核心区别：GROUP BY 折叠行，窗口函数保留每行。",
    # Java 补充主题
    "Java Lambda": "Java 8 引入 Lambda 表达式 (参数) -> { 表达式 }，简化函数式接口（只有一个抽象方法的接口）的匿名实现。常见函数式接口：Function<T,R> 输入T返回R、Predicate<T> 返回boolean、Consumer<T> 消费不返回、Supplier<T> 无输入返回T。方法引用 Class::method 进一步简化。Stream API 配合 Lambda 实现函数式数据处理：filter/map/reduce/collect。",
    "Java泛型": "泛型（Generics）让类/接口/方法在定义时不指定具体类型，使用时再确定。List<String> 保证类型安全，避免 ClassCastException。泛型边界：<? extends T> 上界（生产者）、<? super T> 下界（消费者），PECS 原则（Producer Extends, Consumer Super）。类型擦除：编译后泛型信息被移除，运行时无法获取泛型类型参数。",
    "Java IO": "Java IO 以流（Stream）为核心处理输入输出。字节流 InputStream/OutputStream（FileInputStream/BufferedInputStream）处理二进制数据；字符流 Reader/Writer（FileReader/BufferedReader）处理文本，自动处理编码。BufferedReader/Writer 缓冲加速，ObjectInputStream/ObjectOutputStream 序列化对象。NIO（New IO）提供 Channel+Buffer 非阻塞模型，Files/Paths 简化文件操作。",
    "Java注解": "注解（Annotation）是代码元数据，以 @ 开头，不影响代码逻辑但可被编译器/框架/运行时读取。内置注解：@Override 验证重写、@Deprecated 标记废弃、@SuppressWarnings 抑制警告。元注解：@Target 限定适用范围、@Retention 控制生命周期（SOURCE/CLASS/RUNTIME）、@Inherited 允许子类继承。自定义注解：@interface 定义，配合反射读取，Spring/MyBatis 等框架大量使用注解驱动配置。",
    # JavaScript 补充主题
    "JS闭包": "闭包（Closure）是 JS 核心机制：函数内部定义的函数可以访问外部函数的变量，即使外部函数已执行完毕。闭包让变量私有化（模块模式）、创建工厂函数、实现柯里化和部分应用。经典场景：for 循环中的 var 闭包陷阱（用 let 或 IIFE 解决）、防抖节流函数的计时器保持。闭包可能导致内存泄漏——不再需要的闭包变量不会被 GC 回收。",
    "JS DOM": "DOM（Document Object Model）是浏览器提供的编程接口，将 HTML 文档表示为节点树。核心操作：document.getElementById/querySelector 选择元素、innerHTML/textContent 读写内容、classList.add/remove/toggle 操作类、createElement/appendChild 动态创建元素。事件处理：addEventListener 绑定事件，事件冒泡（子→父）和捕获（父→子），event.stopPropagation() 阻止传播，事件委托利用冒泡减少监听器数量。",
    "JS事件循环": "JS 事件循环（Event Loop）是单线程异步的核心机制：调用栈执行同步代码 → 微任务队列（Promise.then/MutationObserver）→ 宏任务队列（setTimeout/setInterval/IO）。每轮事件循环：先清空一个宏任务 → 清空所有微任务 → 渲染（如需要）→ 下一轮。理解事件循环对 async/await、Promise 执行顺序至关重要。requestAnimationFrame 在渲染前执行，适合动画。",
    "JS错误处理": "JS 错误处理：try-catch-finally 捕获同步错误（不能捕获异步回调中的错误——需在回调内部 try-catch）。Promise 用法：.catch() 捕获 reject 和 then 链中的错误，.finally() 清理。async/await 可用 try-catch 包裹 await。window.onerror 全局捕获未处理的运行时错误，unhandledrejection 事件捕获未处理的 Promise 拒绝。自定义错误：class MyError extends Error。",
    "JS存储": "浏览器存储方案：localStorage（持久化，5-10MB，同源共享，仅字符串）、sessionStorage（会话级别，标签页关闭清除）、Cookie（4KB限制，随 HTTP 请求发送，可设过期时间和 HttpOnly/Secure 属性）。IndexedDB 是大规模结构化数据的客户端存储（异步、支持索引和事务）。Cache API 缓存 HTTP 请求/响应，Service Worker 实现离线应用。",
    "JS设计模式": "JavaScript 常见设计模式：模块模式（IIFE/ES6 export 封装私有变量）、观察者模式（EventEmitter/自定义事件）实现松耦合通信、单例模式（全局唯一实例）、工厂模式（创建对象不暴露细节）、策略模式（根据不同条件选择算法）。装饰器模式（动态添加行为，ES7 @decorator 提案）、代理模式（Proxy 拦截对象操作，Vue 3 响应式核心）。",
    # C++ 补充主题
    "C++模板": "C++ 模板是泛型编程的基石：template<typename T> 定义函数模板和类模板，编译时根据使用实例化具体类型。模板特化：全特化 template<> 为特定类型提供定制实现；偏特化 部分参数特化。变参模板 template<typename... Args> 支持任意数量类型参数（C++11）。SFINAE（替换失败不是错误）和 concept（C++20）约束模板参数。模板元编程：编译期计算（递归模板展开），std::enable_if 条件启用。",
    "C++并发": "C++11 起标准库提供多线程支持：std::thread 创建线程、std::mutex 互斥锁（lock_guard/unique_lock RAII 管理）、std::condition_variable 条件变量实现线程等待/通知。std::atomic 原子操作（无锁编程），memory_order 控制内存序。std::future + std::promise（一对一通信）、std::async 异步任务。std::shared_mutex 读写锁（C++17）。死锁场景与避免：std::lock 同时锁定多个锁、lock_guard + std::adopt_lock。",
    "C++Move": "C++11 引入移动语义，解决不必要的深拷贝。左值（有地址可寻址）vs 右值（临时对象，即将销毁）。std::move() 将左值转为右值引用触发移动构造/赋值。移动构造函数 T(T&& other) 窃取 other 的资源并将 other 置为有效但未定义状态。Rule of Five：定义了析构/拷贝构造/拷贝赋值之一，通常需要同时定义移动构造和移动赋值。std::forward 完美转发保持值类别。",
    "C++异常": "C++ 异常处理：throw 抛出异常、try{} catch(type e){} 捕获特定类型、catch(...) 捕获所有。RAII + 异常安全保证：①基本保证（不泄漏资源）②强保证（失败回滚到调用前状态）③不抛异常保证（noexcept）。noexcept 关键字声明函数不抛异常，编译器可据此优化，且移动构造应标记 noexcept。std::exception 层次结构：logic_error（domain/invalid_argument）、runtime_error（range/overflow）。",
    "C++Lambda": "C++11 Lambda 表达式：[捕获列表](参数列表) -> 返回类型 { 函数体 }，返回类型可省略由编译器推导。捕获方式：[=] 值捕获（只读）、[&] 引用捕获、[this] 捕获 this 指针、[a,&b] 混合捕获。Lambda 本质是匿名函数对象（闭包），可赋值给 auto 或 std::function。泛型 Lambda（C++14）：参数类型用 auto。与 STL 算法配合：std::sort(..., [](auto a,auto b){...})、std::for_each、std::find_if。",
    "C++设计模式": "C++ 设计模式实践：单例模式（Meyer's Singleton：函数内 static 局部变量，C++11 线程安全）、工厂模式（Factory 创建对象，抽象工厂创建产品族）、观察者模式（信号槽机制如 Boost.Signals2）、策略模式（std::function 替代继承，运行时可切换算法）、CRTP（奇异递归模板模式：基类模板参数为子类，编译时多态，避免虚函数开销）。PIMPL 惯用法：将实现细节隐藏在 .cpp 文件中，减少头文件依赖和编译时间。",
    # Go 补充主题
    "Go测试": "Go 内置 testing 包：*_test.go 文件中的 TestXxx(t *testing.T) 函数是单元测试。go test 命令运行测试，-v 详细输出，-cover 覆盖率，-bench 基准测试（BenchmarkXxx(b *testing.B)）。Table-Driven Tests 是最佳实践：将测试用例存入结构体切片循环执行。t.Run() 子测试，t.Parallel() 并行测试。httptest 包 HTTP 测试，testify 第三方断言库。",
    "Go Context": "context 包在 goroutine 间传递截止时间、取消信号和请求范围值。context.Background() 根 context，context.WithCancel() 可取消、WithTimeout/WithDeadline 定时取消、WithValue 传值（仅用于请求范围的元数据）。ctx.Done() 返回只读 channel，取消时关闭。核心原则：Context 作为第一个参数，不存储在 struct 中，不要传 nil。典型场景：gRPC/HTTP 服务中请求链的超时控制和级联取消。",
    "Go反射": "reflect 包提供运行时类型检查能力。reflect.TypeOf() 获取类型信息（Name/Kind/NumField），reflect.ValueOf() 获取值并可修改（需传入指针且 Elem().CanSet()）。StructTag（`json:\"name\"`）通过反射读取。应用场景：JSON 编解码（encoding/json）、ORM 框架（GORM）、依赖注入库（wire/fx）。注意：反射性能较低，可读性差，不要过度使用——能用泛型（Go 1.18+）优先用泛型。",
    "Go GC": "Go 垃圾回收器（GC）是并发、三色标记-清除的追踪式 GC。特点：低延迟（目标 <1ms）、并发执行（STW 极短）、自动触发（堆大小增长触发 GOGC 阈值，默认 100%）。GOGC 环境变量调节 GC 频率（值越大 GC 越少但内存占用越）。逃逸分析：编译器在编译时判断变量是否\"逃逸\"到堆上——能分配在栈上的变量不需要 GC。pprof 分析 GC 性能，runtime.ReadMemStats 获取内存统计。",
    "Go网络编程": "net/http 包构建 HTTP 服务：http.HandleFunc 注册路由、http.ListenAndServe 启动服务。net 包 TCP/UDP 编程：net.Dial 连接、net.Listen 监听、conn.Read/Write 通信。goroutine per connection 模式：每个连接一个 goroutine 处理。中间件模式：func(http.Handler) http.Handler 包装，链式组合（日志/认证/限流）。WebSocket 用 gorilla/websocket，gRPC 用 google.golang.org/grpc。",
    "Go设计模式": "Go 设计模式遵循简洁哲学：Functional Options 模式（可变配置的最常见范式，如 `func WithTimeout(d time.Duration) Option`）、Pipeline 模式（channel 串联处理阶段，扇出扇入）、Worker Pool（固定数量 goroutine 消费 channel）、Decorator 模式（http.Handler 中间件包装）。依赖注入通过接口+构造函数实现，无需框架。Error Wrapping（fmt.Errorf(\"...: %w\", err)）创建错误链，errors.Is/As 判断错误类型。",
    # TypeScript 补充主题
    "TypeScript装饰器": "TypeScript 装饰器是特殊声明 @expression，可附加到类/方法/属性/参数上（实验性特性需 enableExperimentalDecorators）。类装饰器接收构造函数，可返回新构造函数替代原类。方法装饰器 (target, propertyKey, descriptor) 可修改方法行为。属性装饰器 (target, propertyKey)。NestJS 大量使用装饰器（@Controller/@Get/@Injectable），Angular（@Component/@Input）。装饰器的本质是元编程——在定义时修改或注解代码。",
    "TypeScript命名空间": "命名空间（namespace）将相关代码组织在一起，避免全局命名冲突。内部模块 namespace X { export class A {} } → 外部使用 X.A。三斜线指令 /// <reference path=\"...\" /> 声明文件间依赖。现代 TS 项目更多使用 ES Module（import/export）而非命名空间，因为 ESM 有更好的 Tree Shaking 和静态分析支持。declare namespace 为全局库（如 jQuery 的 $）提供类型声明。",
    "TypeScript高级类型": "TypeScript 高级类型系统特性：条件类型 T extends U ? X : Y（根据类型关系分派）、infer 关键字在条件类型中推断类型变量、模板字面量类型 `Hello ${string}`。映射类型 [K in keyof T] 遍历属性，配合 +/? 修饰符（+readonly/-?）。类型体操：DeepPartial 递归可选、Flatten 展平嵌套、DeepReadonly 递归只读。unknown vs any：unknown 安全（操作前需类型守卫），any 绕过类型检查。",
    "TypeScript异步": "TypeScript 中异步编程的类型安全：Promise<T> 泛型指定 resolve 类型、async 函数返回 Promise<T>（T 为 return 类型）。Axios 封装：axios.get<T>(url) 返回 Promise<AxiosResponse<T>>。类型守卫处理 API 响应：isMyType(response) 自定义守卫函数返回 response is MyType。错误处理最佳实践：catch 中 error 类型为 unknown，需 instanceof 检查或类型守卫。",
    "TypeScript设计模式": "TypeScript 中设计模式利用类型系统增强安全性：Builder 模式（链式调用，类型累积）、Adapter 模式（接口适配 + 类型兼容）、Repository 模式（泛型基类 BaseRepository<T>，CRUD 方法类型安全）。工厂模式配合 discriminated union（type + switch 穷举）。依赖注入：tsyringe/InversifyJS 提供 IoC 容器，构造器注入 + @injectable 装饰器。策略模式：用联合类型替代继承，函数式组合。",
    "TypeScript测试": "TypeScript 测试生态：Jest + ts-jest 是主流组合，支持类型检查的测试文件。vitest 是新一代测试框架（Vite 原生、速度快、兼容 Jest API）。类型测试工具：tsd（expectType<T> 编译时断言）、expect-type（更丰富的类型断言 API）。Mock 策略：jest.mock + MockedFunction<T> 类型化 mock、MSW（Mock Service Worker）拦截 HTTP 请求。Testing Library 测试 React 组件（render + screen.getByRole）。",
    # Rust 补充主题
    "Rust宏": "Rust 宏（Macro）在编译时生成代码，分为声明宏和过程宏。声明宏 macro_rules! 通过模式匹配和替换生成代码（如 vec![1,2,3]）。过程宏：#[derive] 自动实现 trait（如 #[derive(Debug)]）、属性宏（#[xxx]）修改标记项、函数式宏（xxx!()）类似声明宏但基于 TokenStream 更灵活。宏与函数的根本区别：宏在编译时展开，可接受可变数量/类型参数，可生成新的语法结构。",
    "Rust异步": "Rust async/.await 语法实现零成本异步编程。async fn 返回 impl Future 类型，.await 等待 Future 完成（不阻塞线程）。Future trait 核心是 poll 方法返回 Poll::Ready(T) 或 Poll::Pending。运行时选择：tokio（最流行，多线程 work-stealing）、async-std（标准库风格）。spawn 并发执行任务、JoinHandle 等待结果、select! 宏多路竞速。async move 闭包捕获所有权进入异步上下文。",
    "Rust Unsafe": "unsafe 关键字解封 Rust 的五种隐藏能力：①解引用裸指针(*const T/*mut T)；②调用 unsafe 函数（如 transmute 重新解释内存）；③访问或修改可变静态变量；④实现 unsafe trait（如 Send/Sync）；⑤访问 union 字段。unsafe 不关闭借用检查，只允许上述五类操作。通常将 unsafe 封装在安全抽象内（如 Vec 内部用 unsafe 操作裸指针，对外暴露安全 API）。FFI（Foreign Function Interface）调用 C 库必须 unsafe。",
    "Rust测试": "Rust 内置测试框架：#[test] 标记单元测试函数，cargo test 运行测试。#[cfg(test)] 模块隔离测试代码。断言宏：assert!（条件）、assert_eq!/assert_ne!（值比较需实现 PartialEq+Debug）、should_panic 验证 panic。集成测试在 tests/ 目录，每个文件为独立 crate。文档测试：/// 注释中的代码块被 cargo test 执行。基准测试（nightly）：#![feature(test)] + #[bench]。",
    "Rust模块系统": "Rust 模块系统组织代码：mod 声明模块，默认 src 目录下同名 .rs 文件或 mod.rs 目录结构。use 引入路径（use std::collections::HashMap）、super 引用父模块、crate 引用根。pub 控制可见性：pub 对外公开，pub(crate) 仅 crate 内可见，pub(super) 仅父模块可见，pub(in path) 指定路径可见。Cargo.toml 中 [dependencies] 引入外部 crate，package::module::item 使用。",
    "Rust设计模式": "Rust 设计模式受所有权系统影响：Newtype 模式（用元组结构体包装类型增加类型安全，如 struct Meters(u32)）、Builder 模式（链式调用 + Result 错误累积，Rust 常见库风格）、RAII（Drop trait 自动清理资源）、Typestate 模式（用类型参数标记状态，编译时保证正确调用顺序）。策略模式：Trait + 泛型约束实现零成本抽象。扩展方法模式：在自己 crate 中为外部类型实现自定义 trait（孤儿规则约束）。",
}

# Python 习题库（30+ 道，覆盖多主题和难度）
PYTHON_EXERCISES: list[dict[str, Any]] = [
    # ===== 数据类型 =====
    {
        "id": "ex_py_001",
        "question": "Python 中，以下哪个是可变数据类型？",
        "options": ["A) int", "B) str", "C) list", "D) tuple", "E) 我不清楚"],
        "answer": 2,
        "difficulty": "easy",
        "topic": "数据类型",
        "explanation": "list 是可变类型，可以原地修改元素。int、str、tuple 都是不可变类型。"
    },
    {
        "id": "ex_py_002",
        "question": "以下代码输出什么？\ntype(3.14) 的结果是？",
        "options": ["A) <class 'int'>", "B) <class 'float'>", "C) <class 'double'>", "D) <class 'number'>", "E) 我不清楚"],
        "answer": 1,
        "difficulty": "easy",
        "topic": "数据类型",
        "explanation": "Python 中带小数点的数字默认为 float 类型，没有 double 类型。"
    },
    {
        "id": "ex_py_003",
        "question": "以下代码输出什么？\nprint(bool([]))",
        "options": ["A) True", "B) False", "C) None", "D) 报错", "E) 我不清楚"],
        "answer": 1,
        "difficulty": "easy",
        "topic": "数据类型",
        "explanation": "空列表 [] 在布尔上下文中为 False。空字符串、空字典、0、None 同样为 False。"
    },
    # ===== 控制流 =====
    {
        "id": "ex_py_004",
        "question": "以下代码输出什么？\nfor i in range(3):\n    print(i, end=' ')",
        "options": ["A) 1 2 3", "B) 0 1 2", "C) 0 1 2 3", "D) 1 2", "E) 我不清楚"],
        "answer": 1,
        "difficulty": "easy",
        "topic": "控制流",
        "explanation": "range(3) 生成 0, 1, 2，不包含 3。"
    },
    {
        "id": "ex_py_005",
        "question": "以下代码输出什么？\nx = 10\nif x > 5:\n    print('A')\nelif x > 8:\n    print('B')\nelse:\n    print('C')",
        "options": ["A) A", "B) B", "C) C", "D) A B", "E) 我不清楚"],
        "answer": 0,
        "difficulty": "easy",
        "topic": "控制流",
        "explanation": "if-elif 中只会执行第一个满足条件的分支。x > 5 满足，输出 'A'，后面的 elif 和 else 不再执行。"
    },
    {
        "id": "ex_py_006",
        "question": "while 循环和 for 循环的区别，以下描述正确的是？",
        "options": [
            "A) while 不能遍历列表",
            "B) for 适用于已知循环次数，while 适用于条件循环",
            "C) while 比 for 快很多",
            "D) for 只能用于 range()",
            "E) 我不清楚"
        ],
        "answer": 1,
        "difficulty": "easy",
        "topic": "控制流",
        "explanation": "for 适合遍历可迭代对象（已知次数），while 根据条件控制循环（次数不确定）。"
    },
    # ===== 函数 =====
    {
        "id": "ex_py_007",
        "question": "以下代码输出什么？\ndef add(a, b=2):\n    return a + b\nprint(add(3))",
        "options": ["A) 报错", "B) 5", "C) 3", "D) None", "E) 我不清楚"],
        "answer": 1,
        "difficulty": "easy",
        "topic": "函数",
        "explanation": "参数 b 有默认值 2，调用 add(3) 时 a=3, b 使用默认值 2，结果为 5。"
    },
    {
        "id": "ex_py_008",
        "question": "以下代码输出什么？\ndef f(a, lst=[]):\n    lst.append(a)\n    return lst\nprint(f(1))\nprint(f(2))",
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
        "explanation": "Python 默认参数只在函数定义时求值一次，可变默认参数在多次调用间共享状态。"
    },
    {
        "id": "ex_py_009",
        "question": "*args 和 **kwargs 的作用是？",
        "options": [
            "A) 分别接收位置参数和关键字参数的打包",
            "B) *args 是列表，**kwargs 是集合",
            "C) 两者没有区别",
            "D) 只能用在类方法中",
            "E) 我不清楚"
        ],
        "answer": 0,
        "difficulty": "medium",
        "topic": "函数",
        "explanation": "*args 将多余的位置参数打包为元组，**kwargs 将多余的关键字参数打包为字典。"
    },
    # ===== 列表操作 =====
    {
        "id": "ex_py_010",
        "question": "以下代码输出什么？\narr = [1, 2, 3]\narr.append([4, 5])\nprint(len(arr))",
        "options": ["A) 3", "B) 4", "C) 5", "D) 报错", "E) 我不清楚"],
        "answer": 1,
        "difficulty": "easy",
        "topic": "列表操作",
        "explanation": "append 将整个 [4, 5] 作为一个元素添加到列表末尾，arr 变为 [1, 2, 3, [4, 5]]，长度为 4。"
    },
    {
        "id": "ex_py_011",
        "question": "以下哪个操作的时间复杂度是 O(1)？",
        "options": [
            "A) 在列表末尾 append",
            "B) 在列表头部 insert(0, x)",
            "C) 在列表中查找元素 x in lst",
            "D) 对列表排序 lst.sort()",
            "E) 我不清楚"
        ],
        "answer": 0,
        "difficulty": "medium",
        "topic": "列表操作",
        "explanation": "list.append 均摊 O(1)。insert(0) 需移动元素为 O(n)，查找 O(n)，排序 O(n log n)。"
    },
    {
        "id": "ex_py_012",
        "question": "列表推导式 [x*2 for x in range(5) if x % 2 == 0] 的结果是？",
        "options": ["A) [0, 2, 4, 6, 8]", "B) [0, 4, 8]", "C) [0, 1, 2, 3, 4]", "D) [0, 2, 4]", "E) 我不清楚"],
        "answer": 1,
        "difficulty": "easy",
        "topic": "列表操作",
        "explanation": "range(5) 中偶数有 0, 2, 4，乘以 2 得 0, 4, 8。"
    },
    # ===== 字典操作 =====
    {
        "id": "ex_py_013",
        "question": "以下代码是否会报错？\nd = {'a': 1}\nprint(d['b'])",
        "options": ["A) 输出 None", "B) 报 KeyError", "C) 输出 0", "D) 输出 False", "E) 我不清楚"],
        "answer": 1,
        "difficulty": "easy",
        "topic": "字典操作",
        "explanation": "访问不存在的 key 会触发 KeyError。用 d.get('b') 则返回 None（或指定默认值）。"
    },
    {
        "id": "ex_py_014",
        "question": "以下代码输出什么？\nd = {'x': 1, 'y': 2}\nprint(list(d.keys()))",
        "options": ["A) ['x', 'y']", "B) [1, 2]", "C) [('x', 1), ('y', 2)]", "D) 报错", "E) 我不清楚"],
        "answer": 0,
        "difficulty": "easy",
        "topic": "字典操作",
        "explanation": "dict.keys() 返回字典所有键的视图，list() 转为列表 ['x', 'y']。"
    },
    {
        "id": "ex_py_015",
        "question": "字典推导式 {k: v*2 for k, v in {'a': 1, 'b': 2}.items()} 的结果是？",
        "options": ["A) {'a': 2, 'b': 4}", "B) {'a': 1, 'b': 2}", "C) [('a', 2), ('b', 4)]", "D) 报错", "E) 我不清楚"],
        "answer": 0,
        "difficulty": "easy",
        "topic": "字典操作",
        "explanation": "字典推导式对每个键值对的值乘以 2，结果为 {'a': 2, 'b': 4}。"
    },
    # ===== 字符串 =====
    {
        "id": "ex_py_016",
        "question": "以下代码输出什么？\nprint('hello'.upper())",
        "options": ["A) 'hello'", "B) 'HELLO'", "C) 'Hello'", "D) 报错", "E) 我不清楚"],
        "answer": 1,
        "difficulty": "easy",
        "topic": "字符串",
        "explanation": "str.upper() 将字符串中所有字母转为大写。"
    },
    {
        "id": "ex_py_017",
        "question": "以下代码输出什么？\nprint('a,b,c'.split(','))",
        "options": ["A) 'a b c'", "B) ['a', 'b', 'c']", "C) ('a', 'b', 'c')", "D) 'abc'", "E) 我不清楚"],
        "answer": 1,
        "difficulty": "easy",
        "topic": "字符串",
        "explanation": "split(',') 按逗号分割字符串，返回列表 ['a', 'b', 'c']。"
    },
    {
        "id": "ex_py_018",
        "question": "f-string 格式化：name='Alice'; print(f'Hello {name}') 输出什么？",
        "options": ["A) Hello {name}", "B) Hello Alice", "C) 报错", "D) Hello name", "E) 我不清楚"],
        "answer": 1,
        "difficulty": "easy",
        "topic": "字符串",
        "explanation": "f-string（f'...'）会将花括号内的表达式求值并替换，输出 'Hello Alice'。"
    },
    # ===== 面向对象 =====
    {
        "id": "ex_py_019",
        "question": "以下代码输出什么？\nclass A:\n    def __init__(self):\n        self.x = 1\na = A()\nprint(a.x)",
        "options": ["A) 报错", "B) 1", "C) None", "D) A.x", "E) 我不清楚"],
        "answer": 1,
        "difficulty": "easy",
        "topic": "面向对象",
        "explanation": "__init__ 在实例化时自动调用，self.x = 1 设置实例属性，a.x 输出 1。"
    },
    {
        "id": "ex_py_020",
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
        "explanation": "__new__ 负责创建实例（分配内存），返回实例后 __init__ 负责初始化。"
    },
    {
        "id": "ex_py_021",
        "question": "@staticmethod 和 @classmethod 的区别是？",
        "options": [
            "A) 没有区别",
            "B) staticmethod 不接收类引用，classmethod 接收 cls 参数",
            "C) staticmethod 更快",
            "D) classmethod 不能被子类继承",
            "E) 我不清楚"
        ],
        "answer": 1,
        "difficulty": "medium",
        "topic": "面向对象",
        "explanation": "@staticmethod 不传递隐式参数；@classmethod 将类本身作为第一个参数 cls 传入。"
    },
    # ===== 异常处理 =====
    {
        "id": "ex_py_022",
        "question": "以下代码输出什么？\ntry:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print('error')\nfinally:\n    print('done')",
        "options": ["A) error", "B) done", "C) error\\ndone", "D) 报错", "E) 我不清楚"],
        "answer": 2,
        "difficulty": "easy",
        "topic": "异常处理",
        "explanation": "ZeroDivisionError 被捕获输出 'error'，finally 子句始终执行输出 'done'。"
    },
    {
        "id": "ex_py_023",
        "question": "捕获多个异常的正确语法是？",
        "options": [
            "A) except (ValueError, TypeError)",
            "B) except ValueError, TypeError",
            "C) except [ValueError, TypeError]",
            "D) except ValueError or TypeError",
            "E) 我不清楚"
        ],
        "answer": 0,
        "difficulty": "easy",
        "topic": "异常处理",
        "explanation": "使用元组捕获多个异常：except (ValueError, TypeError) as e。"
    },
    # ===== 文件IO =====
    {
        "id": "ex_py_024",
        "question": "使用 with open('test.txt', 'r') as f 的好处是？",
        "options": [
            "A) 读取速度更快",
            "B) 自动关闭文件，即使发生异常",
            "C) 可以同时读写",
            "D) 文件内容自动转为列表",
            "E) 我不清楚"
        ],
        "answer": 1,
        "difficulty": "easy",
        "topic": "文件IO",
        "explanation": "with 语句确保文件在代码块结束后自动关闭，无需手动调用 f.close()。"
    },
    {
        "id": "ex_py_025",
        "question": "以写入模式打开文件，如果文件已存在会怎样？",
        "options": [
            "A) 报错",
            "B) 清空原内容再写入",
            "C) 在末尾追加",
            "D) 自动重命名原文件",
            "E) 我不清楚"
        ],
        "answer": 1,
        "difficulty": "easy",
        "topic": "文件IO",
        "explanation": "'w' 模式会清空已有文件内容。'a' 模式在末尾追加，'x' 模式在文件存在时报错。"
    },
    # ===== 装饰器 =====
    {
        "id": "ex_py_026",
        "question": "装饰器的本质是什么？",
        "options": [
            "A) 一种特殊语法，只能用于类方法",
            "B) 一个接收函数并返回新函数的高阶函数",
            "C) 一种注释方式",
            "D) Python 内置的关键字",
            "E) 我不清楚"
        ],
        "answer": 1,
        "difficulty": "medium",
        "topic": "装饰器",
        "explanation": "装饰器本质是一个接收函数作为参数、返回新函数的高阶函数，用于在不修改原函数的情况下扩展功能。"
    },
    {
        "id": "ex_py_027",
        "question": "以下装饰器实现了什么功能？\ndef log(func):\n    def wrapper(*args, **kwargs):\n        print('调用', func.__name__)\n        return func(*args, **kwargs)\n    return wrapper",
        "options": [
            "A) 修改函数返回值",
            "B) 在函数调用前后打印日志",
            "C) 缓存函数结果",
            "D) 限制函数调用次数",
            "E) 我不清楚"
        ],
        "answer": 1,
        "difficulty": "medium",
        "topic": "装饰器",
        "explanation": "该装饰器在函数调用前打印函数名，然后执行原函数，实现了日志记录功能。"
    },
    # ===== 生成器 =====
    {
        "id": "ex_py_028",
        "question": "生成器函数与普通函数的区别是？",
        "options": [
            "A) 生成器使用 return，普通函数使用 yield",
            "B) 生成器使用 yield，可以暂停并恢复执行",
            "C) 没有区别",
            "D) 生成器不能接收参数",
            "E) 我不清楚"
        ],
        "answer": 1,
        "difficulty": "medium",
        "topic": "生成器",
        "explanation": "含 yield 的函数是生成器函数，调用返回生成器对象，每次 yield 暂停执行，下次迭代时恢复。"
    },
    {
        "id": "ex_py_029",
        "question": "生成器表达式 (x*2 for x in range(3)) 返回什么类型？",
        "options": ["A) list", "B) tuple", "C) generator", "D) set", "E) 我不清楚"],
        "answer": 2,
        "difficulty": "medium",
        "topic": "生成器",
        "explanation": "圆括号的推导式返回 generator 对象，惰性求值，节省内存。列表推导式用方括号。"
    },
    # ===== GIL/并发 =====
    {
        "id": "ex_py_030",
        "question": "Python 中 GIL（全局解释器锁）主要影响什么场景？",
        "options": [
            "A) 禁止使用多线程",
            "B) CPU 密集型任务的多线程无法利用多核",
            "C) 影响异步 I/O 性能",
            "D) 所有 Python 代码只能串行执行",
            "E) 我不清楚"
        ],
        "answer": 1,
        "difficulty": "hard",
        "topic": "GIL/并发",
        "explanation": "GIL 确保同一时刻只有一个线程执行 Python 字节码，CPU 密集型用多线程无法加速，I/O 密集型影响不大。"
    },
    {
        "id": "ex_py_031",
        "question": "对于 CPU 密集型任务，以下哪种方案最适合绕过 GIL？",
        "options": [
            "A) 使用更多线程",
            "B) 使用 multiprocessing 多进程",
            "C) 使用 asyncio",
            "D) 使用递归",
            "E) 我不清楚"
        ],
        "answer": 1,
        "difficulty": "hard",
        "topic": "GIL/并发",
        "explanation": "multiprocessing 创建独立进程，每个进程有独立的 GIL，可以真正利用多核 CPU。"
    },
    # ===== 常用库 =====
    {
        "id": "ex_py_032",
        "question": "Python 中处理 JSON 数据应使用哪个模块？",
        "options": ["A) os", "B) sys", "C) json", "D) re", "E) 我不清楚"],
        "answer": 2,
        "difficulty": "easy",
        "topic": "常用库",
        "explanation": "json 模块提供 json.dumps()（序列化）和 json.loads()（反序列化）等方法。"
    },
    {
        "id": "ex_py_033",
        "question": "使用 requests 库发送 GET 请求的正确方式是？",
        "options": [
            "A) requests.fetch('https://api.example.com')",
            "B) requests.get('https://api.example.com')",
            "C) requests.GET('https://api.example.com')",
            "D) requests.request('https://api.example.com')",
            "E) 我不清楚"
        ],
        "answer": 1,
        "difficulty": "easy",
        "topic": "常用库",
        "explanation": "requests.get(url) 发送 GET 请求，返回 Response 对象。"
    },
    {
        "id": "ex_py_034",
        "question": "Python 中 datetime 模块的 datetime.now() 返回什么？",
        "options": [
            "A) 当前时间戳（整数）",
            "B) 当前日期字符串",
            "C) 当前日期时间的 datetime 对象",
            "D) 当前时区",
            "E) 我不清楚"
        ],
        "answer": 2,
        "difficulty": "easy",
        "topic": "常用库",
        "explanation": "datetime.now() 返回包含当前日期和时间的 datetime 对象，可进一步格式化。"
    },
    {
        "id": "ex_py_035",
        "question": "使用 Python 的 os.path.join('a', 'b', 'c') 结果是什么？",
        "options": ["A) 'a/b/c' 或 'a\\\\b\\\\c'（取决于系统）", "B) ['a', 'b', 'c']", "C) 'abc'", "D) 报错", "E) 我不清楚"],
        "answer": 0,
        "difficulty": "easy",
        "topic": "常用库",
        "explanation": "os.path.join 使用系统适当的分隔符拼接路径，Linux 用 '/'，Windows 用 '\\'。"
    },
    # ===== Python 补充习题 (10道) =====
    {
        "id": "ex_py_036",
        "question": "以下代码输出什么？\nprint(any([0, False, None]))",
        "options": ["A) True", "B) False", "C) None", "D) 报错", "E) 我不清楚"],
        "answer": 1,
        "difficulty": "easy",
        "topic": "函数",
        "explanation": "any() 在可迭代对象中所有元素都为 False 时返回 False。0、False、None 都是假值。"
    },
    {
        "id": "ex_py_037",
        "question": "以下代码输出什么？\nprint(list(zip([1,2,3], ['a','b','c'])))",
        "options": ["A) [1, 2, 3, 'a', 'b', 'c']", "B) [(1, 'a'), (2, 'b'), (3, 'c')]", "C) {1: 'a', 2: 'b', 3: 'c'}", "D) 报错", "E) 我不清楚"],
        "answer": 1,
        "difficulty": "easy",
        "topic": "函数",
        "explanation": "zip() 将两个可迭代对象按位置配对，返回迭代器。list() 转为元组列表。"
    },
    {
        "id": "ex_py_038",
        "question": "以下代码输出什么？\ns = {x for x in range(5) if x % 2 == 0}\nprint(type(s).__name__)",
        "options": ["A) list", "B) set", "C) tuple", "D) generator", "E) 我不清楚"],
        "answer": 1,
        "difficulty": "easy",
        "topic": "数据类型",
        "explanation": "花括号 {x for x in ...} 是集合推导式，返回 set 类型。方括号是列表推导式，圆括号是生成器表达式。"
    },
    {
        "id": "ex_py_039",
        "question": "以下代码输出什么？\ndef f(a, b, /, c):\n    return a + b + c\nprint(f(1, 2, c=3))",
        "options": ["A) 6", "B) 报错", "C) 3", "D) 5", "E) 我不清楚"],
        "answer": 0,
        "difficulty": "medium",
        "topic": "函数",
        "explanation": "/ 表示前面的参数必须按位置传递（Python 3.8+）。a、b 位置传参，c 关键字传参。"
    },
    {
        "id": "ex_py_040",
        "question": "以下哪个操作不修改原列表？",
        "options": ["A) lst.sort()", "B) lst.reverse()", "C) sorted(lst)", "D) lst.append(4)", "E) 我不清楚"],
        "answer": 2,
        "difficulty": "medium",
        "topic": "列表操作",
        "explanation": "sorted(lst) 返回新列表，不修改原列表。sort()、reverse()、append() 都是原地修改。"
    },
    {
        "id": "ex_py_041",
        "question": "以下代码输出什么？\nd = {'a': 1, 'b': 2, 'c': 3}\nd.pop('b', None)\nprint(len(d))",
        "options": ["A) 2", "B) 3", "C) None", "D) 报错", "E) 我不清楚"],
        "answer": 0,
        "difficulty": "easy",
        "topic": "字典操作",
        "explanation": "dict.pop(key, default) 删除 key 并返回其值；key 不存在时返回 default。此处删除 'b' 后字典剩 2 项。"
    },
    {
        "id": "ex_py_042",
        "question": "以下代码输出什么？\nclass Parent:\n    def method(self):\n        return 'Parent'\nclass Child(Parent):\n    def method(self):\n        return super().method() + ' + Child'\nc = Child()\nprint(c.method())",
        "options": ["A) Parent", "B) Child", "C) Parent + Child", "D) 报错", "E) 我不清楚"],
        "answer": 2,
        "difficulty": "medium",
        "topic": "面向对象",
        "explanation": "super().method() 调用父类 method 返回 'Parent'，子类拼上 ' + Child'，结果为 'Parent + Child'。"
    },
    {
        "id": "ex_py_043",
        "question": "以下代码输出什么？\ntry:\n    raise ValueError('A')\nexcept ValueError:\n    print('B')\n    raise\nfinally:\n    print('C')",
        "options": ["A) B C", "B) B C + 异常", "C) C", "D) A B C", "E) 我不清楚"],
        "answer": 1,
        "difficulty": "medium",
        "topic": "异常处理",
        "explanation": "除捕获并打印 'B'，裸 raise 重新抛出原异常，finally 执行打印 'C'，最终异常传播出去。"
    },
    {
        "id": "ex_py_044",
        "question": "打开文件时使用 'a' 模式的含义是？",
        "options": ["A) 只读", "B) 覆盖写入", "C) 追加写入（不清空原有内容）", "D) 二进制读取", "E) 我不清楚"],
        "answer": 2,
        "difficulty": "easy",
        "topic": "文件IO",
        "explanation": "'a'（append）模式在文件末尾追加内容，不覆盖已有内容。'w' 是覆盖写入，'r' 是只读。"
    },
    {
        "id": "ex_py_045",
        "question": "以下代码输出什么？\nimport re\ntext = 'abc123def456'\nprint(re.findall(r'\\d+', text))",
        "options": ["A) []", "B) ['123456']", "C) ['123', '456']", "D) 报错", "E) 我不清楚"],
        "answer": 2,
        "difficulty": "medium",
        "topic": "常用库",
        "explanation": "re.findall(r'\\d+', text) 查找所有连续数字序列，返回 ['123', '456']。"
    },
]


def get_exercises(
    language: str = "python",
    topic: str | None = None,
    difficulty: str | None = None,
    count: int = 10,
) -> list[dict[str, Any]]:
    """按条件筛选题目并返回（不含 answer 字段）"""
    # 按语言选择习题库
    bank = ALL_EXERCISE_BANKS.get(language) or PYTHON_EXERCISES
    if not bank:
        bank = PYTHON_EXERCISES

    filtered = bank

    # 按主题筛选
    if topic and topic != "all":
        filtered = [q for q in filtered if q["topic"] == topic]

    # 按难度筛选
    if difficulty and difficulty != "all":
        filtered = [q for q in filtered if q["difficulty"] == difficulty]

    # 不足时随机补齐
    if len(filtered) < count:
        remaining = [q for q in bank if q not in filtered]
        needed = count - len(filtered)
        if remaining:
            extra = random.sample(remaining, min(needed, len(remaining)))
            filtered = filtered + extra

    # 截取所需数量并随机打乱
    selected = filtered[:count]
    random.shuffle(selected)

    # 去掉 answer 字段，并附上概念解释
    return [
        {**{k: v for k, v in q.items() if k != "answer"}, "concept": TOPIC_CONCEPTS.get(q["topic"], "")}
        for q in selected
    ]


def grade_exercises(
    language: str,
    answers_dict: dict[str, int],
) -> dict[str, Any]:
    """评分：返回正确数、每题详情"""
    bank = ALL_EXERCISE_BANKS.get(language) or PYTHON_EXERCISES
    if not bank:
        bank = PYTHON_EXERCISES
    bank_map = {q["id"]: q for q in bank}

    correct = 0
    total = len(answers_dict)
    details = []

    for qid, user_ans in answers_dict.items():
        q = bank_map.get(qid)
        if not q:
            continue
        is_unsure = user_ans == 4
        is_correct = (not is_unsure) and (user_ans == q["answer"])
        if is_correct:
            correct += 1
        details.append({
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
        })

    score = int(correct / total * 100) if total > 0 else 0

    # 按难度统计
    difficulty_stats: dict[str, dict] = {}
    topic_stats: dict[str, dict] = {}
    for d in details:
        diff = d["difficulty"]
        if diff not in difficulty_stats:
            difficulty_stats[diff] = {"total": 0, "correct": 0}
        difficulty_stats[diff]["total"] += 1
        if d["is_correct"]:
            difficulty_stats[diff]["correct"] += 1

        top = d["topic"]
        if top not in topic_stats:
            topic_stats[top] = {"total": 0, "correct": 0}
        topic_stats[top]["total"] += 1
        if d["is_correct"]:
            topic_stats[top]["correct"] += 1

    return {
        "score": score,
        "correct": correct,
        "total": total,
        "details": details,
        "difficulty_stats": difficulty_stats,
        "topic_stats": topic_stats,
    }
