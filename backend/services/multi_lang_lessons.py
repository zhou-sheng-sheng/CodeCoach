"""
多语言课程数据：为每种非 Python 语言提供完整的课程内容（每主题 2+ 节课）。
与 multi_lang_exercises.py 中的习题数据配合使用。
"""

# ================================================================
# TypeScript 课程（10 个主题，每主题 2 节课）
# ================================================================
TS_LEARNING_PATH = [
    {
        "topic": "TypeScript基础",
        "lessons": [
            {
                "id": "lesson_ts_TypeScript基础_1",
                "title": "类型注解入门",
                "topic": "TypeScript基础",
                "content": (
                    "TypeScript 是 JavaScript 的超集，核心特性就是在 JS 之上添加了静态类型系统。"
                    "类型注解用冒号语法：`let name: string = 'Alice'`，告诉编译器变量的预期类型。"
                    "基本类型包括：string / number / boolean / null / undefined / symbol / bigint。"
                    "数组类型用 `T[]` 或 `Array<T>`，元组用 `[T1, T2]` 固定长度和类型。"
                    "枚举 enum 定义命名常量集合，`any` 绕过类型检查（尽量少用），`unknown` 是安全的 any（使用前必须类型收窄）。"
                    "`void` 表示函数无返回值，`never` 表示永远不返回（抛异常或死循环）。"
                    "TypeScript 编译器会自动推断类型，大部分场景不需要显式注解。"
                    "`tsc --init` 初始化 tsconfig.json 配置文件，`tsc` 编译 .ts 为 .js。"
                ),
                "examples": [
                    "// 基本类型注解\nlet name: string = \"Alice\";\nlet age: number = 25;\nlet isActive: boolean = true;\nlet items: string[] = [\"a\", \"b\"];\nlet tuple: [string, number] = [\"ok\", 200];",
                    "// unknown vs any\nlet u: unknown = \"hello\";\n// u.toUpperCase();  // Error: unknown 不能直接操作\nif (typeof u === \"string\") {\n    u.toUpperCase();  // OK: 类型收窄后\n}\nlet a: any = \"hello\";\na.toUpperCase();  // OK, 但失去了类型安全（运行时可能报错）",
                    "// never 类型\nfunction throwError(msg: string): never {\n    throw new Error(msg);\n}\nfunction infiniteLoop(): never {\n    while (true) {}\n}"
                ],
                "key_points": [
                    "类型注解用 `: 类型` 语法，基本类型有 string/number/boolean 等",
                    "unknown 是安全版的 any，使用前必须类型收窄",
                    "void=无返回值，never=永不返回，编译器会自动类型推断",
                ],
            },
            {
                "id": "lesson_ts_TypeScript基础_2",
                "title": "接口与类型别名",
                "topic": "TypeScript基础",
                "content": (
                    "接口（interface）和类型别名（type）是定义对象形状的两种方式。"
                    "interface 定义对象的结构契约，可以声明属性、可选属性（?）、只读属性（readonly）。"
                    "interface 支持 extends 继承，多个同名的 interface 会自动合并（Declaration Merging），这是它与 type 的关键区别。"
                    "type 别名更灵活：可以定义联合类型（`type Status = 'success' | 'error'`）、交叉类型（`type A = B & C`）、"
                    "元组、函数签名等，但不能被 extends 或声明合并。"
                    "选择建议：定义对象形状优先用 interface，需要联合/交叉/元组类型时用 type。"
                    "索引签名 `[key: string]: T` 允许任意 key 的动态属性，适用于不确定属性名的场景。"
                ),
                "examples": [
                    "// interface 定义对象形状\ninterface User {\n    readonly id: number;\n    name: string;\n    email?: string;  // 可选属性\n}\nconst u: User = { id: 1, name: \"Alice\" };\n// u.id = 2;  // Error: readonly",
                    "// interface 继承\ninterface Admin extends User {\n    role: \"admin\" | \"superadmin\";\n    permissions: string[];\n}\nconst admin: Admin = { id: 1, name: \"Bob\", role: \"admin\", permissions: [\"read\"] };",
                    "// type 联合与交叉\ntype Status = \"pending\" | \"success\" | \"error\";\ntype Timestamped = { createdAt: Date; updatedAt: Date };\ntype UserRecord = User & Timestamped;  // 交叉类型",
                ],
                "key_points": [
                    "interface 定义对象结构，支持 extends 和声明合并",
                    "type 更灵活（联合/交叉/元组），但不能声明合并",
                    "对象形状优先用 interface，联合类型/工具类型用 type",
                ],
            },
        ],
    },
    {
        "topic": "TypeScript类型系统",
        "lessons": [
            {
                "id": "lesson_ts_TypeScript类型系统_1",
                "title": "联合与交叉类型",
                "topic": "TypeScript类型系统",
                "content": (
                    "联合类型（Union Types）用 `|` 表示「或」关系：`string | number` 表示值可以是 string 或 number。"
                    "访问联合类型的成员时，只能访问所有类型共有的成员。通过类型守卫（typeof / instanceof / in）收窄后才能访问特定类型的成员。"
                    "字面量联合类型 `type Direction = 'left' | 'right' | 'up' | 'down'` 常用于限定合法值范围。"
                    "交叉类型（Intersection Types）用 `&` 表示「且」关系：`A & B` 必须同时满足 A 和 B。"
                    "常用于组合多个类型：混入（Mixin）模式、组合接口、扩展已有类型。"
                    "联合类型和交叉类型的区别：联合是「或」，值属于其中任一；交叉是「且」，值必须满足所有。"
                ),
                "examples": [
                    "// 联合类型\nfunction pad(value: string | number) {\n    if (typeof value === \"number\") {\n        return \"0\".repeat(value);  // 收窄为 number\n    }\n    return value.padStart(10, \"0\");  // 收窄为 string\n}\n\n// 字面量联合\nfunction move(direction: \"left\" | \"right\" | \"up\" | \"down\") {\n    console.log(`Moving ${direction}`);\n}\nmove(\"left\");  // OK\n// move(\"diagonal\");  // Error",
                    "// 交叉类型\ninterface Nameable { name: string }\ninterface Ageable { age: number }\ntype Person = Nameable & Ageable;\nconst p: Person = { name: \"Alice\", age: 25 };  // 必须同时有 name 和 age",
                ],
                "key_points": [
                    "`|` 联合类型：值属于其中任一，`&` 交叉类型：值满足所有",
                    "联合类型通过类型守卫（typeof/instanceof/in）收窄后使用",
                    "字面量联合常用于枚举替代和约束合法值",
                ],
            },
            {
                "id": "lesson_ts_TypeScript类型系统_2",
                "title": "类型守卫与收窄",
                "topic": "TypeScript类型系统",
                "content": (
                    "类型守卫（Type Guards）是 TypeScript 的核心机制，让编译器在特定代码块中自动收窄变量类型。"
                    "内置守卫：`typeof` 检查原始类型（string/number/boolean/symbol/undefined）、`instanceof` 检查类实例、"
                    "`in` 操作符检查属性存在性。`Array.isArray()` 收窄数组类型。"
                    "自定义守卫：函数返回 `arg is Type` 类型谓词，让编译器信任你的判断。"
                    "判别联合（Discriminated Union）：多个类型共享一个字面量字段（tag），switch/if 该字段后自动收窄。"
                    "这是 Redux action、API 响应等场景的最佳类型安全方案。"
                    "`assertNever()` 模式：在 switch 的 default 分支使用 `assertNever(value)` 确保穷举检查。"
                ),
                "examples": [
                    "// 自定义类型守卫\ninterface Cat { meow(): void; furColor: string }\ninterface Dog { bark(): void; breed: string }\ntype Pet = Cat | Dog;\n\nfunction isCat(pet: Pet): pet is Cat {\n    return (pet as Cat).meow !== undefined;\n}\n\nfunction handle(pet: Pet) {\n    if (isCat(pet)) pet.meow();   // 收窄为 Cat\n    else pet.bark();              // 收窄为 Dog\n}",
                    "// 判别联合\ninterface Success { status: \"success\"; data: string }\ninterface Error   { status: \"error\";   code: number }\ntype Result = Success | Error;\n\nfunction handleResult(r: Result) {\n    switch (r.status) {\n        case \"success\": return r.data;  // 收窄为 Success\n        case \"error\":   return r.code;  // 收窄为 Error\n    }\n}",
                ],
                "key_points": [
                    "typeof / instanceof / in 是内置类型守卫",
                    "自定义守卫 `arg is Type` 让编译器信任你的类型判断",
                    "判别联合 = 共享字面量 tag，switch 后自动收窄",
                ],
            },
        ],
    },
    {
        "topic": "TypeScript泛型",
        "lessons": [
            {
                "id": "lesson_ts_TypeScript泛型_1",
                "title": "泛型基础",
                "topic": "TypeScript泛型",
                "content": (
                    "泛型（Generics）让函数、类、接口在保持类型安全的同时支持多种类型。用 `<T>` 声明类型参数。"
                    "泛型函数：`function identity<T>(arg: T): T { return arg }`，调用时 `identity<string>('hello')`，通常编译器能自动推断。"
                    "泛型约束（`extends`）：`<T extends HasLength>` 限制 T 必须满足某个接口，可用在泛型体内访问约束类型的方法。"
                    "多个类型参数：`function pair<T, U>(a: T, b: U): [T, U]`。泛型接口和泛型类同样支持。"
                    "默认泛型参数：`<T = string>` 在未指定时使用默认类型。"
                    "泛型的核心价值：不丢失类型信息——如果用 any，返回值类型也会变成 any；用泛型则保留了类型推导链。"
                ),
                "examples": [
                    "// 泛型函数\nfunction first<T>(arr: T[]): T {\n    return arr[0];\n}\nconst n = first([1, 2, 3]);    // n: number（自动推断）\nconst s = first(['a', 'b']);   // s: string",
                    "// 泛型约束\ninterface Lengthwise { length: number }\nfunction logLen<T extends Lengthwise>(arg: T): T {\n    console.log(arg.length);  // OK: T 必有 length\n    return arg;\n}\nlogLen(\"hello\");     // 5\nlogLen([1, 2, 3]);   // 3\n// logLen(123);       // Error: number 没有 length",
                    "// 泛型接口\ninterface Box<T> {\n    value: T;\n    getValue(): T;\n}\nconst stringBox: Box<string> = { value: \"hello\", getValue() { return this.value } };",
                ],
                "key_points": [
                    "`<T>` 声明类型参数，调用时可自动推断",
                    "`<T extends Constraint>` 添加约束，访问约束类型的成员",
                    "泛型保留类型推导链，避免 any 的类型信息丢失",
                ],
            },
            {
                "id": "lesson_ts_TypeScript泛型_2",
                "title": "泛型高级用法",
                "topic": "TypeScript泛型",
                "content": (
                    "泛型约束的进阶技巧：`keyof T` 获取 T 的所有属性名联合，常用于限制参数必须是对象的 key。"
                    "`T[K]` 索引访问类型，获取 T 中 K 对应的属性类型。"
                    "泛型在 React 中广泛应用：`useState<number>(0)` 类型化 state、`useRef<HTMLInputElement>(null)` 类型化 ref、"
                    "泛型组件 `<T>(props: Props<T>)` 传递类型参数。"
                    "`infer` 关键字在条件类型中推断类型变量，如 `type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never`。"
                    "`extends` 在泛型中同时作为约束和条件判断，理解上下文中的不同作用很重要。"
                ),
                "examples": [
                    "// keyof 和索引访问\nfunction getProp<T, K extends keyof T>(obj: T, key: K): T[K] {\n    return obj[key];\n}\nconst user = { name: \"Alice\", age: 25 };\nconst name = getProp(user, \"name\");  // name: string\nconst age = getProp(user, \"age\");    // age: number\n// getProp(user, \"email\");            // Error: 'email' 不是 user 的 key",
                    "// React 中的泛型\nimport { useState, useRef } from 'react';\nconst [count, setCount] = useState<number>(0);\nconst inputRef = useRef<HTMLInputElement>(null);\n// inputRef.current?.focus();  // 类型安全",
                    "// infer 推断类型\n// 内置 ReturnType：\ntype MyReturnType<T> = T extends (...args: any[]) => infer R ? R : never;\ntype FnReturn = MyReturnType<() => string>;  // string",
                ],
                "key_points": [
                    "`keyof T` 获取所有属性名，`T[K]` 索引访问属性类型",
                    "React 中 useState<Type>/useRef<Type> 是泛型最常见的实践",
                    "`infer` 在条件类型中推断类型变量，是内置工具类型的实现基础",
                ],
            },
        ],
    },
    {
        "topic": "TypeScript工程化",
        "lessons": [
            {
                "id": "lesson_ts_TypeScript工程化_1",
                "title": "tsconfig 配置详解",
                "topic": "TypeScript工程化",
                "content": (
                    "`tsconfig.json` 是 TypeScript 项目的配置文件，`tsc --init` 自动生成。"
                    "核心编译选项：`target`（输出 JS 版本，如 ES2022）、`module`（模块系统，ESNext/CommonJS）、"
                    "`strict`（启用所有严格检查，强烈推荐开启）、`outDir`（输出目录）、`rootDir`（源码根目录）。"
                    "`paths` 配置模块别名（配合 webpack/vite 的 alias），`include/exclude` 控制编译范围。"
                    "`strict` 子选项：`strictNullChecks`（null/undefined 不赋值给其他类型）、"
                    "`noImplicitAny`（禁止隐式 any）、`strictFunctionTypes`（严格函数类型检查）。"
                    "多个 `tsconfig.json` 可用 `extends` 继承基础配置，`references` 实现项目引用（monorepo）。"
                ),
                "examples": [
                    "// tsconfig.json 典型配置\n{\n  \"compilerOptions\": {\n    \"target\": \"ES2022\",\n    \"module\": \"ESNext\",\n    \"moduleResolution\": \"bundler\",\n    \"strict\": true,\n    \"noImplicitAny\": true,\n    \"strictNullChecks\": true,\n    \"outDir\": \"./dist\",\n    \"rootDir\": \"./src\",\n    \"declaration\": true,\n    \"sourceMap\": true\n  },\n  \"include\": [\"src/**/*.ts\"],\n  \"exclude\": [\"node_modules\", \"dist\"]\n}",
                ],
                "key_points": [
                    "`strict: true` 启用全部严格检查，新项目必须开启",
                    "`target/module/outDir/rootDir` 是核心输出控制选项",
                    "`extends` 继承配置，`references` 支持 monorepo 项目引用",
                ],
            },
            {
                "id": "lesson_ts_TypeScript工程化_2",
                "title": "构建工具集成与 Lint",
                "topic": "TypeScript工程化",
                "content": (
                    "TypeScript 与构建工具集成：Vite 内置 ts 支持（@vitejs/plugin-vue 或直接处理 .tsx），"
                    "Webpack 用 ts-loader 或 babel-loader + @babel/preset-typescript，"
                    "esbuild（通过 vite/webpack/esbuild-loader）极速编译。"
                    "代码规范：ESLint + @typescript-eslint/parser + @typescript-eslint/eslint-plugin 替代 TSLint（已废弃）。"
                    "配合 Prettier 自动格式化，husky + lint-staged 在 git commit 前自动检查和格式化。"
                    "声明文件 .d.ts 为 JS 库提供类型信息。DefinitelyTyped 社区提供 @types/xxx 包。"
                    "如果不满足，可在项目中自定义 `global.d.ts` 补充全局类型声明。"
                ),
                "examples": [
                    "// Vite + TypeScript 配置（vite.config.ts）\nimport { defineConfig } from 'vite';\nimport react from '@vitejs/plugin-react';\n\nexport default defineConfig({\n    plugins: [react()],  // 自动处理 .tsx\n    resolve: {\n        alias: { '@': '/src' }  // 路径别名\n    }\n});",
                    "// .d.ts 声明文件示例\n// calendar.d.ts\nexport function getDaysInMonth(year: number, month: number): number;\nexport function isLeapYear(year: number): boolean;",
                ],
                "key_points": [
                    "Vite 原生支持 TS，Webpack 用 ts-loader 或 babel-loader",
                    "ESLint + @typescript-eslint 替代已废弃的 TSLint",
                    ".d.ts 声明文件 + @types/xxx 为 JS 库提供类型支持",
                ],
            },
        ],
    },
    {
        "topic": "TypeScript装饰器",
        "lessons": [
            {
                "id": "lesson_ts_TypeScript装饰器_1",
                "title": "类与方法装饰器",
                "topic": "TypeScript装饰器",
                "content": (
                    "装饰器是 TypeScript 的实验性特性（需启用 `experimentalDecorators`），用 `@expression` 语法注解和修改类及其成员。"
                    "类装饰器：`function decorator(constructor: Function)` 或 `function decorator<T extends new(...args: any[]) => any>(target: T)`。"
                    "可以返回新构造函数替代原类，或在原型上添加方法/属性。"
                    "方法装饰器：`(target, propertyKey, descriptor) => void | PropertyDescriptor`。"
                    "通过修改 descriptor.value 可以拦截和增强方法调用（日志、计时、权限检查）。"
                    "NestJS 框架大量使用装饰器（@Controller、@Get、@Injectable），Angular 使用 @Component、@Input。"
                    "装饰器的本质是元编程——在定义时修改代码行为，不影响运行时逻辑。"
                ),
                "examples": [
                    "// 类装饰器\nfunction sealed(constructor: Function) {\n    Object.seal(constructor);\n    Object.seal(constructor.prototype);\n}\n\n@sealed\nclass Greeter {\n    greeting: string;\n    constructor(message: string) {\n        this.greeting = message;\n    }\n}",
                    "// 方法装饰器：日志\nfunction log(target: any, key: string, descriptor: PropertyDescriptor) {\n    const original = descriptor.value;\n    descriptor.value = function (...args: any[]) {\n        console.log(`Calling ${key} with`, args);\n        return original.apply(this, args);\n    };\n}\n\nclass Calculator {\n    @log\n    add(a: number, b: number): number {\n        return a + b;\n    }\n}",
                ],
                "key_points": [
                    "装饰器是实验性特性，需 `experimentalDecorators: true`",
                    "类装饰器接收构造函数，可返回新构造；方法装饰器可修改 descriptor",
                    "NestJS/Angular 大量使用装饰器驱动框架功能",
                ],
            },
            {
                "id": "lesson_ts_TypeScript装饰器_2",
                "title": "属性与参数装饰器",
                "topic": "TypeScript装饰器",
                "content": (
                    "属性装饰器：`(target, propertyKey) => void`，不能直接修改属性值（因为属性在原型上是 undefined），"
                    "但可以用 `Reflect.defineMetadata()` 附加元数据，配合其他装饰器在运行时读取。"
                    "参数装饰器：`(target, propertyKey, parameterIndex) => void`，标记方法参数的位置和类型。"
                    "装饰器工厂：返回装饰器函数的函数，支持传参，如 `@Route('users')`。"
                    "装饰器执行顺序：参数装饰器 → 方法装饰器 → 访问器装饰器 → 属性装饰器 → 类装饰器，"
                    "多个同类型装饰器从下往上执行（靠近定义的后执行）。同一位置多个装饰器从下到上。"
                    "装饰器组合示例：`@Validate() @Log() @Cache(60)` 按从下到上顺序执行。"
                ),
                "examples": [
                    "// 装饰器工厂：带参数\nfunction Route(path: string) {\n    return function (constructor: Function) {\n        Reflect.defineMetadata('path', path, constructor);\n    };\n}\n\n@Route('/users')\nclass UsersController {\n    // ...\n}",
                    "// 参数装饰器\nfunction Required(target: any, key: string, index: number) {\n    const requiredParams: number[] = Reflect.getOwnMetadata('required', target, key) || [];\n    requiredParams.push(index);\n    Reflect.defineMetadata('required', requiredParams, target, key);\n}\n\nclass Service {\n    greet(@Required name: string) {\n        return `Hello ${name}`;\n    }\n}",
                ],
                "key_points": [
                    "属性装饰器通过 Reflect Metadata 附加元数据",
                    "装饰器工厂 = 返回装饰器的函数，支持传参定制",
                    "执行顺序：参数→方法→属性→类，同类型从下往上",
                ],
            },
        ],
    },
    {
        "topic": "TypeScript命名空间",
        "lessons": [
            {
                "id": "lesson_ts_TypeScript命名空间_1",
                "title": "命名空间组织代码",
                "topic": "TypeScript命名空间",
                "content": (
                    "命名空间（namespace）将相关代码组织在一起，避免全局命名冲突。"
                    "语法：`namespace MyModule { export class A {} }`，外部通过 `MyModule.A` 访问。"
                    "嵌套命名空间：`namespace A.B.C` 或 namespace 内定义子 namespace。"
                    "`import x = Namespace.ClassName` 为命名空间成员创建别名，简化引用。"
                    "命名空间可以跨多个文件——同名 namespace 会自动合并（与 interface 的声明合并类似）。"
                    "现代 TS 项目中，ES Module（import/export）已取代命名空间成为主流组织方式，"
                    "因为 ESM 有更好的 Tree Shaking、静态分析和依赖管理。"
                    "命名空间主要用于：全局库的类型声明（如 jQuery 的 `$`）、遗留代码迁移、文件间类型共享。"
                ),
                "examples": [
                    "// 命名空间定义\nnamespace Utils {\n    export function formatDate(date: Date): string {\n        return date.toISOString().split('T')[0];\n    }\n    export const VERSION = '1.0.0';\n}\n\nconsole.log(Utils.formatDate(new Date()));  // 2024-01-15",
                    "// 嵌套命名空间\nnamespace App.Models {\n    export class User {\n        constructor(public name: string) {}\n    }\n}\nnamespace App.Services {\n    import User = App.Models.User;\n    export class UserService {\n        getUser(): User { return new User('Alice'); }\n    }\n}",
                ],
                "key_points": [
                    "`namespace` 组织代码防命名冲突，`export` 暴露成员",
                    "同名 namespace 自动合并，支持嵌套和多文件",
                    "现代项目优先用 ES Module，命名空间用于类型声明和遗留代码",
                ],
            },
            {
                "id": "lesson_ts_TypeScript命名空间_2",
                "title": "声明文件与三斜线指令",
                "topic": "TypeScript命名空间",
                "content": (
                    "声明文件（.d.ts）为 JavaScript 库提供类型信息，让 TS 项目可以安全使用 JS 库。"
                    "`declare` 关键字声明全局变量、函数、类、命名空间的存在而不提供实现。"
                    "三斜线指令 `/// <reference path=\"...\" />` 声明文件间依赖关系（主要用于 .d.ts 文件）。"
                    "`/// <reference types=\"...\" />` 引用 @types 包的类型。"
                    "`declare global` 扩展全局作用域，`declare module 'xxx'` 为第三方模块补充或覆盖类型。"
                    "模块扩充（Module Augmentation）：在自己的 .d.ts 中重新 declare module 合并类型。"
                ),
                "examples": [
                    "// declare 全局变量\n// globals.d.ts\ndeclare const API_BASE_URL: string;\ndeclare function initializeApp(config: object): void;\ndeclare namespace MyLib {\n    function doSomething(): void;\n}",
                    "// 模块扩充：为 express 的 Request 添加自定义属性\n// express.d.ts\nimport 'express';\ndeclare module 'express' {\n    interface Request {\n        user?: { id: number; name: string };\n    }\n}\n// 现在 req.user 有类型提示了！",
                ],
                "key_points": [
                    ".d.ts 声明文件提供类型信息，`declare` 声明存在而不实现",
                    "三斜线指令声明 .d.ts 文件间依赖",
                    "`declare module` 模块扩充，为第三方库补充自定义类型",
                ],
            },
        ],
    },
    {
        "topic": "TypeScript高级类型",
        "lessons": [
            {
                "id": "lesson_ts_TypeScript高级类型_1",
                "title": "条件类型与 infer",
                "topic": "TypeScript高级类型",
                "content": (
                    "条件类型（Conditional Types）语法：`T extends U ? X : Y`。根据类型关系在编译时分派不同的类型。"
                    "这是 TypeScript  类型系统的「if-else」，是内置工具类型（Exclude/Extract/NonNullable）的实现基础。"
                    "分布式条件类型：当 T 是联合类型时，`T extends U ? X : Y` 会对联合的每个成员分别求值再联合结果。"
                    "`infer` 关键字：在条件类型的 extends 子句中声明类型变量，让 TypeScript 推断类型。"
                    "经典用法：`type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never`。"
                    "`infer` 还可用于提取数组元素类型、Promise 包裹类型、函数参数类型等。"
                ),
                "examples": [
                    "// 条件类型基本用法\ntype IsString<T> = T extends string ? true : false;\ntype A = IsString<string>;  // true\ntype B = IsString<number>;  // false\n\n// 分布式条件类型\ntype Diff<T, U> = T extends U ? never : T;\ntype C = Diff<'a' | 'b' | 'c', 'a'>;  // 'b' | 'c'",
                    "// infer 提取 ReturnType\ntype MyReturnType<T> = T extends (...args: any[]) => infer R ? R : never;\ntype Fn = (x: number) => string;\ntype Result = MyReturnType<Fn>;  // string",
                    "// infer 提取数组元素\ntype ArrayElement<T> = T extends (infer E)[] ? E : never;\ntype El = ArrayElement<string[]>;  // string",
                ],
                "key_points": [
                    "`T extends U ? X : Y` 编译时分派类型",
                    "分布式条件类型对联合成员分别求值",
                    "`infer` 在条件类型中推断类型变量，是提取类型的关键",
                ],
            },
            {
                "id": "lesson_ts_TypeScript高级类型_2",
                "title": "映射类型与工具类型",
                "topic": "TypeScript高级类型",
                "content": (
                    "映射类型（Mapped Types）语法：`{ [K in keyof T]: NewType }`，遍历 T 的所有属性并转换为新类型。"
                    "`+/-` 修饰符控制 readonly 和可选（?）：`+readonly` 添加只读、`-readonly` 移除只读、`+?` 添加可选、`-?` 移除可选。"
                    "内置工具类型都是映射类型的应用：`Partial<T>` 所有属性可选、`Required<T>` 所有属性必填、"
                    "`Readonly<T>` 所有属性只读、`Pick<T, K>` 选取部分属性、`Omit<T, K>` 排除部分属性。"
                    "`Record<K, T>` 创建键为 K、值为 T 的对象类型。`Exclude<T, U>` / `Extract<T, U>` 联合类型过滤。"
                    "模板字面量类型：``type EventName = `on${Capitalize<string>}` ``，可做字符串级别的类型运算。"
                ),
                "examples": [
                    "// 自定义映射类型\ninterface User {\n    name: string;\n    age: number;\n    email: string;\n}\n// 所有属性变为可选\ntype PartialUser = { [K in keyof User]?: User[K] };\n// 等价于 Partial<User>\n\n// 所有属性变为只读\ntype ReadonlyUser = { readonly [K in keyof User]: User[K] };",
                    "// 内置工具类型实战\ntype UserPreview = Pick<User, 'name' | 'email'>;     // { name: string; email: string }\ntype UserNoEmail = Omit<User, 'email'>;                // { name: string; age: number }\ntype UserRecord = Record<'admin' | 'user', User>;      // { admin: User; user: User }",
                    "// 模板字面量类型\ntype World = \"world\";\ntype Greeting = `hello ${World}`;  // \"hello world\"",
                ],
                "key_points": [
                    "映射类型 `[K in keyof T]` 遍历属性转换，`+/-` 控制修饰符",
                    "Partial/Required/Readonly/Pick/Omit 都是映射类型的应用",
                    "模板字面量类型做字符串级别类型运算",
                ],
            },
        ],
    },
    {
        "topic": "TypeScript异步",
        "lessons": [
            {
                "id": "lesson_ts_TypeScript异步_1",
                "title": "Promise 类型化",
                "topic": "TypeScript异步",
                "content": (
                    "TypeScript 中 Promise 是泛型：`Promise<T>`，T 指定 resolve 的返回值类型。"
                    "`async` 函数自动返回 `Promise<T>`，其中 T 是函数体内 return 的值的类型。"
                    "如果 async 函数可能抛异常，返回值类型是 `Promise<T>`（不是 Promise<T | Error>），"
                    "因为 rejected 的 Promise 不是通过类型系统跟踪的——需要用 .catch() 或 try-catch 处理。"
                    "`Promise.all()` 的类型推断：如果传入 `[Promise<A>, Promise<B>]`，返回 `Promise<[A, B]>`。"
                    "`Promise.race()` 返回类型是入参 Promise 类型的联合。"
                    "Axios 类型化示例：`axios.get<User[]>(url)` 返回 `Promise<AxiosResponse<User[]>>`。"
                ),
                "examples": [
                    "// async 函数的类型推断\nasync function fetchUser(id: number): Promise<User> {\n    const res = await fetch(`/api/users/${id}`);\n    return res.json();  // 返回 User\n}\n\nasync function maybeFail(): Promise<string> {\n    if (Math.random() > 0.5) throw new Error('failed');\n    return 'ok';\n}",
                    "// Promise.all 类型推断\nasync function loadAll() {\n    const [user, posts] = await Promise.all([\n        fetchUser(1),\n        fetch(`/api/posts`).then(r => r.json()) as Promise<Post[]>\n    ]);\n    // user: User, posts: Post[]\n}",
                    "// Axios 类型化\nimport axios from 'axios';\nconst { data } = await axios.get<User[]>('/api/users');  // data: User[]",
                ],
                "key_points": [
                    "`Promise<T>` 泛型指定 resolve 类型，async 函数自动返回 Promise",
                    "`Promise.all()` 保留元组类型，`Promise.race()` 返回联合类型",
                    "Axios API 调用用泛型指定响应数据类型",
                ],
            },
            {
                "id": "lesson_ts_TypeScript异步_2",
                "title": "错误处理模式",
                "topic": "TypeScript异步",
                "content": (
                    "Promise 的 catch 中 error 类型默认是 `unknown`（TS 4.0+），使用前必须类型守卫。"
                    "推荐用 `instanceof Error` 或自定义类型守卫收窄：`if (error instanceof Error)`。"
                    "Result 模式：`type Result<T, E = Error> = { success: true; data: T } | { success: false; error: E }`，"
                    "让错误成为类型系统的一部分，强制调用方处理两种分支。"
                    "`neverthrow` / `ts-results` 等库提供 Rust 风格的 Result 类型，适合函数式风格的错误处理。"
                    "注意 `Promise<void>` 的陷阱：忘记 await 或 catch 时不会有编译错误，但会有运行时未处理的 rejection。"
                    "启用 `no-floating-promises` ESLint 规则可以捕获这类遗漏。"
                ),
                "examples": [
                    "// catch 中 error 类型处理\nasync function safeFetch(url: string) {\n    try {\n        const res = await fetch(url);\n        return await res.json();\n    } catch (error) {\n        if (error instanceof Error) {\n            console.error(error.message);\n        } else {\n            console.error('Unknown error', error);\n        }\n    }\n}",
                    "// Result 模式\ntype Result<T, E = Error> =\n    | { success: true; data: T }\n    | { success: false; error: E };\n\nasync function safeCall(): Promise<Result<string>> {\n    try {\n        const data = await fetchUser(1);\n        return { success: true, data: data.name };\n    } catch (error) {\n        return { success: false, error: error as Error };\n    }\n}",
                ],
                "key_points": [
                    "catch 中 error 是 unknown，需 instanceof 类型收窄",
                    "Result 模式让错误成为类型系统的一部分，强制处理",
                    "启用 no-floating-promises 防止遗漏 await/catch",
                ],
            },
        ],
    },
    {
        "topic": "TypeScript设计模式",
        "lessons": [
            {
                "id": "lesson_ts_TypeScript设计模式_1",
                "title": "TS 常用设计模式",
                "topic": "TypeScript设计模式",
                "content": (
                    "TypeScript 的类型系统让设计模式更安全、更易维护。"
                    "单例模式：`class Singleton { private static instance: Singleton; ... }` 确保全局唯一实例。"
                    "工厂模式：根据参数创建不同子类实例，结合 discriminated union 实现类型安全的工厂。"
                    "Builder 模式：链式调用逐步构建复杂对象，每一步返回 `this`，最终 `.build()` 产出。"
                    "策略模式：定义策略接口，运行时切换算法实现。TypeScript 中可用联合类型 + switch 替代继承。"
                    "观察者模式：`type Listener<T> = (data: T) => void` 定义泛型事件系统，适用于状态管理。"
                ),
                "examples": [
                    "// 单例模式\nclass Config {\n    private static instance: Config;\n    private settings = new Map<string, string>();\n    static getInstance(): Config {\n        if (!Config.instance) Config.instance = new Config();\n        return Config.instance;\n    }\n    get(key: string) { return this.settings.get(key); }\n}",
                    "// Builder 模式\nclass RequestBuilder {\n    private url = '';\n    private method: 'GET' | 'POST' = 'GET';\n    private headers: Record<string, string> = {};\n    setUrl(url: string) { this.url = url; return this; }\n    setMethod(m: 'GET' | 'POST') { this.method = m; return this; }\n    build(): Request { return { url: this.url, method: this.method, headers: this.headers }; }\n}",
                ],
                "key_points": [
                    "单例确保唯一实例，工厂 + discriminated union 类型安全",
                    "Builder 链式调用构建复杂对象",
                    "策略模式可用联合类型 + switch 替代继承层次",
                ],
            },
            {
                "id": "lesson_ts_TypeScript设计模式_2",
                "title": "依赖注入与 IoC",
                "topic": "TypeScript设计模式",
                "content": (
                    "依赖注入（DI）是控制反转（IoC）的实现方式：类不自己创建依赖，而是从外部接收。"
                    "优势：解耦（模块间无直接依赖）、可测试（轻松替换 mock）、可维护（依赖关系透明）。"
                    "tsyringe 是轻量级 TS DI 容器：`@injectable()` 标记类，`@inject()` 注入依赖，`container.resolve()` 获取实例。"
                    "InversifyJS 功能更丰富：`@injectable()` + `@inject()`，需先配置 IoC 容器绑定接口到实现。"
                    "NestJS 内置强大的 DI 系统：`@Injectable()` + 构造器注入，module 中声明 providers。"
                    "在没有 DI 框架的项目中，可通过构造函数参数 + 接口实现手动注入。"
                ),
                "examples": [
                    "// 手动依赖注入\ninterface Logger { log(msg: string): void }\nclass ConsoleLogger implements Logger {\n    log(msg: string) { console.log(msg); }\n}\nclass UserService {\n    constructor(private logger: Logger) {}  // 依赖通过构造器注入\n    createUser(name: string) {\n        this.logger.log(`Creating user ${name}`);\n    }\n}\n// 使用时\nconst service = new UserService(new ConsoleLogger());",
                    "// tsyringe 示例\nimport { injectable, inject, container } from 'tsyringe';\n@injectable()\nclass Database {\n    connect() { /* ... */ }\n}\n@injectable()\nclass Repository {\n    constructor(@inject(Database) private db: Database) {}\n}\nconst repo = container.resolve(Repository);",
                ],
                "key_points": [
                    "DI = 类不创建依赖，从外部接收，实现解耦和可测试",
                    "NestJS 内置 DI 系统最强大，tsyringe 轻量适合小项目",
                    "手动 DI 用构造函数参数 + 接口也能实现",
                ],
            },
        ],
    },
    {
        "topic": "TypeScript测试",
        "lessons": [
            {
                "id": "lesson_ts_TypeScript测试_1",
                "title": "Jest 集成与编写",
                "topic": "TypeScript测试",
                "content": (
                    "Jest 是 TS 项目的主流测试框架，配合 ts-jest 预处理器将 TS 编译为 JS 后运行测试。"
                    "配置：`npx ts-jest config:init` 生成 jest.config.ts，关键是 `preset: 'ts-jest'`。"
                    "基本测试结构：`describe('模块名', () => { it('应该做什么', () => { expect(实际值).toBe(期望值) }) })`。"
                    "常用匹配器：toBe（严格相等）、toEqual（深度相等）、toBeTruthy/Falsy、toContain、toThrow。"
                    "Mock 策略：`jest.fn()` 创建 mock 函数，`jest.mock('./module')` 自动 mock 整个模块，"
                    "`jest.spyOn(obj, 'method')` 监听已有方法。"
                    "异步测试：it 中 return Promise，或 async/await + expect.assertions(N) 确保断言被执行。"
                ),
                "examples": [
                    "// 基本测试\nimport { sum } from './math';\n\ndescribe('sum', () => {\n    it('should add two numbers', () => {\n        expect(sum(1, 2)).toBe(3);\n    });\n\n    it('should handle negative numbers', () => {\n        expect(sum(-1, -2)).toBe(-3);\n    });\n});",
                    "// Mock 示例\njest.mock('./api');  // 自动 mock\nimport { fetchUser } from './api';\nconst mockFetchUser = fetchUser as jest.MockedFunction<typeof fetchUser>;\nmockFetchUser.mockResolvedValue({ id: 1, name: 'Alice' });",
                ],
                "key_points": [
                    "ts-jest 预设让 Jest 直接运行 TS 测试",
                    "describe/it/expect 是测试三件套，toBe/toEqual 常用匹配",
                    "jest.fn() / jest.mock() / jest.spyOn() 三种 mock 策略",
                ],
            },
            {
                "id": "lesson_ts_TypeScript测试_2",
                "title": "类型测试与 Vitest",
                "topic": "TypeScript测试",
                "content": (
                    "类型测试验证的是编译时行为而非运行时行为：确保类型在预期场景中通过/报错。"
                    "tsd 库：`expectType<T>(value)` 编译时断言 value 的类型为 T，`expectError(expr)` 期望表达式类型报错。"
                    "expect-type 库：提供更丰富的类型断言 API，如 `.toBeString()`、`.not.toBeNullable()`。"
                    "Vitest 是新一代测试框架：基于 Vite，零配置兼容 Jest API，原生 ESM 支持，速度快 10x。"
                    "配置：`vitest.config.ts` 设为 `defineConfig({ test: { ... } })` 或在 vite.config.ts 中配置。"
                    "Testing Library（React Testing Library）测试组件：`render(<Component />)` + `screen.getByRole()` / `getByText()` 查询 DOM。"
                ),
                "examples": [
                    "// tsd 类型测试\nimport { expectType } from 'tsd';\n\nfunction identity<T>(arg: T): T { return arg; }\n\nexpectType<string>(identity('hello'));     // 编译通过\nexpectType<number>(identity(42));          // 编译通过\n// expectError(identity<string>(42));      // 期望编译报错：number 不兼容 string",
                    "// Vitest 配置（vitest.config.ts）\nimport { defineConfig } from 'vitest/config';\nexport default defineConfig({\n    test: {\n        globals: true,          // 自动注入 describe/it/expect\n        environment: 'jsdom',   // 或 'node' / 'happy-dom'\n    }\n});",
                ],
                "key_points": [
                    "tsd/expect-type 做编译时类型断言，验证类型正确性",
                    "Vitest 基于 Vite，零配置兼容 Jest API，速度快",
                    "Testing Library 测试组件：render + screen 查询",
                ],
            },
        ],
    },
    {
        "topic": "工具类型与条件类型",
        "lessons": [
        {
            "id": "lesson_ts_工具类型与条件类型_1", "title": "内置工具类型详解",
            "topic": "工具类型与条件类型",
            "content": (
                        "TypeScript 内置了大量实用工具类型（Utility Types），无需额外安装即可使用。`Partial<T>` 将 T 的所有属性变为可选，`Required<T>`"
                        "反之全部必填，`Readonly<T>` 全部只读。`Pick<T, K>` 从 T 中选取指定属性集合 K，`Omit<T, K>` 从 T 中排除指定属性集合。`Record<K, V>` 构造一个键类型为"
                        "K、值类型为 V 的对象类型。`Exclude<T, U>` 从联合类型 T 中排除 U。`Extract<T, U>` 从联合类型 T 中提取 U 的子类型。`NonNullable<T>` 排除 null 和"
                        "undefined。`ReturnType<T>` 获取函数返回类型，`Parameters<T>` 获取参数元组类型。`Awaited<T>` 递归解包"
                        "Promise。这些工具类型的实现基于条件类型和映射类型，理解它们有助于深入掌握 TS 类型系统。"
            ),
            "examples": [
                        """
                        // 常用工具类型
                        interface User {
                            id: number;
                            name: string;
                            email?: string;
                        }
                        type PartialUser = Partial<User>;          // 所有属性可选
                        type ReadonlyUser = Readonly<User>;        // 所有属性只读
                        type UserName = Pick<User, 'id' | 'name'>; // 只取 id 和 name
                        type NoEmail = Omit<User, 'email'>;        // 排除 email
                        
                        // Record 与类型映射
                        type Page = 'home' | 'about' | 'contact';
                        type Routes = Record<Page, { url: string; title: string }>;
                        
                        // ReturnType 与 Parameters
                        type Fn = (a: number, b: string) => boolean;
                        type FnReturn = ReturnType<Fn>;    // boolean
                        type FnParams = Parameters<Fn>;    // [number, string]
                        """,
            ],
            "key_points": [
                        "Partial/Required/Readonly 修改属性的可选/只读状态",
                        "Pick/Omit 按属性名选取或排除，Record 构造键值映射",
                        "ReturnType/Parameters/Awaited 提取函数和异步类型信息",
            ],
        },
        {
            "id": "lesson_ts_工具类型与条件类型_2", "title": "条件类型与推断",
            "topic": "工具类型与条件类型",
            "content": (
                        "条件类型语法：`T extends U ? X : Y`，类似三元运算符但在类型层面工作。结合 `infer` 关键字可推断类型变量。分布式条件类型：当 T 是联合类型时，条件类型会自动分布到每个成员：`T"
                        "extends U ? X : Y` 等价于对联合每个成员单独求值再联合。`infer` 只能在条件类型的 `extends` 子句中使用，用于从类型中推断出某个部分。如 `type Unwrap<T> = T"
                        "extends Promise<infer R> ? R : T`。内置条件类型 `Exclude<T, U> = T extends U ? never : T`，利用 never"
                        "在联合中被吸收的特性实现排除。映射类型 + 条件类型可实现深度变换：`type DeepReadonly<T> = { readonly [K in keyof T]: T[K] extends object ?"
                        "DeepReadonly<T[K]> : T[K] }`。条件类型在库开发中广泛使用，如 zod 的 `z.infer<typeof schema>`、React 的 `ComponentProps<typeof"
                        "Comp>`。"
            ),
            "examples": [
                        """
                        // 条件类型基础
                        type IsString<T> = T extends string ? true : false;
                        type A = IsString<'hello'>;  // true
                        type B = IsString<42>;       // false
                        
                        // 分布式条件类型
                        type ToArray<T> = T extends any ? T[] : never;
                        type C = ToArray<string | number>;  // string[] | number[]
                        
                        // infer 推断 Promise 内部类型
                        type UnwrapPromise<T> = T extends Promise<infer R> ? R : T;
                        type D = UnwrapPromise<Promise<number>>;  // number
                        
                        // 深度 Readonly
                        type DeepReadonly<T> = {
                            readonly [K in keyof T]: T[K] extends object ? DeepReadonly<T[K]> : T[K];
                        };
                        """,
            ],
            "key_points": [
                        "条件类型 `T extends U ? X : Y` 配合 infer 推断类型变量",
                        "分布式条件类型对联合每个成员单独求值再组合",
                        "映射类型 + 条件类型 = 深度类型变换的基石",
            ],
        },
        ],
    },
    {
        "topic": "声明文件与类型发布",
        "lessons": [
        {
            "id": "lesson_ts_声明文件与类型发布_1", "title": "编写 .d.ts 声明文件",
            "topic": "声明文件与类型发布",
            "content": (
                        "声明文件（.d.ts）为 JavaScript 库提供类型描述，让 TS 项目安全调用 JS 代码。三种来源：库自带、DefinitelyTyped（@types/xxx）、自定义。`declare`"
                        "关键字声明全局变量、函数、类、模块的类型而不提供实现。`declare global { ... }` 扩展全局类型。模块声明：`declare module 'xxx' { ... }` 为无类型 npm 包或"
                        "CSS/图片导入声明类型。通配符模块 `declare module '*.css' { const c: Record<string, string>; export default c; }`。`declare"
                        "namespace` 为全局命名空间变量声明类型（如 jQuery 的 `$`）。模块扩充 `declare module 'vue' { interface ComponentCustomProperties {"
                        "$myMethod(): void } }` 扩展第三方库类型。声明文件编译：`tsc --declaration --emitDeclarationOnly` 从 .ts 源码自动生成 .d.ts。types 字段在"
                        "package.json 中指向入口声明文件。"
            ),
            "examples": [
                        """
                        // my-lib.d.ts
                        export function greet(name: string): string;
                        export interface Options {
                            language: 'en' | 'zh';
                            greeting?: string;
                        }
                        export class Greeter {
                            constructor(options: Options);
                            sayHello(): string;
                        }
                        
                        // 全局扩展
                        declare global {
                            interface Window {
                                myAppConfig: { version: string };
                            }
                        }
                        
                        // 模块扩充（扩展 Vue）
                        declare module 'vue' {
                            interface ComponentCustomProperties {
                                $formatDate: (date: Date) => string;
                            }
                        }
                        """,
            ],
            "key_points": [
                        ".d.ts 文件用 declare 描述类型不提供实现",
                        "declare module 为无类型模块声明类型，declare global 扩展全局",
                        "tsc --declaration 自动生成声明文件，package.json types 字段指定入口",
            ],
        },
        {
            "id": "lesson_ts_声明文件与类型发布_2", "title": "类型发布与版本管理",
            "topic": "声明文件与类型发布",
            "content": (
                        "类型发布的三种模式：(1) 源码中内联类型 + tsc 编译出 .d.ts；(2) 独立的 @types/xxx 包；(3) 库自带 types 字段指向 .d.ts。DefinitelyTyped 贡献流程：fork"
                        "仓库 → 写 .d.ts 和 tests → PR。types-publisher 自动审核和发布到 npm。语义化版本中的类型变更：新增类型属性是 Minor 变更，修改已有类型签名是 Major Breaking"
                        "Change。类型测试（dtslint / tsd）：`expectType<Type>(value)` 确保类型推导正确，`expectError(fn())` 验证类型错误。monorepo 中的类型共享：使用"
                        "TypeScript Project References（tsconfig.json 的 references 字段）在不同包间共享类型。"
            ),
            "examples": [
                        """
                        // package.json 中的类型配置
                        {
                            "name": "my-lib",
                            "main": "./dist/index.js",
                            "types": "./dist/index.d.ts",
                            "exports": {
                                ".": {
                                    "types": "./dist/index.d.ts",
                                    "import": "./dist/index.mjs",
                                    "require": "./dist/index.cjs"
                                }
                            }
                        }
                        
                        // tsd 类型测试
                        import { expectType, expectError } from 'tsd';
                        import { greet, Greeter } from 'my-lib';
                        
                        expectType<string>(greet('Alice'));
                        expectError(greet(42));
                        """,
            ],
            "key_points": [
                        "三种类型发布模式：内联编译、独立 @types 包、库自带 types 字段",
                        "类型变更遵循语义化版本，签名修改是 Breaking Change",
                        "dtslint/tsd 进行类型测试，tsconfig references 实现跨包类型共享",
            ],
        },
        ],
    },
    {
        "topic": "模块解析与路径映射",
        "lessons": [
        {
            "id": "lesson_ts_模块解析与路径映射_1", "title": "模块解析策略",
            "topic": "模块解析与路径映射",
            "content": (
                        "模块解析（Module Resolution）是 TypeScript 编译器查找模块对应文件的过程。两种策略：Classic（遗留）和 Node（现代默认）。Node 策略模拟 Node.js 的 require"
                        "解析：先查同名文件（.ts/.tsx/.d.ts），再查同名目录下的 index.ts，最后查 package.json 的 types/main 字段。`moduleResolution` 选项：'node'（传统"
                        "Node 算法）、'bundler'（适用于 Vite/esbuild 等打包工具）、'nodenext'（支持 package.json exports 字段）。相对导入 `./foo`"
                        "从当前文件目录查找，非相对导入 `foo` 从 node_modules 递归查找。条件导出（package.json exports）：根据 import/require/types 条件导出不同路径，支持子路径导出"
                        "`my-lib/button`。"
            ),
            "examples": [
                        """
                        // tsconfig.json 模块解析配置
                        {
                            "compilerOptions": {
                                "module": "ESNext",
                                "moduleResolution": "bundler",     // 打包工具友好
                                "allowImportingTsExtensions": true, // 允许 import 带 .ts 后缀
                                "resolvePackageJsonExports": true   // 支持 package.json exports
                            }
                        }
                        
                        // package.json exports 条件导出
                        {
                            "name": "@scope/ui",
                            "exports": {
                                ".": {
                                    "types": "./dist/index.d.ts",
                                    "import": "./dist/index.mjs",
                                    "require": "./dist/index.cjs"
                                },
                                "./button": {
                                    "types": "./dist/button.d.ts",
                                    "import": "./dist/button.mjs"
                                }
                            }
                        }
                        """,
            ],
            "key_points": [
                        "moduleResolution: node / bundler / nodenext 三种策略",
                        "相对导入查文件树，非相对导入递归查 node_modules",
                        "package.json exports 条件导出支持子路径和双模块格式",
            ],
        },
        {
            "id": "lesson_ts_模块解析与路径映射_2", "title": "路径别名与 Monorepo",
            "topic": "模块解析与路径映射",
            "content": (
                        "路径别名 `paths` 配置将模块名映射到实际路径，配合构建工具的 alias 使用：`'@/*' → './src/*'`。`baseUrl` 设置非相对导入的基准目录，通常设为 '.' 或"
                        "'./src'。Project References：用 tsconfig.json 的 `references` 字段将 monorepo 拆分为多个子项目，每个子项目有自己的"
                        "tsconfig。`composite: true` 启用增量编译和声明文件生成，`declarationMap` 生成声明文件的 source map。monorepo 项目结构：根 tsconfig 用"
                        "references 引用子包，子包 tsconfig 用 composite + outDir 独立编译。`tsc --build` 自动处理引用图的增量构建。"
            ),
            "examples": [
                        """
                        // tsconfig.json 路径别名
                        {
                            "compilerOptions": {
                                "baseUrl": ".",
                                "paths": {
                                    "@/*": ["./src/*"],
                                    "@components/*": ["./src/components/*"],
                                    "@utils/*": ["./src/utils/*"]
                                }
                            }
                        }
                        
                        // Monorepo 根 tsconfig（references）
                        {
                            "files": [],
                            "references": [
                                { "path": "./packages/core" },
                                { "path": "./packages/react" },
                                { "path": "./packages/vue" }
                            ]
                        }
                        // 子包 tsconfig
                        {
                            "compilerOptions": {
                                "composite": true,
                                "declaration": true,
                                "declarationMap": true,
                                "outDir": "./dist",
                                "rootDir": "./src"
                            },
                            "include": ["src"]
                        }
                        """,
            ],
            "key_points": [
                        "paths + baseUrl 实现路径别名映射",
                        "Project References + composite 实现 monorepo 增量编译",
                        "tsc --build 自动处理引用依赖图的构建顺序",
            ],
        },
        ],
    },
    {
        "topic": "类型体操与进阶模式",
        "lessons": [
        {
            "id": "lesson_ts_类型体操与进阶模式_1", "title": "模板字面量类型",
            "topic": "类型体操与进阶模式",
            "content": (
                        "模板字面量类型（Template Literal Types, TS 4.1+）允许在类型层面使用字符串拼接和模式匹配。语法：`` `${prefix}${string}` ``。结合联合类型可实现笛卡尔积：`type"
                        "EventName = `${'on' | 'after'}${Capitalize<'click' | 'hover'>}`` → `'onClick' | 'onHover' | 'afterClick' |"
                        "'afterHover'`。内置字符串工具类型：`Uppercase<T>`、`Lowercase<T>`、`Capitalize<T>`、`Uncapitalize<T>`。`infer`"
                        "配合模板字面量类型实现字符串解析：`type ParseRoute<T> = T extends `${infer Base}/${infer Param}` ? { base: Base; param: Param"
                        "} : never`。实际应用：类型安全的路由参数解析、CSS 属性名验证、事件名生成、国际化 key 类型等。"
            ),
            "examples": [
                        """
                        // 模板字面量类型
                        // 事件名笛卡尔积
                        type Events = 'click' | 'focus' | 'blur';
                        type Handlers = `on${Capitalize<Events>}`;
                        // 'onClick' | 'onFocus' | 'onBlur'
                        
                        // 路由参数解析
                        type ParseId<T extends string> =
                            T extends `${infer _Prefix}/users/${infer Id}` ? Id : never;
                        type UserId = ParseId<'/api/users/42'>;  // '42'
                        
                        // CSS 值约束
                        type Size = 'small' | 'medium' | 'large';
                        type Margin = `m${Capitalize<Size>}`;
                        // 'mSmall' | 'mMedium' | 'mLarge'
                        """,
            ],
            "key_points": [
                        "模板字面量类型实现类型层面的字符串拼接和模式匹配",
                        "与联合类型结合产生笛卡尔积效果",
                        "配合 infer 实现类型安全的字符串解析（路由、CSS、事件等）",
            ],
        },
        {
            "id": "lesson_ts_类型体操与进阶模式_2", "title": "类型安全的 Builder 模式",
            "topic": "类型体操与进阶模式",
            "content": (
                        "类型安全 Builder 模式在编译期捕获配置错误，常用于查询构建器、表单生成、API 客户端。链式调用类型追踪：每一步返回带状态的新类型，逐步收窄可能选项。如"
                        "`QueryBuilder.select('name').from('users').where('age > 18')` 中必须先 select 才能 where。Mapped Types 与 key"
                        "remapping（TS 4.1+）：`{ [K in keyof T as `get${Capitalize<K & string>}`]: () => T[K] }` 批量生成 getter"
                        "方法签名。Branded Types（品牌类型）：通过交叉 `{ __brand: 'UserId' }` 创建名义子类型，防止 ID 混淆（UserId vs PostId）。Flavor 类型比 Brand"
                        "更松：`type Flavor<T, F> = T & { __flavor?: F }` 可以赋值给 T（子类型），适用于函数参数约束。"
            ),
            "examples": [
                        """
                        // 类型安全的 Builder 模式
                        class QueryBuilder<Selected extends string = never, Table extends string = never> {
                            select<T extends string>(cols: T): QueryBuilder<T, Table> {
                                return this as any;
                            }
                            from<T extends string>(table: T): QueryBuilder<Selected, T> {
                                return this as any;
                            }
                            // where 只能在 select 和 from 都设置后调用
                            where(condition: string): this {
                                return this;
                            }
                        }
                        
                        // Branded Types
                        // type UserId = string & { __brand: 'UserId' };
                        // type PostId = string & { __brand: 'PostId' };
                        // function getUser(id: UserId) {}
                        // getUser(postId as PostId); // Error
                        """,
            ],
            "key_points": [
                        "泛型参数状态追踪实现类型安全的 Builder 链式调用",
                        "Mapped Types key remapping 批量生成方法签名",
                        "Branded Types 创建名义子类型防止 ID 混淆",
            ],
        },
        ],
    },
    {
        "topic": "运行时类型验证",
        "lessons": [
        {
            "id": "lesson_ts_运行时类型验证_1", "title": "Zod 与类型推导",
            "topic": "运行时类型验证",
            "content": (
                        "Zod 是 TypeScript 优先的运行时验证库，核心思路：定义 schema → `z.infer<typeof schema>` 推导类型 → `schema.parse(data)` 验证 +"
                        "类型收窄。基本类型：`z.string()`、`z.number()`、`z.boolean()`、`z.date()`、`z.enum()`、`z.literal()`。组合类型：`z.object()`、`z.array()`、`z.tuple()`、`z.union()`。修饰符：`.optional()`、`.nullable()`、`.default()`、`.refine()`（自定义校验）、`.transform()`（值转换）。`z.infer<typeof"
                        "schema>` 从运行时 schema 反推编译时类型，保证类型与运行时校验 100% 一致（Single Source of Truth）。与 React Hook Form"
                        "集成（@hookform/resolvers/zod）实现表单验证。与 tRPC 集成验证 API 输入输出。"
            ),
            "examples": [
                        """
                        import { z } from 'zod';
                        
                        // 定义 Schema
                        const UserSchema = z.object({
                            name: z.string().min(1).max(100),
                            age: z.number().int().min(0).max(150),
                            email: z.string().email().optional(),
                            role: z.enum(['admin', 'user', 'guest']),
                        });
                        
                        // 推断类型（零冗余）
                        type User = z.infer<typeof UserSchema>;
                        
                        // 运行时验证
                        const user = UserSchema.parse(JSON.parse(input));
                        // user 此时类型为 User，且已通过验证
                        
                        // .safeParse 不抛异常
                        const result = UserSchema.safeParse(data);
                        // if (!result.success) console.error(result.error);
                        """,
            ],
            "key_points": [
                        "Schema 定义 → z.infer 推导类型 → parse 验证 + 类型收窄",
                        ".optional()/.nullable()/.default()/.refine() 修饰链",
                        "safeParse 不抛异常，result.success 判断 + result.error 获取详情",
            ],
        },
        {
            "id": "lesson_ts_运行时类型验证_2", "title": "tRPC 与端到端类型安全",
            "topic": "运行时类型验证与全栈",
            "content": (
                        "tRPC 实现前后端共享类型，无需生成 API 文档或 OpenAPI schema。服务端定义 router →"
                        "客户端自动获得类型安全的调用。核心概念：`t.procedure.input(zodSchema).query/mutation(resolver)`。输入用 Zod schema"
                        "验证，输出类型自动推导。客户端调用：`trpc.user.getById.useQuery({ id: '123' })`——入参和返回值完全类型安全，无手动类型声明。tRPC v11 支持 Server-Sent"
                        "Events（subscriptions）、WebSocket 传输、文件上传等高级特性。tRPC + Next.js App Router 集成：route handler 配合"
                        "`fetchRequestHandler`，RSC 用 `caller` 直接调用服务端逻辑。与 REST/GraphQL 对比：tRPC 牺牲跨语言互操作性，换取端到端类型安全 + 零样板代码。"
            ),
            "examples": [
                        """
                        // 服务端 router 定义
                        import { z } from 'zod';
                        import { router, publicProcedure } from '../trpc';
                        
                        export const userRouter = router({
                            getById: publicProcedure
                                .input(z.object({ id: z.string() }))
                                .query(({ input }) => {
                                    return { name: 'Alice', id: input.id };
                                }),
                            create: publicProcedure
                                .input(z.object({ name: z.string(), email: z.string().email() }))
                                .mutation(({ input }) => {
                                    return { id: 'new-1', ...input };
                                }),
                        });
                        
                        // 客户端调用（完全类型安全）
                        // const { data } = trpc.user.getById.useQuery({ id: '123' });
                        // const create = trpc.user.create.useMutation();
                        """,
            ],
            "key_points": [
                        "tRPC 服务端定义 router + Zod input 验证，客户端自动获得类型",
                        "procedure.input(zod).query/mutation 输入输出统一类型链",
                        "牺牲跨语言互操作性，换取端到端类型安全 + 零样板代码",
            ],
        },
        ],
    },
    {
        "topic": "类型安全设计模式",
        "lessons": [
        {
            "id": "lesson_ts_类型安全设计模式_1", "title": "Result 与 Either 模式",
            "topic": "类型安全设计模式",
            "content": (
                        "Rust 风格的 Result 类型可用于 TypeScript 错误处理，消除 try-catch 的不可预测性。`type Result<T, E = Error> = { success: true; data:"
                        "T } | { success: false; error: E }`。优势：(1) 调用方被迫处理两种结果（穷举检查）；(2) 类型系统跟踪错误类型；(3)"
                        "函数签名明确声明可能失败。辅助函数：`ok<T>(data: T): Result<T>` 创建成功结果，`err<E>(error: E): Result<never, E>` 创建失败结果。Either"
                        "模式：`type Either<L, R> = { type: 'left'; value: L } | { type: 'right'; value: R }`，左值通常表示错误、右值表示成功。实际应用：API"
                        "层统一 Result 返回，service 层链式处理，Express/Koa 中间件错误传递。"
            ),
            "examples": [
                        """
                        // Result 类型定义
                        type Result<T, E = Error> =
                            | { success: true; data: T }
                            | { success: false; error: E };
                        
                        function divide(a: number, b: number): Result<number, string> {
                            if (b === 0) return { success: false, error: '除零错误' };
                            return { success: true, data: a / b };
                        }
                        
                        // 消费端穷举处理
                        const r = divide(10, 0);
                        if (r.success) {
                            console.log(r.data);      // number
                        } else {
                            console.error(r.error);   // string - 强制处理错误
                        }
                        """,
            ],
            "key_points": [
                        "Result<T, E> 用判别联合强制处理成功/失败两种情况",
                        "ok/err 辅助函数创建 Result，避免手动构造对象",
                        "函数签名明确声明失败可能，调用方编译期就知晓需要错误处理",
            ],
        },
        {
            "id": "lesson_ts_类型安全设计模式_2", "title": "函数式编程与 immutability",
            "topic": "类型安全设计模式",
            "content": (
                        "`as const` 断言将对象/数组变为深度只读字面量类型：`const routes = ['home', 'about'] as const` → 类型为 `readonly ['home',"
                        "'about']`。`Readonly<T>` 工具类型 + `as const` 组合实现深度不可变数据结构。`readonly` 修饰符确保编译期捕获意外修改。Pipe / Compose"
                        "模式：函数组合从左到右（pipe）或从右到左（compose）。TS 提供重载签名保证中间类型安全传递。Immutable.js / Immer：Immer 用 Proxy 实现「写时看似可变，实际不可变」的"
                        "produce API，TS 完美集成。`satisfies` 关键字（TS 4.9+）：验证表达式匹配类型但不改变其推导类型，常用于保留字面量类型同时满足接口约束。"
            ),
            "examples": [
                        """
                        // as const 深度不可变
                        const config = {
                            api: "https://api.example.com",
                            timeout: 5000,
                            features: ["chat", "search"],
                        } as const;
                        // config.api 类型是 "https://api.example.com"（字面量）
                        
                        // satisfies 保留字面量 + 约束校验
                        type Palette = Record<string, `#${string}`>;
                        const colors = {
                            red: "#ff0000",
                            green: "#00ff00",
                            blue: "#0000ff",
                        } satisfies Palette;
                        // colors.red 类型仍是 "#ff0000"（字面量保留）
                        
                        // Immer produce
                        // import { produce } from "immer";
                        // const nextState = produce(state, draft => {
                        //     draft.items.push(newItem); // 看似可变
                        // }); // 实际不可变
                        """,
            ],
            "key_points": [
                        "as const 深度只读 + 字面量类型，satisfies 约束校验不改变类型",
                        "Pipe/Compose 函数组合配合 TS 重载保证类型安全传递",
                        "Immer produce 实现写时可变读时不可变，TS 原生支持",
            ],
        },
        ],
    },
    {
        "topic": "Node.js TypeScript 开发",
        "lessons": [
        {
            "id": "lesson_ts_Node.js TypeScript 开发_1", "title": "TS + Express/Koa 类型安全",
            "topic": "Node.js TypeScript 开发",
            "content": (
                        "Express + TS：安装 @types/express 后，Request/Response 泛型参数可指定类型。自定义中间件扩展 Request 用 declaration merging。Koa 的 TS"
                        "类型天然优秀：`ctx.request.body` 可通过泛型指定，中间件洋葱模型类型完整推导。Fastify 原生 TypeScript 支持：`fastify.get<{ Params: { id: string"
                        "} }>('/user/:id', async (req, reply) => {...})`。路由参数类型安全：定义统一的路由配置类型 + 泛型 parse 函数，确保路径参数、query、body"
                        "的类型一致性。环境变量类型声明：`declare namespace NodeJS { interface ProcessEnv { DATABASE_URL: string } }` 收窄 `process.env`"
                        "类型。"
            ),
            "examples": [
                        """
                        // Express + TypeScript
                        import express, { Request, Response, NextFunction } from 'express';
                        
                        interface UserRequest extends Request {
                            user?: { id: string; role: 'admin' | 'user' };
                        }
                        
                        function authMiddleware(req: UserRequest, res: Response, next: NextFunction) {
                            req.user = { id: '123', role: 'admin' };
                            next();
                        }
                        
                        app.get('/api/profile', authMiddleware, (req: UserRequest, res) => {
                            res.json({ user: req.user }); // req.user 类型安全
                        });
                        
                        // 环境变量类型
                        declare namespace NodeJS {
                            interface ProcessEnv {
                                NODE_ENV: 'development' | 'production';
                                PORT: string;
                                DATABASE_URL: string;
                            }
                        }
                        """,
            ],
            "key_points": [
                        "Express 用泛型 Request/Response + 自定义接口扩展类型",
                        "Fastify 泛型路由参数天然类型安全",
                        "declare namespace NodeJS.ProcessEnv 收窄环境变量类型",
            ],
        },
        {
            "id": "lesson_ts_Node.js TypeScript 开发_2", "title": "TS 项目架构与 DI",
            "topic": "Node.js TypeScript 开发",
            "content": (
                        "TypeScript 项目架构分层：Controller（HTTP 层）→ Service（业务逻辑）→ Repository（数据访问）。接口定义在 domain"
                        "层，实现注入。依赖注入（DI）容器：tsyringe（轻量 Decorator DI）、inversify（IoC 容器）、NestJS 内置 DI。`@injectable()` + `@inject()`"
                        "声明依赖。接口抽象 + DI = 可测试性：Service 依赖 Repository 接口而非具体实现，测试时可注入 Mock 实现。配置管理：typed-config（zod"
                        "验证配置）、nest/config（NestJS 配置模块）。配置对象而非 `process.env` 散落各处。错误处理层：自定义 AppError 类 + 全局错误中间件。通过 `instanceof`"
                        "区分已知错误和未知异常，HTTP 状态码与错误类型映射。"
            ),
            "examples": [
                        """
                        // DI 容器（tsyringe 示例）
                        import { injectable, inject, container } from 'tsyringe';
                        
                        interface UserRepository {
                            findById(id: string): Promise<User | null>;
                        }
                        
                        @injectable()
                        class PostgresUserRepository implements UserRepository {
                            async findById(id: string) { /* 查询数据库 */ }
                        }
                        
                        @injectable()
                        class UserService {
                            constructor(@inject('UserRepository') private repo: UserRepository) {}
                            async getUser(id: string) { return this.repo.findById(id); }
                        }
                        
                        // 注册
                        container.register('UserRepository', { useClass: PostgresUserRepository });
                        const service = container.resolve(UserService);
                        """,
            ],
            "key_points": [
                        "TS 项目分层：Controller → Service → Repository，接口抽象在 domain 层",
                        "tsyringe/inversify 实现 DI，接口注入便于单元测试 Mock",
                        "配置用类型对象 + Zod 验证，错误用自定义 AppError 统一处理",
            ],
        },
        ],
    },
    {
        "topic": "原型模式与类型编程",
        "lessons": [
        {
            "id": "lesson_ts_原型模式与类型编程_1", "title": "递归类型与类型级编程",
            "topic": "原型模式与类型编程",
            "content": (
                        "递归类型（Recursive Types）允许类型引用自身：`type TreeNode<T> = { value: T; children: TreeNode<T>[] }`。JSON"
                        "类型就是一个经典的递归类型。递归条件类型：`type DeepPartial<T> = { [K in keyof T]?: T[K] extends object ? DeepPartial<T[K]> : T[K]"
                        "}`。TS 4.7+ 尾递归优化防止无限展开。类型级算术：通过递归映射元组长度，如 `type Add<A extends number, B extends number> = [...TupleOf<A>,"
                        "...TupleOf<B>]['length']`。元组操作：`type Head<T extends any[]> = T extends [infer H, ...any[]] ? H : never`；`type"
                        "Tail<T> = T extends [any, ...infer R] ? R : never`。类型安全的 JSONPath：`type Get<T, P extends string> = P extends"
                        "keyof T ? T[P] : ...` 递归解析路径字符串。"
            ),
            "examples": [
                        """
                        // 递归类型：树节点
                        type TreeNode<T> = {
                            value: T;
                            children: TreeNode<T>[];
                        };
                        
                        // 递归条件类型：DeepPartial
                        type DeepPartial<T> = {
                            [K in keyof T]?: T[K] extends object ? DeepPartial<T[K]> : T[K];
                        };
                        
                        // 元组操作
                        type Head<T extends any[]> = T extends [infer H, ...any[]] ? H : never;
                        type Tail<T extends any[]> = T extends [any, ...infer R] ? R : [];
                        type H = Head<[1, 2, 3]>;  // 1
                        type T = Tail<[1, 2, 3]>;  // [2, 3]
                        """,
            ],
            "key_points": [
                        "递归类型用自身引用来建模树/JSON 等嵌套结构",
                        "递归条件类型实现 DeepPartial/DeepReadonly 等深度变换",
                        "元组操作（Head/Tail/Concat）是类型级编程的基础构件",
            ],
        },
        {
            "id": "lesson_ts_原型模式与类型编程_2", "title": "高级类型挑战与调试",
            "topic": "原型模式与类型编程",
            "content": (
                        "类型体操常见练习题：实现 DeepReadonly、TupleToUnion、StringToUnion、LengthOfString、Flatten 等。推荐 type-challenges"
                        "项目练习。类型调试技巧：(1) 用 IDE 的 hover 查看推导结果；(2) 用 `type _Debug<T> = { [K in keyof T]: T[K] }` 展平复杂类型；(3)"
                        "在临时变量上赋值错误观察类型提示。类型性能优化：避免深层嵌套递归、减少分布式条件类型的联合成员数量、避免不必要的 `infer` 操作。已知限制：(1) 类型不支持变异（无循环/赋值）；(2)"
                        "字符串长度无直接内建（需递归 'length'）；(3) 复杂递归可能达到编译器深度限制（约 50 层）。ts-toolbelt / type-fest 提供 200+ 预构建工具类型，覆盖绝大多数日常和进阶需求。"
            ),
            "examples": [
                        """
                        // StringToUnion 类型挑战
                        // type StringToUnion<T extends string> =
                        //     T extends `${infer F}${infer R}` ? F | StringToUnion<R> : never;
                        // type Test = StringToUnion<'hello'>;  // 'h' | 'e' | 'l' | 'o'
                        
                        // 类型调试技巧
                        // type _Expand<T> = T extends infer O ? { [K in keyof O]: O[K] } : never;
                        // type Expanded = _Expand<SomeComplexType>;
                        
                        // Flatten 展平嵌套数组
                        // type Flatten<T extends any[]> =
                        //     T extends [infer First, ...infer Rest]
                        //         ? First extends any[]
                        //             ? [...Flatten<First>, ...Flatten<Rest>]
                        //             : [First, ...Flatten<Rest>]
                        //         : [];
                        """,
            ],
            "key_points": [
                        "类型体操练习建议 type-challenges 项目，覆盖从入门到地狱难度",
                        "用 _Expand/_Debug 辅助类型展平和调试",
                        "ts-toolbelt/type-fest 提供 200+ 预构建工具类型，避免重复造轮子",
            ],
        },
        ],
    },
]

# ================================================================
# Java 课程（10 个主题，每主题 2 节课）
# ================================================================
JAVA_LEARNING_PATH = [
    {
        "topic": "Java基础",
        "lessons": [
            {
                "id": "lesson_java_Java基础_1", "title": "语法与数据类型",
                "topic": "Java基础",
                "content": (
                    "Java 是强类型静态语言，所有变量必须先声明类型。8 种基本类型：byte/short/int/long/float/double/char/boolean。"
                    "引用类型包括类、接口、数组、枚举。自动装箱/拆箱在基本类型和包装类间转换。"
                    "`var` 关键字（Java 10+）支持局部变量类型推断：`var list = new ArrayList<String>()`。"
                    "`final` 修饰变量不可变、方法不可重写、类不可继承。`String` 不可变，每次修改创建新对象。"
                ),
                "examples": [
                    "int num = 42;\ndouble pi = 3.14;\nboolean flag = true;\nString name = \"Java\";\n// var 类型推断（Java 10+）\nvar list = new ArrayList<String>();\n// final 不可变\nfinal int MAX = 100;"
                ],
                "key_points": ["8 种基本类型 + 引用类型", "var 局部类型推断（Java 10+）", "final 常量/String 不可变"],
            },
            {
                "id": "lesson_java_Java基础_2", "title": "流程控制",
                "topic": "Java基础",
                "content": (
                    "分支：if-else、switch（支持 String 和枚举，Java 14+ 支持箭头语法和 yield）。"
                    "循环：for（含增强 for-each）、while、do-while。`break` 跳出循环，`continue` 跳过本次。"
                    "增强 switch 表达式（Java 14+）：`int result = switch (day) { case MON -> 1; case TUE -> 2; default -> 0; }`。"
                    "`instanceof` 模式匹配（Java 16+）：`if (obj instanceof String s) { System.out.println(s.length()); }`。"
                ),
                "examples": [
                    "// 增强 switch（Java 14+）\nString type = switch (score) {\n    case 90, 100 -> \"优秀\";\n    case 80, 89  -> \"良好\";\n    default -> \"其他\";\n};\n// instanceof 模式匹配\nif (obj instanceof String s) {\n    System.out.println(s.toUpperCase());\n}"
                ],
                "key_points": ["switch 支持箭头语法和 yield", "增强 for 遍历集合", "instanceof 模式匹配（Java 16+）"],
            },
        ],
    },
    {
        "topic": "Java集合",
        "lessons": [
            {
                "id": "lesson_java_Java集合_1", "title": "List、Set、Map",
                "topic": "Java集合",
                "content": (
                    "Collection 接口两大分支：List（有序可重复）和 Set（无序不重复）。Map 独立体系，键值对存储。"
                    "ArrayList 基于数组，随机访问 O(1)；LinkedList 双向链表，插入删除快。"
                    "HashSet 基于 HashMap，O(1) 查找；TreeSet 红黑树，有序。"
                    "HashMap O(1)，允许 null 键；TreeMap 红黑树排序；LinkedHashMap 保持插入顺序。"
                    "`Collections.unmodifiableList()` 创建不可变集合，`List.of()`（Java 9+）更简洁。"
                ),
                "examples": [
                    "List<String> list = new ArrayList<>(Arrays.asList(\"a\", \"b\", \"c\"));\nSet<Integer> set = new HashSet<>(Arrays.asList(1, 2, 3));\nMap<String, Integer> map = new HashMap<>();\nmap.put(\"apple\", 3); map.put(\"banana\", 5);\n// 不可变集合\nList<String> unmodifiable = List.of(\"x\", \"y\", \"z\");"
                ],
                "key_points": ["ArrayList 查询快/LinkedList 增删快", "HashSet/HashMap O(1)", "List.of() 不可变集合"],
            },
            {
                "id": "lesson_java_Java集合_2", "title": "Stream API",
                "topic": "Java集合",
                "content": (
                    "Stream API（Java 8）以声明式流水线处理集合：过滤(filter)、映射(map)、排序(sorted)、聚合(collect)。"
                    "惰性求值：中间操作（filter/map/sorted）不立即执行，终结操作（collect/forEach/count）触发计算。"
                    "Collectors 工具类：toList/toSet/toMap/groupingBy/partitioningBy/joining。"
                    "并行流 `.parallelStream()` 利用多核加速，注意线程安全。`flatMap` 展平嵌套结构。"
                ),
                "examples": [
                    "List<String> result = names.stream()\n    .filter(n -> n.startsWith(\"A\"))\n    .map(String::toUpperCase)\n    .sorted()\n    .collect(Collectors.toList());\n// 分组\nMap<Integer, List<User>> byAge = users.stream()\n    .collect(Collectors.groupingBy(User::getAge));"
                ],
                "key_points": ["filter/map/sorted 链式操作", "惰性求值 + 终结操作触发", "groupingBy/partitioningBy 分组"],
            },
        ],
    },
    {
        "topic": "Java OOP",
        "lessons": [
            {
                "id": "lesson_java_Java OOP_1", "title": "继承与多态",
                "topic": "Java OOP",
                "content": (
                    "Java 单继承（extends），一个类只能有一个直接父类。构造器先调用 super() 再初始化子类字段。"
                    "多态：父类引用指向子类对象，`Animal a = new Dog()`，调用方法时动态绑定到实际类型。"
                    "`@Override` 注解标记重写，编译器检查签名匹配。`super` 访问父类成员。"
                    "`instanceof` 运行时类型检查，向下转型需强制 `(Dog) animal`（Java 16+ 用模式匹配简化）。"
                ),
                "examples": [
                    "class Animal {\n    void sound() { System.out.println(\"动物叫\"); }\n}\nclass Dog extends Animal {\n    @Override void sound() { System.out.println(\"汪汪\"); }\n}\nAnimal pet = new Dog();  // 向上转型\npet.sound();  // 输出: 汪汪（多态）"
                ],
                "key_points": ["单继承 extends", "父类引用指向子类对象 = 多态", "@Override 编译检查"],
            },
            {
                "id": "lesson_java_Java OOP_2", "title": "抽象类与接口",
                "topic": "Java OOP",
                "content": (
                    "抽象类 `abstract class` 可有构造器、成员变量、已实现方法；接口 `interface` 只有常量和抽象方法（Java 8+ 支持 default/static 方法）。"
                    "一个类可实现多个接口（多继承行为），但不能多继承类。"
                    "接口默认方法 `default` 提供向后兼容的实现；静态方法属于接口本身。"
                    "`sealed` 类（Java 17+）限制谁可以继承：`public sealed class Shape permits Circle, Rectangle`。"
                ),
                "examples": [
                    "interface Flyable {\n    void fly();\n    default void land() { System.out.println(\"着陆\"); }\n}\ninterface Swimmable { void swim(); }\nclass Duck implements Flyable, Swimmable {\n    public void fly() { System.out.println(\"飞\"); }\n    public void swim() { System.out.println(\"游\"); }\n}"
                ],
                "key_points": ["抽象类 = 部分实现 + 构造器", "接口 = 纯契约 + default 方法", "sealed 类限制继承（Java 17+）"],
            },
        ],
    },
    {
        "topic": "Java异常",
        "lessons": [
            {
                "id": "lesson_java_Java异常_1", "title": "异常体系",
                "topic": "Java异常",
                "content": (
                    "Throwable 两大子类：Error（JVM 错误，不应捕获）和 Exception。Exception 分 RuntimeException（非受检）和其他（受检）。"
                    "受检异常必须 try-catch 或 throws 声明；非受检异常（NPE/IndexOutOfBounds）可不处理。"
                    "try-catch-finally：catch 按顺序匹配，finally 始终执行（return 前也会执行）。"
                    "try-with-resources（Java 7+）：自动关闭实现 AutoCloseable 的资源。"
                ),
                "examples": [
                    "// try-catch-finally\ntry {\n    int result = 10 / 0;\n} catch (ArithmeticException e) {\n    System.out.println(\"除零错误\");\n} finally {\n    System.out.println(\"始终执行\");\n}\n// try-with-resources\ntry (BufferedReader br = new BufferedReader(new FileReader(\"file.txt\"))) {\n    String line = br.readLine();\n}"
                ],
                "key_points": ["Error不可捕获 / Exception分受检非受检", "try-with-resources 自动关闭", "finally 在 return 前也会执行"],
            },
            {
                "id": "lesson_java_Java异常_2", "title": "自定义异常",
                "topic": "Java异常",
                "content": (
                    "继承 Exception 创建受检异常，继承 RuntimeException 创建非受检异常。"
                    "最佳实践：异常消息要具体（含上下文信息），不要空 catch，不要用异常控制流程。"
                    "异常链：构造器传入 cause 保留原始异常：`throw new ServiceException(\"Failed\", e)`。"
                    "全局异常处理：Spring 用 @ControllerAdvice + @ExceptionHandler 统一处理。"
                ),
                "examples": [
                    "class InsufficientFundsException extends Exception {\n    InsufficientFundsException(String msg) { super(msg); }\n}\nvoid withdraw(double amount) throws InsufficientFundsException {\n    if (amount > balance) throw new InsufficientFundsException(\"余额不足\");\n}\n// Spring 全局异常处理\n@ControllerAdvice\nclass GlobalHandler {\n    @ExceptionHandler(IllegalArgumentException.class)\n    ResponseEntity<?> handle(IllegalArgumentException e) {\n        return ResponseEntity.badRequest().body(e.getMessage());\n    }\n}"
                ],
                "key_points": ["继承 Exception/RuntimeException", "异常链保留 cause", "Spring @ControllerAdvice 统一处理"],
            },
        ],
    },
    {
        "topic": "Java并发",
        "lessons": [
            {
                "id": "lesson_java_Java并发_1", "title": "线程基础",
                "topic": "Java并发",
                "content": (
                    "创建线程：继承 Thread 或实现 Runnable（推荐），用 lambda `new Thread(() -> {...}).start()`。"
                    "Callable 有返回值 + 抛异常，配合 Future/FutureTask 获取结果。"
                    "线程池：Executors.newFixedThreadPool(n)，实际推荐用 ThreadPoolExecutor 显式设置参数。"
                    "线程状态：NEW → RUNNABLE → BLOCKED/WAITING/TIMED_WAITING → TERMINATED。"
                ),
                "examples": [
                    "// Runnable + Lambda\nnew Thread(() -> System.out.println(\"线程运行\")).start();\n// Callable + Future\nExecutorService pool = Executors.newFixedThreadPool(4);\nFuture<String> future = pool.submit(() -> \"结果\");\nString result = future.get();  // 阻塞等待\npool.shutdown();"
                ],
                "key_points": ["Runnable 无返回值, Callable 有", "ThreadPoolExecutor 优于 Executors", "线程 6 状态"],
            },
            {
                "id": "lesson_java_Java并发_2", "title": "锁与同步",
                "topic": "Java并发",
                "content": (
                    "`synchronized` 方法或代码块保证互斥，monitor 锁自动释放。静态 synchronized 锁类对象。"
                    "`volatile` 保证可见性和禁止指令重排，但不保证原子性（i++ 仍需锁）。"
                    "`ReentrantLock` 更灵活：tryLock、公平锁、Condition 条件变量。`ReadWriteLock` 读多写少优化。"
                    "`ConcurrentHashMap` 分段锁，`CopyOnWriteArrayList` 写时复制，`AtomicInteger` CAS 无锁。"
                ),
                "examples": [
                    "// synchronized 方法\nsynchronized void transfer(Account to, double amount) {\n    this.balance -= amount;\n    to.balance += amount;\n}\n// ReentrantLock\nLock lock = new ReentrantLock();\nlock.lock();\ntry { /* 临界区 */ } finally { lock.unlock(); }\n// AtomicInteger\nAtomicInteger counter = new AtomicInteger(0);\ncounter.incrementAndGet();  // 原子操作"
                ],
                "key_points": ["synchronized 互斥 / volatile 可见", "ReentrantLock tryLock/公平锁", "ConcurrentHashMap/AtomicInteger"],
            },
        ],
    },
    {
        "topic": "Spring Boot",
        "lessons": [
            {
                "id": "lesson_java_Spring Boot_1", "title": "起步与自动配置",
                "topic": "Spring Boot",
                "content": (
                    "Spring Boot 简化 Spring 应用创建：起步依赖（spring-boot-starter-web）和自动配置（@SpringBootApplication）。"
                    "@SpringBootApplication = @Configuration + @EnableAutoConfiguration + @ComponentScan。"
                    "application.yml/properties 配置参数，@Value 或 @ConfigurationProperties 注入。"
                    "`SpringApplication.run()` 启动嵌入式 Tomcat，无需部署到外部服务器。"
                ),
                "examples": [
                    "@SpringBootApplication\npublic class App {\n    public static void main(String[] args) {\n        SpringApplication.run(App.class, args);\n    }\n}\n// 配置注入 @Value\n@Value(\"${app.name}\")\nprivate String appName;"
                ],
                "key_points": ["@SpringBootApplication 一键启动", "starter 依赖自动配置", "application.yml/@Value 配置"],
            },
            {
                "id": "lesson_java_Spring Boot_2", "title": "Web 开发",
                "topic": "Spring Boot",
                "content": (
                    "@RestController = @Controller + @ResponseBody，返回 JSON 而非视图。"
                    "@RequestMapping/@GetMapping/@PostMapping 映射 HTTP 方法和路径，@PathVariable/@RequestParam 绑定参数。"
                    "@RequestBody 接收 JSON 请求体自动反序列化，@Valid + BindingResult 参数校验。"
                    "Spring Data JPA：@Entity 映射表，继承 JpaRepository 获得 CRUD 方法。@Transactional 声明事务。"
                ),
                "examples": [
                    "@RestController\n@RequestMapping(\"/api/users\")\npublic class UserController {\n    @GetMapping(\"/{id}\")\n    public User getById(@PathVariable Long id) { return userService.findById(id); }\n    @PostMapping\n    public User create(@Valid @RequestBody User user) { return userService.save(user); }\n}\n// JPA Repository\npublic interface UserRepo extends JpaRepository<User, Long> {\n    List<User> findByName(String name);\n}"
                ],
                "key_points": ["@RestController 返回 JSON", "@GetMapping/@PostMapping 映射", "JpaRepository CRUD + 方法命名查询"],
            },
        ],
    },
    {
        "topic": "Java Lambda",
        "lessons": [
            {
                "id": "lesson_java_Java Lambda_1", "title": "Lambda 语法",
                "topic": "Java Lambda",
                "content": (
                    "Lambda 表达式：(参数) -> { 方法体 }，替代匿名内部类。单行可省略 {} 和 return。"
                    "函数式接口：只有一个抽象方法的接口，@FunctionalInterface 标注，如 Runnable/Comparator/Predicate。"
                    "内置函数接口：Predicate<T>（断言）、Function<T,R>（转换）、Consumer<T>（消费）、Supplier<T>（提供）。"
                    "Lambda 捕获外部变量要求其 effectively final（赋值后不再改变）。"
                ),
                "examples": [
                    "// Lambda 替代匿名类\nnew Thread(() -> System.out.println(\"Hi\")).start();\n// Predicate 过滤\nPredicate<String> isLong = s -> s.length() > 5;\nlist.stream().filter(isLong).collect(Collectors.toList());\n// Function 转换\nFunction<String, Integer> toLength = String::length;\ntoLength.apply(\"hello\");  // 5"
                ],
                "key_points": ["(参数) -> { 方法体 }", "@FunctionalInterface 函数式接口", "Predicate/Function/Consumer/Supplier"],
            },
            {
                "id": "lesson_java_Java Lambda_2", "title": "方法引用",
                "topic": "Java Lambda",
                "content": (
                    "方法引用四种形式：静态方法 `ClassName::staticMethod`、实例方法 `object::method`、"
                    "特定类型 `String::length`、构造器 `ClassName::new`。"
                    "方法引用本质是 Lambda 的简写，比 Lambda 更简洁但适用场景更窄。"
                    "Optional 链式调用配合 Lambda 优雅处理 null：`opt.map(User::getName).orElse(\"Unknown\")`。"
                ),
                "examples": [
                    "// 四种方法引用\nlist.forEach(System.out::println);              // 实例方法\nlist.stream().map(String::toUpperCase);          // 特定类型\nlist.stream().map(User::new);                     // 构造器\nlist.sort(Comparator.comparing(User::getAge));   // Lambda 组合\n// Optional\nOptional.ofNullable(user).map(User::getName).orElse(\"未知\");"
                ],
                "key_points": ["四种方法引用形式", ":: 语法比 Lambda 更简洁", "Optional 链式避免 NPE"],
            },
        ],
    },
    {
        "topic": "Java泛型",
        "lessons": [
            {
                "id": "lesson_java_Java泛型_1", "title": "泛型类与方法",
                "topic": "Java泛型",
                "content": (
                    "泛型类：`class Box<T>`，T 占位符在实际使用时指定。泛型方法：`<T> T method(T arg)`。"
                    "类型擦除：编译后泛型参数被擦除为 Object 或上界类型，运行时无法获取泛型类型。"
                    "上界通配符 `? extends T` 只读（生产者），下界通配符 `? super T` 只写（消费者）。"
                    "PECS 原则：Producer Extends, Consumer Super。`Collections.copy(dest, src)` 是经典例子。"
                ),
                "examples": [
                    "// 泛型类\nclass Box<T> {\n    private T value;\n    T get() { return value; }\n    void set(T v) { value = v; }\n}\n// 泛型方法\n<T> T identity(T arg) { return arg; }\n// PECS\nvoid copy(List<? super String> dest, List<? extends String> src) {\n    for (String s : src) dest.add(s);\n}"
                ],
                "key_points": ["类型擦除：运行时无泛型信息", "? extends T 只读 / ? super T 只写", "PECS: Producer Extends, Consumer Super"],
            },
            {
                "id": "lesson_java_Java泛型_2", "title": "通配符与类型推断",
                "topic": "Java泛型",
                "content": (
                    "无界通配符 `?`：`List<?>` 可接受任何 List，但只能读（取出 Object）。"
                    "泛型数组不可直接创建：`new T[10]` 非法，用 `(T[]) new Object[10]` 强制转换。"
                    "类型推断（Java 7+）：`List<String> list = new ArrayList<>()`，菱形语法省略右侧泛型。"
                    "Java 10+ `var` 进一步简化：`var list = new ArrayList<String>()`，左边也省略。"
                ),
                "examples": [
                    "// 无界通配符\nvoid printAll(List<?> list) {\n    for (Object o : list) System.out.println(o);\n}\n// 菱形语法\nMap<String, List<Integer>> map = new HashMap<>();\n// 泛型桥方法（编译器自动生成，确保多态正确）\n// 反编译可见，开发无需手动编写"
                ],
                "key_points": ["无界通配符 ? 只读", "菱形语法 <> 类型推断", "泛型桥方法编译器自动生成"],
            },
        ],
    },
    {
        "topic": "Java IO",
        "lessons": [
            {
                "id": "lesson_java_Java IO_1", "title": "字节流与字符流",
                "topic": "Java IO",
                "content": (
                    "InputStream/OutputStream 字节流（二进制），Reader/Writer 字符流（文本）。"
                    "装饰器模式：BufferedInputStream 缓冲包装，ObjectInputStream 序列化，GZIPOutputStream 压缩。"
                    "try-with-resources（Java 7+）自动关闭流，无需 finally 手动 close。"
                    "Files 工具类（Java 7+ NIO.2）：`Files.readAllLines(path)` 一次性读取，`Files.copy()` / `Files.move()`。"
                ),
                "examples": [
                    "// 字节流拷贝\ntry (FileInputStream in = new FileInputStream(\"src\");\n     FileOutputStream out = new FileOutputStream(\"dst\")) {\n    byte[] buf = new byte[1024];\n    int n;\n    while ((n = in.read(buf)) != -1) out.write(buf, 0, n);\n}\n// Files 一行读取\nList<String> lines = Files.readAllLines(Path.of(\"file.txt\"));"
                ],
                "key_points": ["字节流 InputStream/OutputStream", "字符流 Reader/Writer", "try-with-resources + Files 工具类"],
            },
            {
                "id": "lesson_java_Java IO_2", "title": "NIO 基础",
                "topic": "Java IO",
                "content": (
                    "Java NIO（New IO）：Channel（双向通道）+ Buffer（缓冲区）+ Selector（多路复用）。"
                    "`ByteBuffer` 核心操作：allocate/put/flip/get/clear。flip() 切换写模式到读模式。"
                    "`FileChannel` 支持随机读写和内存映射（MappedByteBuffer）。`Path` 替代 `File` 成为标准路径 API。"
                    "NIO 非阻塞模式配合 Selector 实现单线程管理多连接，是 Netty 等框架的基础。"
                ),
                "examples": [
                    "// FileChannel + ByteBuffer\ntry (FileChannel channel = FileChannel.open(Path.of(\"file.txt\"), StandardOpenOption.READ)) {\n    ByteBuffer buf = ByteBuffer.allocate(1024);\n    channel.read(buf);\n    buf.flip();\n    while (buf.hasRemaining()) System.out.print((char) buf.get());\n}\n// Path API\nPath path = Path.of(\"a\", \"b\", \"c.txt\");\nFiles.createDirectories(path.getParent());"
                ],
                "key_points": ["Channel + Buffer + Selector 三要素", "flip() 切换读写模式", "Path 替代 File"],
            },
        ],
    },
    {
        "topic": "Java注解",
        "lessons": [
            {
                "id": "lesson_java_Java注解_1", "title": "内置注解",
                "topic": "Java注解",
                "content": (
                    "@Override 编译检查重写，@Deprecated 标记废弃，@SuppressWarnings 抑制警告。"
                    "@FunctionalInterface 确保接口只有一个抽象方法。@SafeVarargs 抑制泛型可变参数警告。"
                    "元注解：@Target 指定作用位置（TYPE/METHOD/FIELD），@Retention 控制保留级别（SOURCE/CLASS/RUNTIME）。"
                    "@Documented 包含进 javadoc，@Inherited 允许子类继承，@Repeatable 允许多次使用同一注解。"
                ),
                "examples": [
                    "@Override\npublic String toString() { return \"自定义\"; }\n\n@SuppressWarnings(\"unchecked\")\nList raw = new ArrayList();  // 抑制警告"
                ],
                "key_points": ["@Override/@Deprecated/@SuppressWarnings", "@FunctionalInterface", "元注解: @Target/@Retention"],
            },
            {
                "id": "lesson_java_Java注解_2", "title": "自定义注解与处理",
                "topic": "Java注解",
                "content": (
                    "自定义注解用 `@interface` 声明，成员用 `类型 方法名() default 默认值`。"
                    "运行时注解通过反射读取：`Method.getAnnotation(MyAnno.class)` 获取注解实例。"
                    "注解处理器（APT）：`AbstractProcessor` 在编译期处理注解，生成代码（Lombok、MapStruct 原理）。"
                    "Spring 自定义注解组合：`@Transactional(readOnly=true)` 可封装为自定义 @ReadOnlyTransactional。"
                ),
                "examples": [
                    "@Retention(RetentionPolicy.RUNTIME)\n@Target(ElementType.METHOD)\n@interface Log {\n    String value() default \"\";\n    int level() default 1;\n}\n@Log(value = \"登录\", level = 2)\nvoid login() { /* ... */ }\n// 反射读取\nMethod m = obj.getClass().getMethod(\"login\");\nLog log = m.getAnnotation(Log.class);\nSystem.out.println(log.value());  // \"登录\""
                ],
                "key_points": ["@interface + default 默认值", "反射 getAnnotation 读取", "APT 编译时代码生成"],
            },
        ],
    },
    {
        "topic": "反射与动态代理",
        "lessons": [
        {
            "id": "lesson_java_反射与动态代理_1", "title": "反射机制",
            "topic": "反射与动态代理",
            "content": (
                        "反射（Reflection）在运行时检查和修改类、方法、字段。`Class<?> clazz = obj.getClass()` 获取类对象，`Class.forName(\"com.example.User\")`"
                        "按名加载。获取构造器：`Constructor<?> ctor = clazz.getDeclaredConstructor(String.class, int.class)`，`ctor.newInstance()`"
                        "创建实例（Java 9+ 推荐取代 Class.newInstance()）。获取方法并调用：`Method m = clazz.getDeclaredMethod(\"setName\","
                        "String.class)`，`m.invoke(obj, \"Alice\")`。`setAccessible(true)` 突破 private 限制。获取和修改字段：`Field f ="
                        "clazz.getDeclaredField(\"name\")`，`f.set(obj, value)`。性能开销大，应缓存 Class/Method/Field 对象。反射应用：框架（Spring"
                        "IOC、MyBatis ORM）、序列化库（Jackson、Gson）、单元测试（JUnit @Test 发现）、IDE 自动补全。"
            ),
            "examples": [
                        """
                        // 反射创建对象并调用方法
                        Class<?> clazz = Class.forName("com.example.User");
                        Constructor<?> ctor = clazz.getDeclaredConstructor();
                        Object user = ctor.newInstance();
                        
                        Method setName = clazz.getDeclaredMethod("setName", String.class);
                        setName.invoke(user, "Alice");
                        
                        Method getName = clazz.getDeclaredMethod("getName");
                        String name = (String) getName.invoke(user);
                        System.out.println(name); // Alice
                        """,
                        """
                        // 反射读取注解
                        if (clazz.isAnnotationPresent(Table.class)) {
                            Table table = clazz.getAnnotation(Table.class);
                            System.out.println(table.name());
                        }
                        for (Field f : clazz.getDeclaredFields()) {
                            if (f.isAnnotationPresent(Column.class)) {
                                Column col = f.getAnnotation(Column.class);
                                // 映射字段到数据库列
                            }
                        }
                        """,
            ],
            "key_points": [
                        "Class.forName / getDeclaredConstructor / invoke 核心反射 API",
                        "setAccessible(true) 突破 private，但应缓存反射对象避免性能损失",
                        "反射是 Spring IOC、JUnit、ORM 框架的核心机制",
            ],
        },
        {
            "id": "lesson_java_反射与动态代理_2", "title": "动态代理",
            "topic": "反射与动态代理",
            "content": (
                        "JDK 动态代理：`Proxy.newProxyInstance(classLoader, interfaces, InvocationHandler)` 在运行时创建接口代理类。代理对象的所有方法调用都被拦截到"
                        "invoke 方法。CGLIB（Code Generation Library）：通过继承目标类创建子类代理，不要求接口。Spring AOP 默认 JDK 代理（有接口时）或"
                        "CGLIB（无接口时）。`InvocationHandler.invoke(proxy, method, args)` 在方法调用前后插入横切逻辑（日志、事务、权限检查）。动态代理应用：Spring"
                        "AOP（@Transactional、@Cacheable）、MyBatis Mapper 接口代理、RPC 框架远程调用代理。性能对比：JDK"
                        "代理（纯反射）较慢但无依赖，CGLIB（字节码生成）更快但创建开销大。现代 Java 用 MethodHandle 可提升代理性能。"
            ),
            "examples": [
                        """
                        // JDK 动态代理
                        interface UserService {
                            void save(String name);
                            String findById(int id);
                        }
                        
                        InvocationHandler handler = (proxy, method, args) -> {
                            System.out.println("Before: " + method.getName());
                            Object result = method.invoke(target, args);
                            System.out.println("After: " + method.getName());
                            return result;
                        };
                        
                        UserService proxy = (UserService) Proxy.newProxyInstance(
                            UserService.class.getClassLoader(),
                            new Class<?>[]{UserService.class},
                            handler
                        );
                        proxy.save("Alice"); // 自动经过 handler.invoke
                        """,
                        """
                        // Spring AOP 原理示意
                        // @Aspect + @Around 在编译后等价于创建代理类
                        // @Transactional 方法调用实际走代理对象，在 invoke 中开启/提交事务
                        """,
            ],
            "key_points": [
                        "JDK 动态代理：Proxy + InvocationHandler 拦截接口方法",
                        "CGLIB 继承目标类生成子类代理，Spring AOP 自动选择代理方式",
                        "核心应用：Spring AOP 切面、MyBatis Mapper、RPC 存根",
            ],
        },
        ],
    },
    {
        "topic": "并发编程进阶",
        "lessons": [
        {
            "id": "lesson_java_并发编程进阶_1", "title": "并发集合与工具类",
            "topic": "并发编程进阶",
            "content": (
                        "ConcurrentHashMap（JDK 1.5+）：分段锁 → CAS + synchronized 细粒度锁（JDK 8+），高并发下性能远优于 Hashtable 和"
                        "Collections.synchronizedMap。CopyOnWriteArrayList：写时复制，读无锁且不会"
                        "ConcurrentModificationException，适合读多写少场景（如监听器列表）。BlockingQueue"
                        "接口：ArrayBlockingQueue（有界数组）、LinkedBlockingQueue（可选有界链表）、SynchronousQueue（零容量直接交付，CachedThreadPool"
                        "使用）。`put/take` 阻塞方法，`offer/poll` 带超时。生产者-消费者模式完美匹配 BlockingQueue。CountDownLatch：一次性栅栏，主线程等待 N"
                        "个子任务完成。CyclicBarrier：可重复使用，N 个线程互相等待到齐后同时继续。Semaphore：许可信号量，限流控制。"
            ),
            "examples": [
                        """
                        // ConcurrentHashMap 原子操作
                        ConcurrentHashMap<String, Integer> map = new ConcurrentHashMap<>();
                        map.computeIfAbsent("key", k -> 0);       // 不存在时计算
                        map.computeIfPresent("key", (k, v) -> v + 1); // 存在时自增
                        map.merge("count", 1, Integer::sum);       // 原子合并
                        
                        // BlockingQueue 生产者-消费者
                        BlockingQueue<String> queue = new LinkedBlockingQueue<>(100);
                        // 生产者
                        new Thread(() -> { while (true) queue.put(produce()); }).start();
                        // 消费者
                        new Thread(() -> { while (true) consume(queue.take()); }).start();
                        """,
                        """
                        // CountDownLatch：等待所有服务初始化
                        CountDownLatch latch = new CountDownLatch(3);
                        for (int i = 0; i < 3; i++) {
                            new Thread(() -> {
                                initService();
                                latch.countDown();
                            }).start();
                        }
                        latch.await(); // 等待全部完成
                        System.out.println("All services ready");
                        """,
            ],
            "key_points": [
                        "ConcurrentHashMap 原子操作（computeIfAbsent/merge）替代手动锁",
                        "BlockingQueue put/take 阻塞，offer/poll 超时，完美实现生产者-消费者",
                        "CountDownLatch 一次性等待、CyclicBarrier 循环同步、Semaphore 限流",
            ],
        },
        {
            "id": "lesson_java_并发编程进阶_2", "title": "CompletableFuture 异步编排",
            "topic": "并发编程进阶",
            "content": (
                        "CompletableFuture（Java 8+）是 Promise/Future 的增强版，支持链式异步编排。`supplyAsync(() -> result)` 提交有返回值任务到"
                        "ForkJoinPool。链式转换：`thenApply`（同步转换）、`thenAccept`（消费结果）、`thenRun`（不依赖结果执行）、`thenCompose`（扁平化 Future"
                        "嵌套）。组合：`thenCombine(cf, (a, b) -> result)` 等待两个都完成；`applyToEither(cf, fn)` 任一完成即处理。`allOf`"
                        "等待全部完成。异常处理：`exceptionally(ex -> fallback)` 捕获异常返回默认值，`handle((result, ex) -> {})` 同时处理成功和失败。超时控制（Java"
                        "9+）：`orTimeout(5, TimeUnit.SECONDS)` 超时抛异常，`completeOnTimeout(default, 5, SECONDS)` 超时返回默认值。"
            ),
            "examples": [
                        """
                        // 异步编排链
                        CompletableFuture<User> userFuture = CompletableFuture.supplyAsync(() -> fetchUser(id));
                        CompletableFuture<Order> orderFuture = CompletableFuture.supplyAsync(() -> fetchOrders(userId));
                        
                        CompletableFuture<String> result = userFuture
                            .thenCombine(orderFuture, (user, orders) -> {
                                return String.format("%s has %d orders", user.getName(), orders.size());
                            })
                            .exceptionally(ex -> "Error: " + ex.getMessage())
                            .orTimeout(3, TimeUnit.SECONDS);
                        
                        // allOf 等待全部
                        CompletableFuture.allOf(userFuture, orderFuture).join();
                        """,
                        """
                        // 实际应用：聚合多个 API 调用
                        // var price = CompletableFuture.supplyAsync(() -> priceService.getPrice());
                        // var stock = CompletableFuture.supplyAsync(() -> stockService.getStock());
                        // var rating = CompletableFuture.supplyAsync(() -> ratingService.getRating());
                        // CompletableFuture.allOf(price, stock, rating).join();
                        // ProductDetail detail = new ProductDetail(price.get(), stock.get(), rating.get());
                        """,
            ],
            "key_points": [
                        "supplyAsync 异步计算 → thenApply/thenCompose/thenCombine 链式编排",
                        "exceptionally/handle 异常处理，orTimeout 超时控制（Java 9+）",
                        "allOf 等待全部完成，anyOf 任一完成即继续",
            ],
        },
        ],
    },
    {
        "topic": "网络编程",
        "lessons": [
        {
            "id": "lesson_java_网络编程_1", "title": "Socket 与 NIO 网络模型",
            "topic": "网络编程",
            "content": (
                        "Socket 编程：`ServerSocket.accept()` 阻塞等待连接，`Socket.getInputStream/getOutputStream` 读写数据。每个连接一个线程模型简单但不可扩展。NIO"
                        "Selector 多路复用：单个线程管理多个 Channel，`selector.select()` 阻塞等待就绪事件（OP_ACCEPT/OP_READ/OP_WRITE）。`ServerSocketChannel`"
                        "注册 OP_ACCEPT，接受连接后 `SocketChannel` 注册 OP_READ。SelectionKey 携带就绪的 Channel。ByteBuffer"
                        "三个关键属性：capacity（容量）、position（当前位置）、limit（读取界限）。`flip()` 写模式→读模式，`clear()` 重置。Netty 框架封装 NIO 复杂性：Boss Group"
                        "接受连接，Worker Group 处理 IO。ChannelPipeline + ChannelHandler 责任链模式处理数据。"
            ),
            "examples": [
                        """
                        // NIO Selector 基础
                        Selector selector = Selector.open();
                        ServerSocketChannel ssc = ServerSocketChannel.open();
                        ssc.bind(new InetSocketAddress(8080));
                        ssc.configureBlocking(false);
                        ssc.register(selector, SelectionKey.OP_ACCEPT);
                        
                        while (true) {
                            selector.select();  // 阻塞等待就绪
                            for (SelectionKey key : selector.selectedKeys()) {
                                if (key.isAcceptable()) {
                                    SocketChannel sc = ssc.accept();
                                    sc.configureBlocking(false);
                                    sc.register(selector, SelectionKey.OP_READ);
                                } else if (key.isReadable()) {
                                    SocketChannel sc = (SocketChannel) key.channel();
                                    ByteBuffer buf = ByteBuffer.allocate(1024);
                                    sc.read(buf);
                                    buf.flip();
                                    // 处理数据...
                                }
                            }
                            selector.selectedKeys().clear();
                        }
                        """,
            ],
            "key_points": [
                        "NIO Selector 单线程管理多 Channel，比一连接一线程高 N 倍并发",
                        "ByteBuffer flip/clear 切换读写模式，capacity/position/limit 三属性",
                        "Netty Boss/Worker EventLoopGroup + Pipeline 封装 NIO 复杂性",
            ],
        },
        {
            "id": "lesson_java_网络编程_2", "title": "HTTP 客户端与 REST 调用",
            "topic": "网络编程",
            "content": (
                        "HttpClient（Java 11+ 正式 API）：`HttpClient.newHttpClient()` 创建客户端，`HttpRequest.newBuilder().uri().GET().build()`"
                        "构建请求。同步 `send(req, BodyHandlers.ofString())` vs 异步 `sendAsync(req,"
                        "BodyHandlers.ofString()).thenApply(...)`。HTTP/2"
                        "原生支持：`HttpClient.newBuilder().version(HttpClient.Version.HTTP_2)`，连接池复用。WebSocket"
                        "支持：`newWebSocketBuilder().buildAsync(uri, listener)`。Spring RestClient（Spring"
                        "6.1+）：`RestClient.create().get().uri(...).retrieve().body(User.class)` 替代 RestTemplate。OpenFeign 声明式 HTTP"
                        "客户端：`@FeignClient(name=\"user-service\") interface UserClient { @GetMapping(\"/{id}\") User getById(@PathVariable"
                        "Long id); }` 自动生成实现。"
            ),
            "examples": [
                        """
                        // Java 11 HttpClient
                        HttpClient client = HttpClient.newBuilder()
                            .connectTimeout(Duration.ofSeconds(10))
                            .build();
                        
                        HttpRequest request = HttpRequest.newBuilder()
                            .uri(URI.create("https://api.example.com/users/1"))
                            .header("Accept", "application/json")
                            .GET()
                            .build();
                        
                        HttpResponse<String> response = client.send(request, BodyHandlers.ofString());
                        System.out.println(response.statusCode());
                        System.out.println(response.body());
                        
                        // 异步调用
                        // CompletableFuture<HttpResponse<String>> future = client.sendAsync(request, BodyHandlers.ofString());
                        // future.thenAccept(resp -> System.out.println(resp.body()));
                        """,
                        """
                        // Spring RestClient（Spring 6.1+）
                        // User user = restClient.get()
                        //     .uri("/users/{id}", 1)
                        //     .accept(MediaType.APPLICATION_JSON)
                        //     .retrieve()
                        //     .body(User.class);
                        """,
            ],
            "key_points": [
                        "HttpClient（Java 11+）原生 HTTP/2 + WebSocket + 异步支持",
                        "Spring RestClient（6.1+）替代 RestTemplate，流式 API 更现代化",
                        "OpenFeign 声明式接口自动生成 HTTP 客户端实现",
            ],
        },
        ],
    },
    {
        "topic": "JDBC 与数据库",
        "lessons": [
        {
            "id": "lesson_java_JDBC 与数据库_1", "title": "JDBC 核心操作",
            "topic": "JDBC 与数据库",
            "content": (
                        "JDBC（Java Database Connectivity）是 Java 标准数据库访问 API。核心流程：加载驱动 → 获取连接 → 创建 Statement → 执行 SQL → 处理 ResultSet →"
                        "释放资源。`DriverManager.getConnection(url, user, password)` 获取连接。try-with-resources 自动关闭"
                        "Connection/Statement/ResultSet。PreparedStatement 预编译防 SQL 注入：`conn.prepareStatement(\"SELECT * FROM users"
                        "WHERE id = ?\")`，用 `setInt(1, id)` 绑定参数。事务控制：`conn.setAutoCommit(false)` 开启事务，`conn.commit()`"
                        "提交，`conn.rollback()` 回滚。批量操作：`stmt.addBatch()` + `stmt.executeBatch()`。"
            ),
            "examples": [
                        """
                        // JDBC 基本流程（try-with-resources）
                        String url = "jdbc:mysql://localhost:3306/mydb";
                        try (Connection conn = DriverManager.getConnection(url, "user", "pass");
                             PreparedStatement stmt = conn.prepareStatement("SELECT * FROM users WHERE age > ?")) {
                            stmt.setInt(1, 18);
                            try (ResultSet rs = stmt.executeQuery()) {
                                while (rs.next()) {
                                    System.out.println(rs.getString("name"));
                                }
                            }
                        }
                        
                        // 事务 + 批量
                        conn.setAutoCommit(false);
                        try (PreparedStatement stmt = conn.prepareStatement("INSERT INTO logs VALUES (?, ?)")) {
                            for (Log log : logs) {
                                stmt.setLong(1, log.getId());
                                stmt.setString(2, log.getMsg());
                                stmt.addBatch();
                            }
                            stmt.executeBatch();
                            conn.commit();
                        } catch (Exception e) {
                            conn.rollback();
                            throw e;
                        }
                        """,
            ],
            "key_points": [
                        "PreparedStatement 预编译防 SQL 注入 + 参数绑定",
                        "try-with-resources 自动管理 Connection/Statement/ResultSet 生命周期",
                        "setAutoCommit(false) → commit/rollback 事务控制，addBatch/executeBatch 批量操作",
            ],
        },
        {
            "id": "lesson_java_JDBC 与数据库_2", "title": "连接池与 ORM 原理",
            "topic": "JDBC 与数据库",
            "content": (
                        "连接池原理：预先创建一组连接复用，避免每次请求创建/销毁连接的开销。HikariCP 是默认连接池（Spring Boot 2+），速度和可靠性业界最佳。HikariCP"
                        "配置：`maximumPoolSize`（最大连接数）、`minimumIdle`（最小空闲）、`connectionTimeout`（等待超时）、`idleTimeout`（空闲回收）。ORM（对象关系映射）核心：实体类"
                        "→ 表映射（@Entity/@Table），字段 → 列映射（@Column），关联映射（@OneToMany/@ManyToOne）。JPA/Hibernate 工作流：EntityManager"
                        "管理持久化上下文，一级缓存自动脏检查，`em.persist/merge/remove` 操作实体触发 SQL。JDBC Template（Spring）：`jdbcTemplate.query(sql,"
                        "rowMapper, params)` 简化样板代码，自动资源管理。适合轻量级数据库操作。"
            ),
            "examples": [
                        """
                        // HikariCP 连接池配置
                        HikariConfig config = new HikariConfig();
                        config.setJdbcUrl("jdbc:mysql://localhost:3306/mydb");
                        config.setUsername("user");
                        config.setPassword("pass");
                        config.setMaximumPoolSize(20);
                        config.setMinimumIdle(5);
                        
                        HikariDataSource ds = new HikariDataSource(config);
                        try (Connection conn = ds.getConnection()) {
                            // 操作数据库...
                        }
                        
                        // Spring JdbcTemplate
                        @Repository
                        class UserDao {
                            private final JdbcTemplate jdbc;
                            public List<User> findByAge(int minAge) {
                                return jdbc.query(
                                    "SELECT * FROM users WHERE age > ?",
                                    (rs, rowNum) -> new User(rs.getLong("id"), rs.getString("name")),
                                    minAge
                                );
                            }
                        }
                        """,
            ],
            "key_points": [
                        "HikariCP 连接池复用连接，maximumPoolSize/minimumIdle 核心参数",
                        "ORM 实体映射 + EntityManager 持久化上下文，自动脏检查 + SQL 生成",
                        "JdbcTemplate 简化 JDBC 样板代码，适合轻量级和需要精确控制 SQL 的场景",
            ],
        },
        ],
    },
    {
        "topic": "构建工具与依赖管理",
        "lessons": [
        {
            "id": "lesson_java_构建工具与依赖管理_1", "title": "Maven 核心概念",
            "topic": "构建工具与依赖管理",
            "content": (
                        "Maven 基于 POM（Project Object"
                        "Model）管理项目。核心配置：groupId（组织标识）、artifactId（项目名）、version（版本）。坐标（GAV）唯一标识一个构件：`<groupId>com.example</groupId><artifactId>my-lib</artifactId><version>1.0.0</version>`。依赖管理：`<dependencies>`"
                        "声明直接依赖，`<dependencyManagement>` 统一版本管理。scope 控制依赖范围：compile（默认）/ runtime / provided / test。传递性依赖 +"
                        "仲裁机制：最短路径优先，同路径长度时声明顺序优先。`mvn dependency:tree` 查看依赖树。Maven 生命周期：clean（清理）→ validate → compile → test →"
                        "package → verify → install → deploy。插件绑定到各阶段。"
            ),
            "examples": [
                        """
                        <!-- pom.xml 核心结构 -->
                        <project>
                            <groupId>com.example</groupId>
                            <artifactId>my-app</artifactId>
                            <version>1.0.0</version>
                            <packaging>jar</packaging>
                        
                            <dependencies>
                                <dependency>
                                    <groupId>org.springframework.boot</groupId>
                                    <artifactId>spring-boot-starter-web</artifactId>
                                    <version>3.2.0</version>
                                </dependency>
                                <dependency>
                                    <groupId>org.projectlombok</groupId>
                                    <artifactId>lombok</artifactId>
                                    <scope>provided</scope> <!-- 编译时需要，运行时不打包 -->
                                </dependency>
                            </dependencies>
                        </project>
                        """,
            ],
            "key_points": [
                        "Maven GAV 坐标唯一标识构件，POM 管理项目元数据与依赖",
                        "dependencyManagement 统一版本，scope 控制依赖范围（compile/runtime/provided/test）",
                        "mvn lifecycle（clean→compile→test→package→install→deploy）插件绑定各阶段",
            ],
        },
        {
            "id": "lesson_java_构建工具与依赖管理_2", "title": "Gradle 与依赖冲突",
            "topic": "构建工具与依赖管理",
            "content": (
                        "Gradle 基于 Groovy/Kotlin DSL，比 Maven 更灵活和高效。`build.gradle(.kts)` 中 `dependencies {"
                        "implementation('group:artifact:version') }` 声明依赖。Maven vs Gradle 依赖配置映射：`implementation` ≈"
                        "compile（但不会传递泄漏），`api` = compile（传递），`compileOnly` = provided，`testImplementation` = test。依赖冲突解决：(1)"
                        "`constraints` 强制版本；(2) `exclude` 排除传递依赖；(3) BOM（Bill of Materials）统一版本管理。Maven Enforcer Plugin / Gradle"
                        "Dependency Lock 锁定依赖版本，防止构建不一致。Gradle 的 `implementation` 优于 Maven compile（更快增量编译）。多模块项目：Maven `<modules>` +"
                        "`<parent>` 父子继承，Gradle `settings.gradle` + `include` 子项目 + `implementation project(':sub')` 项目依赖。"
            ),
            "examples": [
                        """
                        // build.gradle.kts (Gradle Kotlin DSL)
                        plugins {
                            id("java")
                            id("org.springframework.boot") version "3.2.0"
                        }
                        
                        dependencies {
                            implementation("org.springframework.boot:spring-boot-starter-web")
                            compileOnly("org.projectlombok:lombok")
                            annotationProcessor("org.projectlombok:lombok")
                            testImplementation("org.junit.jupiter:junit-jupiter")
                        }
                        
                        // 依赖冲突解决（constraints + exclude）
                        dependencies {
                            implementation("com.example:lib-a") {
                                exclude(group = "com.google.guava", module = "guava")  // 排除传递依赖
                            }
                            constraints {
                                implementation("com.google.guava:guava:33.0.0-jre") { because("安全修复") }
                            }
                        }
                        """,
                        """
                        // 多模块 Gradle
                        // settings.gradle.kts:
                        // rootProject.name = "my-project"
                        // include("core", "web", "cli")
                        // 子模块依赖其他子模块:
                        // implementation(project(":core"))
                        """,
            ],
            "key_points": [
                        "Gradle implementation 不传递泄漏（优于 Maven compile），api 传递暴露",
                        "constraints 强制版本 + exclude 排除传递依赖 + BOM 统一版本管理",
                        "多模块项目：Gradle settings.gradle + include + project(':module')",
            ],
        },
        ],
    },
    {
        "topic": "日期时间与国际化",
        "lessons": [
        {
            "id": "lesson_java_日期时间与国际化_1", "title": "java.time 时间 API",
            "topic": "日期时间与国际化",
            "content": (
                        "java.time（Java 8+）替代 java.util.Date 和"
                        "Calendar。核心类：LocalDate（日期）、LocalTime（时间）、LocalDateTime（日期+时间）、ZonedDateTime（带时区）、Instant（时间戳）。不可变 + 线程安全：所有"
                        "java.time 类都是不可变对象，比可变 Date/Calendar 更安全，操作返回新实例。`Duration` 表示时间量（秒+纳秒），`Period`"
                        "表示日期量（年月日）。`LocalDate.plus(Period.ofDays(7))` 加 7 天。格式化：`DateTimeFormatter.ofPattern(\"yyyy-MM-dd"
                        "HH:mm:ss\")`，`LocalDateTime.format(formatter)`。`DateTimeFormatter.ISO_LOCAL_DATE`"
                        "等预置格式。时区转换：`ZonedDateTime.of(localDateTime, ZoneId.of(\"Asia/Shanghai\"))` →"
                        "`withZoneSameInstant(ZoneId.of(\"America/New_York\"))`。"
            ),
            "examples": [
                        """
                        // java.time 常用操作
                        LocalDate today = LocalDate.now();
                        LocalDateTime now = LocalDateTime.now();
                        Instant instant = Instant.now();  // UTC 时间戳
                        
                        LocalDate nextWeek = today.plusWeeks(1);
                        LocalDate lastMonth = today.minusMonths(1);
                        long days = ChronoUnit.DAYS.between(today, nextWeek);  // 7
                        
                        // 格式化和解析
                        DateTimeFormatter fmt = DateTimeFormatter.ofPattern("yyyy-MM-dd");
                        String str = today.format(fmt);                 // "2024-06-26"
                        LocalDate parsed = LocalDate.parse("2024-06-26", fmt);
                        """,
                        """
                        // 时区转换
                        // ZonedDateTime shanghai = ZonedDateTime.now(ZoneId.of("Asia/Shanghai"));
                        // ZonedDateTime newYork = shanghai.withZoneSameInstant(ZoneId.of("America/New_York"));
                        """,
            ],
            "key_points": [
                        "LocalDate/LocalDateTime/Instant/ZonedDateTime 不可变线程安全",
                        "Duration 时间量 / Period 日期量，plus/minus 链式操作",
                        "DateTimeFormatter 自定义格式 + ZoneId 时区转换",
            ],
        },
        {
            "id": "lesson_java_日期时间与国际化_2", "title": "Records 与密封类新特性",
            "topic": "日期时间与国际化",
            "content": (
                        "Records（Java 16+）：`public record User(String name, int age) {}`"
                        "自动生成构造器、equals/hashCode、toString、访问器方法（name()/age()）。Records 是不可变数据载体，字段 private final，不能用 extends"
                        "被继承。可自定义构造器做参数校验（Compact Constructor）。适用场景：DTO/VO、配置对象、不可变键值、API 返回值。不适用：JPA"
                        "Entity（需要可变性）、有复杂继承层次的对象。密封类（Sealed Classes, Java 17+）：`public sealed class Shape permits Circle,"
                        "Rectangle`，限制只能被指定类继承。子类声明 `final`、`sealed` 或 `non-sealed`。模式匹配 switch（Java 21+）：`switch (obj) { case String"
                        "s -> ...; case Integer i -> ...; case null -> ...; default -> ...; }` 无需强制转换。"
            ),
            "examples": [
                        """
                        // Record
                        public record Point(int x, int y) {
                            // Compact Constructor（校验）
                            public Point {
                                if (x < 0 || y < 0) throw new IllegalArgumentException("坐标不能为负");
                            }
                            // 可添加实例方法
                            public double distanceFromOrigin() {
                                return Math.sqrt(x * x + y * y);
                            }
                        }
                        // Point p = new Point(3, 4); // x=3, y=4, 自动 equals/hashCode/toString
                        """,
                        """
                        // 密封类 + 模式匹配 switch
                        // sealed interface Result<T> permits Success, Failure {}
                        // record Success<T>(T data) implements Result<T> {}
                        // record Failure<T>(String error) implements Result<T> {}
                        // 
                        // String handle(Result<String> r) {
                        //     return switch (r) {
                        //         case Success<String> s -> "OK: " + s.data();
                        //         case Failure<String> f -> "FAIL: " + f.error();
                        //     };  // 无需 default（全覆盖）
                        // }
                        """,
            ],
            "key_points": [
                        "Record 自动生成构造器/equals/hashCode/toString，不可变数据载体",
                        "Sealed Class 限制继承范围，为穷举模式匹配提供编译期保证",
                        "Record 适合 DTO/值对象，Sealed Class + Switch 模式匹配（Java 21+）全覆盖",
            ],
        },
        ],
    },
    {
        "topic": "Optional 与函数式编程",
        "lessons": [
        {
            "id": "lesson_java_Optional 与函数式编程_1", "title": "Optional 最佳实践",
            "topic": "Optional 与函数式编程",
            "content": (
                        "Optional 是可能包含或不包含非 null 值的容器，解决 NPE 问题。创建：`Optional.of(value)`（值不为 null）、`Optional.ofNullable(value)`（值可能为"
                        "null）、`Optional.empty()`。安全取值：`orElse(default)` 总是求值 default（即使 Optional 有值），`orElseGet(() -> expensive())`"
                        "惰性求值，`orElseThrow()` 抛异常。链式操作：`map(Function)` 转换内部值，`flatMap(Function<Optional>)` 扁平化嵌套"
                        "Optional，`filter(Predicate)` 条件过滤。最佳实践：(1) 不要用作字段类型（Serializable 问题）；(2) 不要用作方法参数；(3) 只用作返回值类型表示「可能为空」；(4) 不要"
                        "`isPresent() + get()`，用链式 API。Optional 与 Stream"
                        "组合：`list.stream().map(Repo::findById).flatMap(Optional::stream)`（Java 9+ Optional.stream()）。"
            ),
            "examples": [
                        """
                        // Optional 链式操作
                        Optional<User> userOpt = userRepo.findById(id);
                        
                        String displayName = userOpt
                            .map(User::getProfile)
                            .map(Profile::getNickname)
                            .filter(n -> !n.isEmpty())
                            .orElse("匿名用户");  // 整个链安全
                        
                        // 避免 isPresent + get 风格
                        // ❌ if (opt.isPresent()) { doSomething(opt.get()); }
                        // ✅ opt.ifPresent(this::doSomething);
                        
                        // Optional.orElse vs orElseGet
                        // ❌ user.orElse(createExpensiveDefault());  // 即使有值也会执行
                        // ✅ user.orElseGet(() -> createExpensiveDefault());  // 惰性求值
                        """,
                        """
                        // Stream + Optional（Java 9+）
                        // List<User> users = ids.stream()
                        //     .map(userRepo::findById)
                        //     .flatMap(Optional::stream)  // 过滤空 Optional
                        //     .toList();
                        """,
            ],
            "key_points": [
                        "Optional 只做返回值类型，不用做字段或参数",
                        "orElseGet 惰性求值优于 orElse 总是求值",
                        "避免 isPresent()+get()，用 map/filter/orElse 链式 API",
            ],
        },
        {
            "id": "lesson_java_Optional 与函数式编程_2", "title": "函数式编程进阶",
            "topic": "Optional 与函数式编程",
            "content": (
                        "`UnaryOperator<T>` extends `Function<T,T>`，`BinaryOperator<T>` extends `BiFunction<T,T,T>`。`IntFunction<R>`"
                        "接收 int 返回 R（避免装箱）。`Predicate` 组合：`and()`/`or()`/`negate()` 逻辑组合。`Predicate.isEqual(target)`"
                        "创建等于判断。`Comparator` 组合：`comparing(extractor).thenComparing(extractor).reversed()`。`nullsFirst/nullsLast` 处理"
                        "null 排序。高阶函数：接收或返回函数的函数。`Function<X, Function<Y, Z>> curried = x -> y -> compute(x, y)` 实现柯里化。Collectors"
                        "进阶：`collectingAndThen` 收集后转换；`teeing`（Java 12+）两个 Collector 组合；`mapping` 收集前映射。"
            ),
            "examples": [
                        """
                        // Predicate 组合
                        Predicate<User> isAdult = u -> u.getAge() >= 18;
                        Predicate<User> hasEmail = u -> u.getEmail() != null;
                        List<User> validUsers = users.stream()
                            .filter(isAdult.and(hasEmail))
                            .toList();
                        
                        // Comparator 组合
                        Comparator<User> byAgeThenName = Comparator
                            .comparing(User::getAge)
                            .thenComparing(User::getName)
                            .reversed();
                        """,
                        """
                        // Collectors teeing（Java 12+）
                        // record Stats(long count, double avg) {}
                        // Stats stats = employees.stream().collect(Collectors.teeing(
                        //     Collectors.counting(),
                        //     Collectors.averagingDouble(Employee::getSalary),
                        //     Stats::new
                        // ));
                        """,
                        """
                        // 柯里化函数
                        // Function<Integer, Function<Integer, Integer>> add = a -> b -> a + b;
                        // Function<Integer, Integer> add5 = add.apply(5);
                        // int result = add5.apply(3);  // 8
                        """,
            ],
            "key_points": [
                        "Predicate and/or/negate 逻辑组合，Comparator comparing/thenComparing/reversed 链式排序",
                        "Collectors teeing（Java 12+）组合两个 Collector 输出",
                        "柯里化：Function<X, Function<Y, Z>> 实现参数部分应用",
            ],
        },
        ],
    },
    {
        "topic": "安全与加密",
        "lessons": [
        {
            "id": "lesson_java_安全与加密_1", "title": "密码学基础",
            "topic": "安全与加密",
            "content": (
                        "Java Cryptography"
                        "Architecture（JCA）：MessageDigest（哈希）、Cipher（加密/解密）、KeyGenerator（密钥生成）、Mac（消息认证码）、Signature（数字签名）。哈希算法：`MessageDigest.getInstance(\"SHA-256\").digest(data)`"
                        "生成 256 位摘要。Base64 编码：`Base64.getEncoder().encodeToString(bytes)`。对称加密：AES-256-GCM"
                        "推荐模式（加密+认证）。`Cipher.getInstance(\"AES/GCM/NoPadding\")`，GCM 模式需要 IV（12"
                        "字节随机）。密钥管理：`KeyGenerator.getInstance(\"AES\").init(256)` 生成密钥。密钥存储用"
                        "KeyStore（JKS/PKCS12），环境变量传递密钥字符串。安全随机数：`SecureRandom.getInstanceStrong()` 生成加密安全的随机数（用于盐值、IV、Token）。"
            ),
            "examples": [
                        """
                        // SHA-256 哈希
                        MessageDigest md = MessageDigest.getInstance("SHA-256");
                        byte[] hash = md.digest("hello".getBytes(StandardCharsets.UTF_8));
                        String hex = HexFormat.of().formatHex(hash);
                        
                        // AES-GCM 加密
                        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
                        keyGen.init(256);
                        SecretKey key = keyGen.generateKey();
                        
                        Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
                        byte[] iv = new byte[12];
                        SecureRandom.getInstanceStrong().nextBytes(iv);
                        GCMParameterSpec spec = new GCMParameterSpec(128, iv);
                        
                        cipher.init(Cipher.ENCRYPT_MODE, key, spec);
                        byte[] encrypted = cipher.doFinal(plaintext);
                        // 传输时需附带 iv + encrypted
                        """,
            ],
            "key_points": [
                        "MessageDigest 哈希（SHA-256），Cipher 加密（AES-GCM 推荐）",
                        "GCM 模式加密+认证一体，需要 12 字节随机 IV",
                        "SecureRandom 生成安全随机数，KeyStore 管理密钥存储",
            ],
        },
        {
            "id": "lesson_java_安全与加密_2", "title": "安全编码实践",
            "topic": "安全与加密",
            "content": (
                        "OWASP Top 10 在 Java 中的防御：(1) SQL 注入 → PreparedStatement；(2) XSS → 输出编码（OWASP Encoder）；(3) CSRF → Spring"
                        "Security CSRF Token。敏感数据保护：密码用 BCrypt/PBKDF2/Argon2 哈希存储（不是加密！），不可逆。`BCrypt.hashpw(password,"
                        "BCrypt.gensalt())`。路径遍历防御：`Paths.get(baseDir).resolve(userInput).normalize()`，检查结果路径是否在 baseDir"
                        "内。安全日志：记录认证事件、输入验证失败。不要记录密码、Token、密钥等敏感信息。依赖安全：OWASP Dependency-Check 插件（Maven/Gradle）扫描已知 CVE 漏洞。`mvn"
                        "dependency-check:check` 集成 CI。"
            ),
            "examples": [
                        """
                        // BCrypt 密码哈希
                        import org.mindrot.jbcrypt.BCrypt;
                        
                        String hashed = BCrypt.hashpw(password, BCrypt.gensalt(12));  // cost=12
                        // 存储 hashed 到数据库
                        
                        // 验证
                        if (BCrypt.checkpw(inputPassword, storedHash)) {
                            // 登录成功
                        }
                        
                        // 路径遍历防御
                        Path baseDir = Path.of("/var/data");
                        Path requested = baseDir.resolve(userInput).normalize();
                        if (!requested.startsWith(baseDir)) {
                            throw new SecurityException("非法路径访问");
                        }
                        // 安全读取 requested 文件
                        """,
            ],
            "key_points": [
                        "密码用 BCrypt/Argon2 哈希（不可逆），PreparedStatement 防 SQL 注入",
                        "resolve+normalize+startsWith 防路径遍历攻击",
                        "OWASP Dependency-Check 扫描三方库已知 CVE 漏洞",
            ],
        },
        ],
    },
]

# ================================================================
# JavaScript 课程（10 个主题，每主题 2 节课）
# ================================================================
JS_LEARNING_PATH = [
    {
        "topic": "JS基础",
        "lessons": [
            {
                "id": "lesson_js_JS基础_1", "title": "变量与作用域",
                "topic": "JS基础",
                "content": (
                    "`let`（块级作用域）、`const`（常量）、`var`（函数作用域，有提升）。现代 JS 默认用 const，需要改值时用 let。"
                    "作用域链：内层可访问外层，反之不行。闭包是函数记住其词法作用域的能力。"
                    "TDZ（暂时性死区）：let/const 声明前访问会抛 ReferenceError，var 则返回 undefined（提升）。"
                    "数据类型：原始类型（string/number/boolean/null/undefined/symbol/bigint）和引用类型（Object/Array/Function）。"
                ),
                "examples": [
                    "// let vs var\n{\n    let x = 1;\n    var y = 2;\n}\n// console.log(x); // ReferenceError\nconsole.log(y);  // 2（var 无块级作用域）\n\n// 闭包\nfunction counter() {\n    let count = 0;\n    return () => ++count;\n}"
                ],
                "key_points": ["const 优先 / let 块级 / var 函数级", "TDZ：let/const 声明前不可访问", "闭包 = 函数 + 词法作用域"],
            },
            {
                "id": "lesson_js_JS基础_2", "title": "运算符与类型转换",
                "topic": "JS基础",
                "content": (
                    "`==` 会类型转换（\"5\" == 5 为 true），`===` 严格相等（类型和值都相同），日常用 ===。"
                    "逻辑运算符 `&&`/`||` 返回原值（非布尔），常用于短路和默认值：`name || '匿名'`。"
                    "`??` 空值合并（null/undefined 才取默认），`?.` 可选链安全访问深层属性。"
                    "隐式转换：`+` 号遇到字符串会转为字符串拼接，`-*/%` 会将字符串转为数字。"
                ),
                "examples": [
                    "// === vs ==\nconsole.log(5 === '5');  // false\nconsole.log(5 == '5');   // true（避免使用）\n// ?. 和 ??\nconst name = user?.profile?.name ?? '匿名';\n// 隐式转换\nconsole.log('5' + 3);   // '53'\nconsole.log('5' - 3);   // 2"
                ],
                "key_points": ["=== 严格相等，永远优于 ==", "?. 可选链 / ?? 空值合并", "+号遇到字符串优先拼接"],
            },
        ],
    },
    {
        "topic": "JS异步",
        "lessons": [
            {
                "id": "lesson_js_JS异步_1", "title": "Promise",
                "topic": "JS异步",
                "content": (
                    "Promise 三种状态：pending → fulfilled/resolved 或 rejected，状态不可逆。"
                    "`.then(onFulfilled, onRejected)` 链式调用，`.catch()` 捕获任意环节的错误。"
                    "`Promise.all()` 并行等待全部完成（一个失败整体失败），`Promise.race()` 竞速。"
                    "`Promise.allSettled()` 等全部结束（不论成败），`Promise.any()` 任意一个成功即成功。"
                ),
                "examples": [
                    "fetch('/api/data')\n    .then(res => res.json())\n    .then(data => console.log(data))\n    .catch(err => console.error(err));\n// Promise.all 并行\nconst [user, posts] = await Promise.all([fetchUser(1), fetchPosts()]);"
                ],
                "key_points": ["pending → fulfilled/rejected", ".then() 链式 / .catch() 统一", "Promise.all/allSettled/race/any"],
            },
            {
                "id": "lesson_js_JS异步_2", "title": "async/await",
                "topic": "JS异步",
                "content": (
                    "`async` 函数返回 Promise，内部 `await` 暂停等待 Promise 解决，出错抛异常（用 try-catch 捕获）。"
                    "async/await 让异步代码读起来像同步，减少嵌套。"
                    "注意：`await` 不能在顶层使用（ES2022 前），需包裹在 async 函数中。"
                    "性能陷阱：循环中串行 `for...of` + `await` 较慢，应用 `Promise.all` 并行。"
                ),
                "examples": [
                    "async function loadDashboard() {\n    try {\n        const user = await fetchUser(1);\n        const [posts, notifications] = await Promise.all([\n            fetchPosts(user.id),\n            fetchNotifications(user.id)\n        ]);\n        return { user, posts, notifications };\n    } catch (err) {\n        console.error('加载失败', err);\n    }\n}"
                ],
                "key_points": ["async 返回 Promise", "await 暂停等待，try-catch 捕获", "并行用 Promise.all 而非串行 await"],
            },
        ],
    },
    {
        "topic": "JS原型与this",
        "lessons": [
            {
                "id": "lesson_js_JS原型与this_1", "title": "原型链",
                "topic": "JS原型与this",
                "content": (
                    "每个 JS 对象有内部 `[[Prototype]]`（通过 `__proto__` 或 `Object.getPrototypeOf()` 访问）。"
                    "构造函数 `prototype` 属性是实例的原型。`class` 语法是原型继承的语法糖。"
                    "属性查找：先在自身找，找不到沿原型链向上直到 `Object.prototype`（终点是 null）。"
                    "`Object.create(proto)` 创建以 proto 为原型的对象。`hasOwnProperty()` 判断自有属性。"
                ),
                "examples": [
                    "function Person(name) { this.name = name; }\nPerson.prototype.greet = function() { return `Hello, ${this.name}`; };\nconst alice = new Person('Alice');\nalice.greet();  // 'Hello, Alice'\n// class 语法糖\nclass Person {\n    constructor(name) { this.name = name; }\n    greet() { return `Hello, ${this.name}`; }\n}"
                ],
                "key_points": ["原型链：实例 → 构造函数.prototype → Object.prototype → null", "class 是原型继承语法糖", "hasOwnProperty 判断自有属性"],
            },
            {
                "id": "lesson_js_JS原型与this_2", "title": "this 指向",
                "topic": "JS原型与this",
                "content": (
                    "this 的值取决于函数调用方式：普通调用 → window/undefined(strict)；方法调用 → 对象本身；new → 新实例。"
                    "箭头函数没有自己的 this，继承外层作用域的 this（词法绑定）。"
                    "显式绑定：`call(obj, ...args)` / `apply(obj, [args])` 立即调用，`bind(obj)` 返回新函数。"
                    "常见陷阱：回调函数中 this 丢失、事件处理中 this 指向元素、setTimeout 中 this 为 window。"
                ),
                "examples": [
                    "const obj = {\n    name: 'Alice',\n    greet() { console.log(this.name); },\n    greetArrow: () => console.log(this.name),  // this 来自外层\n};\nobj.greet();       // 'Alice'\nobj.greetArrow();  // undefined（箭头函数，this 是 window）\n// bind 绑定\nconst bound = obj.greet.bind({ name: 'Bob' });\nbound();  // 'Bob'"
                ],
                "key_points": ["this 由调用方式决定（非定义处）", "箭头函数 this 来自外层词法作用域", "call/apply 立即调用，bind 返回新函数"],
            },
        ],
    },
    {
        "topic": "JS模块",
        "lessons": [
            {
                "id": "lesson_js_JS模块_1", "title": "ES Module",
                "topic": "JS模块",
                "content": (
                    "ESM (ES2015+)：`export` 导出，`import` 导入。默认导出 `export default` 一次一个，命名导出可多个。"
                    "`import { a as b }` 重命名，`import * as mod` 命名空间导入。`import()` 动态导入返回 Promise。"
                    "ESM 静态分析：编译时确定依赖关系，支持 Tree Shaking（按需打包）。"
                    "Node.js 中：`.mjs` 扩展名或 `package.json` 中 `\"type\": \"module\"` 启用 ESM。"
                ),
                "examples": [
                    "// math.js\nexport function add(a, b) { return a + b; }\nexport const PI = 3.14;\nexport default function multiply(a, b) { return a * b; }\n// main.js\nimport multiply, { add, PI } from './math.js';\n// 动态导入\nconst { default: lodash } = await import('lodash');"
                ],
                "key_points": ["export default / export 命名", "import 静态分析 + Tree Shaking", "import() 动态导入"],
            },
            {
                "id": "lesson_js_JS模块_2", "title": "CommonJS 对比",
                "topic": "JS模块",
                "content": (
                    "CommonJS：`require()` 同步加载，`module.exports` 导出。Node.js 默认模块系统。"
                    "区别：CJS 运行时加载（对象拷贝），ESM 编译时加载（引用）。CJS `this` 指向当前模块。"
                    "`__dirname`/`__filename` 只在 CJS 中可用，ESM 用 `import.meta.url`。"
                    "互操作：CJS 用 `require()` 加载 ESM 需动态导入；ESM 可用 `import` 加载 CJS（部分限制）。"
                ),
                "examples": [
                    "// CommonJS\nconst fs = require('fs');\nmodule.exports = { greet: () => 'Hello' };\n// ESM 等价写法\nimport fs from 'fs';\nexport const greet = () => 'Hello';"
                ],
                "key_points": ["CJS: require/module.exports 同步", "ESM: import/export 静态", "CJS 对象拷贝 vs ESM 引用"],
            },
        ],
    },
    {
        "topic": "JS闭包",
        "lessons": [
            {
                "id": "lesson_js_JS闭包_1", "title": "闭包原理",
                "topic": "JS闭包",
                "content": (
                    "闭包 = 函数 + 其声明的词法环境。即使外部函数已返回，内部函数仍能访问外部变量。"
                    "用途：数据封装（私有变量）、工厂函数、柯里化、模块模式。"
                    "内存影响：闭包会阻止变量被 GC，大量使用需注意内存泄漏（特别是 DOM 引用）。"
                    "`var` 在循环中创建闭包的经典陷阱：用 `let` 或 IIFE 解决。"
                ),
                "examples": [
                    "// 闭包私有变量\nfunction createCounter() {\n    let count = 0;\n    return {\n        inc: () => ++count,\n        get: () => count,\n    };\n}\nconst c = createCounter();\nc.inc(); c.inc();\nc.get();  // 2（count 外部不可直接访问）"
                ],
                "key_points": ["闭包 = 函数 + 词法环境", "私有变量/工厂/柯里化", "循环中 var 陷阱，用 let 解决"],
            },
            {
                "id": "lesson_js_JS闭包_2", "title": "闭包实战",
                "topic": "JS闭包",
                "content": (
                    "节流（throttle）：固定时间内只执行一次，适合滚动事件。用闭包保存上次执行时间。"
                    "防抖（debounce）：连续触发只执行最后一次，适合搜索输入。用闭包保存计时器 ID。"
                    "单例模式：IIFE 返回唯一实例，闭包中保存并返回它。"
                    "函数柯里化：用闭包逐步收集参数，`add(1)(2)(3)` 返回 6。"
                ),
                "examples": [
                    "// 防抖\nfunction debounce(fn, delay) {\n    let timer;\n    return (...args) => {\n        clearTimeout(timer);\n        timer = setTimeout(() => fn(...args), delay);\n    };\n}\n// 柯里化\nconst add = a => b => c => a + b + c;\nadd(1)(2)(3);  // 6"
                ],
                "key_points": ["节流: 固定间隔执行一次", "防抖: 停止触发后执行", "柯里化 = 闭包逐步收集参数"],
            },
        ],
    },
    {
        "topic": "JS DOM",
        "lessons": [
            {
                "id": "lesson_js_JS DOM_1", "title": "DOM 操作",
                "topic": "JS DOM",
                "content": (
                    "选择器：`getElementById` / `querySelector`（单元素）/ `querySelectorAll`（NodeList）。"
                    "创建与插入：`document.createElement` → `appendChild` / `insertBefore` / `insertAdjacentHTML`。"
                    "属性操作：`element.classList.add/remove/toggle` 管理类名，`dataset` 访问 data-* 属性。"
                    "`createDocumentFragment` 批量插入减少回流，`cloneNode(true)` 深拷贝。"
                ),
                "examples": [
                    "const el = document.querySelector('.item');\nel.classList.add('active');\nel.setAttribute('data-id', '123');\nel.innerHTML = '<strong>新内容</strong>';\n// 批量插入用 Fragment\nconst frag = document.createDocumentFragment();\ndata.forEach(d => { const li = document.createElement('li'); li.textContent = d; frag.appendChild(li); });\nul.appendChild(frag);"
                ],
                "key_points": ["querySelector/querySelectorAll", "classList.add/remove/toggle", "createDocumentFragment 减少回流"],
            },
            {
                "id": "lesson_js_JS DOM_2", "title": "事件处理",
                "topic": "JS DOM",
                "content": (
                    "`addEventListener(type, handler, options)` 绑定事件，`removeEventListener` 解除。"
                    "事件流三阶段：捕获 → 目标 → 冒泡。第三个参数控制：true 捕获阶段触发，false（默认）冒泡阶段触发。"
                    "`event.stopPropagation()` 阻止冒泡，`event.preventDefault()` 阻止默认行为。"
                    "事件委托：在父元素上监听，通过 `event.target` 判断实际触发的子元素，减少事件绑定数量。"
                ),
                "examples": [
                    "// 事件委托\nlist.addEventListener('click', (e) => {\n    if (e.target.matches('.delete-btn')) {\n        e.target.closest('li').remove();\n    }\n});\n// options: { once: true }\nel.addEventListener('click', handler, { once: true });  // 自动解绑"
                ],
                "key_points": ["事件流：捕获→目标→冒泡", "stopPropagation/preventDefault", "事件委托减少绑定"],
            },
        ],
    },
    {
        "topic": "JS事件循环",
        "lessons": [
            {
                "id": "lesson_js_JS事件循环_1", "title": "宏任务与微任务",
                "topic": "JS事件循环",
                "content": (
                    "JS 单线程，事件循环协调异步任务。每轮循环：执行一个宏任务 → 清空所有微任务 → 渲染。"
                    "宏任务：setTimeout/setInterval、I/O、UI 渲染、setImmediate（Node.js）。"
                    "微任务：Promise.then、MutationObserver、queueMicrotask、process.nextTick（Node，比微任务更优先）。"
                    "执行顺序：同步代码 → 微任务队列 → 宏任务队列。每个宏任务后有微任务检查点。"
                ),
                "examples": [
                    "console.log('1');\nsetTimeout(() => console.log('2'), 0);\nPromise.resolve().then(() => console.log('3'));\nconsole.log('4');\n// 输出: 1 4 3 2\n// 解释: 1/4 同步 → 清空微任务(3) → 下一轮宏任务(2)"
                ],
                "key_points": ["宏任务: setTimeout/setInterval/I/O", "微任务: Promise.then/queueMicrotask", "执行顺序: 同步→微→宏"],
            },
            {
                "id": "lesson_js_JS事件循环_2", "title": "异步模式优化",
                "topic": "JS事件循环",
                "content": (
                    "`requestAnimationFrame` 在渲染前回调，适合动画；`requestIdleCallback` 在空闲时执行低优先级任务。"
                    "`setTimeout(fn, 0)` 不是立即执行，至少延迟 4ms（嵌套 5 层后），实际延迟受其他任务影响。"
                    "Web Worker 创建独立线程执行 CPU 密集任务，通过 postMessage 通信，不阻塞 UI。"
                    "长时间任务用 `scheduler.postTask()` 或手动分片（`requestIdleCallback`）避免卡顿。"
                ),
                "examples": [
                    "// rAF 动画\nfunction animate() {\n    updatePosition();\n    requestAnimationFrame(animate);\n}\nrequestAnimationFrame(animate);\n// Web Worker\nconst worker = new Worker('worker.js');\nworker.postMessage({ type: 'process', data });\nworker.onmessage = (e) => console.log(e.data);"
                ],
                "key_points": ["rAF 渲染前回调/IdleCallback 空闲", "setTimeout 最小延迟 4ms", "Web Worker 独立线程"],
            },
        ],
    },
    {
        "topic": "JS错误处理",
        "lessons": [
            {
                "id": "lesson_js_JS错误处理_1", "title": "try-catch 与错误类型",
                "topic": "JS错误处理",
                "content": (
                    "`try-catch-finally` 捕获同步异常。Error 子类：TypeError/RangeError/SyntaxError/ReferenceError。"
                    "`throw new Error('message')` 抛出自定义错误，`error.message` 和 `error.stack` 获取信息。"
                    "`window.onerror`（全局错误）和 `window.addEventListener('unhandledrejection')`（未捕获 Promise 拒绝）。"
                    "Sentry/DataDog 等监控平台通常通过全局错误监听 + sourcemap 定位线上报错。"
                ),
                "examples": [
                    "try {\n    JSON.parse('invalid');\n} catch (err) {\n    console.error(err.message, err.stack);\n} finally {\n    cleanup();\n}\n// 全局未捕获 Promise\nwindow.addEventListener('unhandledrejection', (event) => {\n    console.error('未处理的 Promise 拒绝:', event.reason);\n});"
                ],
                "key_points": ["try-catch 只捕获同步", "Error 子类: TypeError/RangeError 等", "unhandledrejection 捕获未处理 Promise"],
            },
            {
                "id": "lesson_js_JS错误处理_2", "title": "错误处理模式",
                "topic": "JS错误处理",
                "content": (
                    "Result 模式：`[error, data]` 元组，Go 风格错误处理。`try { data = await fn() } catch { error = ... }`。"
                    "自定义 Error 类：`class AppError extends Error { constructor(msg, code) { super(msg); this.code = code; } }`。"
                    "`error.cause`（ES2022）链式错误：`throw new Error('失败', { cause: originalError })`。"
                    "防御性编程：`if (!data) return` 提前返回，`assert` 函数检查不变量。"
                ),
                "examples": [
                    "// Result 模式\nasync function safeCall(fn) {\n    try {\n        return [null, await fn()];\n    } catch (err) {\n        return [err, null];\n    }\n}\nconst [err, data] = await safeCall(() => fetchUser(1));\nif (err) return handleError(err);\n// error.cause 链式\nthrow new Error('连接失败', { cause: originalError });"
                ],
                "key_points": ["Result 模式 [error, data]", "error.cause 链式错误", "防御性编程提前返回"],
            },
        ],
    },
    {
        "topic": "JS存储",
        "lessons": [
            {
                "id": "lesson_js_JS存储_1", "title": "Web Storage",
                "topic": "JS存储",
                "content": (
                    "`localStorage`：持久化，5MB 上限，同源共享，手动清除。`sessionStorage`：页签级别，关闭清除。"
                    "API：`getItem(key)`/`setItem(key, value)`/`removeItem(key)`/`clear()`。只能存字符串，对象需 JSON.stringify。"
                    "`storage` 事件：当其他标签页修改 localStorage 时触发（同页面不触发）。"
                    "容量检测：try-catch 写入检测配额溢出。超过限制抛 QuotaExceededError。"
                ),
                "examples": [
                    "// 存对象\nconst user = { name: 'Alice', age: 25 };\nlocalStorage.setItem('user', JSON.stringify(user));\n// 读对象\nconst saved = JSON.parse(localStorage.getItem('user'));\n// 监听变化（其他标签页）\nwindow.addEventListener('storage', (e) => {\n    if (e.key === 'user') console.log('用户信息已变更');\n});"
                ],
                "key_points": ["localStorage 持久/sessionStorage 页签级", "只能存字符串，对象用 JSON", "storage 事件跨标签监听"],
            },
            {
                "id": "lesson_js_JS存储_2", "title": "IndexedDB 与 Cookie",
                "topic": "JS存储",
                "content": (
                    "IndexedDB：异步 NoSQL 数据库，支持索引、事务、大容量（通常 50% 磁盘）。适合离线数据。"
                    "`cookie`：4KB 上限，每次请求自动携带，`document.cookie` 读写。`HttpOnly` 防 XSS 读取。"
                    "`Cache API` + Service Worker 实现 PWA 离线缓存。`navigator.storage.estimate()` 查询存储配额。"
                    "选择建议：小数据用 localStorage、需请求携带用 cookie、大量结构化数据用 IndexedDB。"
                ),
                "examples": [
                    "// IndexedDB 基础\nconst open = indexedDB.open('MyDB', 1);\nopen.onsuccess = (e) => {\n    const db = e.target.result;\n    const tx = db.transaction('store', 'readwrite');\n    tx.objectStore('store').put({ id: 1, name: 'Alice' });\n};\n// Cookie 设置\ndocument.cookie = 'token=abc123; max-age=3600; path=/; Secure; SameSite=Lax';"
                ],
                "key_points": ["IndexedDB: 异步/索引/大容量", "Cookie: 4KB/自动携带/HttpOnly", "PWA: Cache API + Service Worker"],
            },
        ],
    },
    {
        "topic": "JS设计模式",
        "lessons": [
            {
                "id": "lesson_js_JS设计模式_1", "title": "模块与观察者",
                "topic": "JS设计模式",
                "content": (
                    "模块模式：IIFE 或 ESM + 闭包，隐藏内部实现只暴露 API。"
                    "观察者模式：`class EventEmitter { on/off/emit }`，Node.js EventEmitter 是内置实现。"
                    "发布-订阅（Pub/Sub）增加事件通道解耦发布者和订阅者，Redis Pub/Sub、EventBus 是典型。"
                    "单例模式：`const instance = new Config()` 模块级（ESM 天然单例）。"
                ),
                "examples": [
                    "// 观察者 EventEmitter\nclass EventEmitter {\n    #events = new Map();\n    on(event, fn) {\n        if (!this.#events.has(event)) this.#events.set(event, []);\n        this.#events.get(event).push(fn);\n    }\n    emit(event, ...args) {\n        (this.#events.get(event) || []).forEach(fn => fn(...args));\n    }\n}"
                ],
                "key_points": ["模块模式: IIFE + 闭包", "观察者: on/emit 解耦", "ESM 模块级天然单例"],
            },
            {
                "id": "lesson_js_JS设计模式_2", "title": "策略与代理",
                "topic": "JS设计模式",
                "content": (
                    "策略模式：定义算法家族，运行时切换。JS 可用对象映射替代 if-else。"
                    "代理模式：`Proxy(target, handler)` 拦截操作（get/set/apply），Vue 3 响应式系统核心。"
                    "装饰器模式：高阶函数 `withLogging(fn)` 包装增强，不修改原函数。"
                    "适配器模式：统一不同 API 的接口 `newAdapter.adapt(oldAPI)`。"
                ),
                "examples": [
                    "// 策略模式\nconst strategies = {\n    vip: (price) => price * 0.8,\n    normal: (price) => price * 0.95,\n};\nconst discount = strategies[vip] || strategies.normal;\ndiscount(100);  // 80\n// Proxy 代理\nconst handler = {\n    get(target, key) {\n        console.log(`读取 ${key}`);\n        return Reflect.get(target, key);\n    }\n};\nconst proxy = new Proxy({ name: 'Alice' }, handler);"
                ],
                "key_points": ["策略: 对象映射替代 if-else", "Proxy: Vue 3 响应式核心", "装饰器: 高阶函数包装增强"],
            },
        ],
    },

    {
        "topic": "Fetch 与网络请求",
        "lessons": [
            {
                "id": "lesson_js_Fetch 与网络请求_1", "title": "Fetch API 基础",
                "topic": "Fetch 与网络请求",
                "content": (
                    "Fetch API 是现代浏览器内置的网络请求接口，基于 Promise 设计。`fetch(url, options)` 返回 Response Promise。"
                    "默认 GET 请求，`method: 'POST'` + `body: JSON.stringify(data)` + `headers: {'Content-Type': 'application/json'}` 发送 JSON。"
                    "Response 对象：`response.ok` 判断成功（status 200-299），`response.json()` 解析 JSON，`response.text()` 文本，`response.blob()` 二进制。"
                    "错误处理：fetch 只在网络错误时 reject，HTTP 4xx/5xx 仍 resolve 但 `ok` 为 false。需手动 `if (!response.ok) throw new Error(...)`。"
                    "AbortController：`signal` 参数 + `controller.abort()` 取消请求，防止内存泄漏（组件卸载时取消未完成请求）。"
                ),
                "examples": [
                    "// GET 请求\nconst res = await fetch('https://api.example.com/users');\nif (!res.ok) throw new Error(`HTTP ${res.status}`);\nconst users = await res.json();\n\n// POST JSON\nconst resp = await fetch('/api/users', {\n    method: 'POST',\n    headers: { 'Content-Type': 'application/json' },\n    body: JSON.stringify({ name: 'Alice' }),\n});\n\n// AbortController 取消请求\nconst ctrl = new AbortController();\nsetTimeout(() => ctrl.abort(), 5000);\ntry {\n    const r = await fetch(url, { signal: ctrl.signal });\n} catch (err) { if (err.name === 'AbortError') console.log('Cancelled'); }"
                ],
                "key_points": ["fetch 基于 Promise，response.json() 解析 JSON", "4xx/5xx 需手动检查 response.ok", "AbortController + signal 取消请求防内存泄漏"],
            },
            {
                "id": "lesson_js_Fetch 与网络请求_2", "title": "请求拦截与重试",
                "topic": "Fetch 与网络请求",
                "content": (
                    "封装 fetch 实现请求拦截：统一添加认证 Header、base URL、超时控制、日志记录。"
                    "请求重试：指数退避策略，`Math.min(1000 * 2 ** attempt, 30000)` 计算延迟，设置最大重试次数。"
                    "并发请求：`Promise.all([fetch1, fetch2])` 并行，`Promise.allSettled` 不因单个失败而整体失败。"
                    "请求去重：相同参数的并发请求共享同一个 Promise，避免重复发送。用 Map 缓存进行中的请求。"
                    "实际封装方案：自定义 fetch wrapper 或使用 axios 拦截器（request/response interceptor）。"
                ),
                "examples": [
                    "// 请求重试（指数退避）\nasync function fetchWithRetry(url, opts = {}, retries = 3) {\n    for (let i = 0; i <= retries; i++) {\n        try {\n            const res = await fetch(url, opts);\n            if (res.ok || i === retries) return res;\n        } catch (err) { if (i === retries) throw err; }\n        await new Promise(r => setTimeout(r, Math.min(1000*2**i, 10000)));\n    }\n}\n\n// 请求去重\nconst pending = new Map();\nasync function dedupedFetch(url, opts) {\n    const k = JSON.stringify({url, opts});\n    if (pending.has(k)) return pending.get(k);\n    const p = fetch(url, opts).finally(() => pending.delete(k));\n    pending.set(k, p); return p;\n}"
                ],
                "key_points": ["指数退避重试: delay = min(1000*2^n, maxDelay)", "Promise.allSettled 不因单个失败整体失败", "请求去重用 Map 缓存进行中 Promise"],
            },
        ],
    },
    {
        "topic": "面向对象与类",
        "lessons": [
            {
                "id": "lesson_js_面向对象与类_1", "title": "Class 语法与继承",
                "topic": "面向对象与类",
                "content": (
                    "ES6 Class 是原型继承的语法糖。`class Animal { constructor(name) { this.name = name } speak() {...} }` 定义类。"
                    "`extends` 继承：`class Dog extends Animal { constructor(name, breed) { super(name); this.breed = breed } }`。"
                    "实例成员 vs 静态成员：`static` 方法/属性属于类本身，实例通过 `this.constructor.staticField` 访问。"
                    "私有字段（ES2022）：`#privateField` 语法，真正私有（类外不可访问）。`#privateMethod()` 私有方法。"
                    "getter/setter：`get fullName()` / `set fullName(val)` 计算属性。"
                ),
                "examples": [
                    "// Class 继承与 Super\nclass Animal {\n    constructor(name) { this.name = name; }\n    speak() { console.log(`${this.name} makes a sound`); }\n}\nclass Dog extends Animal {\n    constructor(name, breed) { super(name); this.breed = breed; }\n    speak() { console.log(`${this.name} barks!`); }\n}\nconst dog = new Dog('Rex', 'German Shepherd'); dog.speak();\n\n// 私有字段 ES2022\nclass BankAccount {\n    #balance = 0;\n    deposit(amount) { this.#balance += amount; }\n}"
                ],
                "key_points": ["class 是原型继承语法糖，extends + super 实现继承", "static 成员属于类，ES2022 # 语法实现真正私有", "getter/setter 实现计算属性"],
            },
            {
                "id": "lesson_js_面向对象与类_2", "title": "Mixins 与组合模式",
                "topic": "面向对象与类",
                "content": (
                    "JavaScript 不支持多继承，Mixins 代码复用模式：`Object.assign(Class.prototype, mixin)` 混入方法。"
                    "函数式 Mixin：`const Timestamped = Base => class extends Base { createdAt = new Date() }`，`class User extends Timestamped(Entity) {}`。"
                    "组合优于继承：将行为封装为独立对象，类通过持有这些对象获得能力，而非通过继承链。"
                    "Symbol 避免属性名冲突：`const speakSymbol = Symbol('speak')`，`obj[speakSymbol]()`。"
                    "装饰器（Stage 3 提案）：`@readonly`、`@logged` 等注解增强类，更简洁但尚未标准化。"
                ),
                "examples": [
                    "// 函数式 Mixin\nconst WithLogging = Base => class extends Base {\n    log(msg) { console.log(`[${this.constructor.name}] ${msg}`); }\n};\nconst WithTimestamp = Base => class extends Base {\n    get timestamp() { return new Date(); }\n};\nclass Entity { constructor(id) { this.id = id; } }\nclass User extends WithTimestamp(WithLogging(Entity)) {\n    greet() { this.log(`Hello, I'm user ${this.id}`); }\n}\n\n// Symbol 避免冲突\nconst fly = Symbol('fly');\nconst CanFly = Base => class extends Base { [fly]() { console.log('flying'); } };"
                ],
                "key_points": ["函数式 Mixin: class extends mixin(Base) 组合行为", "Object.assign(prototype, mixin) 简单混入", "Symbol 作为 Mixin 方法名防属性冲突"],
            },
        ],
    },
    {
        "topic": "正则表达式",
        "lessons": [
            {
                "id": "lesson_js_正则表达式_1", "title": "正则基础与元字符",
                "topic": "正则表达式",
                "content": (
                    "正则表达式用 `/pattern/flags` 字面量或 `new RegExp('pattern', 'flags')` 构造。flags：g（全局）、i（忽略大小写）、m（多行）、s（dotAll）、u（Unicode）。"
                    "元字符：`.` 任意字符，`\\d` 数字，`\\w` 单词，`\\s` 空白，`\\D/\\W/\\S` 取反。量词：`*`(0+)、`+`(1+)、`?`(0或1)、`{n,m}`。"
                    "分组与捕获：`(...)` 捕获组，`(?:...)` 非捕获组，`(?<name>...)` 命名捕获组。`\\1` 反向引用。"
                    "锚点：`^` 行首，`$` 行尾，`\\b` 单词边界。前瞻/后顾：`(?=...)` 正向前瞻，`(?<=...)` 正向后顾（ES2018+）。"
                ),
                "examples": [
                    "// 常用正则\nconst emailRe = /^[\\w.-]+@[\\w.-]+\\.\\w{2,}$/;\nconst phoneRe = /^1[3-9]\\d{9}$/;\n\n// 命名捕获组\nconst dateRe = /(?<year>\\d{4})-(?<month>\\d{2})-(?<day>\\d{2})/;\nconst m = '2024-06-26'.match(dateRe);\nconsole.log(m.groups.year); // 2024\n\n// 前瞻断言\nconst pwRe = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\\d).{8,}$/;"
                ],
                "key_points": ["元字符 \d/\w/\s + 量词 *+?{n,m}", "命名捕获组 (?<name>...) + match.groups.name", "前瞻断言 (?=...) 不消耗字符"],
            },
            {
                "id": "lesson_js_正则表达式_2", "title": "正则方法与实战",
                "topic": "正则表达式",
                "content": (
                    "String 正则方法：`match` 返回匹配，`matchAll` 返回迭代器（含捕获组），`replace(regex, replacement)`，`search` 返回位置，`split` 分割。"
                    "RegExp 方法：`test(str)` 返回布尔值，`exec(str)` 返回匹配详情（含 index 和 groups），循环调用获取全局匹配。"
                    "替换模式：`$1`、`$&`、`$`` `$'`。replace 第二个参数可为函数：`(match, p1, p2, offset, str) => transformed`。"
                    "实际应用：表单验证、字符串提取、模板引擎、敏感信息脱敏。"
                    "性能陷阱：避免灾难性回溯（嵌套量词如 `(a+)+b`）。用 `regex.test()` 而非 `str.match()` 做布尔判断更快。"
                ),
                "examples": [
                    "// replace 函数回调\nconst tpl = 'Hello, {{name}}! You have {{count}} msgs.';\nconst res = tpl.replace(/\\{\\{(\\w+)\\}\\}/g, (_, k) => data[k] ?? '');\n\n// exec 全局遍历\nconst re = /(\\d{4})-(\\d{2})-(\\d{2})/g; let m;\nwhile ((m = re.exec('2024-01-15, 2024-02-20')) !== null) { console.log(m[1], m[2], m[3]); }\n\n// 手机号脱敏\n'13812345678'.replace(/(\\d{3})\\d{4}(\\d{4})/, '$1****$2');"
                ],
                "key_points": ["matchAll 获取全局匹配+捕获组，replace 支持函数回调", "regex.test() 比 str.match() 更快做布尔判断", "避免灾难性回溯，嵌套量词是常见性能陷阱"],
            },
        ],
    },
    {
        "topic": "Proxy 与 Reflect",
        "lessons": [
            {
                "id": "lesson_js_Proxy 与 Reflect_1", "title": "Proxy 拦截器",
                "topic": "Proxy 与 Reflect",
                "content": (
                    "Proxy 在目标对象前创建拦截层：`new Proxy(target, handler)`。handler 定义 13 种捕获器（trap）。"
                    "get/set 陷阱：`get(target, prop, receiver)` 拦截属性读取，`set(target, prop, value, receiver)` 拦截属性写入。Vue 3 响应式基于此。"
                    "has/deleteProperty/ownKeys：拦截 `in` 操作符、`delete` 操作、`Object.keys()` 等。"
                    "apply/construct：拦截函数调用和 new 构造。`apply(target, thisArg, args)` 和 `construct(target, args)`。"
                    "实际应用：响应式系统（Vue 3）、数据校验、日志/性能监控、负索引数组、默认值对象。"
                ),
                "examples": [
                    "// 响应式基础（Vue 3 原理简化）\nfunction reactive(target) {\n    return new Proxy(target, {\n        get(target, key, receiver) {\n            track(target, key); // 依赖收集\n            return Reflect.get(target, key, receiver);\n        },\n        set(target, key, value, receiver) {\n            const r = Reflect.set(target, key, value, receiver);\n            trigger(target, key); // 触发更新\n            return r;\n        }\n    });\n}\n\n// 负索引数组\nconst arr = new Proxy([], {\n    get(target, prop) {\n        let idx = Number(prop);\n        if (idx < 0) idx = target.length + idx;\n        return Reflect.get(target, String(idx));\n    }\n});"
                ],
                "key_points": ["Proxy 13 种陷阱，get/set 最常用（Vue 3 响应式核心）", "Reflect 提供与陷阱一一对应的默认行为", "应用：响应式、数据校验、日志监控、负索引数组"],
            },
            {
                "id": "lesson_js_Proxy 与 Reflect_2", "title": "Proxy 高级用例",
                "topic": "Proxy 与 Reflect",
                "content": (
                    "数据校验代理：set 陷阱中验证值类型/范围，拒绝无效赋值。"
                    "缓存代理：get 陷阱中缓存计算结果，再次访问直接返回缓存。适合计算密集型 getter。"
                    "只读代理：set 和 deleteProperty 陷阱中直接返回 false 或抛错误，阻止修改。"
                    "隐藏私有属性：`has/get/ownKeys` 陷阱中过滤 `_` 前缀属性，模拟私有成员。"
                    "可撤销 Proxy：`Proxy.revocable(target, handler)` 返回 `{ proxy, revoke }`，`revoke()` 后代理失效（Security 场景）。"
                ),
                "examples": [
                    "// 缓存代理（memoization）\nconst memoize = (fn) => {\n    const cache = new Map();\n    return new Proxy(fn, {\n        apply(target, thisArg, args) {\n            const k = JSON.stringify(args);\n            if (!cache.has(k)) cache.set(k, Reflect.apply(target, thisArg, args));\n            return cache.get(k);\n        }\n    });\n};\n\n// 可撤销 Proxy\nconst {proxy, revoke} = Proxy.revocable({secret: 'key'}, {});\nrevoke(); // proxy 失效"
                ],
                "key_points": ["get 陷阱实现 memoization 懒计算缓存", "Proxy 隐藏 _ 前缀属性模拟私有成员", "Proxy.revocable 创建可撤销代理用于安全沙箱"],
            },
        ],
    },
    {
        "topic": "Web Workers",
        "lessons": [
            {
                "id": "lesson_js_Web Workers_1", "title": "Worker 基础与通信",
                "topic": "Web Workers",
                "content": (
                    "Web Workers 在后台线程执行脚本，不阻塞 UI。`new Worker('worker.js')` 创建专用 Worker。主线程 `postMessage(data)`，Worker `onmessage` 接收。"
                    "Worker 上下文：无 DOM 访问权，无 window 对象。`self` 代表全局作用域，可用 `fetch`、`setTimeout`、`importScripts`。"
                    "数据传输：结构化克隆（Structured Clone）默认。Transferable 对象（ArrayBuffer/MessagePort）可转移所有权零拷贝。"
                    "终止 Worker：主线程 `worker.terminate()` 立即终止，Worker 内部 `self.close()` 优雅关闭。"
                    "错误处理：`worker.onerror` 捕获未处理异常。"
                ),
                "examples": [
                    "// 主线程\nconst worker = new Worker('worker.js');\nworker.postMessage({ type: 'CALC', data: [1,2,3] });\nworker.onmessage = (e) => console.log('Result:', e.data);\nworker.onerror = (e) => console.error('Error:', e.message);\n\n// worker.js\nself.onmessage = (e) => {\n    const sum = e.data.data.reduce((a,b) => a+b, 0);\n    self.postMessage({ type: 'RESULT', result: sum });\n};\n\n// Transferable 零拷贝\nconst buf = new ArrayBuffer(1024*1024);\nworker.postMessage({buf}, [buf]);"
                ],
                "key_points": ["Worker 后台线程不阻塞 UI，无 DOM 访问权", "postMessage/onmessage 通信，结构化克隆默认", "Transferable 零拷贝转移 ArrayBuffer 所有权"],
            },
            {
                "id": "lesson_js_Web Workers_2", "title": "SharedWorker 与 Service Worker",
                "topic": "Web Workers",
                "content": (
                    "SharedWorker：多页面共享 Worker。`new SharedWorker('shared.js')`，通过 `port` 通信（`port.start()` + `port.onmessage`）。"
                    "Service Worker：网络代理层，拦截请求实现离线缓存、后台同步、推送。`navigator.serviceWorker.register('/sw.js')`。"
                    "Service Worker 生命周期：install → waiting → activate → fetch/message。`self.skipWaiting()` + `clients.claim()` 加速激活。"
                    "Cache API：`caches.open('v1').then(cache => cache.addAll(['/']))` 预缓存，`cache.match(request)` 响应拦截。"
                    "Comlink 库：将 Worker 通信抽象为 RPC 风格调用，让 Worker 使用像异步函数。"
                ),
                "examples": [
                    "// Service Worker 缓存策略\n// self.addEventListener('install', e => {\n//   e.waitUntil(caches.open('v1').then(c => c.addAll(['/index.html','/app.js','/style.css'])));\n// });\n// self.addEventListener('fetch', e => {\n//   e.respondWith(caches.match(e.request).then(r => r || fetch(e.request)));\n// });\n\n// Comlink 简化通信\n// import { expose } from 'comlink';\n// const api = { add(a,b) { return a+b; } }; expose(api);\n// // 主线程: const w = wrap(new Worker('w.js')); await w.add(1,2);"
                ],
                "key_points": ["SharedWorker 多页面共享，Service Worker 网络代理层", "SW: install→activate→fetch，Cache API 离线缓存", "Comlink 将 Worker 通信抽象为 RPC 异步调用"],
            },
        ],
    },
    {
        "topic": "性能优化",
        "lessons": [
            {
                "id": "lesson_js_性能优化_1", "title": "渲染性能与重排重绘",
                "topic": "性能优化",
                "content": (
                    "浏览器渲染流水线：JS → Style → Layout（重排）→ Paint（重绘）→ Composite（合成）。重排最昂贵。"
                    "减少重排：(1) DocumentFragment 批量 DOM 操作；(2) `display:none` 离线操作；(3) 读写分离——批量读、批量写；(4) `transform/opacity` 只触发合成。"
                    "`requestAnimationFrame` 浏览器下次重绘前回调，适合动画。`requestIdleCallback` 空闲时执行低优先级任务。"
                    "虚拟列表：只渲染可视区域 DOM。`IntersectionObserver` 检测可见性。"
                ),
                "examples": [
                    "// DocumentFragment 批量更新\nconst frag = document.createDocumentFragment();\nfor (let i=0; i<1000; i++) {\n    const li = document.createElement('li');\n    li.textContent = `Item ${i}`; frag.appendChild(li);\n}\ndocument.getElementById('list').appendChild(frag);\n\n// requestAnimationFrame 动画\nfunction animate() {\n    el.style.transform = `translateX(${x}px)`; // 仅合成\n    x++; requestAnimationFrame(animate);\n}"
                ],
                "key_points": ["重排 > 重绘 > 合成，transform/opacity 仅触发合成", "DocumentFragment + display:none + 读写分离减少重排", "requestAnimationFrame 动画，requestIdleCallback 低优任务"],
            },
            {
                "id": "lesson_js_性能优化_2", "title": "内存与加载优化",
                "topic": "性能优化",
                "content": (
                    "内存泄漏原因：(1) 全局变量；(2) 遗忘的定时器/回调；(3) 闭包保留大对象；(4) DOM 引用（移除节点后仍被 JS 引用）。"
                    "WeakMap/WeakSet：键弱引用，不阻止 GC。适合缓存 DOM 元数据、私有数据。"
                    "代码分割：`import('./module.js')` 动态导入按需加载。Webpack splitChunks / Vite 自动分包。"
                    "Tree Shaking：ES Module 静态分析移除未使用导出。`sideEffects: false`。图片优化：WebP、懒加载 `loading='lazy'`、`srcset`。"
                    "性能监控：Performance API、Lighthouse、Core Web Vitals（LCP/FID/CLS）。"
                ),
                "examples": [
                    "// WeakMap 防 DOM 内存泄漏\nconst metaMap = new WeakMap();\nfunction setMeta(el, data) { metaMap.set(el, data); }\n// el 移除后 meta entry 自动回收\n\n// 动态导入\nbtn.addEventListener('click', async () => {\n    const { showModal } = await import('./modal.js');\n    showModal();\n});\n\n// 图片懒加载\n// <img src=\"placeholder.jpg\" data-src=\"real.jpg\" loading=\"lazy\">"
                ],
                "key_points": ["WeakMap/WeakSet 弱引用防内存泄漏", "动态 import() 代码分割 + Tree Shaking 减体积", "Performance API + Core Web Vitals 性能监控"],
            },
        ],
    },
    {
        "topic": "安全最佳实践",
        "lessons": [
            {
                "id": "lesson_js_安全最佳实践_1", "title": "XSS 与 CSRF 防御",
                "topic": "安全最佳实践",
                "content": (
                    "XSS：注入恶意脚本。三种类型：反射型、存储型、DOM 型。"
                    "防御：(1) `textContent` 而非 `innerHTML`；(2) CSP（Content-Security-Policy）；(3) DOMPurify 清洗 HTML。"
                    "CSRF：利用已登录身份发送恶意请求。防御：(1) SameSite Cookie；(2) CSRF Token；(3) 验证 Referer/Origin。"
                    "HttpOnly Cookie 防 JS 读取，Secure 仅 HTTPS。避免 `eval()` 和 `new Function()`。"
                ),
                "examples": [
                    "// 安全 DOM 操作\n// ❌ element.innerHTML = userInput;\n// ✅ element.textContent = userInput;\n// ✅ element.innerHTML = DOMPurify.sanitize(userInput);\n\n// CSRF Token\n// <meta name=\"csrf-token\" content=\"{{token}}\">\n// fetch('/api', { headers: { 'X-CSRF-Token': token } });\n\n// CSP Header\n// Content-Security-Policy: default-src 'self'; script-src 'self' 'nonce-{r}'"
                ],
                "key_points": ["XSS 防御：textContent + CSP + DOMPurify", "CSRF 防御：SameSite + CSRF Token + Origin 验证", "避免 eval()/new Function()，HttpOnly/Secure Cookie"],
            },
            {
                "id": "lesson_js_安全最佳实践_2", "title": "依赖安全与CORS",
                "topic": "安全最佳实践",
                "content": (
                    "CORS：服务器通过 Access-Control-Allow-Origin Header 控制跨域。预检请求（OPTIONS）。"
                    "安全配置：精确 Origin 不要用 `*` + 凭据。`Access-Control-Allow-Credentials: true`。"
                    "npm 安全：(1) `npm audit` 检查漏洞；(2) Snyk/Dependabot 自动 PR；(3) 锁定版本；(4) 审查许可证。"
                    "原型污染：`Object.assign`/`merge` 递归合并可污染 `__proto__`。防御：`Object.create(null)`、`hasOwnProperty`。"
                    "敏感信息：前端不硬编码 API Key。环境变量 + 服务端代理。`.gitignore` 排除 `.env`。"
                ),
                "examples": [
                    "// 原型污染防御\nconst safeObj = Object.create(null);\nsafeObj.key = 'value'; // 无 __proto__\n\n// 安全深度合并（hasOwnProperty 防御）\n// function safeMerge(target, source) {\n//     for (let k of Object.keys(source)) {\n//         if (k === '__proto__' || k === 'constructor') continue;\n//         target[k] = source[k];\n//     }\n// }\n\n// npm audit\n// $ npm audit && npm audit fix"
                ],
                "key_points": ["CORS 精确配置 Origin，勿用 * + 凭据", "npm audit + 依赖锁定 + Snyk 持续扫描", "原型污染防御：Object.create(null) + hasOwnProperty"],
            },
        ],
    },
    {
        "topic": "迭代器与生成器",
        "lessons": [
            {
                "id": "lesson_js_迭代器与生成器_1", "title": "迭代器协议",
                "topic": "迭代器与生成器",
                "content": (
                    "迭代器协议：`next()` 方法返回 `{ value, done }`。可迭代协议：`[Symbol.iterator]()` 方法返回迭代器。"
                    "内置可迭代：Array、String、Map、Set、TypedArray、arguments、NodeList。`for...of` 消费。"
                    "自定义迭代器：实现 `[Symbol.iterator]() { return { next() { return {value, done} } } }`。`[...iterable]` 展开。"
                    "异步迭代器（ES2018）：`[Symbol.asyncIterator]()`，`for await...of` 消费。"
                ),
                "examples": [
                    "// 自定义可迭代（斐波那契）\nconst fib = {\n    [Symbol.iterator]() {\n        let a=0, b=1;\n        return { next() { const v=a; [a,b]=[b,a+b]; return v>100?{done:true}:{value:v,done:false}; } };\n    }\n};\nconsole.log([...fib]); // [0,1,1,2,3,5,8,13,21,34,55,89]\n\n// 异步迭代器\n// const api = { [Symbol.asyncIterator]() { ... return { async next(){...} } } };\n// for await (const page of api) { console.log(page); }"
                ],
                "key_points": ["迭代器 {next() => {value, done}}，[Symbol.iterator] 返回迭代器", "for...of 消费可迭代，[...obj]/Array.from 展开", "异步迭代器 [Symbol.asyncIterator] + for await...of"],
            },
            {
                "id": "lesson_js_迭代器与生成器_2", "title": "Generator 函数",
                "topic": "迭代器与生成器",
                "content": (
                    "Generator: `function*` + `yield` 暂停/恢复。调用返回迭代器，`next()` 恢复执行到下一 `yield`。"
                    "双向通信：`next(value)` 传入值作为上一个 `yield` 返回值。`throw(err)` 抛异常，`return(val)` 提前终止。"
                    "`yield*` 委托给另一生成器/可迭代对象：`yield* otherGenerator()` 展开内层迭代。"
                    "应用：(1) 惰性求值（无限序列）；(2) 状态机；(3) 异步流程控制（redux-saga）。"
                    "async generator（ES2018）：`async function*` + `yield await`，配合 `for await...of`。"
                ),
                "examples": [
                    "// Generator 惰性 ID 生成器\nfunction* idGen() { let id=0; while(true) yield ++id; }\nconst ids = idGen();\nids.next().value; // 1\nids.next().value; // 2\n\n// yield* 委派\nfunction* walk(node) {\n    yield node.value;\n    for (const c of node.children) yield* walk(c);\n}\n\n// 异步 Generator\n// async function* range(s,e) { for(let i=s;i<=e;i++) { await delay(100); yield i; } }\n// for await (const n of range(1,5)) { console.log(n); }"
                ],
                "key_points": ["function* + yield 暂停/恢复，next(value) 双向通信", "yield* 委派到另一生成器，递归遍历树结构", "async generator + for await...of 处理异步流数据"],
            },
        ],
    },
]

# ================================================================
# C++ 课程（10 个主题，每主题 2 节课）
# ================================================================
CPP_LEARNING_PATH = [
    {
        "topic": "C++基础",
        "lessons": [
            {
                "id": "lesson_cpp_C++基础_1", "title": "C++基础",
                "topic": "C++基础",
                "content": (
                    "\"C++编译模型：预处理#include、编译.cpp到.o、链接。g++/clang++编译器。main()入口函数。\""
                    "\"基本类型：bool/char/int/float/double/void。修饰符signed/unsigned/short/long。sizeof获取字节数。\""
                    "\"引用类型：T&别名必须初始化不可重新绑定。const变量+引用+指针。auto自动类型推导。\""
                ),
                "examples": [
                "#include <iostream>\nint main() {\n    int x = 42;\n    const int& rx = x;\n    auto y = x;\n    return 0;\n}"
                ],
                "key_points": ["预处理、编译、链接三阶段", "引用vs指针，const+auto类型推导"],
            },
            {
                "id": "lesson_cpp_C++基础_2", "title": "C++基础",
                "topic": "C++基础",
                "content": (
                    "\"C++编译模型：预处理#include、编译.cpp到.o、链接。g++/clang++编译器。main()入口函数。\""
                    "\"基本类型：bool/char/int/float/double/void。修饰符signed/unsigned/short/long。sizeof获取字节数。\""
                    "\"引用类型：T&别名必须初始化不可重新绑定。const变量+引用+指针。auto自动类型推导。\""
                ),
                "examples": [
                "#include <iostream>\nint main() {\n    int x = 42;\n    const int& rx = x;\n    auto y = x;\n    return 0;\n}"
                ],
                "key_points": ["预处理、编译、链接三阶段", "引用vs指针，const+auto类型推导"],
            },
        ],
    },
    {
        "topic": "指针与内存",
        "lessons": [
            {
                "id": "lesson_cpp_指针与内存_1", "title": "指针与内存",
                "topic": "指针与内存",
                "content": (
                    "\"指针：T*存储地址，&取地址，*解引用。nullptr (C++11)空指针。指针算术p+n。\""
                    "\"new/delete手动内存管理。new T堆分配、delete释放。new T[]/delete[]数组。\""
                    "\"栈vs堆：栈自动管理快但有限；堆手动管理灵活易泄漏。智能指针替代raw new/delete。\""
                ),
                "examples": [
                "int x = 10;\nint* p = &x;\n*p = 20;\n\nint* arr = new int[100];\ndelete[] arr;"
                ],
                "key_points": ["指针存储地址，&取地址，*解引用", "new/delete堆内存手动管理", "智能指针替换raw pointer避免泄漏"],
            },
            {
                "id": "lesson_cpp_指针与内存_2", "title": "指针与内存",
                "topic": "指针与内存",
                "content": (
                    "\"指针：T*存储地址，&取地址，*解引用。nullptr (C++11)空指针。指针算术p+n。\""
                    "\"new/delete手动内存管理。new T堆分配、delete释放。new T[]/delete[]数组。\""
                    "\"栈vs堆：栈自动管理快但有限；堆手动管理灵活易泄漏。智能指针替代raw new/delete。\""
                ),
                "examples": [
                "int x = 10;\nint* p = &x;\n*p = 20;\n\nint* arr = new int[100];\ndelete[] arr;"
                ],
                "key_points": ["指针存储地址，&取地址，*解引用", "new/delete堆内存手动管理", "智能指针替换raw pointer避免泄漏"],
            },
        ],
    },
    {
        "topic": "面向对象",
        "lessons": [
            {
                "id": "lesson_cpp_面向对象_1", "title": "面向对象",
                "topic": "面向对象",
                "content": (
                    "\"class/struct定义类。public/private/protected访问控制。构造函数+析构函数。\""
                    "\"继承：class Dog : public Animal {}。虚函数virtual+override。纯虚函数=0抽象类。\""
                    "\"多态：基类指针调用派生类方法。虚表(vtable)实现动态绑定。final禁止重写/继承。\""
                ),
                "examples": [
                "class Animal { public: virtual void speak() { } virtual ~Animal() = default; };\nclass Dog : public Animal { public: void speak() override { std::cout << \"Woof\"; } };"
                ],
                "key_points": ["class封装 + public/private/protected", "virtual+override动态多态，纯虚函数抽象类", "虚表(vtable)实现，final禁止重写"],
            },
            {
                "id": "lesson_cpp_面向对象_2", "title": "面向对象",
                "topic": "面向对象",
                "content": (
                    "\"class/struct定义类。public/private/protected访问控制。构造函数+析构函数。\""
                    "\"继承：class Dog : public Animal {}。虚函数virtual+override。纯虚函数=0抽象类。\""
                    "\"多态：基类指针调用派生类方法。虚表(vtable)实现动态绑定。final禁止重写/继承。\""
                ),
                "examples": [
                "class Animal { public: virtual void speak() { } virtual ~Animal() = default; };\nclass Dog : public Animal { public: void speak() override { std::cout << \"Woof\"; } };"
                ],
                "key_points": ["class封装 + public/private/protected", "virtual+override动态多态，纯虚函数抽象类", "虚表(vtable)实现，final禁止重写"],
            },
        ],
    },
    {
        "topic": "运算符重载",
        "lessons": [
            {
                "id": "lesson_cpp_运算符重载_1", "title": "运算符重载",
                "topic": "运算符重载",
                "content": (
                    "\"运算符重载：成员函数或友元函数。operator+/-/*/==等。返回类型合理设计。\""
                    "\"流运算符：ostream& operator<<(ostream&, const T&)必须友元。istream& operator>>。\""
                    "\"赋值与比较：operator=处理自赋值。operator==配合!=。operator<=>三路比较(C++20)。\""
                ),
                "examples": [
                "class Vec { public:\n    Vec operator+(const Vec& o) const { return Vec{x+o.x, y+o.y}; }\n    bool operator==(const Vec& o) const { return x==o.x && y==o.y; }\n    friend std::ostream& operator<<(std::ostream& os, const Vec& v);\n};"
                ],
                "key_points": ["成员/友元函数重载运算符", "operator<<友元输出流", "<=>三路比较(C++20)自动生成比较"],
            },
            {
                "id": "lesson_cpp_运算符重载_2", "title": "运算符重载",
                "topic": "运算符重载",
                "content": (
                    "\"运算符重载：成员函数或友元函数。operator+/-/*/==等。返回类型合理设计。\""
                    "\"流运算符：ostream& operator<<(ostream&, const T&)必须友元。istream& operator>>。\""
                    "\"赋值与比较：operator=处理自赋值。operator==配合!=。operator<=>三路比较(C++20)。\""
                ),
                "examples": [
                "class Vec { public:\n    Vec operator+(const Vec& o) const { return Vec{x+o.x, y+o.y}; }\n    bool operator==(const Vec& o) const { return x==o.x && y==o.y; }\n    friend std::ostream& operator<<(std::ostream& os, const Vec& v);\n};"
                ],
                "key_points": ["成员/友元函数重载运算符", "operator<<友元输出流", "<=>三路比较(C++20)自动生成比较"],
            },
        ],
    },
    {
        "topic": "模板基础",
        "lessons": [
            {
                "id": "lesson_cpp_模板基础_1", "title": "模板基础",
                "topic": "模板基础",
                "content": (
                    "\"函数模板：template<typename T> T max(T a, T b)。编译器根据调用推导参数类型。\""
                    "\"类模板：template<typename T> class Vector { T* data; }。显式指定Vector<int>。\""
                    "\"特化：全特化template<> class Vector<bool> {}。偏特化处理指针/引用等特定类型族。\""
                ),
                "examples": [
                "template<typename T>\nT max(T a, T b) { return a > b ? a : b; }\n\ntemplate<typename T>\nclass Stack { std::vector<T> data; public: void push(T v); T pop(); };"
                ],
                "key_points": ["函数模板+类模板，编译期参数推导", "全特化+偏特化处理特定类型", "模板实例化发生在编译期"],
            },
            {
                "id": "lesson_cpp_模板基础_2", "title": "模板基础",
                "topic": "模板基础",
                "content": (
                    "\"函数模板：template<typename T> T max(T a, T b)。编译器根据调用推导参数类型。\""
                    "\"类模板：template<typename T> class Vector { T* data; }。显式指定Vector<int>。\""
                    "\"特化：全特化template<> class Vector<bool> {}。偏特化处理指针/引用等特定类型族。\""
                ),
                "examples": [
                "template<typename T>\nT max(T a, T b) { return a > b ? a : b; }\n\ntemplate<typename T>\nclass Stack { std::vector<T> data; public: void push(T v); T pop(); };"
                ],
                "key_points": ["函数模板+类模板，编译期参数推导", "全特化+偏特化处理特定类型", "模板实例化发生在编译期"],
            },
        ],
    },
    {
        "topic": "标准库",
        "lessons": [
            {
                "id": "lesson_cpp_标准库_1", "title": "标准库",
                "topic": "标准库",
                "content": (
                    "\"<iostream>：cin/cout输入输出。cerr错误流。getline(cin, s)读取一行。\""
                    "\"<string>：std::string动态字符串，+拼接，find查找，substr截取。string_view零拷贝。\""
                    "\"<vector>：动态数组，push_back追加，size长度，capacity容量。遍历：for(auto& v : vec)。\""
                ),
                "examples": [
                "std::vector<int> v;\nv.push_back(1);\nfor (auto& x : v) { std::cout << x; }\n\nstd::string s = \"hello\";\nauto sub = s.substr(0, 3);"
                ],
                "key_points": ["iostream输入输出，string动态字符串", "vector动态数组，range-for遍历", "string_view零拷贝视图"],
            },
            {
                "id": "lesson_cpp_标准库_2", "title": "标准库",
                "topic": "标准库",
                "content": (
                    "\"<iostream>：cin/cout输入输出。cerr错误流。getline(cin, s)读取一行。\""
                    "\"<string>：std::string动态字符串，+拼接，find查找，substr截取。string_view零拷贝。\""
                    "\"<vector>：动态数组，push_back追加，size长度，capacity容量。遍历：for(auto& v : vec)。\""
                ),
                "examples": [
                "std::vector<int> v;\nv.push_back(1);\nfor (auto& x : v) { std::cout << x; }\n\nstd::string s = \"hello\";\nauto sub = s.substr(0, 3);"
                ],
                "key_points": ["iostream输入输出，string动态字符串", "vector动态数组，range-for遍历", "string_view零拷贝视图"],
            },
        ],
    },
    {
        "topic": "文件操作",
        "lessons": [
            {
                "id": "lesson_cpp_文件操作_1", "title": "文件操作",
                "topic": "文件操作",
                "content": (
                    "\"<fstream>：ifstream读文件，ofstream写文件，fstream读写。open/close管理文件句柄。\""
                    "\"读写模式：ios::in/out/binary/ate/app。二进制读写read/write。\""
                    "\"错误处理：is_open()检查打开。fail()/bad()/eof()判断状态。异常exceptions()。\""
                ),
                "examples": [
                "std::ifstream ifs(\"data.txt\");\nif (!ifs.is_open()) { return 1; }\nstd::string line;\nwhile (std::getline(ifs, line)) { std::cout << line; }\n\nstd::ofstream ofs(\"out.txt\");\nofs << \"Hello\";"
                ],
                "key_points": ["ifstream/ofstream文件读写", "getline逐行读取，is_open检查", "二进制模式+错误状态fail/bad/eof"],
            },
            {
                "id": "lesson_cpp_文件操作_2", "title": "文件操作",
                "topic": "文件操作",
                "content": (
                    "\"<fstream>：ifstream读文件，ofstream写文件，fstream读写。open/close管理文件句柄。\""
                    "\"读写模式：ios::in/out/binary/ate/app。二进制读写read/write。\""
                    "\"错误处理：is_open()检查打开。fail()/bad()/eof()判断状态。异常exceptions()。\""
                ),
                "examples": [
                "std::ifstream ifs(\"data.txt\");\nif (!ifs.is_open()) { return 1; }\nstd::string line;\nwhile (std::getline(ifs, line)) { std::cout << line; }\n\nstd::ofstream ofs(\"out.txt\");\nofs << \"Hello\";"
                ],
                "key_points": ["ifstream/ofstream文件读写", "getline逐行读取，is_open检查", "二进制模式+错误状态fail/bad/eof"],
            },
        ],
    },
    {
        "topic": "命名空间",
        "lessons": [
            {
                "id": "lesson_cpp_命名空间_1", "title": "命名空间",
                "topic": "命名空间",
                "content": (
                    "\"namespace name {}定义命名空间。::作用域解析。using namespace引入命名空间。\""
                    "\"匿名命名空间：内部链接，文件作用域私有。命名空间别名：namespace fs = std::filesystem。\""
                    "\"内联命名空间：inline namespace版本控制。ADL(Argument-Dependent Lookup)参数依赖查找。\""
                ),
                "examples": [
                "namespace math {\n    int add(int a, int b) { return a + b; }\n}\nusing namespace math;\nint r = add(1, 2);\n\nnamespace fs = std::filesystem;"
                ],
                "key_points": ["namespace组织代码防命名冲突", "using namespace引入，::解析", "匿名命名空间文件私有，ADL参数查找"],
            },
            {
                "id": "lesson_cpp_命名空间_2", "title": "命名空间",
                "topic": "命名空间",
                "content": (
                    "\"namespace name {}定义命名空间。::作用域解析。using namespace引入命名空间。\""
                    "\"匿名命名空间：内部链接，文件作用域私有。命名空间别名：namespace fs = std::filesystem。\""
                    "\"内联命名空间：inline namespace版本控制。ADL(Argument-Dependent Lookup)参数依赖查找。\""
                ),
                "examples": [
                "namespace math {\n    int add(int a, int b) { return a + b; }\n}\nusing namespace math;\nint r = add(1, 2);\n\nnamespace fs = std::filesystem;"
                ],
                "key_points": ["namespace组织代码防命名冲突", "using namespace引入，::解析", "匿名命名空间文件私有，ADL参数查找"],
            },
        ],
    },
    {
        "topic": "异常处理",
        "lessons": [
            {
                "id": "lesson_cpp_异常处理_1", "title": "异常处理",
                "topic": "异常处理",
                "content": (
                    "\"try {} catch(exception& e) {}异常捕获。throw抛出。标准异常<stdexcept>。\""
                    "\"标准异常：runtime_error/logic_error/out_of_range。what()获取信息。\""
                    "\"析构函数不应抛异常。异常安全三大保证：基本保证、强保证、无抛保证。\""
                ),
                "examples": [
                "try {\n    if (divisor == 0) throw std::runtime_error(\"Division by zero\");\n    result = a / b;\n} catch (const std::exception& e) {\n    std::cerr << e.what();\n}"
                ],
                "key_points": ["try/catch/throw异常处理三件套", "runtime_error等标准异常", "析构函数不应抛异常"],
            },
            {
                "id": "lesson_cpp_异常处理_2", "title": "异常处理",
                "topic": "异常处理",
                "content": (
                    "\"try {} catch(exception& e) {}异常捕获。throw抛出。标准异常<stdexcept>。\""
                    "\"标准异常：runtime_error/logic_error/out_of_range。what()获取信息。\""
                    "\"析构函数不应抛异常。异常安全三大保证：基本保证、强保证、无抛保证。\""
                ),
                "examples": [
                "try {\n    if (divisor == 0) throw std::runtime_error(\"Division by zero\");\n    result = a / b;\n} catch (const std::exception& e) {\n    std::cerr << e.what();\n}"
                ],
                "key_points": ["try/catch/throw异常处理三件套", "runtime_error等标准异常", "析构函数不应抛异常"],
            },
        ],
    },
    {
        "topic": "现代C++实践",
        "lessons": [
            {
                "id": "lesson_cpp_现代C++实践_1", "title": "现代C++实践",
                "topic": "现代C++实践",
                "content": (
                    "\"C++11/14/17/20各版本核心特性演进路径。auto/decltype类型推导。\""
                    "\"Lambda表达式：[]() -> T { body }捕获外部变量。std::function存储可调用对象。\""
                    "\"智能指针不裸指针、range-for替代下标、constexpr编译期计算、override确保重写。\""
                ),
                "examples": [
                "auto add = [](int a, int b) { return a + b; };\n\nstd::unique_ptr<int> p = std::make_unique<int>(42);\n\nconstexpr int fib(int n) { return n <= 1 ? n : fib(n-1) + fib(n-2); }"
                ],
                "key_points": ["Lambda表达式+std::function可调用", "unique_ptr/make_unique替代raw new", "constexpr编译期计算+override安全重写"],
            },
            {
                "id": "lesson_cpp_现代C++实践_2", "title": "现代C++实践",
                "topic": "现代C++实践",
                "content": (
                    "\"C++11/14/17/20各版本核心特性演进路径。auto/decltype类型推导。\""
                    "\"Lambda表达式：[]() -> T { body }捕获外部变量。std::function存储可调用对象。\""
                    "\"智能指针不裸指针、range-for替代下标、constexpr编译期计算、override确保重写。\""
                ),
                "examples": [
                "auto add = [](int a, int b) { return a + b; };\n\nstd::unique_ptr<int> p = std::make_unique<int>(42);\n\nconstexpr int fib(int n) { return n <= 1 ? n : fib(n-1) + fib(n-2); }"
                ],
                "key_points": ["Lambda表达式+std::function可调用", "unique_ptr/make_unique替代raw new", "constexpr编译期计算+override安全重写"],
            },
        ],
    },
    {
        "topic": "模板元编程",
        "lessons": [
            {
                "id": "lesson_cpp_模板元编程_1", "title": "模板元编程",
                "topic": "模板元编程",
                "content": (
                    "\"模板元编程编译期执行计算。auto+decltype配合模板推导。std::enable_if+SFINAE条件编译。\""
                    "\"变参模板template<typename... Args>处理任意数量参数，sizeof...(Args)获取数量。\""
                    "\"折叠表达式(C++17)：(args+...)左折叠求和。constexpr函数编译期求值。if constexpr编译期分支。\""
                ),
                "examples": [
                "template<typename... Args>\nauto sum(Args... args) { return (args + ...); }\nauto r = sum(1, 2, 3, 4, 5);\n\ntemplate<typename T>\ntypename std::enable_if<std::is_integral<T>::value, T>::type\ndouble_it(T v) { return v * 2; }"
                ],
                "key_points": ["变参模板+折叠表达式编译期计算", "enable_if+SFINAE条件编译", "constexpr+if constexpr编译期求值"],
            },
            {
                "id": "lesson_cpp_模板元编程_2", "title": "模板元编程",
                "topic": "模板元编程",
                "content": (
                    "\"模板元编程编译期执行计算。auto+decltype配合模板推导。std::enable_if+SFINAE条件编译。\""
                    "\"变参模板template<typename... Args>处理任意数量参数，sizeof...(Args)获取数量。\""
                    "\"折叠表达式(C++17)：(args+...)左折叠求和。constexpr函数编译期求值。if constexpr编译期分支。\""
                ),
                "examples": [
                "template<typename... Args>\nauto sum(Args... args) { return (args + ...); }\nauto r = sum(1, 2, 3, 4, 5);\n\ntemplate<typename T>\ntypename std::enable_if<std::is_integral<T>::value, T>::type\ndouble_it(T v) { return v * 2; }"
                ],
                "key_points": ["变参模板+折叠表达式编译期计算", "enable_if+SFINAE条件编译", "constexpr+if constexpr编译期求值"],
            },
        ],
    },
    {
        "topic": "移动语义与转发",
        "lessons": [
            {
                "id": "lesson_cpp_移动语义_1", "title": "移动语义与转发",
                "topic": "移动语义与转发",
                "content": (
                    "\"右值引用T&&绑定临时对象。std::move将左值转为右值触发移动而非拷贝。\""
                    "\"移动构造T(T&&)noexcept和移动赋值。Rule of Five：5个特殊函数一起定义或全部缺省。\""
                    "\"std::forward<T>(arg)完美转发保留值类别。万能引用T&&右值推导，搭配forward使用。\""
                ),
                "examples": [
                "class Buffer {\n    std::vector<int> data;\npublic:\n    Buffer(Buffer&& other) noexcept : data(std::move(other.data)) {}\n};\n\ntemplate<typename T, typename... Args>\nauto make(Args&&... args) { return std::make_unique<T>(std::forward<Args>(args)...); }"
                ],
                "key_points": ["右值引用+std::move触发移动语义", "std::forward完美转发保留值类别", "Rule of Five：五函数同时定义或缺省"],
            },
            {
                "id": "lesson_cpp_移动语义_2", "title": "移动语义与转发",
                "topic": "移动语义与转发",
                "content": (
                    "\"右值引用T&&绑定临时对象。std::move将左值转为右值触发移动而非拷贝。\""
                    "\"移动构造T(T&&)noexcept和移动赋值。Rule of Five：5个特殊函数一起定义或全部缺省。\""
                    "\"std::forward<T>(arg)完美转发保留值类别。万能引用T&&右值推导，搭配forward使用。\""
                ),
                "examples": [
                "class Buffer {\n    std::vector<int> data;\npublic:\n    Buffer(Buffer&& other) noexcept : data(std::move(other.data)) {}\n};\n\ntemplate<typename T, typename... Args>\nauto make(Args&&... args) { return std::make_unique<T>(std::forward<Args>(args)...); }"
                ],
                "key_points": ["右值引用+std::move触发移动语义", "std::forward完美转发保留值类别", "Rule of Five：五函数同时定义或缺省"],
            },
        ],
    },
    {
        "topic": "RAII与资源管理",
        "lessons": [
            {
                "id": "lesson_cpp_RAII资源管理_1", "title": "RAII与资源管理",
                "topic": "RAII与资源管理",
                "content": (
                    "\"RAII：构造获取资源、析构自动释放，异常安全。unique_ptr独占、shared_ptr共享、weak_ptr打破循环。\""
                    "\"std::lock_guard/std::scoped_lock RAII锁，自动释放避免死锁。std::fstream自动关闭。\""
                    "\"自定义RAII类：delete拷贝构造/赋值，提供移动语义。析构函数noexcept保证。\""
                ),
                "examples": [
                "class FileGuard {\n    std::fstream fs;\npublic:\n    FileGuard(const std::string& path) : fs(path) {\n        if (!fs) throw std::runtime_error(\"Cannot open\");\n    }\n    ~FileGuard() { if (fs.is_open()) fs.close(); }\n    FileGuard(const FileGuard&) = delete;\n    FileGuard(FileGuard&&) noexcept = default;\n};"
                ],
                "key_points": ["RAII：构造获取资源，析构自动释放", "unique_ptr/shared_ptr/weak_ptr三件套", "scoped_lock RAII锁防死锁"],
            },
            {
                "id": "lesson_cpp_RAII资源管理_2", "title": "RAII与资源管理",
                "topic": "RAII与资源管理",
                "content": (
                    "\"RAII：构造获取资源、析构自动释放，异常安全。unique_ptr独占、shared_ptr共享、weak_ptr打破循环。\""
                    "\"std::lock_guard/std::scoped_lock RAII锁，自动释放避免死锁。std::fstream自动关闭。\""
                    "\"自定义RAII类：delete拷贝构造/赋值，提供移动语义。析构函数noexcept保证。\""
                ),
                "examples": [
                "class FileGuard {\n    std::fstream fs;\npublic:\n    FileGuard(const std::string& path) : fs(path) {\n        if (!fs) throw std::runtime_error(\"Cannot open\");\n    }\n    ~FileGuard() { if (fs.is_open()) fs.close(); }\n    FileGuard(const FileGuard&) = delete;\n    FileGuard(FileGuard&&) noexcept = default;\n};"
                ],
                "key_points": ["RAII：构造获取资源，析构自动释放", "unique_ptr/shared_ptr/weak_ptr三件套", "scoped_lock RAII锁防死锁"],
            },
        ],
    },
    {
        "topic": "STL容器与算法",
        "lessons": [
            {
                "id": "lesson_cpp_STL容器算法_1", "title": "STL容器与算法",
                "topic": "STL容器与算法",
                "content": (
                    "\"序列容器：vector动态数组、deque双端、list双向链表、forward_list。array固定大小。\""
                    "\"关联容器：set/map红黑树有序；unordered_set/map哈希O(1)。multiset/multimap允许重复。\""
                    "\"算法：sort排序、find查找、transform转换、accumulate累加、copy_if过滤。C++20 ranges管道惰性求值。\""
                ),
                "examples": [
                "std::vector<int> v{5,2,8,1,9};\nstd::sort(v.begin(), v.end(), [](int a,int b){return a>b;});\nauto it = std::find_if(v.begin(), v.end(), [](int n){return n>5;});\n\nnamespace sv = std::views;\nauto r = v | sv::filter([](int n){return n%2==0;}) | sv::transform([](int n){return n*n;});"
                ],
                "key_points": ["序列/关联/无序三大容器家族", "stdlib algorithms + Lambda组合", "C++20 ranges管道惰性求值"],
            },
            {
                "id": "lesson_cpp_STL容器算法_2", "title": "STL容器与算法",
                "topic": "STL容器与算法",
                "content": (
                    "\"序列容器：vector动态数组、deque双端、list双向链表、forward_list。array固定大小。\""
                    "\"关联容器：set/map红黑树有序；unordered_set/map哈希O(1)。multiset/multimap允许重复。\""
                    "\"算法：sort排序、find查找、transform转换、accumulate累加、copy_if过滤。C++20 ranges管道惰性求值。\""
                ),
                "examples": [
                "std::vector<int> v{5,2,8,1,9};\nstd::sort(v.begin(), v.end(), [](int a,int b){return a>b;});\nauto it = std::find_if(v.begin(), v.end(), [](int n){return n>5;});\n\nnamespace sv = std::views;\nauto r = v | sv::filter([](int n){return n%2==0;}) | sv::transform([](int n){return n*n;});"
                ],
                "key_points": ["序列/关联/无序三大容器家族", "stdlib algorithms + Lambda组合", "C++20 ranges管道惰性求值"],
            },
        ],
    },
    {
        "topic": "异常安全",
        "lessons": [
            {
                "id": "lesson_cpp_异常安全_1", "title": "异常安全",
                "topic": "异常安全",
                "content": (
                    "\"三级别：基本保证(不泄漏)、强保证(commit-or-rollback)、noexcept无抛保证。\""
                    "\"noexcept声明编译器可优化。移动构造应noexcept。noexcept(expr)条件判断。\""
                    "\"std::optional(C++17)表示可能无值；std::expected(C++23)带错误信息；std::variant多类型联合。\""
                ),
                "examples": [
                "class MyClass {\n    friend void swap(MyClass& a,MyClass& b) noexcept { std::swap(a.p,b.p); }\npublic:\n    MyClass& operator=(MyClass other) noexcept { swap(*this,other); return *this; }\n};\n\nstd::optional<int> divide(int a,int b) { return b ? std::optional{a/b} : std::nullopt; }"
                ],
                "key_points": ["noexcept声明+copy-and-swap强安全", "std::optional替代空指针", "std::expected(C++23)错误返回值"],
            },
            {
                "id": "lesson_cpp_异常安全_2", "title": "异常安全",
                "topic": "异常安全",
                "content": (
                    "\"三级别：基本保证(不泄漏)、强保证(commit-or-rollback)、noexcept无抛保证。\""
                    "\"noexcept声明编译器可优化。移动构造应noexcept。noexcept(expr)条件判断。\""
                    "\"std::optional(C++17)表示可能无值；std::expected(C++23)带错误信息；std::variant多类型联合。\""
                ),
                "examples": [
                "class MyClass {\n    friend void swap(MyClass& a,MyClass& b) noexcept { std::swap(a.p,b.p); }\npublic:\n    MyClass& operator=(MyClass other) noexcept { swap(*this,other); return *this; }\n};\n\nstd::optional<int> divide(int a,int b) { return b ? std::optional{a/b} : std::nullopt; }"
                ],
                "key_points": ["noexcept声明+copy-and-swap强安全", "std::optional替代空指针", "std::expected(C++23)错误返回值"],
            },
        ],
    },
    {
        "topic": "并发与多线程",
        "lessons": [
            {
                "id": "lesson_cpp_并发多线程_1", "title": "并发与多线程",
                "topic": "并发与多线程",
                "content": (
                    "\"std::thread创建线程，join()等待，detach()分离。jthread(C++20)自动join。\""
                    "\"mutex+lock_guard/unique_lock互斥。shared_mutex读写锁。条件变量condition_variable。\""
                    "\"atomic无锁原子操作。async+future异步。promise设置结果。latch/barrier(C++20)。\""
                ),
                "examples": [
                "std::atomic<int> counter{0};\nstd::vector<std::jthread> threads;\nfor (int i=0; i<4; ++i)\n    threads.emplace_back([&]{ for(int j=0;j<1000;++j) counter.fetch_add(1); });\n\nstd::mutex mtx;\n{ std::lock_guard<std::mutex> lock(mtx); /* critical */ }"
                ],
                "key_points": ["std::thread+atomic+mutex多线程", "jthread自动join，async+future异步", "shared_mutex读写锁，condition_variable"],
            },
            {
                "id": "lesson_cpp_并发多线程_2", "title": "并发与多线程",
                "topic": "并发与多线程",
                "content": (
                    "\"std::thread创建线程，join()等待，detach()分离。jthread(C++20)自动join。\""
                    "\"mutex+lock_guard/unique_lock互斥。shared_mutex读写锁。条件变量condition_variable。\""
                    "\"atomic无锁原子操作。async+future异步。promise设置结果。latch/barrier(C++20)。\""
                ),
                "examples": [
                "std::atomic<int> counter{0};\nstd::vector<std::jthread> threads;\nfor (int i=0; i<4; ++i)\n    threads.emplace_back([&]{ for(int j=0;j<1000;++j) counter.fetch_add(1); });\n\nstd::mutex mtx;\n{ std::lock_guard<std::mutex> lock(mtx); /* critical */ }"
                ],
                "key_points": ["std::thread+atomic+mutex多线程", "jthread自动join，async+future异步", "shared_mutex读写锁，condition_variable"],
            },
        ],
    },
    {
        "topic": "设计模式实践",
        "lessons": [
            {
                "id": "lesson_cpp_设计模式_1", "title": "设计模式实践",
                "topic": "设计模式实践",
                "content": (
                    "\"CRTP静态多态：template<typename D> class Base { D& derived() { return static_cast<D&>(*this); } }。\""
                    "\"PIMPL惯用法：隐藏实现减少编译依赖+ABI稳定。类型擦除：std::any/std::function。\""
                    "\"单例：静态局部变量C++11线程安全。工厂：static unique_ptr<T> create()。观察者：function回调。\""
                ),
                "examples": [
                "template<typename D> class Base { public: void iface() { static_cast<D*>(this)->impl(); } };\n\nclass Widget { struct Impl; std::unique_ptr<Impl> pImpl; public: Widget(); ~Widget(); };\n\nstd::any val = 42; int n = std::any_cast<int>(val);"
                ],
                "key_points": ["CRTP编译期静态多态，无虚表开销", "PIMPL隐藏实现减少编译依赖", "类型擦除：std::any/std::function"],
            },
            {
                "id": "lesson_cpp_设计模式_2", "title": "设计模式实践",
                "topic": "设计模式实践",
                "content": (
                    "\"CRTP静态多态：template<typename D> class Base { D& derived() { return static_cast<D&>(*this); } }。\""
                    "\"PIMPL惯用法：隐藏实现减少编译依赖+ABI稳定。类型擦除：std::any/std::function。\""
                    "\"单例：静态局部变量C++11线程安全。工厂：static unique_ptr<T> create()。观察者：function回调。\""
                ),
                "examples": [
                "template<typename D> class Base { public: void iface() { static_cast<D*>(this)->impl(); } };\n\nclass Widget { struct Impl; std::unique_ptr<Impl> pImpl; public: Widget(); ~Widget(); };\n\nstd::any val = 42; int n = std::any_cast<int>(val);"
                ],
                "key_points": ["CRTP编译期静态多态，无虚表开销", "PIMPL隐藏实现减少编译依赖", "类型擦除：std::any/std::function"],
            },
        ],
    },
    {
        "topic": "C++17/20新特性",
        "lessons": [
            {
                "id": "lesson_cpp_C1720新特性_1", "title": "C++17/20新特性",
                "topic": "C++17/20新特性",
                "content": (
                    "\"C++17：结构化绑定auto [x,y]=pair、if constexpr编译期分支、string_view零拷贝。\""
                    "\"C++20 Concepts：template<std::integral T>约束类型。requires子句表达复杂约束。\""
                    "\"C++20 Modules：import std;替代#include加速编译。std::format类型安全格式化。协程co_await/co_yield。\""
                ),
                "examples": [
                "auto [iter,ok] = mymap.insert({k,v});\ntemplate<typename T> auto get(T&& obj) {\n    if constexpr (std::is_pointer_v<T>) return *obj; else return obj;\n}\n\ntemplate<std::integral T> T gcd(T a,T b) { return b ? gcd(b,a%b) : a; }\nauto s = std::format(\"Hi {}!\", name);"
                ],
                "key_points": ["结构化绑定+if constexpr(C++17)", "Concepts+Modules+format(C++20)", "协程co_await/co_yield简化异步"],
            },
            {
                "id": "lesson_cpp_C1720新特性_2", "title": "C++17/20新特性",
                "topic": "C++17/20新特性",
                "content": (
                    "\"C++17：结构化绑定auto [x,y]=pair、if constexpr编译期分支、string_view零拷贝。\""
                    "\"C++20 Concepts：template<std::integral T>约束类型。requires子句表达复杂约束。\""
                    "\"C++20 Modules：import std;替代#include加速编译。std::format类型安全格式化。协程co_await/co_yield。\""
                ),
                "examples": [
                "auto [iter,ok] = mymap.insert({k,v});\ntemplate<typename T> auto get(T&& obj) {\n    if constexpr (std::is_pointer_v<T>) return *obj; else return obj;\n}\n\ntemplate<std::integral T> T gcd(T a,T b) { return b ? gcd(b,a%b) : a; }\nauto s = std::format(\"Hi {}!\", name);"
                ],
                "key_points": ["结构化绑定+if constexpr(C++17)", "Concepts+Modules+format(C++20)", "协程co_await/co_yield简化异步"],
            },
        ],
    }
]

GO_LEARNING_PATH = [
    {
        "topic": "Go基础",
        "lessons": [
            {
                "id": "lesson_go_Go基础_1", "title": "语法速览",
                "topic": "Go基础",
                "content": (
                    "Go 是静态强类型编译型语言，简洁为核心哲学。类型后置：`var name string`，短声明 `:=` 自动推断。"
                    "基本类型：bool/string/int/float/byte/rune，int 大小依赖平台。零值机制：未初始化变量有默认值（int=0, string=\"\"）。"
                    "控制流：`if` 可带短声明 `if n := len(s); n > 0 {}`，`for` 是唯一循环关键字（无 while），`switch` 默认不穿透。"
                    "`defer` 延迟执行（LIFO），`panic` 中断程序，`recover` 只在 defer 中捕获 panic。"
                ),
                "examples": [
                    "// 短声明\nname := \"Go\"\nage := 16\n// if 带短声明\nif n := len(s); n > 0 {\n    fmt.Println(n)\n}\n// defer LIFO\ndefer fmt.Println(\"first\")   // 最后执行\ndefer fmt.Println(\"second\")  // 先执行\n// recover\nfunc safeRun() {\n    defer func() {\n        if r := recover(); r != nil { fmt.Println(\"recovered:\", r) }\n    }()\n    panic(\"error\")\n}"
                ],
                "key_points": ["类型后置 / := 短声明", "for 是唯一循环 / switch 不穿透", "defer LIFO / panic-recover"],
            },
            {
                "id": "lesson_go_Go基础_2", "title": "包与模块",
                "topic": "Go基础",
                "content": (
                    "每个 .go 文件以 `package` 声明开头。`main` 包生成可执行文件，其他包生成库。大写符号导出，小写私有。"
                    "Go Modules（Go 1.11+）：`go mod init` 初始化模块，`go mod tidy` 清理依赖。`go.work`（1.18+）多模块工作区。"
                    "`import` 导入包，可用别名 `import f \"fmt\"`，空白导入 `import _ \"driver\"` 只执行 init()。"
                    "`init()` 函数在包导入时自动执行，用于初始化。每文件可有多个 init。"
                ),
                "examples": [
                    "// 包声明\npackage main\n\nimport (\n    \"fmt\"\n    m \"math\"  // 别名\n    _ \"database/sql/driver\"  // 只运行 init\n)\n\nfunc init() { fmt.Println(\"init\") }\nfunc main() { fmt.Println(m.Pi) }"
                ],
                "key_points": ["大写导出 / 小写私有", "go mod init/tidy 依赖管理", "init() 包导入时自动执行"],
            },
        ],
    },
    {
        "topic": "Go并发",
        "lessons": [
            {
                "id": "lesson_go_Go并发_1", "title": "goroutine 与 channel",
                "topic": "Go并发",
                "content": (
                    "`go fn()` 启动 goroutine（轻量级线程，~2KB 栈），M:N 调度器映射到 OS 线程。"
                    "channel 是 goroutine 间通信管道：`ch := make(chan int)`（无缓冲）或 `make(chan int, 10)`（缓冲）。"
                    "`ch <- v` 发送，`v := <-ch` 接收。无缓冲 channel 同步阻塞，缓冲 channel 满发送/空接收阻塞。"
                    "`close(ch)` 关闭 channel，`v, ok := <-ch` 检测关闭。`for v := range ch` 自动在关闭后退出。"
                ),
                "examples": [
                    "// goroutine\nfunc main() {\n    ch := make(chan string)\n    go func() { ch <- \"hello\" }()\n    msg := <-ch\n    fmt.Println(msg)\n}\n// range channel\nfor item := range ch {\n    process(item)\n}\n// select 多路复用\nselect {\ncase msg := <-ch1:\n    fmt.Println(msg)\ncase ch2 <- \"data\":\n    fmt.Println(\"sent\")\ndefault:\n    fmt.Println(\"no activity\")\n}"
                ],
                "key_points": ["go 关键字启动 goroutine", "channel: 发<-ch / 收ch<-", "select 多路复用/default 非阻塞"],
            },
            {
                "id": "lesson_go_Go并发_2", "title": "sync 与并发模式",
                "topic": "Go并发",
                "content": (
                    "`sync.Mutex`（互斥锁）+ `sync.RWMutex`（读写锁）+ `sync.WaitGroup`（等待组）+ `sync.Once`（单次执行）。"
                    "Pipeline 模式：多个 goroutine 通过 channel 串联处理数据流。"
                    "Fan-out/Fan-in：一个输入 channel 分发到多个 worker（fan-out），结果汇入一个 channel（fan-in）。"
                    "`context.Context`：超时、取消、传值，函数签名第一个参数 `func(ctx context.Context) error`。"
                ),
                "examples": [
                    "// WaitGroup\nvar wg sync.WaitGroup\nfor i := 0; i < 5; i++ {\n    wg.Add(1)\n    go func(id int) {\n        defer wg.Done()\n        work(id)\n    }(i)\n}\nwg.Wait()\n// context 超时\nctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)\ndefer cancel()\nselect {\ncase <-work(ctx):\ncase <-ctx.Done():\n    return ctx.Err()\n}"
                ],
                "key_points": ["Mutex/RWMutex/WaitGroup", "Pipeline + Fan-out/Fan-in", "context 超时/取消/传值"],
            },
        ],
    },
    {
        "topic": "Go接口",
        "lessons": [
            {
                "id": "lesson_go_Go接口_1", "title": "隐式接口",
                "topic": "Go接口",
                "content": (
                    "Go 接口是隐式满足：只要类型实现了接口所有方法，就自动实现接口，无需 `implements` 关键字。"
                    "`interface{}`（空接口，1.18+ 用 `any`）可存任意类型，需类型断言或反射取出。"
                    "类型断言：`v, ok := x.(T)` 安全断言，`switch x.(type)` 类型分支。"
                    "常见接口：`io.Reader` / `io.Writer` / `fmt.Stringer` / `error` / `sort.Interface`。"
                ),
                "examples": [
                    "type Greeter interface {\n    Greet() string\n}\ntype Person struct{ Name string }\nfunc (p Person) Greet() string { return \"Hi \" + p.Name }\n// 隐式满足 —— 无需 implements\nvar g Greeter = Person{Name: \"Go\"}\n\n// 类型断言\nif p, ok := g.(Person); ok {\n    fmt.Println(p.Name)\n}"
                ],
                "key_points": ["隐式满足接口", "any 存任意类型", "v, ok := x.(T) 安全断言"],
            },
            {
                "id": "lesson_go_Go接口_2", "title": "接口设计原则",
                "topic": "Go接口",
                "content": (
                    "\"接受接口，返回结构体\" 是 Go 核心设计原则，减少依赖。定义小接口（1-3 方法），如 io.Reader 只有 Read。"
                    "`http.Handler` 接口：`ServeHTTP(ResponseWriter, *Request)`，`http.HandlerFunc` 适配普通函数。"
                    "接口嵌套：`ReadWriter = Reader + Writer`。空接口 `any` 用于 JSON/数据库等通用场景。"
                    "接口值的内部表示：`(type, value)` 对，nil 接口 vs nil 值：仅当 type 和 value 都为 nil 时接口才是 nil。"
                ),
                "examples": [
                    "// 接受接口，返回结构体\nfunc Save(w io.Writer, data []byte) error {\n    _, err := w.Write(data)\n    return err\n}\n// 小接口组合\ntype ReadWriteCloser interface {\n    io.Reader\n    io.Writer\n    io.Closer\n}\n// nil 接口陷阱\nvar w io.Writer          // nil（type=nil, value=nil）\nvar buf *bytes.Buffer\nw = buf                  // 非 nil！（type=*bytes.Buffer, value=nil）"
                ],
                "key_points": ["接受接口，返回结构体", "小接口组合成大接口", "nil 接口陷阱：type 也需 nil"],
            },
        ],
    },
    {
        "topic": "Go错误处理",
        "lessons": [
            {
                "id": "lesson_go_Go错误处理_1", "title": "error 接口",
                "topic": "Go错误处理",
                "content": (
                    "Go 无异常机制，通过返回 `error` 表示错误：`func do() (result, error)`。调用方检查 `if err != nil`。"
                    "`errors.New(\"msg\")` 创建简单错误，`fmt.Errorf(\"context: %w\", err)` 包装错误（%w 保留原错误）。"
                    "`errors.Is(err, target)` 检查链中是否包含特定错误，`errors.As(err, &target)` 取出特定类型。"
                    "`errors.Join()`（1.20+）合并多个错误：`err := errors.Join(err1, err2)`。"
                ),
                "examples": [
                    "func divide(a, b float64) (float64, error) {\n    if b == 0 {\n        return 0, fmt.Errorf(\"divide: b is zero, a=%.2f\", a)\n    }\n    return a / b, nil\n}\nresult, err := divide(10, 0)\nif err != nil {\n    log.Fatal(err)\n}\n// 错误链\nvar targetErr *MyError\nif errors.As(err, &targetErr) { /* 处理 */ }"
                ],
                "key_points": ["返回 (value, error)", "fmt.Errorf %w 包装", "errors.Is/As 检查错误链"],
            },
            {
                "id": "lesson_go_Go错误处理_2", "title": "自定义错误与 sentinel",
                "topic": "Go错误处理",
                "content": (
                    "自定义错误类型：实现 `Error() string` 方法。Sentinel 错误：包级 var 表示特定状态 `var ErrNotFound = errors.New(\"not found\")`。"
                    "错误包装保留堆栈：`fmt.Errorf` 只能保留一层，用 `github.com/pkg/errors` 或 Go 1.23+ 标准库包装堆栈。"
                    "`defer` + 错误处理：`defer func() { if err != nil { err = fmt.Errorf(...) } }()` 在 defer 中修改命名返回值。"
                    "`io.EOF` 表示正常结束（非错误），`context.Canceled` / `context.DeadlineExceeded` 超时取消。"
                ),
                "examples": [
                    "// 自定义错误类型\ntype ValidationError struct {\n    Field string\n    Value any\n}\nfunc (e *ValidationError) Error() string {\n    return fmt.Sprintf(\"validation failed: %s=%v\", e.Field, e.Value)\n}\n// Sentinel 错误\nvar ErrNotFound = errors.New(\"not found\")\nif errors.Is(err, ErrNotFound) { /* 处理 */ }\n// defer 错误\nfunc do() (err error) {\n    defer func() {\n        if err != nil { err = fmt.Errorf(\"wrap: %w\", err) }\n    }()\n    return fmt.Errorf(\"bang\")\n}"
                ],
                "key_points": ["Error() string 自定义", "Sentinel 错误 errors.Is 匹配", "defer + 命名返回值修改错误"],
            },
        ],
    },
    {
        "topic": "Go数据结构",
        "lessons": [
            {
                "id": "lesson_go_Go数据结构_1", "title": "切片与映射",
                "topic": "Go数据结构",
                "content": (
                    "切片 slice：动态数组 `[]T`，底层引用数组。`make([]int, len, cap)` 创建，`append` 追加，扩容接近翻倍。"
                    "切片切割 `s[low:high]` 共享底层数组，`copy(dst, src)` 深拷贝。空切片 nil（len=0, cap=0）。"
                    "映射 map：`make(map[string]int)` 哈希表实现，`v, ok := m[key]` 安全取值。遍历无序。"
                    "`delete(m, key)` 删除键。不要依赖 map 遍历顺序，并发读写需加锁或用 `sync.Map`。"
                ),
                "examples": [
                    "// 切片\ns := make([]int, 0, 10)\ns = append(s, 1, 2, 3)\nsub := s[1:3]  // [2,3] 共享底层\n// map\nm := map[string]int{\"a\": 1, \"b\": 2}\nif v, ok := m[\"c\"]; ok {\n    fmt.Println(v)\n} else {\n    fmt.Println(\"not found\")\n}\ndelete(m, \"a\")"
                ],
                "key_points": ["slice = 动态数组 + append", "map 取值用 ,ok 判断", "切片切割共享底层数组"],
            },
            {
                "id": "lesson_go_Go数据结构_2", "title": "结构体与方法",
                "topic": "Go数据结构",
                "content": (
                    "`type Name struct { ... }` 定义结构体。`p := Person{Name: \"Go\"}` 字面量创建，`p.Name` 点访问。"
                    "方法：`func (p Person) Greet() string` 值接收者（只读），`func (p *Person) SetName(n string)` 指针接收者（可修改）。"
                    "`struct{}` 零内存占用，用作信号 channel：`ch := make(chan struct{})`。嵌入（组合）：`type Employee struct { Person }`。"
                    "`encoding/json` 标签控制序列化：`Name string \\`json:\"name\"\\``，`-` 忽略字段，`omitempty` 省略零值。"
                ),
                "examples": [
                    "type Person struct {\n    Name string `json:\"name\"`\n    Age  int    `json:\"age,omitempty\"`\n}\nfunc (p *Person) SetName(name string) { p.Name = name }\n// 嵌入（组合）\ntype Employee struct {\n    Person\n    Salary int\n}\ne := Employee{Person{Name: \"Go\"}, 100}\ne.Name  // 直接访问\n// struct{} 用途\nch := make(chan struct{})\nclose(ch)  // 无内存开销的信号"
                ],
                "key_points": ["值接收者 vs 指针接收者", "struct{} 零内存信号", "嵌入组合 + json 标签"],
            },
        ],
    },
    {
        "topic": "Go泛型",
        "lessons": [
            {
                "id": "lesson_go_Go泛型_1", "title": "类型参数与约束",
                "topic": "Go泛型",
                "content": (
                    "Go 1.18 引入泛型：`func Max[T constraints.Ordered](a, b T) T`，类型参数用方括号。"
                    "约束 `constraints.Ordered` 或自定义接口约束 `type Integer interface { ~int | ~int64 | ... }`。"
                    "`~` 近似约束：`~int` 匹配 int 及以其为底层类型的自定义类型。"
                    "泛型类型：`type Stack[T any] struct { items []T }`，方法也使用类型参数。"
                ),
                "examples": [
                    "// 泛型函数\nfunc Max[T cmp.Ordered](a, b T) T {\n    if a > b { return a }\n    return b\n}\n// 自定义约束\ntype Number interface {\n    ~int | ~int64 | ~float64\n}\nfunc Sum[T Number](nums []T) T {\n    var total T\n    for _, n := range nums { total += n }\n    return total\n}\n// 泛型类型\ntype Stack[T any] struct {\n    items []T\n}\nfunc (s *Stack[T]) Push(v T) { s.items = append(s.items, v) }"
                ],
                "key_points": ["func Name[T constraint](a T) T", "~int 近似约束", "any = interface{} 类型约束"],
            },
            {
                "id": "lesson_go_Go泛型_2", "title": "泛型接口与实战",
                "topic": "Go泛型",
                "content": (
                    "泛型接口：`type Comparable[T any] interface { Compare(T) int }`。注意 Go 不允许类型参数列表中的方法。"
                    "通用数据结构：`slices.Sort`（1.21+）、`maps.Clone`、`slices.Contains` 利用泛型提供通用操作。"
                    "性能：Go 泛型在运行时进行类型特化（GCShape stenciling），对同底层类型的类型共享一份代码（非单态化）。"
                    "设计建议：不要过度泛型化，简单场景用具体类型更清晰。优先为 slice/map 操作使用泛型。"
                ),
                "examples": [
                    "// slices 包（Go 1.21+）\nimport \"slices\"\nnames := []string{\"Bob\", \"Alice\", \"Charlie\"}\nslices.Sort(names)\nidx := slices.Index(names, \"Alice\")\n// maps 包\nimport \"maps\"\nm1 := map[string]int{\"a\": 1}\nm2 := maps.Clone(m1)\n// 泛型过滤器\nfunc Filter[T any](s []T, fn func(T) bool) []T {\n    var result []T\n    for _, v := range s { if fn(v) { result = append(result, v) } }\n    return result\n}"
                ],
                "key_points": ["slices/maps 泛型工具包", "GCShape stenciling 性能模型", "不过度泛型化，优先简单"],
            },
        ],
    },
    {
        "topic": "Go测试",
        "lessons": [
            {
                "id": "lesson_go_Go测试_1", "title": "单元测试与表格测试",
                "topic": "Go测试",
                "content": (
                    "测试文件以 `_test.go` 结尾，函数签名 `func TestXxx(t *testing.T)`。`go test` 运行，`-v` 详细，`-run` 过滤。"
                    "表格驱动测试（Table-Driven Tests）：用匿名结构体切片定义输入和期望，循环执行。Go 社区标准风格。"
                    "`t.Run()` 创建子测试，`t.Parallel()` 并行运行。`t.Helper()` 标记辅助函数，错误报告定位到调用方。"
                    "`t.Fatal` 立即终止，`t.Fatalf` 带格式终止，`t.Error` 报告后继续。"
                ),
                "examples": [
                    "// 表格驱动测试\nfunc TestAdd(t *testing.T) {\n    tests := []struct {\n        name     string\n        a, b, want int\n    }{\n        {\"positive\", 1, 2, 3},\n        {\"negative\", -1, -2, -3},\n        {\"zero\", 0, 0, 0},\n    }\n    for _, tt := range tests {\n        t.Run(tt.name, func(t *testing.T) {\n            got := Add(tt.a, tt.b)\n            if got != tt.want { t.Errorf(\"Add(%d,%d)=%d, want %d\", tt.a, tt.b, got, tt.want) }\n        })\n    }\n}"
                ],
                "key_points": ["_test.go + TestXxx(t *testing.T)", "表格驱动测试 = 匿名结构体切片", "t.Run/t.Parallel/t.Helper"],
            },
            {
                "id": "lesson_go_Go测试_2", "title": "基准测试与竞态检测",
                "topic": "Go测试",
                "content": (
                    "基准测试：`func BenchmarkXxx(b *testing.B)`，`b.N` 次循环自动调整。`go test -bench=.` 运行。"
                    "`b.ResetTimer()` 排除初始化时间，`b.ReportAllocs()` 报告内存分配。"
                    "竞态检测：`go test -race` 编译时插入检测代码，运行时发现数据竞争（有性能开销，仅测试用）。"
                    "`testing/quick` 随机测试，`fuzz`（1.18+）模糊测试：`func FuzzXxx(f *testing.F)`，自动生成随机输入。"
                ),
                "examples": [
                    "// 基准测试\nfunc BenchmarkAdd(b *testing.B) {\n    for i := 0; i < b.N; i++ {\n        Add(100, 200)\n    }\n}\n// go test -bench=. -benchmem\n// Fuzz 测试\nfunc FuzzDivide(f *testing.F) {\n    f.Add(10.0, 2.0)\n    f.Fuzz(func(t *testing.T, a, b float64) {\n        if b == 0 { t.Skip() }\n        _ = a / b\n    })\n}\n// go test -fuzz=FuzzDivide"
                ],
                "key_points": ["Benchmark + b.N 循环", "go test -race 竞态检测", "Fuzz 模糊测试自动生成输入"],
            },
        ],
    },
    {
        "topic": "Go网络",
        "lessons": [
            {
                "id": "lesson_go_Go网络_1", "title": "HTTP 服务端",
                "topic": "Go网络",
                "content": (
                    "`net/http` 标准库：`http.HandleFunc` 注册路由，`http.ListenAndServe` 启动服务。"
                    "`http.Handler` 接口 `ServeHTTP(w http.ResponseWriter, r *http.Request)`。`http.NewServeMux` 多路复用器。"
                    "中间件：`func(h http.Handler) http.Handler` 函数签名包装。`r.Context()` 传递请求上下文。"
                    "`encoding/json`：`json.NewEncoder(w).Encode(v)` 输出 JSON，`json.NewDecoder(r.Body).Decode(&v)` 解析。"
                ),
                "examples": [
                    "// 简单 HTTP 服务\nfunc main() {\n    http.HandleFunc(\"/hello\", func(w http.ResponseWriter, r *http.Request) {\n        name := r.URL.Query().Get(\"name\")\n        json.NewEncoder(w).Encode(map[string]string{\"greeting\": \"Hello, \" + name})\n    })\n    http.ListenAndServe(\":8080\", nil)\n}\n// 中间件\nfunc Logger(next http.Handler) http.Handler {\n    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {\n        log.Println(r.Method, r.URL.Path)\n        next.ServeHTTP(w, r)\n    })\n}"
                ],
                "key_points": ["http.HandleFunc + ListenAndServe", "中间件 func(h Handler) Handler", "json.NewEncoder/Decoder 序列化"],
            },
            {
                "id": "lesson_go_Go网络_2", "title": "HTTP 客户端与 gRPC",
                "topic": "Go网络",
                "content": (
                    "`http.Get` 简单 GET，`http.Client{Timeout: ...}.Do(req)` 定制请求。`http.NewRequest` 创建请求。"
                    "`io.ReadAll(resp.Body)` 读取响应，`resp.Body.Close()` 必须关闭。"
                    "gRPC：Protobuf 定义 `.proto` → `protoc` 生成代码 → `grpc.NewServer` + `pb.RegisterXxxServer`。"
                    "gRPC 四种模式：Unary（一问一答）、Server Streaming、Client Streaming、Bidirectional Streaming。"
                ),
                "examples": [
                    "// HTTP 客户端\nresp, err := http.Get(\"https://api.example.com/data\")\nif err != nil { log.Fatal(err) }\ndefer resp.Body.Close()\nbody, _ := io.ReadAll(resp.Body)\n// gRPC 服务端\ns := grpc.NewServer()\npb.RegisterGreeterServer(s, &server{})\n// 四种模式\n// Unary: rpc Method(Request) returns (Response)\n// ServerStream: rpc Method(Request) returns (stream Response)\n// ClientStream: rpc Method(stream Request) returns (Response)\n// BidiStream: rpc Method(stream Request) returns (stream Response)"
                ],
                "key_points": ["http.Client + Timeout", "resp.Body 必须 Close", "gRPC 四种通信模式"],
            },
        ],
    },
    {
        "topic": "Go工程化",
        "lessons": [
            {
                "id": "lesson_go_Go工程化_1", "title": "项目布局与工具链",
                "topic": "Go工程化",
                "content": (
                    "标准布局：`cmd/`（入口）、`internal/`（私有）、`pkg/`（可复用）、`api/`（协议定义）。"
                    "`gofmt` / `goimports` 自动格式化，`go vet` 静态分析，`golangci-lint` 聚合检查。"
                    "`go build` 编译，`-ldflags=\"-X main.version=$(VERSION)\"` 注入版本。交叉编译：`GOOS=linux GOARCH=amd64 go build`。"
                    "`embed`（1.16+）将静态文件嵌入二进制：`//go:embed templates/*.html var tmplFS embed.FS`。"
                ),
                "examples": [
                    "// 版本注入\n// go build -ldflags=\"-X main.version=v1.2.3\"\npackage main\nvar version = \"dev\"\nfunc main() { fmt.Println(version) }\n// embed 嵌入文件\nimport \"embed\"\n//go:embed static/*\nvar staticFiles embed.FS\n// 交叉编译\n// GOOS=linux GOARCH=amd64 go build -o app-linux\n// GOOS=windows GOARCH=amd64 go build -o app.exe"
                ],
                "key_points": ["cmd/internal/pkg 布局", "gofmt/go vet/golangci-lint", "交叉编译 GOOS/GOARCH"],
            },
            {
                "id": "lesson_go_Go工程化_2", "title": "依赖注入与配置",
                "topic": "Go工程化",
                "content": (
                    "依赖注入（DI）：wire（Google）编译时生成、fx（Uber）运行时注入、手动构造函数注入。"
                    "配置管理：`os.Getenv` 环境变量，`flag` 命令行参数，`viper` 库读取 YAML/JSON/ENV 多源配置。"
                    "优雅关闭：`signal.NotifyContext` 监听 SIGINT/SIGTERM → `srv.Shutdown(ctx)` 等待活跃请求完成。"
                    "`net/http/pprof` 性能分析：`import _ \"net/http/pprof\"`，`go tool pprof` 分析 CPU/内存。"
                ),
                "examples": [
                    "// 优雅关闭\nctx, stop := signal.NotifyContext(context.Background(), os.Interrupt, syscall.SIGTERM)\ndefer stop()\nsrv := &http.Server{Addr: \":8080\"}\ngo srv.ListenAndServe()\n<-ctx.Done()\nshutdownCtx, cancel := context.WithTimeout(context.Background(), 30*time.Second)\ndefer cancel()\nsrv.Shutdown(shutdownCtx)\n// wire 依赖注入\n//go:build wireinject\nfunc InitApp() (*App, error) {\n    wire.Build(NewDB, NewService, NewController, NewApp)\n    return &App{}, nil\n}"
                ],
                "key_points": ["wire 编译时 DI", "viper 多源配置", "signal.NotifyContext 优雅关闭"],
            },
        ],
    },
    {
        "topic": "Go性能",
        "lessons": [
            {
                "id": "lesson_go_Go性能_1", "title": "内存与分配优化",
                "topic": "Go性能",
                "content": (
                    "逃逸分析：编译器决定变量分配在栈还是堆。`go build -gcflags=\"-m\"` 查看逃逸报告。"
                    "`sync.Pool` 复用临时对象减少 GC 压力。`strings.Builder` 优于 `+=` 拼接字符串。"
                    "预分配容量：`make([]T, 0, cap)` 避免多次扩容。`bytes.Buffer` 重用缓冲区。"
                    "GC 调优：`GOGC` 环境变量控制 GC 频率（默认 100，即堆翻倍触发）。"
                ),
                "examples": [
                    "// sync.Pool\nvar bufPool = sync.Pool{\n    New: func() any { return new(bytes.Buffer) },\n}\nbuf := bufPool.Get().(*bytes.Buffer)\nbuf.Reset()\ndefer bufPool.Put(buf)\n// 预分配\nusers := make([]User, 0, 100)\n// strings.Builder\nvar sb strings.Builder\nsb.WriteString(\"hello\")\nsb.WriteString(\" world\")\nresult := sb.String()"
                ],
                "key_points": ["逃逸分析：栈 vs 堆", "sync.Pool 复用临时对象", "预分配容量 + strings.Builder"],
            },
            {
                "id": "lesson_go_Go性能_2", "title": "性能剖析与优化",
                "topic": "Go性能",
                "content": (
                    "pprof CPU 分析：`go tool pprof http://localhost:6060/debug/pprof/profile?seconds=30`。"
                    "火焰图：`go tool pprof -http=:8081 profile.out` 可视化调用链。内存分析：`/debug/pprof/heap`。"
                    "`trace` 工具：`runtime/trace` 捕获 goroutine 调度、GC、系统调用等全貌。`go tool trace trace.out` 可视化。"
                    "优化顺序：先 profile → 找到热点 → 优化算法/降低分配 → 基准测试验证 → 生产监控。"
                ),
                "examples": [
                    "// CPU 分析\nimport _ \"net/http/pprof\"\n// 启动服务后: go tool pprof -http=:8081 http://localhost:6060/debug/pprof/profile?seconds=30\n// 内存分析\n// go tool pprof -http=:8081 http://localhost:6060/debug/pprof/heap\n// trace\nf, _ := os.Create(\"trace.out\")\ntrace.Start(f)\ndefer trace.Stop()\n// go tool trace trace.out"
                ],
                "key_points": ["pprof CPU/内存分析", "go tool pprof -http 火焰图", "trace 调度/GC 全貌分析"],
            },
        ],
    },
    {
        "topic": "接口与类型断言",
        "lessons": [
            {
                "id": "lesson_go_接口与类型断言_1", "title": "接口与类型断言",
                "topic": "接口与类型断言",
                "content": (
                    "\"Go接口是隐式实现约定的方法集合。type Reader interface { Read([]byte) (int, error) }。任何有Read方法的类型自动实现Reader。\""
                    "\"空接口interface{}可接受任意类型(Go 1.18+用any)。类型断言v, ok := x.(T)检查具体类型。type switch按类型分支。\""
                    "\"接口组合：type ReadWriter interface { Reader; Writer }。小接口优于大接口(ISP)。io.Reader/Writer标准组合。\""
                ),
                "examples": [
                "type Speaker interface { Speak() string }\n\ntype Dog struct{ Name string }\nfunc (d Dog) Speak() string { return d.Name + \" says woof!\" }\n\nvar s Speaker = Dog{Name: \"Rex\"}\n\n# 类型断言\nif dog, ok := s.(Dog); ok { fmt.Println(dog.Name) }\n\n# type switch\nswitch v := s.(type) {\ncase Dog: fmt.Println(\"Dog:\", v.Name)\ndefault: fmt.Println(\"Unknown\")\n}"
                ],
                "key_points": ["隐式接口实现，无需implements关键字", "类型断言 x.(T) 和 type switch", "空接口 any 可接受任意类型"],
            },
            {
                "id": "lesson_go_接口与类型断言_2", "title": "接口与类型断言",
                "topic": "接口与类型断言",
                "content": (
                    "\"Go接口是隐式实现约定的方法集合。type Reader interface { Read([]byte) (int, error) }。任何有Read方法的类型自动实现Reader。\""
                    "\"空接口interface{}可接受任意类型(Go 1.18+用any)。类型断言v, ok := x.(T)检查具体类型。type switch按类型分支。\""
                    "\"接口组合：type ReadWriter interface { Reader; Writer }。小接口优于大接口(ISP)。io.Reader/Writer标准组合。\""
                ),
                "examples": [
                "type Speaker interface { Speak() string }\n\ntype Dog struct{ Name string }\nfunc (d Dog) Speak() string { return d.Name + \" says woof!\" }\n\nvar s Speaker = Dog{Name: \"Rex\"}\n\n# 类型断言\nif dog, ok := s.(Dog); ok { fmt.Println(dog.Name) }\n\n# type switch\nswitch v := s.(type) {\ncase Dog: fmt.Println(\"Dog:\", v.Name)\ndefault: fmt.Println(\"Unknown\")\n}"
                ],
                "key_points": ["隐式接口实现，无需implements关键字", "类型断言 x.(T) 和 type switch", "空接口 any 可接受任意类型"],
            },
        ],
    },
    {
        "topic": "并发模型与Goroutine",
        "lessons": [
            {
                "id": "lesson_go_并发模型与Goroutine_1", "title": "并发模型与Goroutine",
                "topic": "并发模型与Goroutine",
                "content": (
                    "\"goroutine是Go运行时管理的轻量级线程。go func()启动。栈动态扩展(初始2KB)，百万级并发可行。\""
                    "\"channel：无缓冲ch := make(chan T)同步；有缓冲make(chan T, n)异步。ch <- v发送，v := <-ch接收。\""
                    "\"select多路复用：select { case v := <-ch1: ... case ch2 <- v: ... default: ... }。非阻塞default。\""
                ),
                "examples": [
                "# goroutine + channel\nch := make(chan string)\ngo func() { ch <- \"hello\" }()\nmsg := <-ch\n\n# select 多路复用\nselect {\ncase msg1 := <-ch1:\n    fmt.Println(\"from ch1:\", msg1)\ncase msg2 := <-ch2:\n    fmt.Println(\"from ch2:\", msg2)\ncase <-time.After(time.Second):\n    fmt.Println(\"timeout\")\n}"
                ],
                "key_points": ["goroutine轻量级线程，百万并发", "channel goroutine间通信", "select多路复用+超时控制"],
            },
            {
                "id": "lesson_go_并发模型与Goroutine_2", "title": "并发模型与Goroutine",
                "topic": "并发模型与Goroutine",
                "content": (
                    "\"goroutine是Go运行时管理的轻量级线程。go func()启动。栈动态扩展(初始2KB)，百万级并发可行。\""
                    "\"channel：无缓冲ch := make(chan T)同步；有缓冲make(chan T, n)异步。ch <- v发送，v := <-ch接收。\""
                    "\"select多路复用：select { case v := <-ch1: ... case ch2 <- v: ... default: ... }。非阻塞default。\""
                ),
                "examples": [
                "# goroutine + channel\nch := make(chan string)\ngo func() { ch <- \"hello\" }()\nmsg := <-ch\n\n# select 多路复用\nselect {\ncase msg1 := <-ch1:\n    fmt.Println(\"from ch1:\", msg1)\ncase msg2 := <-ch2:\n    fmt.Println(\"from ch2:\", msg2)\ncase <-time.After(time.Second):\n    fmt.Println(\"timeout\")\n}"
                ],
                "key_points": ["goroutine轻量级线程，百万并发", "channel goroutine间通信", "select多路复用+超时控制"],
            },
        ],
    },
    {
        "topic": "Context与超时控制",
        "lessons": [
            {
                "id": "lesson_go_Context与超时控制_1", "title": "Context与超时控制",
                "topic": "Context与超时控制",
                "content": (
                    "\"context.Context贯穿调用链传递截止时间、取消信号和请求级数据。context.Background()根上下文。\""
                    "\"WithCancel：ctx, cancel := context.WithCancel(parent)。cancel()取消所有子goroutine。\""
                    "\"WithTimeout/WithDeadline：自动超时取消。ctx.Done() channel在取消时关闭。ctx.Err()获取原因。\""
                ),
                "examples": [
                "ctx, cancel := context.WithTimeout(context.Background(), 3*time.Second)\ndefer cancel()\n\nresult := make(chan string)\ngo func() {\n    time.Sleep(2 * time.Second)\n    result <- \"done\"\n}()\n\nselect {\ncase res := <-result:\n    fmt.Println(res)\ncase <-ctx.Done():\n    fmt.Println(\"timeout:\", ctx.Err())\n}\n\n# 传递ctx\nfunc doWork(ctx context.Context) {\n    select { case <-ctx.Done(): return; default: /* work */ }\n}"
                ],
                "key_points": ["Context传递取消信号+截止时间", "WithCancel/WithTimeout/WithDeadline", "ctx.Done()监听取消，ctx.Err()原因"],
            },
            {
                "id": "lesson_go_Context与超时控制_2", "title": "Context与超时控制",
                "topic": "Context与超时控制",
                "content": (
                    "\"context.Context贯穿调用链传递截止时间、取消信号和请求级数据。context.Background()根上下文。\""
                    "\"WithCancel：ctx, cancel := context.WithCancel(parent)。cancel()取消所有子goroutine。\""
                    "\"WithTimeout/WithDeadline：自动超时取消。ctx.Done() channel在取消时关闭。ctx.Err()获取原因。\""
                ),
                "examples": [
                "ctx, cancel := context.WithTimeout(context.Background(), 3*time.Second)\ndefer cancel()\n\nresult := make(chan string)\ngo func() {\n    time.Sleep(2 * time.Second)\n    result <- \"done\"\n}()\n\nselect {\ncase res := <-result:\n    fmt.Println(res)\ncase <-ctx.Done():\n    fmt.Println(\"timeout:\", ctx.Err())\n}\n\n# 传递ctx\nfunc doWork(ctx context.Context) {\n    select { case <-ctx.Done(): return; default: /* work */ }\n}"
                ],
                "key_points": ["Context传递取消信号+截止时间", "WithCancel/WithTimeout/WithDeadline", "ctx.Done()监听取消，ctx.Err()原因"],
            },
        ],
    },
    {
        "topic": "错误处理与panic",
        "lessons": [
            {
                "id": "lesson_go_错误处理与panic_1", "title": "错误处理与panic",
                "topic": "错误处理与panic",
                "content": (
                    "\"Go显式错误处理：函数返回(value, error)。if err != nil { return err }逐层传递。\""
                    "\"errors.New/text创建错误。fmt.Errorf(\"%%w\", err)包装错误。errors.Is/As错误链判断。\""
                    "\"panic用于不可恢复错误(数组越界/空指针)。recover在defer中捕获panic恢复执行。慎用panic。\""
                ),
                "examples": [
                "func readConfig(path string) (*Config, error) {\n    data, err := os.ReadFile(path)\n    if err != nil { return nil, fmt.Errorf(\"read config: %w\", err) }\n    var cfg Config\n    if err := json.Unmarshal(data, &cfg); err != nil { return nil, err }\n    return &cfg, nil\n}\n\n# defer + recover\nfunc safeCall() {\n    defer func() { if r := recover(); r != nil { fmt.Println(\"recovered:\", r) } }()\n    panic(\"oops\")\n}"
                ],
                "key_points": ["显式 (value, error) 返回", "fmt.Errorf %w 包装，errors.Is/As 判断", "defer+recover捕获panic"],
            },
            {
                "id": "lesson_go_错误处理与panic_2", "title": "错误处理与panic",
                "topic": "错误处理与panic",
                "content": (
                    "\"Go显式错误处理：函数返回(value, error)。if err != nil { return err }逐层传递。\""
                    "\"errors.New/text创建错误。fmt.Errorf(\"%%w\", err)包装错误。errors.Is/As错误链判断。\""
                    "\"panic用于不可恢复错误(数组越界/空指针)。recover在defer中捕获panic恢复执行。慎用panic。\""
                ),
                "examples": [
                "func readConfig(path string) (*Config, error) {\n    data, err := os.ReadFile(path)\n    if err != nil { return nil, fmt.Errorf(\"read config: %w\", err) }\n    var cfg Config\n    if err := json.Unmarshal(data, &cfg); err != nil { return nil, err }\n    return &cfg, nil\n}\n\n# defer + recover\nfunc safeCall() {\n    defer func() { if r := recover(); r != nil { fmt.Println(\"recovered:\", r) } }()\n    panic(\"oops\")\n}"
                ],
                "key_points": ["显式 (value, error) 返回", "fmt.Errorf %w 包装，errors.Is/As 判断", "defer+recover捕获panic"],
            },
        ],
    },
    {
        "topic": "测试与基准",
        "lessons": [
            {
                "id": "lesson_go_测试与基准_1", "title": "测试与基准",
                "topic": "测试与基准",
                "content": (
                    "\"go test运行测试。文件名_test.go。函数签名TestXxx(t *testing.T)。t.Error/t.Fatal报告失败。\""
                    "\"表驱动测试(table-driven)：结构体切片定义多组输入输出，循环执行。覆盖率go test -cover。\""
                    "\"基准测试：BenchmarkXxx(b *testing.B)。b.ResetTimer()重置计时。go test -bench=. -benchmem。\""
                ),
                "examples": [
                "func TestAdd(t *testing.T) {\n    tests := []struct{ a, b, want int }{\n        {1, 2, 3}, {-1, 1, 0}, {0, 0, 0},\n    }\n    for _, tt := range tests {\n        got := Add(tt.a, tt.b)\n        if got != tt.want { t.Errorf(\"Add(%d,%d)=%d, want %d\", tt.a, tt.b, got, tt.want) }\n    }\n}\n\nfunc BenchmarkAdd(b *testing.B) {\n    for i := 0; i < b.N; i++ { Add(1, 2) }\n}"
                ],
                "key_points": ["go test + _test.go 文件", "表驱动测试多组输入输出", "go test -bench 基准测试"],
            },
            {
                "id": "lesson_go_测试与基准_2", "title": "测试与基准",
                "topic": "测试与基准",
                "content": (
                    "\"go test运行测试。文件名_test.go。函数签名TestXxx(t *testing.T)。t.Error/t.Fatal报告失败。\""
                    "\"表驱动测试(table-driven)：结构体切片定义多组输入输出，循环执行。覆盖率go test -cover。\""
                    "\"基准测试：BenchmarkXxx(b *testing.B)。b.ResetTimer()重置计时。go test -bench=. -benchmem。\""
                ),
                "examples": [
                "func TestAdd(t *testing.T) {\n    tests := []struct{ a, b, want int }{\n        {1, 2, 3}, {-1, 1, 0}, {0, 0, 0},\n    }\n    for _, tt := range tests {\n        got := Add(tt.a, tt.b)\n        if got != tt.want { t.Errorf(\"Add(%d,%d)=%d, want %d\", tt.a, tt.b, got, tt.want) }\n    }\n}\n\nfunc BenchmarkAdd(b *testing.B) {\n    for i := 0; i < b.N; i++ { Add(1, 2) }\n}"
                ],
                "key_points": ["go test + _test.go 文件", "表驱动测试多组输入输出", "go test -bench 基准测试"],
            },
        ],
    },
    {
        "topic": "Package与模块",
        "lessons": [
            {
                "id": "lesson_go_Package与模块_1", "title": "Package与模块",
                "topic": "Package与模块",
                "content": (
                    "\"go mod init modulepath创建模块。go.mod声明依赖，go.sum校验和锁定版本。\""
                    "\"包名与目录名一致。大写标识符Public导出，小写private包内可见。init()函数包初始化。\""
                    "\"go get/add添加依赖，go mod tidy清理。内部包internal/仅父目录及子目录可导入。\""
                ),
                "examples": [
                "# go.mod\nmodule github.com/user/project\ngo 1.21\nrequire github.com/gin-gonic/gin v1.9.1\n\n# 包结构\n// math/math.go\npackage math\nfunc Add(a, b int) int { return a + b }  # Public\nfunc sub(a, b int) int { return a - b }  # private\n\n// main.go\nimport \"github.com/user/project/math\"\nresult := math.Add(1, 2)"
                ],
                "key_points": ["go.mod声明模块+依赖版本", "大写导出Public，小写private", "internal包限制可见性"],
            },
            {
                "id": "lesson_go_Package与模块_2", "title": "Package与模块",
                "topic": "Package与模块",
                "content": (
                    "\"go mod init modulepath创建模块。go.mod声明依赖，go.sum校验和锁定版本。\""
                    "\"包名与目录名一致。大写标识符Public导出，小写private包内可见。init()函数包初始化。\""
                    "\"go get/add添加依赖，go mod tidy清理。内部包internal/仅父目录及子目录可导入。\""
                ),
                "examples": [
                "# go.mod\nmodule github.com/user/project\ngo 1.21\nrequire github.com/gin-gonic/gin v1.9.1\n\n# 包结构\n// math/math.go\npackage math\nfunc Add(a, b int) int { return a + b }  # Public\nfunc sub(a, b int) int { return a - b }  # private\n\n// main.go\nimport \"github.com/user/project/math\"\nresult := math.Add(1, 2)"
                ],
                "key_points": ["go.mod声明模块+依赖版本", "大写导出Public，小写private", "internal包限制可见性"],
            },
        ],
    },
    {
        "topic": "泛型编程",
        "lessons": [
            {
                "id": "lesson_go_泛型编程_1", "title": "泛型编程",
                "topic": "泛型编程",
                "content": (
                    "\"Go 1.18+支持泛型。类型参数：func Max[T cmp.Ordered](a, b T) T { if a > b { return a } return b }。\""
                    "\"类型约束：interface定义约束集。cmp.Ordered（有序类型）、constraints包（Go 1.21弃用转cmp）。\""
                    "\"泛型类型：type Stack[T any] struct { items []T }。方法带类型参数接收者。\""
                ),
                "examples": [
                "import \"cmp\"\n\nfunc Max[T cmp.Ordered](a, b T) T {\n    if a > b { return a } else { return b }\n}\nfmt.Println(Max(1, 2))       # int\nfmt.Println(Max(\"a\", \"b\"))   # string\n\ntype Stack[T any] struct { items []T }\nfunc (s *Stack[T]) Push(v T) { s.items = append(s.items, v) }\nfunc (s *Stack[T]) Pop() T { v := s.items[len(s.items)-1]; s.items = s.items[:len(s.items)-1]; return v }"
                ],
                "key_points": ["Go 1.18+泛型，类型参数[T constraint]", "any/cmp.Ordered标准约束", "泛型类型+泛型方法"],
            },
            {
                "id": "lesson_go_泛型编程_2", "title": "泛型编程",
                "topic": "泛型编程",
                "content": (
                    "\"Go 1.18+支持泛型。类型参数：func Max[T cmp.Ordered](a, b T) T { if a > b { return a } return b }。\""
                    "\"类型约束：interface定义约束集。cmp.Ordered（有序类型）、constraints包（Go 1.21弃用转cmp）。\""
                    "\"泛型类型：type Stack[T any] struct { items []T }。方法带类型参数接收者。\""
                ),
                "examples": [
                "import \"cmp\"\n\nfunc Max[T cmp.Ordered](a, b T) T {\n    if a > b { return a } else { return b }\n}\nfmt.Println(Max(1, 2))       # int\nfmt.Println(Max(\"a\", \"b\"))   # string\n\ntype Stack[T any] struct { items []T }\nfunc (s *Stack[T]) Push(v T) { s.items = append(s.items, v) }\nfunc (s *Stack[T]) Pop() T { v := s.items[len(s.items)-1]; s.items = s.items[:len(s.items)-1]; return v }"
                ],
                "key_points": ["Go 1.18+泛型，类型参数[T constraint]", "any/cmp.Ordered标准约束", "泛型类型+泛型方法"],
            },
        ],
    },
    {
        "topic": "标准库核心",
        "lessons": [
            {
                "id": "lesson_go_标准库核心_1", "title": "标准库核心",
                "topic": "标准库核心",
                "content": (
                    "\"net/http：HTTP服务与客户端。http.HandleFunc注册路由，http.ListenAndServe启动。encoding/json序列化。\""
                    "\"sync包：Mutex互斥锁，RWMutex读写锁，WaitGroup等待goroutine完成，Once单次执行。\""
                    "\"time包：time.Now()当前时间，Format格式化(2006-01-02 15:04:05)，Parse解析，Duration时间间隔。\""
                ),
                "examples": [
                "# HTTP Server\nhttp.HandleFunc(\"/hello\", func(w http.ResponseWriter, r *http.Request) {\n    json.NewEncoder(w).Encode(map[string]string{\"msg\": \"hello\"})\n})\nhttp.ListenAndServe(\":8080\", nil)\n\n# sync\nvar mu sync.Mutex; var wg sync.WaitGroup\nwg.Add(1); go func() { defer wg.Done(); mu.Lock(); defer mu.Unlock(); /* work */ }(); wg.Wait()\n\n# time\nt := time.Now(); t.Format(\"2006-01-02\"); dur := 3 * time.Second"
                ],
                "key_points": ["net/http + encoding/json", "sync.Mutex/WaitGroup/Once", "time.Format 2006-01-02 参照时间"],
            },
            {
                "id": "lesson_go_标准库核心_2", "title": "标准库核心",
                "topic": "标准库核心",
                "content": (
                    "\"net/http：HTTP服务与客户端。http.HandleFunc注册路由，http.ListenAndServe启动。encoding/json序列化。\""
                    "\"sync包：Mutex互斥锁，RWMutex读写锁，WaitGroup等待goroutine完成，Once单次执行。\""
                    "\"time包：time.Now()当前时间，Format格式化(2006-01-02 15:04:05)，Parse解析，Duration时间间隔。\""
                ),
                "examples": [
                "# HTTP Server\nhttp.HandleFunc(\"/hello\", func(w http.ResponseWriter, r *http.Request) {\n    json.NewEncoder(w).Encode(map[string]string{\"msg\": \"hello\"})\n})\nhttp.ListenAndServe(\":8080\", nil)\n\n# sync\nvar mu sync.Mutex; var wg sync.WaitGroup\nwg.Add(1); go func() { defer wg.Done(); mu.Lock(); defer mu.Unlock(); /* work */ }(); wg.Wait()\n\n# time\nt := time.Now(); t.Format(\"2006-01-02\"); dur := 3 * time.Second"
                ],
                "key_points": ["net/http + encoding/json", "sync.Mutex/WaitGroup/Once", "time.Format 2006-01-02 参照时间"],
            },
        ],
    }
]

# ================================================================
# Rust 课程（10 个主题，每主题 2 节课）
# ================================================================
RUST_LEARNING_PATH = [
    {
        "topic": "Rust基础",
        "lessons": [
            {
                "id": "lesson_rust_Rust基础_1", "title": "类型与所有权",
                "topic": "Rust基础",
                "content": (
                    "Rust 静态强类型，类型推断。基本类型：i8-u128/f32-f64/bool/char/usize/isize。`let` 默认不可变，`let mut` 可变。"
                    "所有权三原则：每个值有唯一所有者、离开作用域自动释放（drop）、所有权可转移（move）。"
                    "栈上 Copy 类型（整数/bool/char）自动复制，堆上数据（String/Vec）move 后原变量失效。"
                    "`Clone` 显式深拷贝，`Copy` 自动复制（互斥于 Drop）。`Drop` trait 自定义析构。"
                ),
                "examples": [
                    "// 所有权 move\nlet s1 = String::from(\"hello\");\nlet s2 = s1;  // s1 已失效\n// println!(\"{s1}\"); // Error: value borrowed after move\n\n// Copy vs Clone\nlet x = 42;\nlet y = x;  // Copy（x 仍有效）\nlet s3 = s2.clone();  // Clone（s2 仍有效）\n\n// Drop\ndrop(s3);  // 提前释放"
                ],
                "key_points": ["let 不可变 / let mut 可变", "所有权 move 后原变量失效", "Copy 自动复制 / Clone 显式"],
            },
            {
                "id": "lesson_rust_Rust基础_2", "title": "借用与生命周期",
                "topic": "Rust基础",
                "content": (
                    "借用：`&T` 不可变引用（可多个），`&mut T` 可变引用（只能一个）。同一作用域内不可变引用和可变引用不能共存。"
                    "引用必须始终有效（不能出现悬垂指针），编译器静态保证。"
                    "生命周期 `'a` 标注引用有效期，大部分情况编译器自动推导。`fn longest<'a>(x: &'a str, y: &'a str) -> &'a str`。"
                    "生命周期省略规则：每个引用参数都有独立生命周期，一个输入则赋给输出，方法中 &self 生命周期赋给输出。"
                ),
                "examples": [
                    "// 不可变借用\nlet s = String::from(\"hello\");\nlet r1 = &s;\nlet r2 = &s;  // OK: 多个不可变引用\n// let r3 = &mut s; // Error: 已有不可变引用\nprintln!(\"{r1} {r2}\");\n\n// 生命周期标注\nfn longest<'a>(x: &'a str, y: &'a str) -> &'a str {\n    if x.len() > y.len() { x } else { y }\n}"
                ],
                "key_points": ["&T 多读 / &mut T 单写", "引用永不悬垂", "生命周期 'a 编译器大多自动推导"],
            },
        ],
    },
    {
        "topic": "Rust枚举与匹配",
        "lessons": [
            {
                "id": "lesson_rust_Rust枚举与匹配_1", "title": "枚举与模式匹配",
                "topic": "Rust枚举与匹配",
                "content": (
                    "Rust 枚举可携带数据：`enum Result<T,E> { Ok(T), Err(E) }`。`Option<T>` 代替 null：`None` 或 `Some(v)`。"
                    "`match` 穷举匹配，编译器强制处理所有分支。`_` 通配符匹配其余，`if let` 只匹配一种模式。"
                    "解构：`match p { Point { x, y: 0 } => ... }`，`@` 绑定：`n @ 1..=5 => n`。"
                    "`matches!` 宏返回布尔值：`assert!(matches!(x, Ok(_)))`。"
                ),
                "examples": [
                    "// match\nlet result: Result<i32, &str> = Ok(42);\nmatch result {\n    Ok(v) => println!(\"成功: {v}\"),\n    Err(e) => println!(\"失败: {e}\"),\n}\n// if let\nif let Some(v) = maybe_value {\n    println!(\"{v}\");\n}\n// @ 绑定\nmatch num {\n    n @ 1..=5 => println!(\"小数字: {n}\"),\n    _ => (),\n}"
                ],
                "key_points": ["Option<T> 替代 null", "match 穷举匹配", "if let / matches! 简洁模式"],
            },
            {
                "id": "lesson_rust_Rust枚举与匹配_2", "title": "Result 与错误处理",
                "topic": "Rust枚举与匹配",
                "content": (
                    "`Result<T, E>` 是 Rust 错误处理标准。`?` 运算符传播错误：`let data = read_file()?`，遇到 Err 提前返回。"
                    "`main` 函数可返回 `Result<(), E>`。`unwrap()` 和 `expect(msg)` 取出值或 panic（仅开发/测试）。"
                    "`map`/`and_then`/`or_else` 组合子链式处理。`ok()` 转 Option，`ok_or()` 反向。"
                    "`thiserror` 库自动派生 Error，`anyhow` 库简化应用层错误处理。"
                ),
                "examples": [
                    "// ? 传播\nfn read_config() -> Result<String, io::Error> {\n    let mut file = File::open(\"config.toml\")?;\n    let mut s = String::new();\n    file.read_to_string(&mut s)?;\n    Ok(s)\n}\n// 组合子\nlet num: Result<i32, _> = \"42\".parse();\nlet doubled = num.map(|n| n * 2).unwrap_or(0);\n// thiserror\n#[derive(Error, Debug)]\nenum MyError {\n    #[error(\"IO: {0}\")]\n    Io(#[from] std::io::Error),\n}"
                ],
                "key_points": ["? 传播错误", "unwrap/expect 仅开发测试", "thiserror/anyhow 错误库"],
            },
        ],
    },
    {
        "topic": "Rust集合",
        "lessons": [
            {
                "id": "lesson_rust_Rust集合_1", "title": "Vec/String/HashMap",
                "topic": "Rust集合",
                "content": (
                    "`Vec<T>` 动态数组：`vec![]` 宏创建，`push/pop/extend` 修改，`&vec[..]` 切片引用。"
                    "`String` 是 `Vec<u8>` 的包装（UTF-8），`push_str`/`+` 拼接。`&str` 是字符串切片引用。"
                    "`HashMap<K,V>`：`insert(key, val)` 插入，`entry(key).or_insert(val)` 存在返回/不存在插入。"
                    "`VecDeque` 双端队列，`LinkedList` 链表，`BinaryHeap` 大顶堆。迭代器 `iter()/iter_mut()/into_iter()`。"
                ),
                "examples": [
                    "// Vec\nlet mut v = vec![1, 2, 3];\nv.push(4);\nv.extend([5, 6]);\n// HashMap\nlet mut scores = HashMap::new();\nscores.insert(\"Alice\", 100);\nlet bob_score = scores.entry(\"Bob\").or_insert(0);\n*bob_score += 10;\n// 迭代器\nlet doubled: Vec<_> = v.iter().map(|x| x * 2).collect();"
                ],
                "key_points": ["vec![] 宏创建 Vec", "String 是 UTF-8 Vec<u8>", "entry.or_insert 安全插入"],
            },
            {
                "id": "lesson_rust_Rust集合_2", "title": "迭代器与闭包",
                "topic": "Rust集合",
                "content": (
                    "迭代器：惰性求值，零成本抽象。`iter()` 不可变引用迭代，`iter_mut()` 可变引用，`into_iter()` 消耗集合。"
                    "闭包：`|params| { body }`，自动推断参数类型。`Fn`（不可变借用）/`FnMut`（可变借用）/`FnOnce`（消耗）。"
                    "`map`/`filter`/`fold`/`reduce`/`flat_map` 链式组合。`collect::<Vec<_>>()` 收集结果。"
                    "`take_while`/`skip_while`/`enumerate`/`zip` 工具方法。闭包捕获变量通过引用或 move 关键字转移所有权。"
                ),
                "examples": [
                    "// 闭包\nlet add = |a, b| a + b;\nassert_eq!(add(1, 2), 3);\n// 迭代器链\nlet result: i32 = (1..=10)\n    .filter(|x| x % 2 == 0)\n    .map(|x| x * 2)\n    .sum();  // 2*2 + 4*2 + ... = 60\n// move 闭包\nlet name = String::from(\"Rust\");\nstd::thread::spawn(move || println!(\"{name}\"));"
                ],
                "key_points": ["iter/iter_mut/into_iter", "Fn/FnMut/FnOnce 三种闭包", "map/filter/fold 零成本抽象"],
            },
        ],
    },
    {
        "topic": "Rust泛型与Trait",
        "lessons": [
            {
                "id": "lesson_rust_Rust泛型与Trait_1", "title": "泛型与 Trait 基础",
                "topic": "Rust泛型与Trait",
                "content": (
                    "泛型：`fn largest<T: PartialOrd>(list: &[T]) -> &T`。单态化：编译器为每种具体类型生成独立代码。"
                    "Trait 定义共享行为：`trait Summary { fn summarize(&self) -> String; }`。`impl Summary for Type` 实现。"
                    "孤儿规则：只能为当前 crate 中的类型实现当前 crate 中的 trait。"
                    "`impl Trait` 参数语法糖：`fn notify(item: &impl Summary)` = `fn notify<T: Summary>(item: &T)`。"
                ),
                "examples": [
                    "// trait 定义与实现\ntrait Greet {\n    fn greet(&self) -> String;\n}\nimpl Greet for String {\n    fn greet(&self) -> String { format!(\"Hello, {self}\") }\n}\n// 泛型约束\nfn say_hello<T: Greet>(target: &T) {\n    println!(\"{}\", target.greet());\n}\n// impl Trait 语法糖\nfn create_greeter() -> impl Greet {\n    String::from(\"Rust\")\n}"
                ],
                "key_points": ["泛型单态化零开销", "trait 定义共享行为", "孤儿规则防冲突"],
            },
            {
                "id": "lesson_rust_Rust泛型与Trait_2", "title": "Trait 进阶",
                "topic": "Rust泛型与Trait",
                "content": (
                    "关联类型：`trait Iterator { type Item; fn next(&mut self) -> Option<Self::Item>; }`。"
                    "默认实现：trait 方法可提供默认体，实现者可选重写。`Sized` trait：编译期已知大小。"
                    "`dyn Trait` 动态分发（vtable，有运行时开销），`impl Trait` / 泛型 `T: Trait` 静态分发（零开销）。"
                    "Supertrait：`trait OutlinePrint: fmt::Display {}` 要求实现者同时实现 Display。Blanket implementations：`impl<T: Display> ToString for T {}`。"
                ),
                "examples": [
                    "// 关联类型\ntrait Container {\n    type Item;\n    fn get(&self) -> Option<&Self::Item>;\n}\nimpl<T> Container for Vec<T> {\n    type Item = T;\n    fn get(&self) -> Option<&T> { self.first() }\n}\n// dyn Trait 动态分发\nfn draw_all(shapes: &[&dyn Draw]) {\n    for s in shapes { s.draw(); }\n}"
                ],
                "key_points": ["关联类型 type Item", "dyn Trait 动态 / impl Trait 静态", "Supertrait + Blanket impl"],
            },
        ],
    },
    {
        "topic": "Rust并发",
        "lessons": [
            {
                "id": "lesson_rust_Rust并发_1", "title": "线程与消息传递",
                "topic": "Rust并发",
                "content": (
                    "`std::thread::spawn` 创建线程，返回 `JoinHandle`，`.join()` 等待结束。`move` 闭包转移所有权给新线程。"
                    "`mpsc::channel()` 消息传递：`tx.send()` 发送，`rx.recv()` 阻塞接收，`rx.try_recv()` 不阻塞。"
                    "多个生产者：`let tx2 = tx.clone()`。`sync_channel(n)` 有限容量，满阻塞。"
                    "\"Do not communicate by sharing memory; share memory by communicating\" —— Go 并发哲学同样适用于 Rust。"
                ),
                "examples": [
                    "// 线程\nlet handle = std::thread::spawn(|| {\n    for i in 1..10 { println!(\"{i}\"); }\n});\nhandle.join().unwrap();\n// channel\nlet (tx, rx) = std::sync::mpsc::channel();\nstd::thread::spawn(move || {\n    tx.send(\"hello\").unwrap();\n});\nlet msg = rx.recv().unwrap();"
                ],
                "key_points": ["thread::spawn + move", "mpsc::channel 消息传递", "Do not communicate by sharing memory"],
            },
            {
                "id": "lesson_rust_Rust并发_2", "title": "Mutex/Arc/原子",
                "topic": "Rust并发",
                "content": (
                    "`Mutex<T>` 互斥访问：`.lock()` 返回 `MutexGuard`（RAII 自动解锁）。`Arc<T>` 原子引用计数（线程安全 Rc）。"
                    "`Arc<Mutex<T>>` 经典组合：多线程共享可变数据。注意死锁风险，避免嵌套 lock。"
                    "`RwLock<T>` 读写锁（读多写少优化），`Barrier` 同步屏障，`Condvar` 条件变量。"
                    "原子类型：`AtomicBool/I32/I64/Usize/Ptr`，`Ordering::SeqCst/Acquire/Release/Relaxed` 内存序。"
                ),
                "examples": [
                    "// Arc + Mutex\nlet counter = Arc::new(Mutex::new(0));\nlet mut handles = vec![];\nfor _ in 0..10 {\n    let counter = Arc::clone(&counter);\n    handles.push(std::thread::spawn(move || {\n        let mut num = counter.lock().unwrap();\n        *num += 1;\n    }));\n}\nfor h in handles { h.join().unwrap(); }\n// Atomic\nlet flag = Arc::new(AtomicBool::new(false));\nflag.store(true, Ordering::SeqCst);\nlet val = flag.load(Ordering::SeqCst);"
                ],
                "key_points": ["Arc<Mutex<T>> 共享可变", "lock() 返回 MutexGuard RAII", "Atomic 原子操作 + 内存序"],
            },
        ],
    },
    {
        "topic": "Rust宏",
        "lessons": [
            {
                "id": "lesson_rust_Rust宏_1", "title": "声明宏",
                "topic": "Rust宏",
                "content": (
                    "`macro_rules!` 创建声明宏（Declarative Macro），模式匹配语法：`($($x:expr),*)`。"
                    "重复模式：`$()*` 零次或多次，`$()+` 一次或多次，`$(),*` 带分隔符。"
                    "常用内置宏：`vec!`/`println!`/`format!`/`assert!`/`dbg!`/`todo!`/`unreachable!`。"
                    "`macro_export` 导出宏供其他 crate 使用。卫生性：宏内部变量默认不与外部冲突。"
                ),
                "examples": [
                    "// 声明宏\nmacro_rules! my_vec {\n    ( $( $x:expr ),* ) => {{\n        let mut v = Vec::new();\n        $( v.push($x); )*\n        v\n    }};\n}\nlet v = my_vec![1, 2, 3];\n// 错误类型模式\nmacro_rules! create {\n    ($typ:ty) => { $typ::default() };\n    ($expr:expr) => { $expr };\n}"
                ],
                "key_points": ["macro_rules! 模式匹配", "$()* 重复模式", "宏卫生性：变量不冲突"],
            },
            {
                "id": "lesson_rust_Rust宏_2", "title": "过程宏",
                "topic": "Rust宏",
                "content": (
                    "过程宏（Procedural Macro）：操作 TokenStream 的函数。三种：`#[derive]` 派生宏、`#[attribute]` 属性宏、函数式宏。"
                    "`syn` crate 解析 Tokens → AST，`quote` crate 生成 Tokens。`proc_macro` 标准库提供 TokenStream。"
                    "派生宏：`#[proc_macro_derive(MyTrait)]`，为 struct/enum 自动生成 trait 实现（如 serde 的 Serialize/Deserialize）。"
                    "属性宏：`#[proc_macro_attribute]`，类似装饰器。函数式宏：`my_macro!()` 自由形式。"
                ),
                "examples": [
                    "// 派生宏（proc-macro crate）\nuse proc_macro::TokenStream;\n#[proc_macro_derive(Hello)]\npub fn hello_derive(input: TokenStream) -> TokenStream {\n    let ast: DeriveInput = syn::parse(input).unwrap();\n    let name = &ast.ident;\n    let gen = quote! {\n        impl #name { fn hello() { println!(\"Hello from {}!\") } }\n    };\n    gen.into()\n}"
                ],
                "key_points": ["过程宏操作 TokenStream", "syn 解析 / quote 生成", "derive/attribute/函数式 三种"],
            },
        ],
    },
    {
        "topic": "Rust异步",
        "lessons": [
            {
                "id": "lesson_rust_Rust异步_1", "title": "async/await 与 Future",
                "topic": "Rust异步",
                "content": (
                    "`async fn` 返回 `Future`，惰性求值，需要 `.await` 或交给 executor 才执行。`tokio` 是最流行的异步运行时。"
                    "`#[tokio::main]` 宏启动异步运行时。`tokio::spawn` 并发执行多个 Future。"
                    "`Future` trait：`fn poll(self: Pin<&mut Self>, cx: &mut Context) -> Poll<Self::Output>`。状态机自动生成。"
                    "`async move` 闭包转移所有权进异步块。`join!` 等待全部，`select!` 竞速。"
                ),
                "examples": [
                    "// tokio 异步\n#[tokio::main]\nasync fn main() {\n    let (res1, res2) = tokio::join!(\n        fetch_data(1),\n        fetch_data(2),\n    );\n    println!(\"{:?} {:?}\", res1, res2);\n}\nasync fn fetch_data(id: u32) -> String {\n    tokio::time::sleep(Duration::from_secs(1)).await;\n    format!(\"data-{id}\")\n}"
                ],
                "key_points": ["async fn 返回 Future 惰性", "tokio::spawn/join!/select!", "Future poll + 自动状态机"],
            },
            {
                "id": "lesson_rust_Rust异步_2", "title": "异步 I/O 与生态",
                "topic": "Rust异步",
                "content": (
                    "`tokio::net::TcpListener` 异步网络，`tokio::fs` 异步文件（内部用线程池）。"
                    "`tokio::sync::Mutex` 异步互斥锁（非阻塞，不同于 std::Mutex）。`tokio::sync::mpsc` 异步 channel。"
                    "`Stream` trait（类似 Future 但多值），`tokio_stream` crate 提供适配器。`futures` crate 提供组合子。"
                    "axum/hyper（web）、tonic（gRPC）、reqwest（HTTP 客户端）是主流异步库。"
                ),
                "examples": [
                    "// tokio TCP echo server\n#[tokio::main]\nasync fn main() {\n    let listener = tokio::net::TcpListener::bind(\"127.0.0.1:8080\").await.unwrap();\n    loop {\n        let (mut socket, _) = listener.accept().await.unwrap();\n        tokio::spawn(async move {\n            let (mut reader, mut writer) = socket.split();\n            tokio::io::copy(&mut reader, &mut writer).await.unwrap();\n        });\n    }\n}"
                ],
                "key_points": ["tokio::net/fs 异步 I/O", "Stream 多值 Future", "axum/tonic/reqwest 生态"],
            },
        ],
    },
    {
        "topic": "Rust工程化",
        "lessons": [
            {
                "id": "lesson_rust_Rust工程化_1", "title": "Cargo 与包管理",
                "topic": "Rust工程化",
                "content": (
                    "`cargo new/init` 创建项目，`cargo build/run/test` 编译运行测试。`--release` 优化编译。"
                    "Cargo.toml：[dependencies] 声明依赖，`^` 语义化版本，`features` 可选功能。`[workspace]` 多 crate 工作区。"
                    "`cargo doc --open` 生成文档，`cargo fmt` 格式化，`cargo clippy` lint 检查，`cargo audit` 安全审计。"
                    "`criterion` 基准测试框架，`cargo-flamegraph` 火焰图。`cargo install` 安装二进制 crate。"
                ),
                "examples": [
                    "# Cargo.toml\n[package]\nname = \"my-app\"\nversion = \"0.1.0\"\nedition = \"2021\"\n\n[dependencies]\ntokio = { version = \"1\", features = [\"full\"] }\nserde = { version = \"1\", features = [\"derive\"] }\n\n[profile.release]\nlto = true  # Link Time Optimization\ncodegen-units = 1"
                ],
                "key_points": ["cargo build/run/test/doc", "Cargo.toml 依赖 + features", "clippy/fmt/audit 质量工具"],
            },
            {
                "id": "lesson_rust_Rust工程化_2", "title": "测试与 CI",
                "topic": "Rust工程化",
                "content": (
                    "单元测试：`#[cfg(test)]`  模块 + `#[test]` 函数。集成测试：`tests/` 目录。`cargo test` 运行。"
                    "文档测试：`///` 中的代码块 `assert_eq!` 自动编译运行（`cargo test` 执行）。"
                    "`#[should_panic]` 测试 panic，`#[ignore]` 跳过。`cargo test -- --nocapture` 显示输出。"
                    "CI 常见配置：GitHub Actions 矩阵测试多 OS/版本，`cargo tarpaulin` 代码覆盖率，`cargo deny` 许可证检查。"
                ),
                "examples": [
                    "// 单元测试\n#[cfg(test)]\nmod tests {\n    use super::*;\n    #[test]\n    fn test_add() { assert_eq!(add(1, 2), 3); }\n    #[test]\n    #[should_panic]\n    fn test_panic() { divide(1, 0); }\n}\n// 文档测试\n/// 求和\n/// assert_eq!(my_crate::add(1, 2), 3);\npub fn add(a: i32, b: i32) -> i32 { a + b }"
                ],
                "key_points": ["#[test] + #[cfg(test)]", "文档测试自动运行", "tarpaulin 覆盖率"],
            },
        ],
    },
    {
        "topic": "Rust安全",
        "lessons": [
            {
                "id": "lesson_rust_Rust安全_1", "title": "unsafe Rust",
                "topic": "Rust安全",
                "content": (
                    "`unsafe` 不是关闭借用检查，而是解锁五个超能力：解引用裸指针、调用 unsafe 函数、访问可变静态变量、实现 unsafe trait、访问 union 字段。"
                    "裸指针 `*const T` / `*mut T` 不遵守借用规则，无自动释放。`NonNull<T>` 非空指针包装。"
                    "`unsafe` 代码应尽量少而隔离，用安全抽象包装。`unsafe { ... }` 块标注责任边界。"
                    "FFI（外部函数接口）：`extern \"C\" fn` 声明 C ABI，`#[no_mangle]` 禁止名称改写。"
                ),
                "examples": [
                    "// unsafe 块\nlet mut num = 5;\nlet r1 = &num as *const i32;\nlet r2 = &mut num as *mut i32;\nunsafe {\n    println!(\"r1: {}\", *r1);\n    *r2 = 10;\n}\n// FFI\nextern \"C\" {\n    fn abs(input: i32) -> i32;\n}\nunsafe { println!(\"{}\", abs(-3)); }"
                ],
                "key_points": ["unsafe 五大超能力", "裸指针无借用/自动释放", "抽象隔离 unsafe"],
            },
            {
                "id": "lesson_rust_Rust安全_2", "title": "Send + Sync",
                "topic": "Rust安全",
                "content": (
                    "`Send`：类型可在线程间转移所有权。大多数类型是 Send，`Rc` 不是。"
                    "`Sync`：类型可在线程间共享引用。`RefCell` 不是 Sync，`Mutex` 是。"
                    "`Send` 和 `Sync` 是自动推导的不安全 trait（auto trait），编译器默认实现。手工 `unsafe impl` 需保证正确。"
                    "`PhantomData` 虚类型标记：告诉编译器类型参数的所有权/生命周期关系，不占空间。"
                ),
                "examples": [
                    "// Send/Sync 是 auto trait\nuse std::marker::Send;\nfn assert_send<T: Send>(_: T) {}\nassert_send(String::from(\"hello\"));  // String 是 Send\n// assert_send(std::rc::Rc::new(1)); // Error: Rc 不是 Send\n// PhantomData\nstruct MyStruct<T> {\n    _marker: std::marker::PhantomData<T>,\n}\n// 编译器推断 MyStruct<T> 的 Send/Sync 取决于 T"
                ],
                "key_points": ["Send: 跨线程转移 / Sync: 跨线程共享", "auto trait 自动推导", "PhantomData 虚类型标记"],
            },
        ],
    },
    {
        "topic": "Rust设计模式",
        "lessons": [
            {
                "id": "lesson_rust_Rust设计模式_1", "title": "创建型模式的 Rust 实现",
                "topic": "Rust设计模式",
                "content": (
                    "Builder 模式：`struct ConfigBuilder { ... } impl ConfigBuilder { fn build(self) -> Config }`，链式调用。"
                    "Newtype 模式：`struct Meter(f64)` 给类型附加语义，避免混淆。`Deref` trait 实现透明解引用。"
                    "`Default` + Struct Update Syntax：`let c = Config { name: \"test\".into(), ..Config::default() }`。"
                    "`Lazy`/`OnceCell`（标准库，rust 1.80+）懒初始化：`static CONFIG: LazyLock<String> = LazyLock::new(|| load_config())`。"
                ),
                "examples": [
                    "// Builder\nstruct ServerBuilder {\n    host: String,\n    port: u16,\n}\nimpl ServerBuilder {\n    fn new() -> Self { Self { host: \"0.0.0.0\".into(), port: 8080 } }\n    fn host(mut self, h: &str) -> Self { self.host = h.into(); self }\n    fn port(mut self, p: u16) -> Self { self.port = p; self }\n    fn build(self) -> Server { Server { host: self.host, port: self.port } }\n}"
                ],
                "key_points": ["Builder 链式 + build()", "Newtype 语义包装", "LazyLock 懒初始化"],
            },
            {
                "id": "lesson_rust_Rust设计模式_2", "title": "行为模式的 Rust 实现",
                "topic": "Rust设计模式",
                "content": (
                    "策略模式：用 `Box<dyn Strategy>` 或泛型 `T: Strategy` 注入算法，泛型版零开销。"
                    "观察者：trait + Vec<Box<dyn Observer>>，或 channel 解耦。"
                    "状态模式：enum 表示状态，`match` 处理转换。也可用 typestate 在编译期锁住非法操作。"
                    "RAII 守卫：`MutexGuard`/`File` 等基于 Drop 自动释放资源，是 Rust 最自然的设计模式。"
                ),
                "examples": [
                    "// 策略模式（泛型）\ntrait Compressor { fn compress(&self, data: &[u8]) -> Vec<u8>; }\nstruct Processor<C: Compressor> {\n    compressor: C,\n}\nimpl<C: Compressor> Processor<C> {\n    fn process(&self, data: &[u8]) -> Vec<u8> { self.compressor.compress(data) }\n}\n// 状态模式（enum）\nenum ConnectionState {\n    Connected(TcpStream),\n    Disconnected,\n}\n// RAII 守卫\n// MutexGuard 离开作用域自动解锁"
                ],
                "key_points": ["策略: 泛型零开销注入", "状态: enum + match", "RAII 守卫 = Rust 最自然模式"],
            },
        ],
    },
    {
        "topic": "生命周期",
        "lessons": [
            {
                "id": "lesson_rust_生命周期_1", "title": "生命周期",
                "topic": "生命周期",
                "content": (
                    "\"生命周期标注确保引用有效性：&a T 声明引用存活范围。fn longest<a>(x: &a str, y: &a str) -> &a str。\""
                    "\"生命周期省略规则(Elision)：编译器自动推断多数情况。3条规则：每个引用参数有独立生命周期；单引用输入则输出同；&self则输出同self。\""
                    "\"静态生命周期astatic：程序整个期间有效。字符串字面量是 &static str。慎用static防止内存泄漏。\""
                ),
                "examples": [
                "fn longest<a>(x: &a str, y: &a str) -> &a str {\n    if x.len() > y.len() { x } else { y }\n}\n\n# struct 生命周期\nstruct Excerpt<a> {\n    part: &a str,\n}\n\n# static\nlet s: &static str = \"I live forever\";"
                ],
                "key_points": ["生命周期标注 &a 确保引用有效", "省略规则：编译器自动推断", "static 全程有效，慎用防泄漏"],
            },
            {
                "id": "lesson_rust_生命周期_2", "title": "生命周期",
                "topic": "生命周期",
                "content": (
                    "\"生命周期标注确保引用有效性：&a T 声明引用存活范围。fn longest<a>(x: &a str, y: &a str) -> &a str。\""
                    "\"生命周期省略规则(Elision)：编译器自动推断多数情况。3条规则：每个引用参数有独立生命周期；单引用输入则输出同；&self则输出同self。\""
                    "\"静态生命周期astatic：程序整个期间有效。字符串字面量是 &static str。慎用static防止内存泄漏。\""
                ),
                "examples": [
                "fn longest<a>(x: &a str, y: &a str) -> &a str {\n    if x.len() > y.len() { x } else { y }\n}\n\n# struct 生命周期\nstruct Excerpt<a> {\n    part: &a str,\n}\n\n# static\nlet s: &static str = \"I live forever\";"
                ],
                "key_points": ["生命周期标注 &a 确保引用有效", "省略规则：编译器自动推断", "static 全程有效，慎用防泄漏"],
            },
        ],
    },
    {
        "topic": "Trait进阶",
        "lessons": [
            {
                "id": "lesson_rust_Trait进阶_1", "title": "Trait进阶",
                "topic": "Trait进阶",
                "content": (
                    "\"trait定义共享行为。fn summarize(&self) -> String。impl Trait for Type实现。孤儿规则限制外部trait实现。\""
                    "\"关联类型：type Item; 在trait中定义，实现时指定。Iterator trait的Item。默认方法带默认实现。\""
                    "\"Trait Bound约束泛型：fn notify<T: Summary>(item: &T)。+合并：T: Summary + Display。where子句复杂约束。\""
                ),
                "examples": [
                "trait Summary {\n    type Item;\n    fn summarize(&self) -> String { String::from(\"(Read more...)\") }\n}\n\nstruct Article { headline: String }\nimpl Summary for Article {\n    type Item = String;\n    fn summarize(&self) -> String { self.headline.clone() }\n}\n\nfn notify<T: Summary>(item: &T) { println!(\"{}\", item.summarize()); }\nfn complex<T, U>(t: &T, u: &U) where T: Summary + Display, U: Clone {}"
                ],
                "key_points": ["trait定义共享行为 + impl实现", "关联类型 type Item 简化泛型", "Trait Bound + where 复杂约束"],
            },
            {
                "id": "lesson_rust_Trait进阶_2", "title": "Trait进阶",
                "topic": "Trait进阶",
                "content": (
                    "\"trait定义共享行为。fn summarize(&self) -> String。impl Trait for Type实现。孤儿规则限制外部trait实现。\""
                    "\"关联类型：type Item; 在trait中定义，实现时指定。Iterator trait的Item。默认方法带默认实现。\""
                    "\"Trait Bound约束泛型：fn notify<T: Summary>(item: &T)。+合并：T: Summary + Display。where子句复杂约束。\""
                ),
                "examples": [
                "trait Summary {\n    type Item;\n    fn summarize(&self) -> String { String::from(\"(Read more...)\") }\n}\n\nstruct Article { headline: String }\nimpl Summary for Article {\n    type Item = String;\n    fn summarize(&self) -> String { self.headline.clone() }\n}\n\nfn notify<T: Summary>(item: &T) { println!(\"{}\", item.summarize()); }\nfn complex<T, U>(t: &T, u: &U) where T: Summary + Display, U: Clone {}"
                ],
                "key_points": ["trait定义共享行为 + impl实现", "关联类型 type Item 简化泛型", "Trait Bound + where 复杂约束"],
            },
        ],
    },
    {
        "topic": "错误处理",
        "lessons": [
            {
                "id": "lesson_rust_错误处理_1", "title": "错误处理",
                "topic": "错误处理",
                "content": (
                    "\"Result<T, E>枚举：Ok(T)成功，Err(E)失败。?操作符传播错误：let x = func()?；Err时提前返回。\""
                    "\"自定义错误：derive(Debug) + impl Display + impl Error。thiserror库简化样板代码。\""
                    "\"panic!宏用于不可恢复错误。unwrap()/expect()在Err时panic。Option<T>用?传播None。\""
                ),
                "examples": [
                "use std::fs::File;\nuse std::io::{self, Read};\n\nfn read_file(path: &str) -> Result<String, io::Error> {\n    let mut file = File::open(path)?;\n    let mut contents = String::new();\n    file.read_to_string(&mut contents)?;\n    Ok(contents)\n}\n\n# thiserror 自定义错误\n#[derive(Error, Debug)]\nenum MyError {\n    #[error(\"IO error: {0}\")] Io(#[from] io::Error),\n    #[error(\"Parse error\")] Parse,\n}"
                ],
                "key_points": ["Result<T,E> + ? 操作符传播错误", "自定义错误: Debug+Display+Error", "panic!不可恢复，unwrap在Err时panic"],
            },
            {
                "id": "lesson_rust_错误处理_2", "title": "错误处理",
                "topic": "错误处理",
                "content": (
                    "\"Result<T, E>枚举：Ok(T)成功，Err(E)失败。?操作符传播错误：let x = func()?；Err时提前返回。\""
                    "\"自定义错误：derive(Debug) + impl Display + impl Error。thiserror库简化样板代码。\""
                    "\"panic!宏用于不可恢复错误。unwrap()/expect()在Err时panic。Option<T>用?传播None。\""
                ),
                "examples": [
                "use std::fs::File;\nuse std::io::{self, Read};\n\nfn read_file(path: &str) -> Result<String, io::Error> {\n    let mut file = File::open(path)?;\n    let mut contents = String::new();\n    file.read_to_string(&mut contents)?;\n    Ok(contents)\n}\n\n# thiserror 自定义错误\n#[derive(Error, Debug)]\nenum MyError {\n    #[error(\"IO error: {0}\")] Io(#[from] io::Error),\n    #[error(\"Parse error\")] Parse,\n}"
                ],
                "key_points": ["Result<T,E> + ? 操作符传播错误", "自定义错误: Debug+Display+Error", "panic!不可恢复，unwrap在Err时panic"],
            },
        ],
    },
    {
        "topic": "智能指针",
        "lessons": [
            {
                "id": "lesson_rust_智能指针_1", "title": "智能指针",
                "topic": "智能指针",
                "content": (
                    "\"Box<T>堆分配，用于递归类型、大型数据、trait对象。Box::new(value)分配。*解引用。\""
                    "\"Rc<T>引用计数共享所有权(单线程)。Rc::clone增加计数。多线程版本Arc<T>原子引用计数。\""
                    "\"RefCell<T>内部可变性：运行时借用检查替代编译期。borrow()/borrow_mut()。Rc<RefCell<T>>组合。\""
                ),
                "examples": [
                "# Box\nlet b = Box::new(5);\nprintln!(\"{}\", *b); # 解引用\n\n# Rc\nuse std::rc::Rc;\nlet a = Rc::new(vec![1, 2, 3]);\nlet b = Rc::clone(&a);\nprintln!(\"count: {}\", Rc::strong_count(&a));\n\n# RefCell\nuse std::cell::RefCell;\nlet data = RefCell::new(42);\n*data.borrow_mut() = 100;\nprintln!(\"{}\", data.borrow());"
                ],
                "key_points": ["Box堆分配+递归类型", "Rc单线程/Arc多线程引用计数", "RefCell运行时借用检查"],
            },
            {
                "id": "lesson_rust_智能指针_2", "title": "智能指针",
                "topic": "智能指针",
                "content": (
                    "\"Box<T>堆分配，用于递归类型、大型数据、trait对象。Box::new(value)分配。*解引用。\""
                    "\"Rc<T>引用计数共享所有权(单线程)。Rc::clone增加计数。多线程版本Arc<T>原子引用计数。\""
                    "\"RefCell<T>内部可变性：运行时借用检查替代编译期。borrow()/borrow_mut()。Rc<RefCell<T>>组合。\""
                ),
                "examples": [
                "# Box\nlet b = Box::new(5);\nprintln!(\"{}\", *b); # 解引用\n\n# Rc\nuse std::rc::Rc;\nlet a = Rc::new(vec![1, 2, 3]);\nlet b = Rc::clone(&a);\nprintln!(\"count: {}\", Rc::strong_count(&a));\n\n# RefCell\nuse std::cell::RefCell;\nlet data = RefCell::new(42);\n*data.borrow_mut() = 100;\nprintln!(\"{}\", data.borrow());"
                ],
                "key_points": ["Box堆分配+递归类型", "Rc单线程/Arc多线程引用计数", "RefCell运行时借用检查"],
            },
        ],
    },
    {
        "topic": "闭包与迭代器",
        "lessons": [
            {
                "id": "lesson_rust_闭包与迭代器_1", "title": "闭包与迭代器",
                "topic": "闭包与迭代器",
                "content": (
                    "\"闭包：|params| { body }。类型推断自动。三种trait：Fn(不可变借用)、FnMut(可变借用)、FnOnce(获取所有权)。\""
                    "\"迭代器：Iterator trait。iter()不可变借用、iter_mut()可变、into_iter()消耗。map/filter/fold链式。\""
                    "\"闭包捕获环境：move关键字强制获取所有权。适合多线程场景(thread::spawn)。\""
                ),
                "examples": [
                "let nums = vec![1, 2, 3, 4, 5];\n\n# map + filter + collect\nlet evens: Vec<i32> = nums.iter()\n    .filter(|&&x| x % 2 == 0)\n    .map(|&x| x * x)\n    .collect();\n\n# 闭包\nlet add = |a, b| a + b;\nprintln!(\"{}\", add(1, 2));\n\n# move 闭包\nlet name = String::from(\"Rust\");\nstd::thread::spawn(move || { println!(\"{}\", name); });"
                ],
                "key_points": ["闭包三种trait: Fn/FnMut/FnOnce", "Iterator链式: map/filter/fold/collect", "move闭包获取所有权"],
            },
            {
                "id": "lesson_rust_闭包与迭代器_2", "title": "闭包与迭代器",
                "topic": "闭包与迭代器",
                "content": (
                    "\"闭包：|params| { body }。类型推断自动。三种trait：Fn(不可变借用)、FnMut(可变借用)、FnOnce(获取所有权)。\""
                    "\"迭代器：Iterator trait。iter()不可变借用、iter_mut()可变、into_iter()消耗。map/filter/fold链式。\""
                    "\"闭包捕获环境：move关键字强制获取所有权。适合多线程场景(thread::spawn)。\""
                ),
                "examples": [
                "let nums = vec![1, 2, 3, 4, 5];\n\n# map + filter + collect\nlet evens: Vec<i32> = nums.iter()\n    .filter(|&&x| x % 2 == 0)\n    .map(|&x| x * x)\n    .collect();\n\n# 闭包\nlet add = |a, b| a + b;\nprintln!(\"{}\", add(1, 2));\n\n# move 闭包\nlet name = String::from(\"Rust\");\nstd::thread::spawn(move || { println!(\"{}\", name); });"
                ],
                "key_points": ["闭包三种trait: Fn/FnMut/FnOnce", "Iterator链式: map/filter/fold/collect", "move闭包获取所有权"],
            },
        ],
    },
    {
        "topic": "模块系统",
        "lessons": [
            {
                "id": "lesson_rust_模块系统_1", "title": "模块系统",
                "topic": "模块系统",
                "content": (
                    "\"mod定义模块。pub关键字控制可见性。use引入路径。super::访问父模块。crate::访问根。\""
                    "\"文件模块：mod foo; 加载foo.rs或foo/mod.rs。pub use重导出(re-export)简化API。\""
                    "\"Cargo.toml定义包。lib.rs库根，main.rs二进制根。workspace管理多crate项目。\""
                ),
                "examples": [
                "# 模块结构\nmod front_of_house {\n    pub mod hosting {\n        pub fn add_to_waitlist() {}\n    }\n}\nuse front_of_house::hosting;\nhosting::add_to_waitlist();\n\n# pub use 重导出\npub use crate::front_of_house::hosting;\n\n# Cargo.toml\n[package]\nname = \"my-app\"\n[dependencies]\nserde = \"1\""
                ],
                "key_points": ["mod+pub控制可见性", "use+super::+crate::路径", "Cargo workspace管理多crate"],
            },
            {
                "id": "lesson_rust_模块系统_2", "title": "模块系统",
                "topic": "模块系统",
                "content": (
                    "\"mod定义模块。pub关键字控制可见性。use引入路径。super::访问父模块。crate::访问根。\""
                    "\"文件模块：mod foo; 加载foo.rs或foo/mod.rs。pub use重导出(re-export)简化API。\""
                    "\"Cargo.toml定义包。lib.rs库根，main.rs二进制根。workspace管理多crate项目。\""
                ),
                "examples": [
                "# 模块结构\nmod front_of_house {\n    pub mod hosting {\n        pub fn add_to_waitlist() {}\n    }\n}\nuse front_of_house::hosting;\nhosting::add_to_waitlist();\n\n# pub use 重导出\npub use crate::front_of_house::hosting;\n\n# Cargo.toml\n[package]\nname = \"my-app\"\n[dependencies]\nserde = \"1\""
                ],
                "key_points": ["mod+pub控制可见性", "use+super::+crate::路径", "Cargo workspace管理多crate"],
            },
        ],
    },
    {
        "topic": "Unsafe与FFI",
        "lessons": [
            {
                "id": "lesson_rust_Unsafe与FFI_1", "title": "Unsafe与FFI",
                "topic": "Unsafe与FFI",
                "content": (
                    "\"unsafe块允许5种操作：解引用裸指针、调用unsafe函数、访问可变静态变量、实现unsafe trait、访问union字段。\""
                    "\"裸指针：*const T / *mut T。可在unsafe外创建，仅unsafe内解引用。无自动解引用/生命周期/别名规则。\""
                    "\"FFI外部函数接口：extern \"C\" { fn func(); } 调用C库。#[no_mangle] pub extern \"C\" fn供C调用。\""
                ),
                "examples": [
                "# 裸指针\nlet mut num = 5;\nlet r1 = &num as *const i32;\nlet r2 = &mut num as *mut i32;\nunsafe { println!(\"r1: {}\", *r1); *r2 = 10; }\n\n# FFI 调用C\nunsafe {\n    extern \"C\" { fn abs(input: i32) -> i32; }\n    println!(\"{}\", abs(-3));\n}\n\n# 供C调用\n#[no_mangle]\npub extern \"C\" fn rust_function() { println!(\"Called from C\"); }"
                ],
                "key_points": ["unsafe 5种超级权限", "*const T/*mut T裸指针", "FFI: extern C 互操作"],
            },
            {
                "id": "lesson_rust_Unsafe与FFI_2", "title": "Unsafe与FFI",
                "topic": "Unsafe与FFI",
                "content": (
                    "\"unsafe块允许5种操作：解引用裸指针、调用unsafe函数、访问可变静态变量、实现unsafe trait、访问union字段。\""
                    "\"裸指针：*const T / *mut T。可在unsafe外创建，仅unsafe内解引用。无自动解引用/生命周期/别名规则。\""
                    "\"FFI外部函数接口：extern \"C\" { fn func(); } 调用C库。#[no_mangle] pub extern \"C\" fn供C调用。\""
                ),
                "examples": [
                "# 裸指针\nlet mut num = 5;\nlet r1 = &num as *const i32;\nlet r2 = &mut num as *mut i32;\nunsafe { println!(\"r1: {}\", *r1); *r2 = 10; }\n\n# FFI 调用C\nunsafe {\n    extern \"C\" { fn abs(input: i32) -> i32; }\n    println!(\"{}\", abs(-3));\n}\n\n# 供C调用\n#[no_mangle]\npub extern \"C\" fn rust_function() { println!(\"Called from C\"); }"
                ],
                "key_points": ["unsafe 5种超级权限", "*const T/*mut T裸指针", "FFI: extern C 互操作"],
            },
        ],
    },
    {
        "topic": "异步编程",
        "lessons": [
            {
                "id": "lesson_rust_异步编程_1", "title": "异步编程",
                "topic": "异步编程",
                "content": (
                    "\"async fn返回Future。.await等待而不阻塞线程。tokio运行时：#[tokio::main] + tokio::spawn。\""
                    "\"async move闭包。join!并发执行多个Future。select!竞速多个Future取先完成者。\""
                    "\"Stream流式异步迭代器(Futures crate)。tokio::sync::mpsc异步Channel。Mutex异步锁tokio::sync::Mutex。\""
                ),
                "examples": [
                "use tokio;\n\n#[tokio::main]\nasync fn main() {\n    let result = async_task().await;\n    println!(\"{}\", result);\n\n    # join! 并发\n    let (r1, r2) = tokio::join!(task1(), task2());\n\n    # select!\n    tokio::select! {\n        _ = task1() => println!(\"task1 done\"),\n        _ = tokio::time::sleep(Duration::from_secs(2)) => println!(\"timeout\"),\n    }\n}\n\nasync fn async_task() -> String { \"done\".into() }\nasync fn task1() {}\nasync fn task2() {}"
                ],
                "key_points": ["async/await + tokio运行时", "join!并发，select!竞速", "tokio::sync异步同步原语"],
            },
            {
                "id": "lesson_rust_异步编程_2", "title": "异步编程",
                "topic": "异步编程",
                "content": (
                    "\"async fn返回Future。.await等待而不阻塞线程。tokio运行时：#[tokio::main] + tokio::spawn。\""
                    "\"async move闭包。join!并发执行多个Future。select!竞速多个Future取先完成者。\""
                    "\"Stream流式异步迭代器(Futures crate)。tokio::sync::mpsc异步Channel。Mutex异步锁tokio::sync::Mutex。\""
                ),
                "examples": [
                "use tokio;\n\n#[tokio::main]\nasync fn main() {\n    let result = async_task().await;\n    println!(\"{}\", result);\n\n    # join! 并发\n    let (r1, r2) = tokio::join!(task1(), task2());\n\n    # select!\n    tokio::select! {\n        _ = task1() => println!(\"task1 done\"),\n        _ = tokio::time::sleep(Duration::from_secs(2)) => println!(\"timeout\"),\n    }\n}\n\nasync fn async_task() -> String { \"done\".into() }\nasync fn task1() {}\nasync fn task2() {}"
                ],
                "key_points": ["async/await + tokio运行时", "join!并发，select!竞速", "tokio::sync异步同步原语"],
            },
        ],
    }
]

# ================================================================
# SQL 课程（10 个主题，每主题 2 节课）
# ================================================================
SQL_LEARNING_PATH = [
    {
        "topic": "SQL查询",
        "lessons": [
            {
                "id": "lesson_sql_SQL查询_1", "title": "SELECT 基础",
                "topic": "SQL查询",
                "content": (
                    "标准查询结构：`SELECT [DISTINCT] 列 FROM 表 WHERE 条件 GROUP BY 分组 HAVING 过滤 ORDER BY 排序 LIMIT 限制`。"
                    "执行顺序（逻辑）：FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT。"
                    "WHERE 过滤原始行，HAVING 过滤分组后聚合结果。DISTINCT 去重。"
                    "聚合函数：COUNT/SUM/AVG/MIN/MAX，GROUP BY 按列分组，多列组合分组。"
                ),
                "examples": [
                    "-- 基本查询\nSELECT name, age FROM users WHERE age >= 18 ORDER BY age DESC LIMIT 10;\n-- 聚合 + 分组\nSELECT department, COUNT(*) AS cnt, AVG(salary) AS avg_sal\nFROM employees\nWHERE status = 'active'\nGROUP BY department\nHAVING COUNT(*) > 5\nORDER BY avg_sal DESC;"
                ],
                "key_points": ["SELECT-FROM-WHERE-GROUP-HAVING-ORDER-LIMIT", "逻辑执行顺序", "HAVING 过滤聚合结果"],
            },
            {
                "id": "lesson_sql_SQL查询_2", "title": "JOIN 连接",
                "topic": "SQL查询",
                "content": (
                    "INNER JOIN：返回两表匹配的行。LEFT JOIN：保留左表所有行，右表无匹配填充 NULL。RIGHT JOIN：保留右表。FULL OUTER JOIN：两边都保留。"
                    "CROSS JOIN：笛卡尔积（很少用，除非需要所有组合）。SELF JOIN：表自连接（如员工-经理查询）。"
                    "ON 指定连接条件。USING(column) 简化同名列。NATURAL JOIN 自动匹配同名列（不推荐）。"
                    "多表 JOIN 用链式：`FROM a JOIN b ON ... JOIN c ON ...`。子查询也可替代部分 JOIN。"
                ),
                "examples": [
                    "-- INNER JOIN\nSELECT u.name, o.order_date\nFROM users u\nJOIN orders o ON u.id = o.user_id;\n-- LEFT JOIN\nSELECT u.name, o.order_date\nFROM users u\nLEFT JOIN orders o ON u.id = o.user_id;  -- 保留无订单的用户\n-- SELF JOIN（员工-经理）\nSELECT e.name AS employee, m.name AS manager\nFROM employees e\nLEFT JOIN employees m ON e.manager_id = m.id;"
                ],
                "key_points": ["INNER/LEFT/RIGHT/FULL JOIN", "LEFT JOIN 保留左表所有行", "SELF JOIN 自连接"],
            },
        ],
    },
    {
        "topic": "SQL子查询",
        "lessons": [
            {
                "id": "lesson_sql_SQL子查询_1", "title": "标量与关联子查询",
                "topic": "SQL子查询",
                "content": (
                    "标量子查询：返回单值，可用在 SELECT、WHERE、HAVING 中。`WHERE salary > (SELECT AVG(salary) FROM employees)`。"
                    "关联子查询：内层引用外层列，每行执行一次内查询。性能较差，尽量用 JOIN 替代。"
                    "EXISTS / NOT EXISTS：检查子查询是否有结果，比 IN 利用索引更好。"
                    "IN / NOT IN：检查值是否在子查询结果中。注意 NULL：`NOT IN (subquery with NULL)` 永远返回 false。"
                ),
                "examples": [
                    "-- 标量子查询\nSELECT name, salary\nFROM employees\nWHERE salary > (SELECT AVG(salary) FROM employees);\n-- EXISTS（比 IN 更优）\nSELECT * FROM users u\nWHERE EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id);\n-- NOT IN + NULL 陷阱\n-- 如果 subquery 包含 NULL, NOT IN 永远为空\n-- 用 NOT EXISTS 代替"
                ],
                "key_points": ["标量子查询返回单值", "EXISTS 优于 IN（索引）", "NOT IN + NULL = 空（用 NOT EXISTS）"],
            },
            {
                "id": "lesson_sql_SQL子查询_2", "title": "CTE 与递归查询",
                "topic": "SQL子查询",
                "content": (
                    "CTE（Common Table Expression）：`WITH cte AS (query) SELECT * FROM cte`。提高可读性，可多次引用。"
                    "递归 CTE：`WITH RECURSIVE cte AS (base UNION ALL recursive) SELECT * FROM cte`。适合树/图遍历。"
                    "窗口函数与 CTE 组合：先 CTE 预处理，再窗口函数分析，适合复杂报表。"
                    "CTE 与临时表的区别：CTE 查询中临时存在（优化器可内联），临时表显式创建（持久到会话结束）。"
                ),
                "examples": [
                    "-- CTE\nWITH user_orders AS (\n    SELECT user_id, COUNT(*) AS cnt\n    FROM orders GROUP BY user_id\n)\nSELECT u.name, COALESCE(uo.cnt, 0) AS order_count\nFROM users u LEFT JOIN user_orders uo ON u.id = uo.user_id;\n-- 递归 CTE（组织架构）\nWITH RECURSIVE org_tree AS (\n    SELECT id, name, manager_id, 1 AS level FROM employees WHERE manager_id IS NULL\n    UNION ALL\n    SELECT e.id, e.name, e.manager_id, ot.level + 1\n    FROM employees e JOIN org_tree ot ON e.manager_id = ot.id\n)\nSELECT * FROM org_tree ORDER BY level;"
                ],
                "key_points": ["CTE: WITH ... SELECT", "递归 CTE 树遍历", "CTE + 窗口函数 复杂报表"],
            },
        ],
    },
    {
        "topic": "SQL窗口",
        "lessons": [
            {
                "id": "lesson_sql_SQL窗口_1", "title": "窗口函数基础",
                "topic": "SQL窗口",
                "content": (
                    "窗口函数：`FUNC() OVER (PARTITION BY col ORDER BY col)`，在结果集上滑动计算，不改变行数。"
                    "`ROW_NUMBER()` 连续编号，`RANK()` 跳号排名（并列占位），`DENSE_RANK()` 不跳号。"
                    "`LEAD(col, n)` 向后取值，`LAG(col, n)` 向前取值。`FIRST_VALUE/LAST_VALUE/NTH_VALUE` 窗口首尾值。"
                    "PARTITION BY 分区，ORDER BY 排序，ROWS/RANGE frame 定义窗口范围（`ROWS BETWEEN 2 PRECEDING AND CURRENT ROW`）。"
                ),
                "examples": [
                    "-- 排名\nSELECT name, score,\n    ROW_NUMBER() OVER (ORDER BY score DESC) AS rn,\n    RANK() OVER (ORDER BY score DESC) AS rk,\n    DENSE_RANK() OVER (ORDER BY score DESC) AS dr\nFROM students;\n-- 同比/环比\nSELECT date, revenue,\n    LAG(revenue, 1) OVER (ORDER BY date) AS prev_day,\n    LEAD(revenue, 1) OVER (ORDER BY date) AS next_day\nFROM daily_sales;"
                ],
                "key_points": ["ROW_NUMBER/RANK/DENSE_RANK", "LEAD/LAG 前后取值", "PARTITION BY + ORDER BY 窗口"],
            },
            {
                "id": "lesson_sql_SQL窗口_2", "title": "窗口聚合与分析",
                "topic": "SQL窗口",
                "content": (
                    "窗口聚合：`SUM/AVG/COUNT/MIN/MAX` 配合 OVER，不折叠行。`SUM(salary) OVER (PARTITION BY dept ORDER BY hire_date)` 累计求和。"
                    "`NTILE(n)` 分桶：把数据均匀分为 n 组。帧（Frame）：ROWS 按物理行，RANGE 按值范围。"
                    "`CUME_DIST()` 累积分布，`PERCENT_RANK()` 百分比排名。`PERCENTILE_CONT/DISC` 百分位数（需 WITHIN GROUP）。"
                    "窗口函数执行顺序：在 SELECT/JOIN/WHERE/HAVING 之后，ORDER BY 之前。不能直接在 WHERE 中引用窗口函数。"
                ),
                "examples": [
                    "-- 累计求和\nSELECT date, revenue,\n    SUM(revenue) OVER (ORDER BY date) AS cumulative\nFROM sales;\n-- 移动平均\nSELECT date, price,\n    AVG(price) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS ma7\nFROM stock_prices;\n-- NTILE 分桶\nSELECT name, score, NTILE(4) OVER (ORDER BY score) AS quartile\nFROM students;"
                ],
                "key_points": ["SUM OVER 累计/移动平均", "NTILE 分桶", "窗口不能用于 WHERE（用子查询）"],
            },
        ],
    },
    {
        "topic": "SQL索引",
        "lessons": [
            {
                "id": "lesson_sql_SQL索引_1", "title": "索引原理",
                "topic": "SQL索引",
                "content": (
                    "B+Tree 索引：MySQL InnoDB 默认结构，叶子节点存全部数据（聚簇索引）。查找 O(log n)，范围查询高效。"
                    "Hash 索引：等值查询 O(1)，不支持范围/排序。PostgreSQL/MemCache 常用。"
                    "索引类型：主键索引（唯一、聚簇）、唯一索引、普通索引、前缀索引（只索引前 N 字符）、全文索引。"
                    "覆盖索引：查询所需列全在索引中，不回表（Using index）。最左前缀原则：复合索引先匹配最左列。"
                ),
                "examples": [
                    "-- 创建索引\nCREATE INDEX idx_email ON users(email);\n-- 复合索引（最左前缀）\nCREATE INDEX idx_name_age ON users(name, age);\n-- 以下查询可用此索引: WHERE name = 'Alice'\n-- 以下不可用: WHERE age = 25（跳过了 name）\n-- 覆盖索引\nSELECT name, age FROM users WHERE name = 'Alice';\n-- 如果 idx_name_age 存在，不需要回表查聚集索引"
                ],
                "key_points": ["B+Tree O(log n) 范围高效", "最左前缀原则", "覆盖索引避免回表"],
            },
            {
                "id": "lesson_sql_SQL索引_2", "title": "索引优化与执行计划",
                "topic": "SQL索引",
                "content": (
                    "EXPLAIN 分析执行计划：关注 type（ALL 全表扫描 → ref/eq_ref 索引查找）、key（使用索引）、rows（扫描行数）。"
                    "索引失效常见场景：列上做函数/运算（`WHERE YEAR(date)=2024`）、前置模糊（`LIKE '%abc'`）、隐式类型转换。"
                    "前缀索引：`INDEX(col(10))` 省空间但可能降低选择性。索引下推（ICP）：存储引擎层先过滤再回表。"
                    "不适合索引：小表、频繁更新、区分度低的列（性别等）。索引越多写入越慢。"
                ),
                "examples": [
                    "-- 查看执行计划\nEXPLAIN SELECT * FROM users WHERE email = 'alice@example.com';\n-- 索引失效示例\n-- WHERE UPPER(name) = 'ALICE'       -- 列上函数\n-- WHERE name LIKE '%abc'            -- 前置模糊\n-- WHERE id = '123'（id 是 int）     -- 隐式转换\n-- 优化写法\n-- WHERE name = 'Alice' AND UPPER(name) = 'ALICE' -- 先精确匹配\nCREATE INDEX idx_name ON users(name(10));  -- 前缀索引"
                ],
                "key_points": ["EXPLAIN 分析 type/key/rows", "避免列上函数/前置模糊/隐式转换", "前缀索引 + 索引下推"],
            },
        ],
    },
    {
        "topic": "SQL事务",
        "lessons": [
            {
                "id": "lesson_sql_SQL事务_1", "title": "ACID 与隔离级别",
                "topic": "SQL事务",
                "content": (
                    "ACID：原子性（全部成功或回滚）、一致性（约束满足）、隔离性（并发如串行）、持久性（提交后不丢失）。"
                    "四大隔离级别：READ UNCOMMITTED（脏读）→ READ COMMITTED（不可重复读）→ REPEATABLE READ（幻读，MySQL 默认）→ SERIALIZABLE（串行）。"
                    "脏读：读到未提交数据。不可重复读：同一事务两次读结果不同（被 UPDATE）。幻读：范围查询结果变化（被 INSERT）。"
                    "MySQL InnoDB REPEATABLE READ 通过 MVCC + Next-Key Lock 避免幻读。PostgreSQL 默认 READ COMMITTED。"
                ),
                "examples": [
                    "-- 开始事务\nSTART TRANSACTION;\nUPDATE accounts SET balance = balance - 100 WHERE id = 1;\nUPDATE accounts SET balance = balance + 100 WHERE id = 2;\nCOMMIT;\n-- 或\nROLLBACK;\n-- 设置隔离级别\nSET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;"
                ],
                "key_points": ["ACID 四大特性", "四种隔离级别递增", "MVCC + Next-Key Lock 防幻读"],
            },
            {
                "id": "lesson_sql_SQL事务_2", "title": "锁与 MVCC",
                "topic": "SQL事务",
                "content": (
                    "锁粒度：行锁（InnoDB 默认，并发高）、表锁（MyISAM/DDL）、间隙锁（防止幻读的范围锁）。"
                    "共享锁 `SELECT ... LOCK IN SHARE MODE`，排他锁 `SELECT ... FOR UPDATE`。死锁检测：InnoDB 自动检测并回滚。"
                    "MVCC（多版本并发控制）：读写不互斥。每行存事务 ID + 回滚指针，Undo Log 构造历史版本。"
                    "`READ VIEW` 判断可见性：trx_id < min_trx_id 可见，trx_id > max_trx_id 不可见（等 Undo 回滚）。"
                ),
                "examples": [
                    "-- 共享锁\nSELECT * FROM users WHERE id = 1 LOCK IN SHARE MODE;\n-- 排他锁\nSELECT * FROM users WHERE id = 1 FOR UPDATE;\n-- 死锁示例（两事务交叉更新）\n-- T1: UPDATE t SET v=1 WHERE id=1;  -- 锁 id=1\n-- T2: UPDATE t SET v=2 WHERE id=2;  -- 锁 id=2\n-- T1: UPDATE t SET v=3 WHERE id=2;  -- 等 T2\n-- T2: UPDATE t SET v=4 WHERE id=1;  -- 等 T1 -> 死锁"
                ],
                "key_points": ["行锁/表锁/间隙锁", "SELECT ... FOR UPDATE 排他锁", "MVCC 读写不互斥"],
            },
        ],
    },
    {
        "topic": "SQL优化",
        "lessons": [
            {
                "id": "lesson_sql_SQL优化_1", "title": "查询优化",
                "topic": "SQL优化",
                "content": (
                    "最左前缀原则：复合索引先匹配最左列，`WHERE a=1 AND b=2` 可用 `(a,b)` 索引，`WHERE b=2` 不行。"
                    "分页优化：`LIMIT 100000,20` 慢，用延迟关联 `SELECT * FROM t JOIN (SELECT id FROM t LIMIT 100000,20) t2 ON t.id=t2.id`。"
                    "COUNT 优化：`COUNT(*)` 优于 `COUNT(col)`（不检查 NULL），MyISAM `COUNT(*)` 直接读统计，InnoDB 需扫描。"
                    "避免 SELECT *，只取所需列；用 UNION ALL 代替 UNION（跳过去重）；小表驱动大表。"
                ),
                "examples": [
                    "-- 分页延迟关联\nSELECT * FROM orders o\nJOIN (SELECT id FROM orders ORDER BY id LIMIT 100000, 20) tmp\nON o.id = tmp.id;\n-- 小表驱动大表\nSELECT * FROM users u\nJOIN orders o ON u.id = o.user_id\nWHERE u.created_at > '2024-01-01';  -- 先过滤小结果再 JOIN\n-- 用 UNION ALL\nSELECT name FROM users_2023\nUNION ALL\nSELECT name FROM users_2024;  -- 不去重，快"
                ],
                "key_points": ["最左前缀 + 延迟关联分页", "COUNT(*) 优于 COUNT(col)", "UNION ALL / 小表驱动"],
            },
            {
                "id": "lesson_sql_SQL优化_2", "title": "慢查询与配置优化",
                "topic": "SQL优化",
                "content": (
                    "慢查询日志：`slow_query_log=ON` + `long_query_time=1`，`mysqldumpslow` 分析。pt-query-digest 更强大。"
                    "Buffer Pool 配置（InnoDB）：建议为可用内存的 50-80%，`innodb_buffer_pool_size`。"
                    "连接池：`max_connections` 控制最大连接数，`wait_timeout` 空闲超时。应用层用 HikariCP（Java）/PGbouncer（PG）管理连接。"
                    "读写分离：主库写，从库读。分库分表：水平拆分（按 ID 取模）或垂直拆分（按业务模块）。"
                ),
                "examples": [
                    "-- 开启慢查询日志\nSET GLOBAL slow_query_log = ON;\nSET GLOBAL long_query_time = 0.5;  -- 超过 0.5 秒记录\n-- 查询 Buffer Pool 命中率\nSHOW STATUS LIKE 'Innodb_buffer_pool_read%';\n-- 计算: 1 - (reads / requests) = 命中率\n-- 连接池配置（HikariCP Java）\n-- hikari.maximumPoolSize=20\n-- hikari.minimumIdle=5\n-- hikari.idleTimeout=600000"
                ],
                "key_points": ["慢查询日志 + mysqldumpslow", "buffer_pool_size 50-80% 内存", "读写分离 + 连接池"],
            },
        ],
    },
    {
        "topic": "SQL设计",
        "lessons": [
            {
                "id": "lesson_sql_SQL设计_1", "title": "范式与反范式",
                "topic": "SQL设计",
                "content": (
                    "1NF：列不可再分（原子性）。2NF：非主键列完全依赖主键（消除部分依赖）。3NF：非主键列不传递依赖（消除传递依赖）。"
                    "BCNF：每个决定因素都是候选键。3NF 通常就足够，过度范式化导致 JOIN 过多。"
                    "反范式：适当冗余减少 JOIN，用空间换时间。常见反范式：冗余统计字段（如 `order_count`）、JSON 字段存储嵌套数据。"
                    "设计建议：根据查询模式（OLTP 高并发写 vs OLAP 大量聚合读）决定范式程度。"
                ),
                "examples": [
                    "-- 3NF 示例\n-- orders: id, user_id, product_id, quantity  -- 不存 user_name\n-- users: id, name, email\n-- products: id, name, price\n-- 反范式示例\n-- user_orders: user_id, user_name, total_orders, last_order_date\n-- 冗余 user_name 和统计，避免 JOIN\n-- JSON 字段（PostgreSQL/MySQL 5.7+）\nCREATE TABLE events (\n    id INT PRIMARY KEY,\n    payload JSON\n);"
                ],
                "key_points": ["1NF 原子性 / 2NF 部分依赖 / 3NF 传递依赖", "反范式冗余用空间换时间", "OLTP vs OLAP 设计取舍"],
            },
            {
                "id": "lesson_sql_SQL设计_2", "title": "数据建模实战",
                "topic": "SQL设计",
                "content": (
                    "ER 图 → 实体（表）+ 关系（外键/中间表）。一对一：唯一外键。一对多：多端加外键。多对多：中间表。"
                    "ID 生成：自增 ID（简单）、UUID（分布式，但索引不友好）、雪花 ID（有序分布式 ID）。"
                    "时间字段：`created_at`（创建时间）、`updated_at`（更新时间，用 ON UPDATE）、`deleted_at`（软删除）。"
                    "枚举 vs 关联表：枚举值少且固定用 ENUM/CHECK 约束，值多或动态变化用关联表。"
                ),
                "examples": [
                    "-- 多对多中间表\nCREATE TABLE user_roles (\n    user_id INT REFERENCES users(id),\n    role_id INT REFERENCES roles(id),\n    PRIMARY KEY (user_id, role_id)\n);\n-- 时间戳字段\nCREATE TABLE articles (\n    id BIGINT PRIMARY KEY AUTO_INCREMENT,\n    title VARCHAR(255) NOT NULL,\n    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,\n    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,\n    deleted_at TIMESTAMP NULL  -- 软删除\n);"
                ],
                "key_points": ["1:1 外键 / 1:N 多端外键 / N:M 中间表", "自增/雪花 ID 对比", "created_at + updated_at ON UPDATE"],
            },
        ],
    },
    {
        "topic": "SQL视图与存储",
        "lessons": [
            {
                "id": "lesson_sql_SQL视图与存储_1", "title": "视图与物化视图",
                "topic": "SQL视图与存储",
                "content": (
                    "普通视图 `CREATE VIEW ... AS SELECT ...`：保存查询定义，每次引用时执行，不存数据。"
                    "物化视图（PostgreSQL `CREATE MATERIALIZED VIEW`）：实际存储结果，需 `REFRESH MATERIALIZED VIEW` 更新。"
                    "可更新视图：基于简单 SELECT（无 JOIN/聚合/DISTINCT）的视图可 UPDATE/INSERT（WITH CHECK OPTION 约束）。"
                    "视图用途：封装复杂查询、权限控制（隐藏列）、提供向后兼容的 API。"
                ),
                "examples": [
                    "-- 普通视图\nCREATE VIEW active_users AS\nSELECT id, name, email FROM users WHERE status = 'active';\n-- 物化视图（PostgreSQL）\nCREATE MATERIALIZED VIEW user_stats AS\nSELECT user_id, COUNT(*) AS order_count, SUM(amount) AS total\nFROM orders GROUP BY user_id;\nREFRESH MATERIALIZED VIEW user_stats;\n-- 可更新视图\nCREATE VIEW vip_users AS\nSELECT * FROM users WHERE level = 'VIP'\nWITH CHECK OPTION;  -- INSERT/UPDATE 的 level 必须为 VIP"
                ],
                "key_points": ["普通视图不存数据", "物化视图存结果需刷新", "WITH CHECK OPTION 约束更新"],
            },
            {
                "id": "lesson_sql_SQL视图与存储_2", "title": "存储过程与触发器",
                "topic": "SQL视图与存储",
                "content": (
                    "存储过程：`CREATE PROCEDURE name(params) BEGIN ... END`，预处理编译，减少网络传输，封装业务逻辑。"
                    "函数：`CREATE FUNCTION name(params) RETURNS type` 有返回值，可内嵌 SQL（DETERMINISTIC 优化）。"
                    "触发器：`CREATE TRIGGER name BEFORE/AFTER INSERT/UPDATE/DELETE ON table FOR EACH ROW ...`，自动响应数据变更。"
                    "使用建议：存储过程增加数据库耦合，现代架构倾向应用层逻辑。触发器难调试，仅用于审计日志等简单场景。"
                ),
                "examples": [
                    "-- 存储过程（MySQL）\nDELIMITER $$\nCREATE PROCEDURE transfer(\n    IN from_acc INT, IN to_acc INT, IN amount DECIMAL(10,2)\n)\nBEGIN\n    START TRANSACTION;\n    UPDATE accounts SET balance = balance - amount WHERE id = from_acc;\n    UPDATE accounts SET balance = balance + amount WHERE id = to_acc;\n    COMMIT;\nEND$$\nDELIMITER ;\n-- 触发器\nCREATE TRIGGER trg_audit\nAFTER UPDATE ON accounts\nFOR EACH ROW\nINSERT INTO audit_log VALUES (OLD.id, OLD.balance, NEW.balance, NOW());"
                ],
                "key_points": ["存储过程封装事务逻辑", "函数 vs 存储过程：函数有返回值", "触发器仅简单场景（审计）"],
            },
        ],
    },
    {
        "topic": "SQL安全",
        "lessons": [
            {
                "id": "lesson_sql_SQL安全_1", "title": "SQL 注入防御",
                "topic": "SQL安全",
                "content": (
                    "SQL 注入原理：拼接用户输入到 SQL 字符串，如 `\"SELECT * FROM users WHERE id = \" + userId` 被注入 `1 OR 1=1`。"
                    "防御：参数化查询（Prepared Statement）是第一道防线。`stmt = conn.prepareStatement(\"SELECT * FROM users WHERE id = ?\")`。"
                    "ORM（Sequelize/Hibernate/ActiveRecord）通常内置参数化，但要小心原生查询拼接。"
                    "最小权限原则：应用账号只授予 SELECT/INSERT/UPDATE/DELETE，不给 DDL/CREATE/DROP。存储过程隔离。"
                ),
                "examples": [
                    "-- ❌ 危险拼接\n-- query = \"SELECT * FROM users WHERE name = '\" + input + \"'\"\n-- input = \"' OR '1'='1\" → 返回所有用户\n-- ✅ 参数化查询（Java PreparedStatement）\n-- PreparedStatement stmt = conn.prepareStatement(\"SELECT * FROM users WHERE name = ?\");\n-- stmt.setString(1, input);\n-- ✅ Python\n-- cursor.execute(\"SELECT * FROM users WHERE name = %s\", (input,))"
                ],
                "key_points": ["SQL 注入：拼接用户输入", "Prepared Statement 参数化", "最小权限原则"],
            },
            {
                "id": "lesson_sql_SQL安全_2", "title": "备份与恢复",
                "topic": "SQL安全",
                "content": (
                    "备份策略：全量备份（mysqldump/pg_dump）+ 增量备份（binlog/WAL 归档）+ 定期演练恢复流程。"
                    "mysqldump：逻辑备份，跨版本兼容但慢。XtraBackup：物理备份，快且不锁表（InnoDB）。"
                    "pg_dump/pg_restore：PostgreSQL 逻辑备份。pg_basebackup：物理备份 + WAL 连续归档实现 PITR（时间点恢复）。"
                    "高可用：主从复制 + 自动故障转移（MHA/Orchestrator/Patroni）、读写分离（ProxySQL/Pgpool-II）。"
                ),
                "examples": [
                    "# mysqldump 备份\nmysqldump -u root -p --single-transaction --all-databases > backup.sql\n# PostgreSQL 备份\npg_dump -U postgres -Fc mydb > mydb.dump\npg_restore -U postgres -d mydb mydb.dump\n# 时间点恢复（PostgreSQL）\n# recovery.conf 中设置 restore_command + recovery_target_time"
                ],
                "key_points": ["全量 + 增量备份策略", "mysqldump 逻辑 / XtraBackup 物理", "主从复制 + 故障转移"],
            },
        ],
    },
    {
        "topic": "SQL新特性",
        "lessons": [
            {
                "id": "lesson_sql_SQL新特性_1", "title": "JSON 与全文搜索",
                "topic": "SQL新特性",
                "content": (
                    "MySQL JSON 函数：`JSON_EXTRACT(doc, '$.key')` 提取，`->` 操作符（5.7.13+），`JSON_SET` 修改，虚拟列 + 索引。"
                    "PostgreSQL JSONB：索引友好二进制 JSON，GIN 索引加速 `@>` 包含查询。`jsonb_path_query` 路径查询。"
                    "全文索引：MySQL `FULLTEXT` 索引 + `MATCH(col) AGAINST('keyword')`，ngram 解析器支持中文。"
                    "PostgreSQL `tsvector` + `tsquery` + `@@` 全文搜索，`to_tsvector('english', text)` 分词。"
                ),
                "examples": [
                    "-- MySQL JSON 查询\nSELECT doc->'$.name' AS name FROM logs WHERE JSON_EXTRACT(doc, '$.level') = 'error';\n-- 虚拟列 + 索引\nALTER TABLE logs ADD COLUMN level VARCHAR(50)\n    GENERATED ALWAYS AS (doc->>'$.level') STORED;\nCREATE INDEX idx_level ON logs(level);\n-- PostgreSQL 全文搜索\nSELECT title FROM articles\nWHERE to_tsvector('english', content) @@ to_tsquery('english', 'database & optimization');"
                ],
                "key_points": ["MySQL JSON_EXTRACT / -> 操作符", "PostgreSQL JSONB + GIN 索引", "全文索引 MATCH AGAINST / tsvector"],
            },
            {
                "id": "lesson_sql_SQL新特性_2", "title": "窗口函数与分区表",
                "topic": "SQL新特性",
                "content": (
                    "窗口函数（MySQL 8.0+/PostgreSQL/所有主流 RDBMS）：排名、累计、移动平均。`OVER (PARTITION BY ... ORDER BY ... 帧)`。"
                    "分区表：按范围/RANGE、列表/LIST、哈希/HASH 分区。`PARTITION BY RANGE (date_col) (PARTITION p1 VALUES LESS THAN (...))`。"
                    "分区裁剪：查询自动只扫描相关分区。适合按时间归档的大表。"
                    "生成列（MySQL 5.7+/PostgreSQL）：VIRTUAL（计算不存储）vs STORED（计算并存储，可索引）。"
                ),
                "examples": [
                    "-- MySQL 分区表\nCREATE TABLE orders (\n    id INT, order_date DATE, amount DECIMAL(10,2)\n) PARTITION BY RANGE (YEAR(order_date)) (\n    PARTITION p2022 VALUES LESS THAN (2023),\n    PARTITION p2023 VALUES LESS THAN (2024),\n    PARTITION p2024 VALUES LESS THAN (2025),\n    PARTITION p_future VALUES LESS THAN MAXVALUE\n);\n-- 生成列\nALTER TABLE users ADD COLUMN full_name VARCHAR(200)\n    GENERATED ALWAYS AS (CONCAT(first_name, ' ', last_name)) STORED;"
                ],
                "key_points": ["窗口函数 MySQL 8.0+ 全支持", "RANGE/LIST/HASH 分区 + 分区裁剪", "VIRTUAL vs STORED 生成列"],
            },
        ],
    },
    {
        "topic": "索引优化",
        "lessons": [
            {
                "id": "lesson_sql_索引优化_1", "title": "索引优化",
                "topic": "索引优化",
                "content": (
                    "\"索引加速查询但增写开销。B-Tree默认类型：适合范围/排序。Hash索引仅等值查询。GIN/GiST全文/几何。\""
                    "\"EXPLAIN ANALYZE分析查询计划。Seq Scan全表扫描昂贵，Index Scan/Index Only Scan利用索引。\""
                    "\"覆盖索引：索引包含查询所需全部列避免回表。复合索引最左前缀原则。部分索引WHERE子句减少大小。\""
                ),
                "examples": [
                "# 创建索引\nCREATE INDEX idx_user_email ON users(email);\nCREATE INDEX idx_order_date_status ON orders(order_date, status);\n\n# 分析查询\nEXPLAIN ANALYZE SELECT * FROM orders WHERE user_id = 123 AND status = pending;\n\n# 部分索引\nCREATE INDEX idx_active_users ON users(email) WHERE status = active;"
                ],
                "key_points": ["B-Tree默认索引，Hash仅等值", "EXPLAIN ANALYZE分析执行计划", "覆盖索引+最左前缀+部分索引"],
            },
            {
                "id": "lesson_sql_索引优化_2", "title": "索引优化",
                "topic": "索引优化",
                "content": (
                    "\"索引加速查询但增写开销。B-Tree默认类型：适合范围/排序。Hash索引仅等值查询。GIN/GiST全文/几何。\""
                    "\"EXPLAIN ANALYZE分析查询计划。Seq Scan全表扫描昂贵，Index Scan/Index Only Scan利用索引。\""
                    "\"覆盖索引：索引包含查询所需全部列避免回表。复合索引最左前缀原则。部分索引WHERE子句减少大小。\""
                ),
                "examples": [
                "# 创建索引\nCREATE INDEX idx_user_email ON users(email);\nCREATE INDEX idx_order_date_status ON orders(order_date, status);\n\n# 分析查询\nEXPLAIN ANALYZE SELECT * FROM orders WHERE user_id = 123 AND status = pending;\n\n# 部分索引\nCREATE INDEX idx_active_users ON users(email) WHERE status = active;"
                ],
                "key_points": ["B-Tree默认索引，Hash仅等值", "EXPLAIN ANALYZE分析执行计划", "覆盖索引+最左前缀+部分索引"],
            },
        ],
    },
    {
        "topic": "事务与隔离级别",
        "lessons": [
            {
                "id": "lesson_sql_事务与隔离_1", "title": "事务与隔离级别",
                "topic": "事务与隔离级别",
                "content": (
                    "\"ACID：原子性、一致性、隔离性、持久性。BEGIN/COMMIT/ROLLBACK控制事务。\""
                    "\"四种隔离级别：Read Uncommitted(脏读)、Read Committed(不可重复读)、Repeatable Read(幻读)、Serializable。\""
                    "\"MVCC多版本并发控制：每行多版本，读不阻塞写。PG使用XID，MySQL InnoDB使用undo log。\""
                ),
                "examples": [
                "# 事务 + 隔离级别\nBEGIN;\nSET TRANSACTION ISOLATION LEVEL REPEATABLE READ;\nUPDATE accounts SET balance = balance - 100 WHERE id = 1;\nUPDATE accounts SET balance = balance + 100 WHERE id = 2;\nCOMMIT;\n\n# 死锁检测\n# PG自动检测并终止一个事务; MySQL innodb_lock_wait_timeout"
                ],
                "key_points": ["ACID + BEGIN/COMMIT/ROLLBACK", "4种隔离级别，MVCC多版本并发", "PG XID / MySQL undo log"],
            },
            {
                "id": "lesson_sql_事务与隔离_2", "title": "事务与隔离级别",
                "topic": "事务与隔离级别",
                "content": (
                    "\"ACID：原子性、一致性、隔离性、持久性。BEGIN/COMMIT/ROLLBACK控制事务。\""
                    "\"四种隔离级别：Read Uncommitted(脏读)、Read Committed(不可重复读)、Repeatable Read(幻读)、Serializable。\""
                    "\"MVCC多版本并发控制：每行多版本，读不阻塞写。PG使用XID，MySQL InnoDB使用undo log。\""
                ),
                "examples": [
                "# 事务 + 隔离级别\nBEGIN;\nSET TRANSACTION ISOLATION LEVEL REPEATABLE READ;\nUPDATE accounts SET balance = balance - 100 WHERE id = 1;\nUPDATE accounts SET balance = balance + 100 WHERE id = 2;\nCOMMIT;\n\n# 死锁检测\n# PG自动检测并终止一个事务; MySQL innodb_lock_wait_timeout"
                ],
                "key_points": ["ACID + BEGIN/COMMIT/ROLLBACK", "4种隔离级别，MVCC多版本并发", "PG XID / MySQL undo log"],
            },
        ],
    },
    {
        "topic": "窗口函数",
        "lessons": [
            {
                "id": "lesson_sql_窗口函数_1", "title": "窗口函数",
                "topic": "窗口函数",
                "content": (
                    "\"窗口函数在结果集上滑动计算：func() OVER (PARTITION BY col ORDER BY col)。不折叠行。\""
                    "\"常用：ROW_NUMBER()行号、RANK()/DENSE_RANK()排名、LAG/LEAD前后行、SUM/AVG累计。\""
                    "\"帧定义：ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW。默认RANGE。GROUPS (PG 11+)。\""
                ),
                "examples": [
                "# ROW_NUMBER 排名\nSELECT name, salary,\n    ROW_NUMBER() OVER (ORDER BY salary DESC) AS rank\nFROM employees;\n\n# LAG 前后行对比\nSELECT date, revenue,\n    LAG(revenue) OVER (ORDER BY date) AS prev_revenue,\n    revenue - LAG(revenue) OVER (ORDER BY date) AS change\nFROM daily_sales;\n\n# 累计 SUM\nSELECT date, amount,\n    SUM(amount) OVER (ORDER BY date ROWS UNBOUNDED PRECEDING) AS running_total\nFROM transactions;"
                ],
                "key_points": ["OVER(PARTITION BY...ORDER BY...)", "ROW_NUMBER/RANK/DENSE_RANK/LAG/LEAD", "ROWS/RANGE/GROUPS帧定义"],
            },
            {
                "id": "lesson_sql_窗口函数_2", "title": "窗口函数",
                "topic": "窗口函数",
                "content": (
                    "\"窗口函数在结果集上滑动计算：func() OVER (PARTITION BY col ORDER BY col)。不折叠行。\""
                    "\"常用：ROW_NUMBER()行号、RANK()/DENSE_RANK()排名、LAG/LEAD前后行、SUM/AVG累计。\""
                    "\"帧定义：ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW。默认RANGE。GROUPS (PG 11+)。\""
                ),
                "examples": [
                "# ROW_NUMBER 排名\nSELECT name, salary,\n    ROW_NUMBER() OVER (ORDER BY salary DESC) AS rank\nFROM employees;\n\n# LAG 前后行对比\nSELECT date, revenue,\n    LAG(revenue) OVER (ORDER BY date) AS prev_revenue,\n    revenue - LAG(revenue) OVER (ORDER BY date) AS change\nFROM daily_sales;\n\n# 累计 SUM\nSELECT date, amount,\n    SUM(amount) OVER (ORDER BY date ROWS UNBOUNDED PRECEDING) AS running_total\nFROM transactions;"
                ],
                "key_points": ["OVER(PARTITION BY...ORDER BY...)", "ROW_NUMBER/RANK/DENSE_RANK/LAG/LEAD", "ROWS/RANGE/GROUPS帧定义"],
            },
        ],
    },
    {
        "topic": "CTE与递归查询",
        "lessons": [
            {
                "id": "lesson_sql_CTE公共表表达式_1", "title": "CTE与递归查询",
                "topic": "CTE与递归查询",
                "content": (
                    "\"CTE：WITH name AS (query) 命名子查询。可读性优于嵌套子查询。多次引用不重复执行(MATERIALIZED)。\""
                    "\"递归CTE：WITH RECURSIVE 处理树/图。UNION ALL + 终止条件。组织架构/物料BOM/路径查找。\""
                    "\"多CTE：WITH cte1 AS (...), cte2 AS (...)。CTE可引用前面的CTE。PG支持数据修改CTE(INSERT...RETURNING)。\""
                ),
                "examples": [
                "# 简单CTE\nWITH high_salary AS (\n    SELECT * FROM employees WHERE salary > 100000\n)\nSELECT dept, COUNT(*) FROM high_salary GROUP BY dept;\n\n# 递归CTE: 组织树\nWITH RECURSIVE org_tree AS (\n    SELECT id, name, manager_id, 1 AS level FROM employees WHERE manager_id IS NULL\n    UNION ALL\n    SELECT e.id, e.name, e.manager_id, t.level + 1\n    FROM employees e INNER JOIN org_tree t ON e.manager_id = t.id\n)\nSELECT * FROM org_tree ORDER BY level, name;"
                ],
                "key_points": ["CTE可读性优于嵌套子查询", "递归CTE处理树/图结构", "多CTE链式引用"],
            },
            {
                "id": "lesson_sql_CTE公共表表达式_2", "title": "CTE与递归查询",
                "topic": "CTE与递归查询",
                "content": (
                    "\"CTE：WITH name AS (query) 命名子查询。可读性优于嵌套子查询。多次引用不重复执行(MATERIALIZED)。\""
                    "\"递归CTE：WITH RECURSIVE 处理树/图。UNION ALL + 终止条件。组织架构/物料BOM/路径查找。\""
                    "\"多CTE：WITH cte1 AS (...), cte2 AS (...)。CTE可引用前面的CTE。PG支持数据修改CTE(INSERT...RETURNING)。\""
                ),
                "examples": [
                "# 简单CTE\nWITH high_salary AS (\n    SELECT * FROM employees WHERE salary > 100000\n)\nSELECT dept, COUNT(*) FROM high_salary GROUP BY dept;\n\n# 递归CTE: 组织树\nWITH RECURSIVE org_tree AS (\n    SELECT id, name, manager_id, 1 AS level FROM employees WHERE manager_id IS NULL\n    UNION ALL\n    SELECT e.id, e.name, e.manager_id, t.level + 1\n    FROM employees e INNER JOIN org_tree t ON e.manager_id = t.id\n)\nSELECT * FROM org_tree ORDER BY level, name;"
                ],
                "key_points": ["CTE可读性优于嵌套子查询", "递归CTE处理树/图结构", "多CTE链式引用"],
            },
        ],
    },
    {
        "topic": "存储过程与函数",
        "lessons": [
            {
                "id": "lesson_sql_存储过程与函数_1", "title": "存储过程与函数",
                "topic": "存储过程与函数",
                "content": (
                    "\"函数(Function)：必须返回值，可在SELECT中调用。RETURNS type。LANGUAGE SQL/plpgsql。IMMUTABLE/STABLE/VOLATILE。\""
                    "\"存储过程(Procedure)：CALL调用，不返回值但可有OUT参数。支持事务控制COMMIT/ROLLBACK。PG 11+。\""
                    "\"触发器(Trigger)：BEFORE/AFTER/INSTEAD OF + INSERT/UPDATE/DELETE。NEW/OLD引用行。行级vs语句级。\""
                ),
                "examples": [
                "# PostgreSQL 函数\nCREATE FUNCTION get_total_sales(p_year INT)\nRETURNS NUMERIC AS $$\nDECLARE total NUMERIC;\nBEGIN\n    SELECT SUM(amount) INTO total FROM orders WHERE EXTRACT(YEAR FROM order_date) = p_year;\n    RETURN COALESCE(total, 0);\nEND;\n$$ LANGUAGE plpgsql;\n\n# 触发器\nCREATE TRIGGER update_timestamp\n    BEFORE UPDATE ON users\n    FOR EACH ROW EXECUTE FUNCTION update_modified_column();"
                ],
                "key_points": ["Function返回类型+PL语言", "Procedure支持事务控制", "Trigger+BEFORE/AFTER表事件"],
            },
            {
                "id": "lesson_sql_存储过程与函数_2", "title": "存储过程与函数",
                "topic": "存储过程与函数",
                "content": (
                    "\"函数(Function)：必须返回值，可在SELECT中调用。RETURNS type。LANGUAGE SQL/plpgsql。IMMUTABLE/STABLE/VOLATILE。\""
                    "\"存储过程(Procedure)：CALL调用，不返回值但可有OUT参数。支持事务控制COMMIT/ROLLBACK。PG 11+。\""
                    "\"触发器(Trigger)：BEFORE/AFTER/INSTEAD OF + INSERT/UPDATE/DELETE。NEW/OLD引用行。行级vs语句级。\""
                ),
                "examples": [
                "# PostgreSQL 函数\nCREATE FUNCTION get_total_sales(p_year INT)\nRETURNS NUMERIC AS $$\nDECLARE total NUMERIC;\nBEGIN\n    SELECT SUM(amount) INTO total FROM orders WHERE EXTRACT(YEAR FROM order_date) = p_year;\n    RETURN COALESCE(total, 0);\nEND;\n$$ LANGUAGE plpgsql;\n\n# 触发器\nCREATE TRIGGER update_timestamp\n    BEFORE UPDATE ON users\n    FOR EACH ROW EXECUTE FUNCTION update_modified_column();"
                ],
                "key_points": ["Function返回类型+PL语言", "Procedure支持事务控制", "Trigger+BEFORE/AFTER表事件"],
            },
        ],
    },
    {
        "topic": "权限与安全",
        "lessons": [
            {
                "id": "lesson_sql_权限与安全_1", "title": "权限与安全",
                "topic": "权限与安全",
                "content": (
                    "\"GRANT/REVOKE控制对象权限：SELECT/INSERT/UPDATE/DELETE/REFERENCES/TRIGGER。角色(ROLE)管理权限集。\""
                    "\"行级安全(RLS)：ALTER TABLE ENABLE ROW LEVEL SECURITY。CREATE POLICY定义访问规则。USING/CHECK。\""
                    "\"SQL注入防御：参数化查询(PreparedStatement)而非字符串拼接。输入验证+最小权限原则。加密敏感列。\""
                ),
                "examples": [
                "# 角色与权限\nCREATE ROLE readonly;\nGRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly;\nGRANT readonly TO alice;\n\n# 行级安全\nALTER TABLE posts ENABLE ROW LEVEL SECURITY;\nCREATE POLICY user_posts ON posts\n    FOR SELECT USING (author_id = current_user_id());\n\n# 参数化查询 (应用层)\n# PREPARE stmt AS SELECT * FROM users WHERE id = $1;\n# EXECUTE stmt(123);"
                ],
                "key_points": ["GRANT/REVOKE+ROLE权限管理", "RLS行级安全+Policy规则", "参数化查询防SQL注入"],
            },
            {
                "id": "lesson_sql_权限与安全_2", "title": "权限与安全",
                "topic": "权限与安全",
                "content": (
                    "\"GRANT/REVOKE控制对象权限：SELECT/INSERT/UPDATE/DELETE/REFERENCES/TRIGGER。角色(ROLE)管理权限集。\""
                    "\"行级安全(RLS)：ALTER TABLE ENABLE ROW LEVEL SECURITY。CREATE POLICY定义访问规则。USING/CHECK。\""
                    "\"SQL注入防御：参数化查询(PreparedStatement)而非字符串拼接。输入验证+最小权限原则。加密敏感列。\""
                ),
                "examples": [
                "# 角色与权限\nCREATE ROLE readonly;\nGRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly;\nGRANT readonly TO alice;\n\n# 行级安全\nALTER TABLE posts ENABLE ROW LEVEL SECURITY;\nCREATE POLICY user_posts ON posts\n    FOR SELECT USING (author_id = current_user_id());\n\n# 参数化查询 (应用层)\n# PREPARE stmt AS SELECT * FROM users WHERE id = $1;\n# EXECUTE stmt(123);"
                ],
                "key_points": ["GRANT/REVOKE+ROLE权限管理", "RLS行级安全+Policy规则", "参数化查询防SQL注入"],
            },
        ],
    },
    {
        "topic": "JSON与NoSQL特性",
        "lessons": [
            {
                "id": "lesson_sql_JSON与NoSQL_1", "title": "JSON与NoSQL特性",
                "topic": "JSON与NoSQL特性",
                "content": (
                    "\"JSON类型：PG jsonb(二进制高效) / MySQL JSON。->提取字段，->>提取文本。@>包含操作符。\""
                    "\"JSON索引：GIN索引加速jsonb查询。jsonb_path_ops操作符类优化。JSON_TABLE展开数组(PG 15+)。\""
                    "\"全文搜索：tsvector文本向量，tsquery查询。to_tsvector分段，plainto_tsquery简单查询。@@匹配。\""
                ),
                "examples": [
                "# jsonb 操作\nSELECT data->>name AS name,\n       data->metrics->>views AS views\nFROM api_logs\nWHERE data @> {\"status\": \"active\"}::jsonb;\n\n# GIN 索引\nCREATE INDEX idx_data ON api_logs USING GIN (data jsonb_path_ops);\n\n# 全文搜索\nSELECT title FROM articles\nWHERE to_tsvector(english, content) @@ plainto_tsquery(english, postgresql performance);"
                ],
                "key_points": ["jsonb (PG)/JSON (MySQL)类型", "GIN索引加速jsonb查询", "tsvector全文搜索向量"],
            },
            {
                "id": "lesson_sql_JSON与NoSQL_2", "title": "JSON与NoSQL特性",
                "topic": "JSON与NoSQL特性",
                "content": (
                    "\"JSON类型：PG jsonb(二进制高效) / MySQL JSON。->提取字段，->>提取文本。@>包含操作符。\""
                    "\"JSON索引：GIN索引加速jsonb查询。jsonb_path_ops操作符类优化。JSON_TABLE展开数组(PG 15+)。\""
                    "\"全文搜索：tsvector文本向量，tsquery查询。to_tsvector分段，plainto_tsquery简单查询。@@匹配。\""
                ),
                "examples": [
                "# jsonb 操作\nSELECT data->>name AS name,\n       data->metrics->>views AS views\nFROM api_logs\nWHERE data @> {\"status\": \"active\"}::jsonb;\n\n# GIN 索引\nCREATE INDEX idx_data ON api_logs USING GIN (data jsonb_path_ops);\n\n# 全文搜索\nSELECT title FROM articles\nWHERE to_tsvector(english, content) @@ plainto_tsquery(english, postgresql performance);"
                ],
                "key_points": ["jsonb (PG)/JSON (MySQL)类型", "GIN索引加速jsonb查询", "tsvector全文搜索向量"],
            },
        ],
    },
    {
        "topic": "性能调优",
        "lessons": [
            {
                "id": "lesson_sql_性能调优_1", "title": "性能调优",
                "topic": "性能调优",
                "content": (
                    "\"查询优化：避免SELECT *，用具体列。合理JOIN顺序小表驱动。子查询改JOIN/EXISTS。LIMIT限制返回。\""
                    "\"配置调优：shared_buffers(25%%内存)、work_mem、effective_cache_size。连接池PgBouncer。\""
                    "\"监控：pg_stat_statements慢查询。VACUUM清理死行。ANALYZE更新统计信息。auto_explain自动记录计划。\""
                ),
                "examples": [
                "# 查询优化前后对比\n# 差: SELECT * FROM orders o, users u WHERE o.user_id = u.id;\n# 好: SELECT o.id, o.amount, u.name FROM orders o JOIN users u ON o.user_id = u.id;\n\n# 慢查询分析\nSELECT query, calls, mean_exec_time\nFROM pg_stat_statements ORDER BY mean_exec_time DESC LIMIT 10;\n\n# VACUUM + ANALYZE\nVACUUM ANALYZE orders;"
                ],
                "key_points": ["避免SELECT *，JOIN代替子查询", "shared_buffers+work_mem配置", "pg_stat_statements慢查询分析"],
            },
            {
                "id": "lesson_sql_性能调优_2", "title": "性能调优",
                "topic": "性能调优",
                "content": (
                    "\"查询优化：避免SELECT *，用具体列。合理JOIN顺序小表驱动。子查询改JOIN/EXISTS。LIMIT限制返回。\""
                    "\"配置调优：shared_buffers(25%%内存)、work_mem、effective_cache_size。连接池PgBouncer。\""
                    "\"监控：pg_stat_statements慢查询。VACUUM清理死行。ANALYZE更新统计信息。auto_explain自动记录计划。\""
                ),
                "examples": [
                "# 查询优化前后对比\n# 差: SELECT * FROM orders o, users u WHERE o.user_id = u.id;\n# 好: SELECT o.id, o.amount, u.name FROM orders o JOIN users u ON o.user_id = u.id;\n\n# 慢查询分析\nSELECT query, calls, mean_exec_time\nFROM pg_stat_statements ORDER BY mean_exec_time DESC LIMIT 10;\n\n# VACUUM + ANALYZE\nVACUUM ANALYZE orders;"
                ],
                "key_points": ["避免SELECT *，JOIN代替子查询", "shared_buffers+work_mem配置", "pg_stat_statements慢查询分析"],
            },
        ],
    }
]

# ================================================================
# 多语言课程映射
# ================================================================
ALL_LANG_LEARNING_PATHS = {
    "typescript": TS_LEARNING_PATH,
    "java": JAVA_LEARNING_PATH,
    "javascript": JS_LEARNING_PATH,
    "cpp": CPP_LEARNING_PATH,
    "go": GO_LEARNING_PATH,
    "rust": RUST_LEARNING_PATH,
    "sql": SQL_LEARNING_PATH,
}
