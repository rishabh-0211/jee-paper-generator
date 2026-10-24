@echo off
setlocal enabledelayedexpansion
title GitHub 24/7 Cloud Deployment - JEE Paper Generator
color 0b

echo ===============================================================================
echo        JEE ENTRANCE EXAM PAPER GENERATOR - PUSH TO GITHUB FOR RENDER
echo ===============================================================================
echo.
echo  STEP 1: Create an Empty Repository on GitHub (Takes 15 seconds)
echo  ----------------------------------------------------------------
echo  1. Open: https://github.com/new in your browser
echo  2. Repository name: jee-paper-generator
echo  3. Choose: Public
echo  4. IMPORTANT: Do NOT check "Add a README", .gitignore, or license!
echo  5. Click the green "Create repository" button.
echo.
echo ===============================================================================
echo.

set /p REPO_URL="Paste your GitHub Repository URL (e.g. https://github.com/YOUR_USER/jee-paper-generator.git): "
if "%REPO_URL%"=="" (
    echo [ERROR] Repository URL cannot be empty.
    pause
    exit /b
)

echo.
echo ===============================================================================
echo  UPLOADING APP AND 51,000+ QUESTIONS TO GITHUB...
echo  (A browser popup may appear to sign in to GitHub if not already signed in)
echo ===============================================================================
echo.

cd /d "%~dp0"
git remote remove origin 2>nul
git remote add origin %REPO_URL%
git branch -M main
git add -A
git commit -m "Deploy JEE Exam Paper Generator with KaTeX and Render support" 2>nul

echo Pushing code to GitHub...
git push -u origin main --force

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ===============================================================================
    echo                     SUCCESS! CODE PUSHED TO GITHUB!
    echo ===============================================================================
    echo.
    echo  NOW DEPLOY ON RENDER IN 2 CLICKS (100%% FREE FOREVER):
    echo  1. Open: https://dashboard.render.com (Sign in with your GitHub)
    echo  2. Click "New +" -> Select "Web Service"
    echo  3. Select your "jee-paper-generator" repository
    echo  4. Click "Connect" -> Scroll down and click "Create Web Service"
    echo.
    echo  Render will automatically build and give you a permanent 24/7 HTTPS link:
    echo  https://jee-paper-generator-xxxx.onrender.com
    echo.
    echo  You can now open this link on your mobile phone, add it to your home screen,
    echo  and share it with anyone in the world without needing your laptop!
    echo ===============================================================================
) else (
    echo.
    echo [ERROR] Push failed.
    echo Make sure:
    echo 1. The repository URL is correct.
    echo 2. You selected "Sign in with your browser" when prompted.
)

echo.
pause
