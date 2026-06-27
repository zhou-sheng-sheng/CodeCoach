"""代码沙箱执行限制配置"""

import signal
import platform

# 执行超时（秒）
EXECUTION_TIMEOUT = 10

# 最大输出字符数
MAX_OUTPUT_CHARS = 50_000

# 最大内存限制（MB），仅 Unix 有效
MAX_MEMORY_MB = 256

# 禁止的模块/内置函数（安全加固）
FORBIDDEN_IMPORTS = {
    "os", "subprocess", "sys", "shutil", "importlib",
    "ctypes", "multiprocessing", "socket", "http",
    "ftplib", "smtplib", "telnetlib", "xmlrpc",
    "pty", "fcntl", "posix", "signal",
    "pickle", "shelve", "marshal",
}

FORBIDDEN_BUILTINS = {
    "open", "exec", "eval", "compile", "__import__",
    "globals", "locals", "vars", "getattr", "setattr",
    "delattr", "breakpoint",
}

# 白名单内置函数（允许使用的）
ALLOWED_BUILTINS = {
    "abs", "all", "any", "bin", "bool", "bytes", "chr",
    "complex", "dict", "divmod", "enumerate", "filter",
    "float", "format", "frozenset", "hash", "hex",
    "int", "isinstance", "issubclass", "iter", "len",
    "list", "map", "max", "min", "next", "oct",
    "ord", "pow", "print", "range", "repr", "reversed",
    "round", "set", "slice", "sorted", "str", "sum",
    "tuple", "type", "zip", "help", "dir",
    "True", "False", "None", "Exception", "ValueError",
    "TypeError", "KeyError", "IndexError", "StopIteration",
    "ZeroDivisionError", "AssertionError", "RuntimeError",
    "ArithmeticError", "AttributeError", "ImportError",
    "LookupError", "MemoryError", "NameError", "NotImplementedError",
    "OSError", "OverflowError", "RecursionError", "SyntaxError",
    "UnicodeError", "UnboundLocalError", "KeyboardInterrupt",
}
