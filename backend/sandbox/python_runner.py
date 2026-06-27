"""Python 代码沙箱执行器 — subprocess 隔离 + 超时 + 输出捕获"""
import subprocess
import tempfile
import os
from .limits import (
    EXECUTION_TIMEOUT,
    MAX_OUTPUT_CHARS,
    FORBIDDEN_IMPORTS,
    FORBIDDEN_BUILTINS,
    ALLOWED_BUILTINS,
)

# 注入到用户代码前的安全序言
SANDBOX_PROLOGUE = f"""
# === 安全沙箱序言（对用户透明） ===
import builtins as __sandbox_builtins__
__allowed_builtins__ = {ALLOWED_BUILTINS}

# 保存对内置函数的原始引用（避免后续被屏蔽后无法使用）
__orig_setattr = __sandbox_builtins__.setattr
__orig_getattr = __sandbox_builtins__.getattr

# 屏蔽危险内置函数 —— 使用可调用类
class __SandboxBlocker:
    __slots__ = ('_name',)
    def __init__(self, name):
        self._name = name
    def __call__(self, *a, **k):
        raise RuntimeError(f"禁止使用 {{self._name}}")
    def __repr__(self):
        return f"<Blocked: {{self._name}}>"

for __name in dir(__sandbox_builtins__):
    if __name not in __allowed_builtins__ and not __name.startswith('_'):
        __orig_setattr(__sandbox_builtins__, __name, __SandboxBlocker(__name))

# 钩子拦截危险导入
__original_import__ = __import__
def __safe_import__(name, *args, **kwargs):
    top_level = name.split('.')[0]
    if top_level in {FORBIDDEN_IMPORTS}:
        raise ImportError(f"沙箱禁止导入模块: {{top_level}}")
    return __original_import__(name, *args, **kwargs)
__orig_setattr(__sandbox_builtins__, '__import__', __safe_import__)

# 禁用 open（文件读写）
__orig_setattr(__sandbox_builtins__, 'open', __SandboxBlocker("open"))
"""


def run_python(code: str, stdin: str = "") -> dict:
    """在子进程中安全执行 Python 代码

    Returns:
        {
            "success": bool,
            "stdout": str,
            "stderr": str,
            "error": str | None,
            "exit_code": int,
            "timed_out": bool,
        }
    """
    # 写入临时文件（避免命令行注入）
    tmp_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".py", delete=False, encoding="utf-8"
        ) as f:
            f.write(SANDBOX_PROLOGUE + "\n\n# === 用户代码 ===\n" + code)
            tmp_path = f.name

        proc = subprocess.Popen(
            ["python", tmp_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8",
            errors="replace",
        )

        try:
            stdout, stderr = proc.communicate(input=stdin, timeout=EXECUTION_TIMEOUT)
            timed_out = False
        except subprocess.TimeoutExpired:
            proc.kill()
            stdout, stderr = proc.communicate()
            timed_out = True

        # 截断过长输出
        stdout = stdout[:MAX_OUTPUT_CHARS]
        stderr = stderr[:MAX_OUTPUT_CHARS]

        # 过滤掉沙箱内部报错（如禁止导入导致的 NameError 等）
        if stderr.strip().startswith("Traceback"):
            # 保留原始 traceback
            pass

        return {
            "success": proc.returncode == 0 and not timed_out,
            "stdout": stdout,
            "stderr": stderr,
            "error": "执行超时" if timed_out else None,
            "exit_code": proc.returncode if not timed_out else -1,
            "timed_out": timed_out,
        }

    except FileNotFoundError:
        return {
            "success": False,
            "stdout": "",
            "stderr": "",
            "error": "Python 解释器未找到，请确认已安装 Python",
            "exit_code": -1,
            "timed_out": False,
        }
    except Exception as e:
        return {
            "success": False,
            "stdout": "",
            "stderr": "",
            "error": f"沙箱执行异常: {str(e)}",
            "exit_code": -1,
            "timed_out": False,
        }
    finally:
        if tmp_path and os.path.exists(tmp_path):
            try:
                os.unlink(tmp_path)
            except OSError:
                pass
