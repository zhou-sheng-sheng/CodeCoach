Set-Location "E:\编程AI陪练系统"
# Start vite in background
$viteJob = Start-Job -ScriptBlock {
    Set-Location "E:\编程AI陪练系统"
    npx vite 2>&1
}
# Wait for vite to be ready
$ready = $false
for ($i = 0; $i -lt 30; $i++) {
    Start-Sleep -Seconds 2
    try {
        $null = Invoke-WebRequest -Uri "http://localhost:5173" -TimeoutSec 2 -UseBasicParsing
        $ready = $true
        Write-Output "Vite is ready"
        break
    } catch {}
}
if (-not $ready) {
    Write-Output "Vite did not start"
    Receive-Job $viteJob
    exit 1
}
# Start Electron
Write-Output "Starting Electron..."
npx electron . 2>&1
