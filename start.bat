@echo off
title ScriptClone - Launcher
color 0A

echo.
echo ===============================================
echo          SCRIPTCLONE - LAUNCHER
echo ===============================================
echo.

REM Verificar se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python nao encontrado!
    echo.
    echo Por favor, instale Python 3.8+ de:
    echo https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo ✅ Python encontrado
echo.

REM Verificar se os arquivos existem
if not exist "run.py" (
    echo ❌ Arquivo run.py nao encontrado!
    echo Certifique-se de estar na pasta correta do projeto.
    echo.
    pause
    exit /b 1
)

echo ✅ Arquivos do projeto encontrados
echo.

REM Executar o launcher
echo 🚀 Iniciando ScriptClone...
echo.
python run.py

echo.
echo Pressione qualquer tecla para fechar...
pause >nul