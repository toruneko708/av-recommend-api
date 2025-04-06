@echo off
cd /d "%~dp0"

git add .
git commit -m "Update: 全般的な変更をコミット"
git push origin main

pause