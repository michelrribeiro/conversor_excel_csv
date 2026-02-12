echo off
setlocal

REM ============================================
REM  Configuração de ambiente Python 3.13
REM ============================================

REM Caminho para o executável Python:
set PYTHON=C:\Users\user\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\python.exe

REM Nome da pasta do ambiente virtual
set VENV_DIR=virtual_env
set ACTIVATE=%VENV_DIR%\Scripts\activate.bat
set VENV_PY=%VENV_DIR%\Scripts\python.exe

echo.
echo Verificando ambiente virtual...
echo.

REM ============================================
REM 1) Verifica se o ambiente já existe
REM ============================================
IF NOT EXIST "%ACTIVATE%" (
    echo Ambiente nao encontrado. Criando ambiente virtual...
    "%PYTHON%" -m venv "%VENV_DIR%"
) ELSE (
    echo Ambiente virtual ja existe.
)

REM ============================================
REM 2) Ativa o ambiente
REM ============================================
echo Ativando ambiente virtual...
call "%ACTIVATE%"

REM ============================================
REM 3) Atualiza pip
REM ============================================
echo Atualizando pip...
%VENV_PY% -m pip install --upgrade pip

REM ============================================
REM 4) Instala dependencias
REM ============================================
echo Instalando dependencias via requirements.txt...
%VENV_PY% -m pip install -r requirements.txt

echo.
echo Ambiente configurado com sucesso!
pause
