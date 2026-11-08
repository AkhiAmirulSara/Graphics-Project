@echo off
cd /d "%~dp0"
echo Installing project dependencies...
py -m pip install -r requirements.txt
if errorlevel 1 goto failed
echo Starting SIR IS COMING!...
py -m streamlit run app.py
goto end
:failed
echo Dependency installation failed. Check your Python and internet connection.
:end
pause
