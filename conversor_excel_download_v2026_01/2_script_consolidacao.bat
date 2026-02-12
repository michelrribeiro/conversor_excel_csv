echo off
setlocal

set ACTIVATE=virtual_env\Scripts\activate.bat
set VENV_PY=virtual_env\Scripts\python.exe

call "%ACTIVATE%"
"%VENV_PY%" ".\script_consolidacao.py"
pause