# 1) 別ウィンドウで HTTP サーバー起動  2) 待機  3) ブラウザで開く
# 「URL だけ開いても繋がらない」→ サーバーが動いていないのが原因のことが多いです。
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot
$port = 8765
$url = "http://127.0.0.1:$port/index.html"

function Test-PortListen([int]$p) {
  try {
    $c = Get-NetTCPConnection -LocalPort $p -State Listen -ErrorAction SilentlyContinue
    return [bool]$c
  } catch {
    return $false
  }
}

if (Test-PortListen $port) {
  Write-Host "ポート $port は既に使用中です。ブラウザだけ開きます: $url" -ForegroundColor Yellow
  Start-Process $url
  exit 0
}

$python = $null
if (Get-Command python -ErrorAction SilentlyContinue) { $python = "python" }
elseif (Get-Command py -ErrorAction SilentlyContinue) { $python = "py" }

if (-not $python) {
  Write-Host "Python が見つかりません。Node なら次をこのフォルダで実行:" -ForegroundColor Yellow
  Write-Host "  npx --yes serve . -l $port" -ForegroundColor Yellow
  exit 1
}

# 別プロセスでサーバー（作業ディレクトリはこの HTML と同じフォルダ）
Start-Process -FilePath $python -ArgumentList @("-m", "http.server", "$port") -WorkingDirectory $PSScriptRoot -WindowStyle Minimized

$ok = $false
for ($i = 0; $i -lt 40; $i++) {
  Start-Sleep -Milliseconds 250
  if (Test-PortListen $port) { $ok = $true; break }
}

if (-not $ok) {
  Write-Host "サーバーが $port で待ち受けになりませんでした。最小化された「コマンド プロンプト」を開き、エラー内容を確認してください。" -ForegroundColor Red
  exit 1
}

Start-Process $url
Write-Host "開きました: $url" -ForegroundColor Cyan
Write-Host "表示されないときは数秒待ってからブラウザで更新（F5）。" -ForegroundColor DarkGray
Write-Host "停止: タスクバーの「コマンド プロンプト」ウィンドウを閉じる（またはその中で Ctrl+C）。" -ForegroundColor DarkGray
