#!/bin/bash

# ScriptClone - Launcher para Linux/Mac
# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}"
echo "==============================================="
echo "          SCRIPTCLONE - LAUNCHER"
echo "==============================================="
echo -e "${NC}"

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo -e "${RED}❌ Python não encontrado!${NC}"
        echo ""
        echo "Por favor, instale Python 3.8+ de:"
        echo "https://www.python.org/downloads/"
        echo ""
        echo "Ou use seu gerenciador de pacotes:"
        echo "  Ubuntu/Debian: sudo apt install python3"
        echo "  macOS: brew install python3"
        echo ""
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

echo -e "${GREEN}✅ Python encontrado${NC}"
echo ""

# Verificar se os arquivos existem
if [ ! -f "run.py" ]; then
    echo -e "${RED}❌ Arquivo run.py não encontrado!${NC}"
    echo "Certifique-se de estar na pasta correta do projeto."
    echo ""
    exit 1
fi

echo -e "${GREEN}✅ Arquivos do projeto encontrados${NC}"
echo ""

# Tornar o script executável
chmod +x "$0"

# Executar o launcher
echo -e "${YELLOW}🚀 Iniciando ScriptClone...${NC}"
echo ""

$PYTHON_CMD run.py

echo ""
echo "Pressione Enter para fechar..."
read