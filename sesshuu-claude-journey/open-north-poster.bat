@echo off
chcp 65001 >nul
cd /d "%~dp0"

REM デッキの open-preview.bat（8765）と重ならないよう 8766 を使用
set PORT=8766

where python >nul 2>&1
if errorlevel 1 (
  echo [エラー] Python が PATH にありません。
  echo 代替: エクスプローラーで north-poster.html をダブルクリック
  echo 代替: npx --yes serve . -l %PORT%
  pause
  exit /b 1
)

echo NORTH ポスターをブラウザで開きます（http://127.0.0.1:%PORT%/north-poster.html^）
echo プレビュー用サーバーを起動（別ウィンドウ・最小化）...
start "sesshuu-north-poster" /MIN python -m http.server %PORT%

ping 127.0.0.1 -n 5 >nul

echo 既定のブラウザで開きます。
start "" "http://127.0.0.1:%PORT%/north-poster.html"

echo.
echo 表示されない場合は数秒待って F5。終了はタスクバーの「sesshuu-north-poster」を閉じる。
echo デッキ本体は open-preview.bat（ポート 8765）を使用。
echo.
pause
