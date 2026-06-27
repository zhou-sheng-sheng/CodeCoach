$env:HF_ENDPOINT = "https://hf-mirror.com"
$env:HF_HUB_ENABLE_HF_TRANSFER = "1"
cd "E:\编程AI陪练系统\backend"
& "E:\Marvis\MarvisAgent\1.0.1100.230\runtime\python311\python.exe" -m uvicorn main:app --host 127.0.0.1 --port 18080 2>&1 | Out-File "E:\编程AI陪练系统\server.log"
