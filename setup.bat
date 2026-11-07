@echo off
REM One-time setup for StudentWise (Windows). Double-click or run: setup.bat
if not exist venv python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
if not exist .env (
  copy .env.example .env >nul
  powershell -NoProfile -Command "(Get-Content .env) -replace 'change-me-to-a-long-random-string', [guid]::NewGuid().ToString('N') | Set-Content .env"
)
if not exist migrations\env.py flask --app run.py db init
if not exist migrations\versions\*.py flask --app run.py db migrate -m "initial"
flask --app run.py db upgrade
echo.
echo Setup finished. Now run start.bat
pause
