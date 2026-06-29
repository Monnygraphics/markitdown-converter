@echo off
echo.
echo ========================================
echo   MarkItDown Live Converter
echo ========================================
echo.
echo Starting servers...
echo.

REM Start Flask server in a new window
start "Flask Server" python app.py

REM Wait for Flask to start
timeout /t 2 /nobreak

REM Start ngrok to create public URL
echo.
echo Creating public URL...
echo.
ngrok http 5000 --log=stdout

pause
