"""编程知识库 — 概念、语法、最佳实践等通用编程知识的向量检索"""
import uuid
from rag.embedder import embedder
from rag.store import get_collection, KNOWLEDGE_BASE_COLLECTION as COLLECTION_NAME


class KnowledgeBase:
    def __init__(self):
        self.collection = get_collection(COLLECTION_NAME)

    def add(self, texts: list[str], metadatas: list[dict] | None = None) -> list[str]:
        ids = [str(uuid.uuid4()) for _ in texts]
        embeddings = embedder.embed(texts)
        self.collection.add(
            documents=texts,
            metadatas=metadatas or [{}] * len(texts),
            embeddings=embeddings,
            ids=ids
        )
        return ids

    def search(self, query: str, k: int = 5) -> list[dict]:
        qe = embedder.embed_query(query)
        results = self.collection.query(query_embeddings=[qe], n_results=k)
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

    def search_as_context(self, query: str, k: int = 3) -> str:
        results = self.search(query, k=k)
        if not results:
            return ""
        lines = []
        for i, r in enumerate(results, 1):
            source = r["metadata"].get("topic", "通用")
            lines.append(f"[知识 {i}] ({source})\n{r['content']}")
        return "\n\n".join(lines)

    def count(self) -> int:
        return self.collection.count()

    def reset(self):
        try:
            self.collection._client.delete_collection(name=COLLECTION_NAME)
        except Exception:
            pass
        self.collection = get_collection(COLLECTION_NAME)


SEED_KNOWLEDGE = [
    {"text": "闭包（Closure）是指一个函数可以记住并访问其词法作用域，即使该函数在其词法作用域之外执行。在Python中，闭包由嵌套函数实现：内部函数引用了外部函数的变量，且外部函数返回内部函数。常见用途：数据隐藏、回调函数、装饰器。", "topic": "闭包", "language": "python"},
    {"text": "Python装饰器（Decorator）是接受函数作参数并返回新函数的高阶函数，用于在不修改原函数代码的情况下添加新功能。语法糖：@decorator_name。常见装饰器：@staticmethod, @classmethod, @property, @functools.lru_cache。", "topic": "装饰器", "language": "python"},
    {"text": "Python列表推导式（List Comprehension）是创建列表的简洁语法：[表达式 for 变量 in 可迭代对象 if 条件]。相比for循环更简洁高效。嵌套推导式超过两层会降低可读性，此时应使用普通循环。", "topic": "列表推导式", "language": "python"},
    {"text": "Python生成器（Generator）是一种惰性求值的迭代器，使用yield关键字定义。优势：节省内存（按需生成而非一次性加载）、可表示无限序列。生成器表达式语法：(x*2 for x in range(10))。", "topic": "生成器", "language": "python"},
    {"text": "Python GIL（Global Interpreter Lock）是CPython中的互斥锁，确保同一时刻只有一个线程执行Python字节码。CPU密集型任务在多线程下无法利用多核优势。解决方案：多进程（multiprocessing）、异步编程（asyncio）、C扩展释放GIL。", "topic": "GIL", "language": "python"},
    {"text": "SOLID原则：S-单一职责、O-开闭原则（对扩展开放对修改关闭）、L-里氏替换、I-接口隔离、D-依赖倒置（依赖抽象而非具体实现）。", "topic": "SOLID", "language": "通用"},
    {"text": "时间复杂度 O(n) 表示算法执行时间随输入规模线性增长。常见复杂度排序：O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)。衡量的是增长率而非绝对时间。", "topic": "时间复杂度", "language": "通用"},
    {"text": "RESTful API 设计：使用名词作端点（GET /users）、HTTP方法表达操作、状态码语义化（200/201/400/404/500）、版本管理（/api/v1/）、分页参数（?page=1&size=20）。", "topic": "REST API", "language": "通用"},
    {"text": "Python asyncio 使用事件循环实现协作式多任务。async def 定义协程，await 挂起等待。适用I/O密集型任务。常用工具：asyncio.gather() 并发执行多个协程。", "topic": "asyncio", "language": "python"},
    {"text": "Git 分支策略：main（稳定版本）、develop（开发主线）、feature/xxx（功能分支）、hotfix/xxx（紧急修复）。常用工作流：Git Flow、GitHub Flow、Trunk-Based Development。", "topic": "Git", "language": "通用"},
    {"text": "数据库索引（Index）是加速数据检索的数据结构（B+树）。优点：提升查询速度。代价：额外存储，写入时需维护索引。最佳实践：为WHERE/JOIN/ORDER BY列建索引，避免低选择性列。", "topic": "数据库索引", "language": "通用"},
    {"text": "Python 上下文管理器通过 with 语句管理资源（文件、锁、连接），确保资源正确获取和释放。实现方式：__enter__/__exit__ 方法或 @contextmanager 装饰器。", "topic": "上下文管理器", "language": "python"},
    {"text": "Python *args 和 **kwargs：*args 将位置参数打包为元组，**kwargs 将关键字参数打包为字典。常用于装饰器和函数包装。", "topic": "可变参数", "language": "python"},
    {"text": "单例模式确保一个类只有一个实例。Python实现：模块级别变量、__new__方法控制、元类实现。多线程环境需考虑线程安全。", "topic": "单例模式", "language": "python"},
    {"text": "Python 异常处理：try/except/else/finally。最佳实践：捕获具体异常、不要用异常控制正常流程、自定义异常继承自Exception。", "topic": "异常处理", "language": "python"},
    {"text": "JavaScript Promise 表示异步操作的最终完成或失败。三种状态：pending/fulfilled/rejected。.then() 处理成功，.catch() 处理失败。async/await 是基于Promise的语法糖。", "topic": "Promise", "language": "javascript"},
    {"text": "JavaScript 事件循环：调用栈执行同步代码，异步任务由Web APIs处理，回调进入任务队列。微任务（Promise.then）优先于宏任务（setTimeout）。", "topic": "事件循环", "language": "javascript"},
    {"text": "TypeScript 类型系统：基础类型、联合类型、交叉类型、泛型、类型守卫、工具类型（Partial/Omit/Pick/Record）。interface可声明合并，type可定义复杂类型。", "topic": "TypeScript", "language": "typescript"},
    {"text": "React Hooks 规则：① 只在函数组件顶层调用；② 只在React函数组件或自定义Hook中调用。常用：useState/useEffect/useCallback/useMemo/useRef/useContext。", "topic": "React Hooks", "language": "javascript"},
    {"text": "二分查找（Binary Search）：在有序数组中每次将搜索范围减半，时间复杂度 O(log n)。mid = left + (right-left)//2 避免溢出。Python可用 bisect 模块。", "topic": "二分查找", "language": "python"},
    # ===== Java =====
    {"text": "Java 是静态强类型语言的代表，所有变量必须先声明类型。基本类型（int/long/double/boolean/char）存值，引用类型（String/数组/对象）存地址。基本类型与包装类（Integer/Long/Double）之间的自动装箱/拆箱是常见考点。", "topic": "Java基础", "language": "java"},
    {"text": "Java JVM 内存结构：堆（Heap）存放对象实例和数组，所有线程共享；栈（Stack）存放局部变量和方法调用帧，线程私有；方法区（Method Area）存放类信息/常量/静态变量；程序计数器记录当前执行位置。理解 JVM 内存是排查 OOM 的基础。", "topic": "JVM内存模型", "language": "java"},
    {"text": "Java 面向对象四大特性：封装（private/getter/setter 隐藏内部状态）、继承（extends，单继承，所有类继承自 Object）、多态（父类引用指向子类对象，运行时动态绑定方法）、抽象（abstract 类和接口 interface）。接口从 Java 8 起支持 default 方法实现。", "topic": "Java OOP", "language": "java"},
    {"text": "Java 集合框架核心接口：List（有序可重复，ArrayList/LinkedList）、Set（无序不可重复，HashSet/TreeSet）、Map（键值对，HashMap/TreeMap）。HashMap 底层是数组+链表+红黑树（JDK 8+），put/get 均摊 O(1)。ConcurrentHashMap 是线程安全的替代方案。", "topic": "Java集合", "language": "java"},
    {"text": "Java 异常体系：Throwable 下分 Error（严重系统错误，不要求处理）和 Exception（可处理的异常）。Exception 又分 RuntimeException（非受检，如 NPE/ArrayIndexOutOfBounds）和其他（受检异常，必须 try-catch 或 throws）。finally 块保证执行，即使 try 中有 return。", "topic": "Java异常", "language": "java"},
    {"text": "Java 多线程基础：创建线程（extends Thread 或 implements Runnable/Callable）。synchronized 实现互斥（对象锁/类锁），volatile 保证变量可见性和禁止指令重排。wait/notify/notifyAll 用于线程间通信，必须在 synchronized 块内调用。", "topic": "Java并发", "language": "java"},
    {"text": "Java 线程池（ThreadPoolExecutor）：核心参数包括 corePoolSize（常驻线程数）、maximumPoolSize（最大线程数）、keepAliveTime（空闲线程存活时间）、workQueue（任务队列）。推荐使用 Executors 工厂方法或直接构造 ThreadPoolExecutor，避免 OOM。", "topic": "Java线程池", "language": "java"},
    {"text": "Java 泛型（Generics）：编译期类型检查，运行时类型擦除（泛型信息在字节码中被擦除，替换为上限类型或 Object）。通配符：<?> 无界、<? extends T> 上界（生产者）、<? super T> 下界（消费者）。PECS 原则：Producer Extends, Consumer Super。", "topic": "Java泛型", "language": "java"},
    {"text": "Java Stream API（JDK 8+）：提供函数式数据处理管道。核心操作：filter/map/flatMap 为中间操作（惰性），collect/forEach/reduce 为终端操作（触发计算）。配合 Lambda 表达式可大幅简化集合操作代码。", "topic": "Java Stream", "language": "java"},
    {"text": "Spring Boot 核心特性：自动配置（@SpringBootApplication 包含 @EnableAutoConfiguration）、起步依赖（starter）、Actuator 监控端点、嵌入式 Servlet 容器（Tomcat/Jetty）。@RestController + @RequestMapping 快速构建 REST API，@Autowired 依赖注入。", "topic": "Spring Boot", "language": "java"},
    {"text": "Java equals() 与 hashCode() 约定：两个对象 equals 相等则 hashCode 必须相等；hashCode 相等时 equals 不一定相等。重写 equals 必须同时重写 hashCode。HashMap/HashSet 依赖此约定正确工作，Lombok @EqualsAndHashCode 可自动生成。", "topic": "equals与hashCode", "language": "java"},
    {"text": "Java 反射（Reflection）允许运行时获取类信息（Class.forName()）、访问私有字段和方法（setAccessible(true)）、动态创建实例。常用于框架开发（Spring DI、JUnit、ORM），但性能开销较大且破坏封装性，谨慎使用。", "topic": "Java反射", "language": "java"},
    # ===== C++ =====
    {"text": "C++ 指针与引用：指针（*）存储内存地址，可为空（nullptr），可重新赋值；引用（&）是变量的别名，必须初始化且不可更改引用对象。指针支持算术运算，引用语法更安全。现代 C++ 推荐优先使用引用和智能指针。", "topic": "指针与引用", "language": "cpp"},
    {"text": "C++ RAII（Resource Acquisition Is Initialization）是核心资源管理思想：资源获取即初始化，利用对象生命周期自动管理资源（内存、文件句柄、锁）。智能指针（unique_ptr/shared_ptr/weak_ptr）是 RAII 的典型应用，C++11 起应避免裸 new/delete。", "topic": "RAII与智能指针", "language": "cpp"},
    {"text": "C++ 内存管理：栈内存自动分配/释放（局部变量），堆内存需手动管理（new/delete）。Smart Pointers：unique_ptr 独占所有权不可拷贝，shared_ptr 引用计数共享所有权，weak_ptr 不影响引用计数用于打破循环引用。make_unique/make_shared 更高效、异常安全。", "topic": "C++内存管理", "language": "cpp"},
    {"text": "C++ STL（标准模板库）六大组件：容器（vector/ list/ map/ set/ unordered_map）、算法（sort/ find/ transform/ accumulate）、迭代器（iterator/ const_iterator/ reverse_iterator）、适配器（stack/ queue/ priority_queue）、函数对象（functor/ lambda）、分配器。", "topic": "C++ STL", "language": "cpp"},
    {"text": "C++ vector：动态数组，连续内存存储，随机访问 O(1)，尾部增删 O(1)，中间插入 O(n)。push_back 触发扩容时按 1.5~2 倍增长，可能导致迭代器失效。emplace_back 原地构造元素避免拷贝，reserve(n) 预分配避免多次扩容。", "topic": "vector", "language": "cpp"},
    {"text": "C++ 移动语义（C++11）：std::move 将左值转为右值引用（标记资源可转移），移动构造函数和移动赋值运算符通过\"窃取\"资源避免深拷贝。noexcept 声明移动操作可提升性能（如 vector 扩容时优先移动而非拷贝）。默认情况下编译器自动生成移动操作。", "topic": "移动语义", "language": "cpp"},
    {"text": "C++ 多态：编译时多态（模板 template，函数/运算符重载）+ 运行时多态（虚函数 virtual，纯虚函数=0 定义抽象基类）。虚函数通过 vtable（虚函数表）+ vptr（虚表指针）实现动态绑定。析构函数应为 virtual 以确保通过基类指针正确析构子类对象。", "topic": "C++多态", "language": "cpp"},
    {"text": "C++ 模板（Template）是泛型编程的核心：函数模板和类模板在编译期生成具体代码（代码膨胀但零运行时开销）。模板特化（全特化/偏特化）为特定类型提供定制实现。变参模板（C++11 variadic template）支持任意数量模板参数，用于可变参数列表。", "topic": "C++模板", "language": "cpp"},
    {"text": "C++ const 与 constexpr：const 声明运行时常量（不可修改），constexpr 声明编译期常量（可用于数组大小、模板参数等编译期上下文）。const 成员函数不能修改成员变量（mutable 例外），const 对象只能调用 const 成员函数。顶层 const 与底层 const 的区别是常见考点。", "topic": "const与constexpr", "language": "cpp"},
    {"text": "C++ 异常处理：try/throw/catch 机制。throw 抛出任意类型（推荐 std::exception 子类），catch 按类型匹配（按声明顺序，子类在前）。栈展开（stack unwinding）时自动调用局部对象的析构函数。noexcept 声明函数不抛异常（编译器可优化，但若抛出则调用 std::terminate）。", "topic": "C++异常处理", "language": "cpp"},
    {"text": "C++ 运算符重载：允许自定义类型使用 + - * / == << >> 等运算符。作为成员函数（左操作数是该类）或友元函数（左右对称）。不能重载的运算符：:: . .* ?: 。拷贝赋值 operator= 必须处理自赋值（或使用 copy-and-swap 惯用法）。", "topic": "运算符重载", "language": "cpp"},
    {"text": "C++ Lambda 表达式（C++11）：[捕获列表](参数列表) -> 返回类型 { 函数体 }。捕获方式：[]不捕获、[=]值捕获、[&]引用捕获、[this]捕获 this 指针。可为每个参数单独指定捕获方式：[=, &x] 表示 x 按引用捕获，其余按值。泛型 lambda（C++14）：(auto a, auto b) => a + b。", "topic": "Lambda", "language": "cpp"},
    # ===== Go =====
    {"text": "Go 语言的设计哲学：简洁、高效、并发优先。没有类和继承，通过 struct + 接口（隐式实现）达到多态。错误处理通过返回 error 值而非异常。gofmt 统一代码格式，`go mod` 管理依赖，编译速度极快，产物为静态链接的独立可执行文件。", "topic": "Go设计哲学", "language": "go"},
    {"text": "Go 并发核心：goroutine 是轻量级线程（~2KB 栈），由 Go 运行时调度，一条 `go func()` 即可启动。channel 是 goroutine 间的通信管道：chan 无缓冲通道同步阻塞、带缓冲通道异步非满不阻塞。select 语句多路监听多个 channel。\nCSP 哲学：通过通信来共享内存，而非通过共享内存来通信。", "topic": "Goroutine与Channel", "language": "go"},
    {"text": "Go 接口（Interface）是隐式实现的：类型只需实现接口定义的所有方法即自动满足该接口，无需显式声明 implements。空接口 interface{} 可接受任意类型（Go 1.18 起推荐用 any 别名）。类型断言：v, ok := x.(T)；类型选择：switch v := x.(type)。", "topic": "Go接口", "language": "go"},
    {"text": "Go 错误处理：函数返回 (result, error)，调用方必须检查 error != nil。fmt.Errorf(\"context: %w\", err) 包装错误并保留原始错误链（errors.Is/As 可解包）。defer + recover 可捕获 panic（类似 try-catch），但 Go 惯例是仅在不可恢复错误时 panic。", "topic": "Go错误处理", "language": "go"},
    {"text": "Go 数据结构和内置类型：数组 [n]T 固定长度、切片 []T 动态长度（底层数组 + len + cap）。map[T]T 无序键值对，通过 \", ok\" 惯用法安全取值。struct 定义复合类型，通过组合而非继承复用代码。Go 1.18 引入泛型（类型参数），支持泛型函数和类型约束。", "topic": "Go数据结构", "language": "go"},
    {"text": "Go 并发同步原语：sync.Mutex（互斥锁，Lock/Unlock）、sync.RWMutex（读写锁，读共享写互斥）、sync.WaitGroup（等待组，Add/Done/Wait，协调多个 goroutine）、sync.Once（确保函数只执行一次，常用于单例初始化）。sync/atomic 提供无锁原子操作。", "topic": "Go并发同步", "language": "go"},
    {"text": "Go 内存管理：自动垃圾回收（并发标记清除三色算法），栈内存自动管理。make() 用于 slice/map/chan 的初始化（分配并初始化底层结构），new(T) 仅分配零值内存返回 *T。逃逸分析决定变量分配在栈还是堆，影响 GC 压力。", "topic": "Go内存管理", "language": "go"},
    {"text": "Go 包管理与工程结构：go mod init 初始化模块，go mod tidy 整理依赖。标准工程布局：/cmd（入口）、/internal（私有包）、/pkg（公共库）、/api（协议定义）。大写字母开头的标识符为导出（public），小写为包内私有。init() 函数在包加载时自动执行。", "topic": "Go工程结构", "language": "go"},
    {"text": "Go context 包：context.Context 贯穿整个请求链路，携带 deadline、取消信号和请求范围的值。context.Background() 作为根上下文，context.WithCancel/WithTimeout/WithDeadline 派生可取消的子上下文。HTTP 请求的 r.Context() 在客户端断开时自动取消。", "topic": "Go Context", "language": "go"},
    {"text": "Go defer 机制：defer 语句将函数调用压入栈中，在外层函数返回前按 LIFO（后进先出）顺序执行。常用于资源释放（关闭文件、释放锁）、panic 恢复。注意：defer 的参数在声明时求值而非执行时。defer func() 闭包方式可访问最新变量值。", "topic": "Go defer", "language": "go"},
    {"text": "Go 标准库精选：net/http（HTTP 客户端与服务端）、encoding/json（JSON 编解码，通过 struct tag 控制字段映射）、database/sql（数据库操作接口，配合驱动使用）、testing（内置测试框架，Table-Driven Tests 是 Go 测试最佳实践）、time（时间处理，注意时区）。", "topic": "Go标准库", "language": "go"},
    {"text": "Go GC 调优：Go 的 GC 延迟目标 < 1ms（GOGC 控制 GC 触发阈值，默认 100 即堆增长 100% 触发）。减少 GC 压力的手段：对象复用（sync.Pool）、减少指针、预分配 slice/map 容量、使用值类型替代指针类型（减少堆分配）。pprof 可分析内存分配热点。", "topic": "Go GC调优", "language": "go"},
    # ===== JavaScript 补充 =====
    {"text": "JavaScript 原型链（Prototype Chain）：每个 JS 对象都有一个内部 [[Prototype]] 链接（通过 __proto__ 或 Object.getPrototypeOf() 访问）。属性查找沿原型链向上追溯，直到找到或返回 undefined。ES6 class 语法是原型继承的语法糖，底层仍是原型链。", "topic": "原型链", "language": "javascript"},
    {"text": "JavaScript this 绑定规则（优先级从高到低）：① new 绑定（this 指向新创建的对象）；② 显式绑定（call/apply/bind）；③ 隐式绑定（obj.fn() 中 this 指向 obj）；④ 默认绑定（严格模式 undefined，非严格模式 window/global）。箭头函数不绑定自己的 this，继承外层作用域的 this。", "topic": "this绑定", "language": "javascript"},
    {"text": "JavaScript 模块系统演进：CommonJS（Node.js 默认，require/module.exports，同步加载）、AMD（异步模块定义，浏览器端）、ESM（ES6 标准，import/export，静态分析、Tree Shaking 友好）。package.json 中 \"type\": \"module\" 启用 ESM。", "topic": "JS模块系统", "language": "javascript"},

    # ===== TypeScript 补充 =====
    {"text": "TypeScript 接口（Interface）与类型别名（Type Alias）对比：接口可被实现（implements）和扩展（extends），支持声明合并（同名接口自动合并）。类型别名可定义联合类型、交叉类型、元组，但不能被类 implements，也不能声明合并。默认优先使用 interface，需要联合/交叉/元组时用 type。", "topic": "Interface vs Type", "language": "typescript"},
    {"text": "TypeScript 泛型（Generics）允许创建可复用的组件：函数泛型 function identity<T>(arg: T): T、接口泛型 interface Box<T> { value: T }、类泛型 class Queue<T>。泛型约束用 extends：<T extends HasId>。默认类型参数：<T = string>。泛型在编译后擦除。", "topic": "TypeScript泛型", "language": "typescript"},
    {"text": "TypeScript 类型守卫（Type Guard）帮助在条件分支中缩小类型。内置守卫：typeof（'string'/'number'/'boolean'/'symbol'）、instanceof 判断原型链、in 操作符判断属性存在。自定义类型守卫：function isFish(pet: Fish | Bird): pet is Fish。as 断言强制类型转换，但无运行时检查。", "topic": "类型守卫", "language": "typescript"},
    {"text": "TypeScript 工具类型（Utility Types）精选：Partial<T> 全部可选、Required<T> 全部必填、Readonly<T> 全部只读、Pick<T,K> 选取部分属性、Omit<T,K> 排除部分属性、Record<K,T> 创建键值对象映射、Exclude<T,U> 联合排除、Extract<T,U> 联合提取、NonNullable<T> 排除 null/undefined、ReturnType<T> 获取函数返回值类型。", "topic": "TypeScript工具类型", "language": "typescript"},
    {"text": "TypeScript 装饰器（Decorator）是实验性功能（需开启 experimentalDecorators）：@decorator 语法在类、方法、属性、参数声明前应用。类装饰器接收构造函数；方法装饰器接收 (target, propertyKey, descriptor)。常用于元数据反射（reflect-metadata），Angular 和 NestJS 重度使用装饰器。", "topic": "TypeScript装饰器", "language": "typescript"},
    {"text": "TypeScript tsconfig.json 核心配置：compilerOptions.target 指定编译 JS 版本（ES6/ES2020 等）、module 指定模块系统（commonjs/esnext）、strict 启用全部严格检查、paths 路径别名映射、include/exclude 控制编译范围、outDir 输出目录。extends 继承其他配置文件。", "topic": "tsconfig配置", "language": "typescript"},
    {"text": "TypeScript 枚举（enum）：数字枚举默认从 0 递增，可手动设起始值。字符串枚举常量值，无自增。const enum 内联到使用处不生成对象，减少运行时开销。异构枚举（混用数字和字符串）不推荐。枚举的反向映射：数字枚举可通过值获取名称。", "topic": "TypeScript枚举", "language": "typescript"},
    {"text": "TypeScript 模块解析策略：classic（TypeScript 原始策略，非相对导入逐级向上查找 node_modules）和 node（模拟 Node.js 解析，查找 package.json types/main 字段、index.d.ts）。moduleResolution 在 tsconfig 中设置。TypeScript 也支持路径映射（paths + baseUrl）实现非相对导入。", "topic": "TypeScript模块解析", "language": "typescript"},
    {"text": "TypeScript 声明文件（.d.ts）：为已存在的 JS 库提供类型信息，不包含实现。通过 declare 关键字：declare module/var/function/class/namespace。@types 或 DefinitelyTyped 提供社区维护的类型定义包。三重斜线指令 /// <reference types=\"...\" /> 引用声明依赖。", "topic": "声明文件", "language": "typescript"},
    # ===== Rust =====
    {"text": "Rust 所有权（Ownership）是 Rust 最核心的特性，不用 GC 也不用手动管理内存。三条规则：①每个值有且仅有一个所有者（变量）；②值在任何时刻只能有一个所有者；③所有者离开作用域时值被 drop（释放）。所有权通过 move（赋值/传参会转移所有权）和 clone（深拷贝）操作控制。", "topic": "所有权", "language": "rust"},
    {"text": "Rust 借用（Borrowing）允许在不转移所有权的情况下使用值： &T 创建不可变引用（可多个同时存在）， &mut T 创建可变引用（独占，不可同时有其他引用）。借用规则：①任意时刻只能有一个可变引用或多个不可变引用；②引用必须始终有效（编译器检查生命周期）。引用默认不可变。", "topic": "借用与引用", "language": "rust"},
    {"text": "Rust 生命周期（Lifetime）标注用 'a 语法表示引用有效的作用域范围。目的：帮助编译器验证所有引用在其引用的数据有效时一直有效。函数签名中 fn longest<'a>(x: &'a str, y: &'a str) -> &'a str 表示返回值生命周期与较短参数的相同。生命周期标注不改变代码的运行时行为。", "topic": "生命周期", "language": "rust"},
    {"text": "Rust 错误处理：可恢复错误用 Result<T, E>（Ok(T) 成功 / Err(E) 失败），? 运算符自动传播 Err。不可恢复错误用 panic!（程序中止）。Option<T>（Some/None）表示值可能存在，用于替代 null。组合子：map、and_then、unwrap_or、ok_or 等链式处理。", "topic": "错误处理", "language": "rust"},
    {"text": "Rust 枚举（Enum）与模式匹配（Pattern Matching）：enum 可携带不同类型的数据（变体 + 关联数据）。match 穷举匹配所有变体，配合 if let 和 while let 简洁处理。Option<T> 和 Result<T,E> 是标准库最重要的枚举。模式匹配支持解构、守卫条件、绑定（@）。", "topic": "枚举与模式匹配", "language": "rust"},
    {"text": "Rust Trait（特征）定义共享行为，类似接口。通过 impl TraitName for TypeName 实现 Trait。Trait Bound <T: Trait> 约束泛型。常用标准 Trait：Display/ Debug（打印）、Clone/Copy（复制）、PartialEq/Eq（比较）、Iterator（迭代）、From/Into（转换）、Drop（析构）。孤儿规则：不能为外部类型实现外部 Trait。", "topic": "Trait与泛型约束", "language": "rust"},
    {"text": "Rust 智能指针：Box<T>（堆分配，用于递归类型和 trait object）、Rc<T>（单线程引用计数，不可变共享）、Arc<T>（多线程引用计数，原子操作）、RefCell<T>（运行时借用检查，内部可变性）、Cell<T>（Copy 类型的内部可变性）。Mutex<T> 和 RwLock<T> 提供线程间同步。", "topic": "智能指针", "language": "rust"},
    {"text": "Rust 并发模型：线程通过 std::thread::spawn 创建，消息传递用 mpsc::channel（多生产者单消费者：send/recv）。共享状态用 Arc<Mutex<T>> 或 Arc<RwLock<T>>。Send trait 标记类型可安全转移线程所有权，Sync trait 标记类型可安全跨线程共享引用。Rust 编译器在编译期防止数据竞争。", "topic": "并发与线程安全", "language": "rust"},
    {"text": "Rust Cargo 包管理：cargo new/build/run/test/check/clippy 是日常命令。Cargo.toml 定义包元数据和依赖（[dependencies]），Cargo.lock 锁定精确版本。Workspace 管理多 crate 项目。crates.io 是 Rust 的中央包仓库。features 支持条件编译和可选依赖。", "topic": "Cargo与工程化", "language": "rust"},
    {"text": "Rust 字符串：String 是可变、可增长的堆分配字符串（类似 Vec<u8>），&str 是字符串切片/引用（不可变）。str 是动态大小类型（DST），总是通过引用使用。字符串字面量是 &'static str。String 与 &str 互转：s.as_str() / String::from(&str) / &s[..]。注意字符串操作按字节而非字符（UTF-8 编码，中文字符占 3 字节）。", "topic": "字符串与集合", "language": "rust"},
    # ===== SQL =====
    {"text": "SQL JOIN 类型总结：INNER JOIN 取两表匹配行交集；LEFT JOIN 保留左表全部行（右表无匹配填 NULL）；RIGHT JOIN 保留右表全部行；FULL OUTER JOIN 保畾两表所有行；CROSS JOIN 笛卡尔积（每行组合）；SELF JOIN 表自连接（用别名区分）。ON 指定连接条件。", "topic": "JOIN", "language": "sql"},
    {"text": "SQL 聚合函数：COUNT(*) 计数、SUM 求和、AVG 平均值、MAX/MIN 最大最小值。通常配合 GROUP BY 分组使用。HAVING 对分组结果过滤。聚合函数忽略 NULL（COUNT(*) 除外）。窗口函数（OVER）在不合并行的情况下计算聚合。", "topic": "聚合函数", "language": "sql"},
    {"text": "SQL 子查询（Subquery）：SELECT 中的标量子查询（返回单值）、FROM 中的派生表、WHERE 中的 EXISTS / IN / ANY / ALL。关联子查询引用外部查询的列，每行重执行。EXISTS 通常比 IN 快（找到即停），NOT EXISTS 处理 NULL 更安全。", "topic": "子查询", "language": "sql"},
    {"text": "SQL 索引（Index）：B-Tree 索引加速 WHERE / JOIN / ORDER BY 查询，但减慢 INSERT/UPDATE/DELETE。复合索引最左前缀原则：WHERE 条件必须从索引最左列开始使用。覆盖索引：查询列全部在索引中避免回表。聚簇索引（主键索引）决定了数据的物理存储顺序。EXPLAIN 分析查询执行计划。", "topic": "索引", "language": "sql"},
    {"text": "SQL 事务（Transaction）ACID：Atomicity 原子性（全做或全不做）、Consistency 一致性（事务前后数据满足约束）、Isolation 隔离性（并发事务互不干扰）、Durability 持久性（提交后数据永固）。隔离级别：READ UNCOMMITTED / READ COMMITTED / REPEATABLE READ / SERIALIZABLE。问题：脏读/不可重复读/幻读。", "topic": "事务与隔离级别", "language": "sql"},
    {"text": "SQL DDL（数据定义语言）核心操作：CREATE TABLE/DATABASE/INDEX/VIEW、ALTER TABLE（ADD/DROP/MODIFY COLUMN、ADD CONSTRAINT）、DROP TABLE、TRUNCATE TABLE（清空数据保留结构）。约束：PRIMARY KEY、FOREIGN KEY、UNIQUE、NOT NULL、CHECK、DEFAULT。", "topic": "DDL与约束", "language": "sql"},
    {"text": "SQL 窗口函数（Window Function）：ROW_NUMBER() 行号、RANK() 排名（并列跳号）、DENSE_RANK() 排名（并列不跳号）、LAG/LEAD 前后行取值、SUM/AVG 移动聚合。OVER (PARTITION BY ... ORDER BY ...) 定义窗口范围，不改变行数。", "topic": "窗口函数", "language": "sql"},
    {"text": "SQL 查询优化基础：①SELECT 只取需要的列，避免 SELECT *；②为 WHERE/JOIN 条件列建索引；③用 EXPLAIN 分析执行计划找瓶颈（全表扫描/排序/临时表）；④小表驱动大表（小表放 JOIN 左边）；⑤子查询优化为 JOIN 或 EXISTS；⑥避免在 WHERE 中对列使用函数（导致索引失效）。", "topic": "SQL查询优化", "language": "sql"},
    {"text": "SQL 视图（View）是虚拟表，封装复杂查询供复用。CREATE VIEW v_name AS SELECT ...。物化视图（Materialized View）存储查询结果的物理副本，牺牲实时性换性能。视图可简化复杂查询、实现列级权限控制、隔离底层表结构变更。", "topic": "视图", "language": "sql"},
    {"text": "SQL 数据库设计范式：1NF（列不可再分，无重复组）、2NF（满足 1NF 且非主键列完全依赖于主键）、3NF（满足 2NF 且非主键列不传递依赖于主键）。反范式化：有意引入冗余以提升查询性能（如缓存计数值）。设计时权衡归一与查询性能。", "topic": "数据库设计", "language": "sql"},
]

knowledge_base = KnowledgeBase()
