from agents.base import BaseAgent

REVIEW_SYSTEM_PROMPT = """你是一个严格的代码审查专家，名叫 CodeReviewer。你的职责是对每一段代码进行专业审查。

## 审查维度
1. **正确性**：逻辑错误、边界条件、空值处理、类型错误
2. **安全性**：注入风险、敏感信息泄露、权限问题、依赖漏洞
3. **性能**：时间复杂度、内存泄漏、不必要的计算、N+1查询
4. **可读性**：命名规范、注释质量、代码结构、函数长度
5. **最佳实践**：设计模式、SOLID原则、错误处理、测试覆盖
6. **语言特性**：是否合理使用语言特性、反模式

## 输出格式
使用以下结构化格式输出审查结果：

```
## 代码审查报告

### 总体评级
[优/良/中/差] — [一句话总结]

### 关键问题
1. [严重程度] 问题描述 → 建议修复方案
2. ...

### 改进建议
1. 建议描述 → 理由
2. ...

### 优化后代码示例 (如有必要)
```language
// 改进后的代码片段
```
```

## 审查原则
- 每个问题都要给出具体行号或代码片段引用
- 区分"必须修复"和"建议改进"
- 对初学者友好，解释清楚为什么这样改更好
- 使用中文回答，代码和术语保持英文
"""


class ReviewAgent:
    """代码审查Agent - 负责对代码进行多维度专业审查"""

    def __init__(self):
        self.agent = BaseAgent(
            name="reviewer",
            system_prompt=REVIEW_SYSTEM_PROMPT,
            temperature=0.3  # 低温，保证审查一致性
        )

    async def review(self, code: str, language: str = "", history: list[dict] | None = None):
        """
        审查代码
        :param code: 待审查的代码
        :param language: 编程语言（如 python, javascript, java 等）
        :param history: 对话历史
        """
        prompt = f"请审查以下代码"
        if language:
            prompt += f"（{language}）"
        prompt += f"：\n\n```{language if language else ''}\n{code}\n```"

        async for chunk in self.agent.stream(history or [], prompt):
            yield chunk

    async def review_file(self, file_path: str, content: str):
        """
        审查整个文件的代码
        :param file_path: 文件路径
        :param content: 文件内容
        """
        # 根据扩展名推断语言
        ext_map = {
            ".py": "python", ".js": "javascript", ".ts": "typescript",
            ".tsx": "typescript", ".jsx": "javascript", ".java": "java",
            ".go": "go", ".rs": "rust", ".cpp": "cpp", ".c": "c",
            ".html": "html", ".css": "css", ".sql": "sql", ".sh": "bash",
        }
        ext = file_path[file_path.rfind("."):] if "." in file_path else ""
        language = ext_map.get(ext.lower(), "")

        prompt = f"请审查文件 `{file_path}` 的完整代码：\n\n```{language}\n{content}\n```"

        async for chunk in self.agent.stream([], prompt):
            yield chunk
