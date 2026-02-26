@echo off
echo ========================================
echo GitHub Push Script for cleaner-pro
echo ========================================
echo.

echo 1. Checking Git status...
git status
echo.

echo 2. Adding all files...
git add .
echo.

echo 3. Committing changes...
git commit -m "Update project files"
echo.

echo 4. Pushing to GitHub...
git push -u origin main
echo.

echo 5. Verifying push...
git log --oneline -3
echo.

echo ========================================
echo If push fails, check:
echo 1. Internet connection
echo 2. GitHub repository exists: https://github.com/helei1800-beep/cleaner-pro
echo 3. Git credentials are configured
echo ========================================
pause