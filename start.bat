@echo off
call venv\Scripts\activate
REM Bring the database up to date (adds tables for new features; keeps your existing data)
flask --app run.py db upgrade
flask --app run.py db migrate -m "update" >nul 2>&1
flask --app run.py db upgrade
echo.
echo Open http://127.0.0.1:5000 in Chrome or Edge. Press Ctrl+C to stop.
python run.py

