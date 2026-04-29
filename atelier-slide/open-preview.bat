@echo off
chcp 65001 >nul
cd /d "%~dp0"

where python >nul 2>&1
if errorlevel 1 (
  echo [エラー] Python が PATH にありません。
  echo このフォルダで:  npx --yes serve . -l 8765
  pause
  exit /b 1
)

echo プレビュー用サーバーを起動しています（別ウィンドウ・最小化）...
start "sesshuu-claude-journey-preview" /MIN python -m http.server 8765

ping 127.0.0.1 -n 5 >nul

echo 既定のブラウザで開きます。
start "" "http://127.0.0.1:8765/index.html"

echo.
echo NORTHポスター（north-poster.html）: 同フォルダの open-north-poster.bat を実行するか
echo   ブラウザで http://127.0.0.1:8765/north-poster.html を開く（サーバー起動中のみ）。
echo.
echo ページが出ない場合: 数秒待ってからブラウザで F5 更新。
echo 終了: タスクバーの「sesshuu-claude-journey-preview」を閉じる。
echo.
pause
