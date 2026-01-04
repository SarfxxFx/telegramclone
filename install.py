#!/usr/bin/env python3
"""
Instalador automático para o ScriptClone
Facilita a instalação de dependências e configuração inicial
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def print_header():
    print("\n" + "="*60)
    print("🚀 INSTALADOR AUTOMÁTICO - SCRIPTCLONE")
    print("="*60)
    print("Este script irá:")
    print("• Verificar se o Python está instalado")
    print("• Instalar as dependências necessárias")
    print("• Criar estrutura de pastas")
    print("• Preparar o ambiente para uso")
    print("="*60 + "\n")

def check_python():
    """Verifica se o Python está instalado e a versão"""
    print("🔍 Verificando instalação do Python...")
    
    try:
        version = sys.version_info
        if version.major == 3 and version.minor >= 8:
            print(f"✅ Python {version.major}.{version.minor}.{version.micro} encontrado")
            return True
        else:
            print(f"❌ Python {version.major}.{version.minor} encontrado, mas é necessário Python 3.8+")
            return False
    except Exception as e:
        print(f"❌ Erro verificando Python: {e}")
        return False

def install_dependencies():
    """Instala as dependências do projeto"""
    print("\n📦 Instalando dependências...")
    
    try:
        # Tentar instalar via requirements.txt primeiro
        if os.path.exists("requirements.txt"):
            print("Instalando via requirements.txt...")
            result = subprocess.run([
                sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ Dependências instaladas com sucesso!")
                return True
            else:
                print(f"❌ Erro instalando via requirements.txt: {result.stderr}")
        
        # Fallback: instalar dependências essenciais manualmente
        print("Instalando dependências essenciais...")
        essential_packages = [
            "telethon==1.37.0",
            "requests>=2.32.0",
            "rich>=14.0.0"
        ]
        
        for package in essential_packages:
            print(f"Instalando {package}...")
            result = subprocess.run([
                sys.executable, "-m", "pip", "install", package
            ], capture_output=True, text=True)
            
            if result.returncode != 0:
                print(f"❌ Erro instalando {package}: {result.stderr}")
                return False
        
        print("✅ Dependências essenciais instaladas!")
        return True
        
    except Exception as e:
        print(f"❌ Erro durante instalação: {e}")
        return False

def create_directories():
    """Cria diretórios necessários"""
    print("\n📁 Criando estrutura de pastas...")
    
    directories = [
        "temp_mediaErosFree",
        "logs",
        "backups"
    ]
    
    for directory in directories:
        try:
            Path(directory).mkdir(exist_ok=True)
            print(f"✅ Pasta criada: {directory}")
        except Exception as e:
            print(f"❌ Erro criando pasta {directory}: {e}")
            return False
    
    return True

def check_files():
    """Verifica se os arquivos necessários existem"""
    print("\n📄 Verificando arquivos do projeto...")
    
    required_files = [
        "Eros_free.py",
        "requirements.txt"
    ]
    
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ Encontrado: {file}")
        else:
            print(f"❌ Faltando: {file}")
            missing_files.append(file)
    
    if missing_files:
        print(f"\n❌ Arquivos faltando: {', '.join(missing_files)}")
        print("Certifique-se de que todos os arquivos do projeto estão na pasta atual.")
        return False
    
    return True

def show_next_steps():
    """Mostra os próximos passos após a instalação"""
    print("\n" + "="*60)
    print("🎉 INSTALAÇÃO CONCLUÍDA COM SUCESSO!")
    print("="*60)
    print("\n📋 PRÓXIMOS PASSOS:")
    print("\n1. Configure suas credenciais do Telegram:")
    print("   • Execute: python config.py")
    print("   • Ou edite manualmente o arquivo Eros_free.py")
    
    print("\n2. Para usar o script:")
    print("   • Execute: python Eros_free.py")
    
    print("\n3. Arquivos importantes:")
    print("   • Eros_free.py - Script principal")
    print("   • config.py - Configurador interativo")
    print("   • transfer_progress_ErosFree.db - Progresso salvo")
    print("   • transfer.log - Log de execução")
    
    print("\n📚 Para mais informações, consulte o README.md")
    print("="*60 + "\n")

def main():
    """Função principal do instalador"""
    print_header()
    
    # Verificar Python
    if not check_python():
        print("\n❌ Instalação abortada. Instale Python 3.8+ e tente novamente.")
        print("Download: https://www.python.org/downloads/")
        return False
    
    # Verificar arquivos
    if not check_files():
        print("\n❌ Instalação abortada. Arquivos necessários não encontrados.")
        return False
    
    # Instalar dependências
    if not install_dependencies():
        print("\n❌ Instalação abortada. Erro instalando dependências.")
        return False
    
    # Criar diretórios
    if not create_directories():
        print("\n❌ Instalação abortada. Erro criando diretórios.")
        return False
    
    # Mostrar próximos passos
    show_next_steps()
    return True

if __name__ == "__main__":
    try:
        success = main()
        if not success:
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n❌ Instalação cancelada pelo usuário.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        sys.exit(1)