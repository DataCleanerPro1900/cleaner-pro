@echo off
echo ============================================
echo GitHub访问问题解决方案脚本
echo ============================================
echo.

echo [1] 测试GitHub连接性...
ping -n 2 github.com
echo.

echo [2] 当前Git远程配置...
git remote -v
echo.

echo [3] 尝试方案1: 使用GitHub镜像...
echo 选项A: ghproxy.com
git remote set-url origin https://ghproxy.com/https://github.com/helei1800-beep/cleaner-pro.git
echo 测试连接...
git ls-remote --get-url origin
echo.

echo 选项B: fastgit.org
git remote set-url origin https://hub.fastgit.org/helei1800-beep/cleaner-pro.git
echo 测试连接...
git ls-remote --get-url origin
echo.

echo 选项C: gitclone.com
git remote set-url origin https://gitclone.com/github.com/helei1800-beep/cleaner-pro.git
echo 测试连接...
git ls-remote --get-url origin
echo.

echo [4] 尝试方案2: 优化Git配置...
git config --global http.postBuffer 524288000
git config --global http.lowSpeedLimit 0
git config --global http.lowSpeedTime 999999
git config --global http.sslVerify false
echo Git配置已优化
echo.

echo [5] 尝试方案3: 使用SSH（需要SSH密钥）...
echo 检查SSH密钥...
if exist "%USERPROFILE%\.ssh\id_rsa.pub" (
    echo SSH密钥存在
    git remote set-url origin git@github.com:helei1800-beep/cleaner-pro.git
) else (
    echo SSH密钥不存在，跳过SSH方案
)
echo.

echo [6] 最终测试和推送...
echo 当前远程URL: 
git ls-remote --get-url origin
echo.

echo 尝试推送代码...
git push -u origin main
echo.

if %ERRORLEVEL% EQU 0 (
    echo ============================================
    echo ✅ 推送成功！
    echo 仓库地址: https://github.com/helei1800-beep/cleaner-pro
    echo ============================================
) else (
    echo ============================================
    echo ❌ 推送失败，尝试以下手动方案：
    echo.
    echo 方案A: 使用网页上传
    echo   1. 访问: https://github.com/helei1800-beep/cleaner-pro
    echo   2. 点击"Add file" -> "Upload files"
    echo   3. 上传整个cleaner-pro文件夹
    echo.
    echo 方案B: 使用GitHub Desktop
    echo   1. 安装GitHub Desktop
    echo   2. 添加本地仓库
    echo   3. 使用GUI界面推送
    echo.
    echo 方案C: 使用VPN或代理
    echo   1. 开启VPN连接
    echo   2. 重新运行本脚本
    echo ============================================
)

pause