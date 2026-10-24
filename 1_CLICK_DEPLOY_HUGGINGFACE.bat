@echo off
setlocal enabledelayedexpansion
title Hugging Face 24/7 Cloud Deployment - JEE Paper Generator
color 0b

echo ===============================================================================
echo        JEE ENTRANCE EXAM PAPER GENERATOR - 24/7 FREE CLOUD HOSTING
echo ===============================================================================
echo.
echo  This tool will deploy your JEE Paper Generator to Hugging Face Spaces for FREE.
echo  Once deployed:
echo    * Access it 24/7 from ANY phone or browser in the world
echo    * ZERO laptop dependency (laptop can be completely shut down / turned off)
echo    * Free permanent HTTPS link to share with anyone!
echo.
echo ===============================================================================
echo  STEP 1: Create a Free Hugging Face Space (Takes 30 seconds)
echo ===============================================================================
echo  1. Open: https://huggingface.co/join (if you don't have an account) or login.
echo  2. Open: https://huggingface.co/new-space
echo     - Space Name: jee-exam-generator (or any name you like)
echo     - License: MIT (or Apache 2.0)
echo     - Space SDK: Docker -> Blank
echo     - Hardware: CPU basic (2 vCPU, 16 GB RAM) - 100%% FREE FOREVER
echo     - Visibility: Public
echo  3. Click "Create Space"
echo.
echo ===============================================================================
echo  STEP 2: Get a Free Access Token
echo ===============================================================================
echo  1. Open: https://huggingface.co/settings/tokens
echo  2. Click "Create new token" -> Name: deploy -> Role: "Write"
echo  3. Copy your token (starts with hf_...)
echo.
echo ===============================================================================
echo.
set /p HF_USERNAME="Enter your Hugging Face Username: "
if "%HF_USERNAME%"=="" (
    echo Username cannot be empty.
    pause
    exit /b
)

set /p SPACE_NAME="Enter your Space Name [default: jee-exam-generator]: "
if "%SPACE_NAME%"=="" (
    set SPACE_NAME=jee-exam-generator
)

set /p HF_TOKEN="Enter your Hugging Face Access Token (hf_...): "
if "%HF_TOKEN%"=="" (
    echo Token cannot be empty.
    pause
    exit /b
)

echo.
echo ===============================================================================
echo  UPLOADING APP AND 51,000+ QUESTIONS TO HUGGING FACE SPACES...
echo  (This may take 1-3 minutes depending on your internet upload speed)
echo ===============================================================================
echo.

git remote remove origin 2>nul
git remote add origin https://%HF_USERNAME%:%HF_TOKEN%@huggingface.co/spaces/%HF_USERNAME%/%SPACE_NAME%
git add -A
git commit -m "Deploy JEE Exam Paper Generator to Cloud" 2>nul

echo Pushing code and datasets to Hugging Face...
git push -u origin main --force

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ===============================================================================
    echo                     SUCCESS! DEPLOYMENT COMPLETED!
    echo ===============================================================================
    echo.
    echo  Your application is now building and running 24/7 in the cloud!
    echo.
    echo  Your Permanent Mobile & Public URL:
    echo  https://%HF_USERNAME%-%SPACE_NAME%.hf.space
    echo.
    echo  Space Dashboard & Build Logs:
    echo  https://huggingface.co/spaces/%HF_USERNAME%/%SPACE_NAME%
    echo.
    echo  * Note: Give it 2-3 minutes on the first build for Docker to finish.
    echo  * You can now SHUT DOWN your laptop completely!
    echo  * Bookmark the link on your mobile phone or tap "Add to Home Screen".
    echo ===============================================================================
) else (
    echo.
    echo [ERROR] Git push failed. Please check:
    echo 1. Is your username and space name exact?
    echo 2. Did your token have "Write" permissions?
    echo 3. Did you select "Docker" when creating the space?
)

echo.
pause
