@echo off
cd /d "%~dp0"
git add static/index.html
git commit -m "Fix: UIレイアウト微調整（検索結果枠の横幅）"
git push origin main
pause
