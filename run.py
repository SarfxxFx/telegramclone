#!/usr/bin/env python3
"""
Launcher simplificado para o ScriptClone
Verifica configurações e executa o script principal
"""

import os
import sys
import json
import subprocess
from pathlib import Path

def print_header():
    print("\n" + "="*60)
    print("🚀 SCRIPTCLONE - LAUNCHER")
    print("="*60)

def check_configuration():
    """Verifica se o script está configurado"""
    script_file = "Eros_free.py"
    
    if not os.path.exists(script_file):
        print("❌ Arquivo Eros_free.py não encontrado!")
        return False
    
    try:
        with open(script_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Verificar se ainda tem valores padrão
        if 'READER_API_ID = 12345678' in content:
            print("❌ Script não configurado! API ID ainda está com valor padrão.")
            return False
        
        if 'DIGITE SUA API HASH AQUI' in content:
            print("❌ Script não configurado! API Hash não foi definido.")
            return False
        
        if 'LINK DA PRIMEIRA MENSAGEM DO GRUPO AQUI' in content:
            print("❌ Script não configurado! Link da primeira mensagem não foi definido.")
            return False
        
        print("✅ Script parece estar configurado.")
        return True
        
    except Exception as e:
        print(f"❌ Erro verificando configuração: {e}")
        return False

def check_dependencies():
    """Verifica se as dependências estão instaladas"""
    print("🔍 Verificando dependências...")
    
    try:
        import telethon
        print(f"✅ Telethon {telethon.__version__} instalado")
        return True
    except ImportError:
        print("❌ Telethon não instalado!")
        return False

def show_menu():
    """Mostra menu de opções"""
    print("\n📋 OPÇÕES DISPONÍVEIS:")
    print("1. 🚀 Executar transferência")
    print("2. ⚙️  Configurar script")
    print("3. 📦 Instalar dependências")
    print("4. 📊 Ver status/logs")
    print("5. 🧹 Limpar arquivos temporários")
    print("6. ❌ Sair")
    
    while True:
        choice = input("\nEscolha uma opção (1-6): ").strip()
        if choice in ['1', '2', '3', '4', '5', '6']:
            return choice
        print("❌ Opção inválida! Digite um número de 1 a 6.")

def run_script():
    """Executa o script principal"""
    print("\n🚀 Iniciando transferência...")
    print("="*60)
    print("⚠️  IMPORTANTE:")
    print("• Mantenha esta janela aberta")
    print("• Não desligue o computador")
    print("• Para parar, pressione Ctrl+C")
    print("="*60 + "\n")
    
    try:
        subprocess.run([sys.executable, "Eros_free.py"], check=True)
        print("\n✅ Transferência concluída!")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Erro durante execução: {e}")
    except KeyboardInterrupt:
        print("\n⚠️  Transferência interrompida pelo usuário.")
        print("O progresso foi salvo e pode ser retomado posteriormente.")

def run_configurator():
    """Executa o configurador"""
    if not os.path.exists("config.py"):
        print("❌ Configurador não encontrado!")
        return
    
    try:
        subprocess.run([sys.executable, "config.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro no configurador: {e}")
    except KeyboardInterrupt:
        print("\n⚠️  Configuração cancelada.")

def install_dependencies():
    """Executa o instalador"""
    if not os.path.exists("install.py"):
        print("❌ Instalador não encontrado!")
        return
    
    try:
        subprocess.run([sys.executable, "install.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro no instalador: {e}")
    except KeyboardInterrupt:
        print("\n⚠️  Instalação cancelada.")

def show_status():
    """Mostra status e logs"""
    print("\n📊 STATUS DO SISTEMA")
    print("="*60)
    
    # Verificar arquivos importantes
    files_to_check = [
        ("Eros_free.py", "Script principal"),
        ("config.py", "Configurador"),
        ("install.py", "Instalador"),
        ("transfer_progress_ErosFree.db", "Banco de progresso"),
        ("transfer.log", "Log de execução"),
        ("config_backup.json", "Backup de configuração")
    ]
    
    print("\n📁 ARQUIVOS:")
    for file, description in files_to_check:
        if os.path.exists(file):
            size = os.path.getsize(file)
            print(f"✅ {file} ({description}) - {size} bytes")
        else:
            print(f"❌ {file} ({description}) - Não encontrado")
    
    # Mostrar últimas linhas do log se existir
    log_file = "transfer.log"
    if os.path.exists(log_file):
        print(f"\n📄 ÚLTIMAS LINHAS DO LOG:")
        print("-" * 40)
        try:
            with open(log_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines[-10:]:  # Últimas 10 linhas
                    print(line.rstrip())
        except Exception as e:
            print(f"Erro lendo log: {e}")
        print("-" * 40)
    
    # Verificar progresso se existir
    db_file = "transfer_progress_ErosFree.db"
    if os.path.exists(db_file):
        print(f"\n💾 BANCO DE DADOS: {db_file} existe ({os.path.getsize(db_file)} bytes)")
    else:
        print("\n💾 BANCO DE DADOS: Nenhum progresso salvo ainda")

def cleanup_temp_files():
    """Limpa arquivos temporários"""
    print("\n🧹 LIMPEZA DE ARQUIVOS TEMPORÁRIOS")
    print("="*60)
    
    temp_dirs = ["temp_mediaErosFree", "temp_media"]
    temp_files = ["*.tmp", "*.temp"]
    
    cleaned = 0
    
    # Limpar diretórios temporários
    for temp_dir in temp_dirs:
        if os.path.exists(temp_dir):
            try:
                import shutil
                shutil.rmtree(temp_dir)
                print(f"✅ Removido diretório: {temp_dir}")
                cleaned += 1
            except Exception as e:
                print(f"❌ Erro removendo {temp_dir}: {e}")
    
    # Limpar arquivos de sessão órfãos (opcional)
    session_files = [f for f in os.listdir('.') if f.endswith('.session')]
    if session_files:
        print(f"\n📱 Encontrados {len(session_files)} arquivos de sessão:")
        for session in session_files:
            print(f"   • {session}")
        
        choice = input("\n❓ Deseja remover arquivos de sessão? (s/n): ").strip().lower()
        if choice in ['s', 'sim', 'y', 'yes']:
            for session in session_files:
                try:
                    os.remove(session)
                    print(f"✅ Removido: {session}")
                    cleaned += 1
                except Exception as e:
                    print(f"❌ Erro removendo {session}: {e}")
    
    if cleaned == 0:
        print("✅ Nenhum arquivo temporário encontrado.")
    else:
        print(f"\n✅ Limpeza concluída! {cleaned} itens removidos.")

def main():
    """Função principal do launcher"""
    print_header()
    
    while True:
        choice = show_menu()
        
        if choice == '1':  # Executar transferência
            if not check_dependencies():
                print("\n❌ Dependências não instaladas. Execute a opção 3 primeiro.")
                continue
            
            if not check_configuration():
                print("\n❌ Script não configurado. Execute a opção 2 primeiro.")
                continue
            
            run_script()
        
        elif choice == '2':  # Configurar
            run_configurator()
        
        elif choice == '3':  # Instalar dependências
            install_dependencies()
        
        elif choice == '4':  # Ver status
            show_status()
        
        elif choice == '5':  # Limpar temporários
            cleanup_temp_files()
        
        elif choice == '6':  # Sair
            print("\n👋 Até logo!")
            break
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Saindo...")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        sys.exit(1)