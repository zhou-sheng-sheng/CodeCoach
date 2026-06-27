"""JavaScript 代码沙箱执行器 — Node.js 子进程执行"""
import subprocess
import tempfile
import os
from .limits import EXECUTION_TIMEOUT, MAX_OUTPUT_CHARS


def run_javascript(code: str, stdin: str = "") -> dict:
    """在 Node.js 子进程中安全执行 JavaScript 代码

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
    tmp_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".js", delete=False, encoding="utf-8"
        ) as f:
            f.write(code)
            tmp_path = f.name

        proc = subprocess.Popen(
            ["node", tmp_path],
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

        stdout = stdout[:MAX_OUTPUT_CHARS]
        stderr = stderr[:MAX_OUTPUT_CHARS]

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
            "error": "Node.js 未找到，请确认已安装 Node.js",
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
