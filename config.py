#!/usr/bin/env python3
"""
Configurador interativo para o ScriptClone
Facilita a configuração das credenciais e IDs necessários
"""

import os
import re
import json
from pathlib import Path

def print_header():
    print("\n" + "="*60)
    print("⚙️  CONFIGURADOR INTERATIVO - SCRIPTCLONE")
    print("="*60)
    print("Este assistente irá ajudá-lo a configurar:")
    print("• API ID e API Hash do Telegram")
    print("• IDs dos grupos de origem e destino")
    print("• Link da primeira mensagem")
    print("• Modo de transferência")
    print("="*60 + "\n")

def get_telegram_credentials():
    """Coleta as credenciais do Telegram API"""
    print("🔑 CONFIGURAÇÃO DAS CREDENCIAIS DO TELEGRAM")
    print("-" * 50)
    print("Para obter suas credenciais:")
    print("1. Acesse: https://my.telegram.org")
    print("2. Faça login com seu número de telefone")
    print("3. Vá em 'API Development Tools'")
    print("4. Crie um novo app se necessário")
    print("5. Copie o API ID e API Hash")
    print("-" * 50)
    
    while True:
        try:
            api_id = input("\n📱 Digite seu API ID: ").strip()
            if not api_id.isdigit():
                print("❌ API ID deve conter apenas números!")
                continue
            api_id = int(api_id)
            break
        except ValueError:
            print("❌ API ID inválido!")
    
    while True:
        api_hash = input("🔐 Digite seu API Hash: ").strip()
        if len(api_hash) < 10:
            print("❌ API Hash muito curto! Verifique se copiou corretamente.")
            continue
        break
    
    return api_id, api_hash

def get_chat_ids():
    """Coleta os IDs dos grupos"""
    print("\n🏠 CONFIGURAÇÃO DOS GRUPOS")
    print("-" * 50)
    print("Para obter o ID de um grupo:")
    print("1. Adicione o bot @userinfobot ao grupo")
    print("2. Digite /id no grupo")
    print("3. Copie o ID que aparece (incluindo o sinal de menos)")
    print("-" * 50)
    
    while True:
        source_id = input("\n📥 ID do grupo de ORIGEM (que será clonado): ").strip()
        if not source_id.startswith('-'):
            print("❌ ID do grupo deve começar com '-' (ex: -1001234567890)")
            continue
        try:
            int(source_id)
            break
        except ValueError:
            print("❌ ID inválido! Use apenas números após o '-'")
    
    while True:
        target_id = input("📤 ID do grupo de DESTINO (que receberá as mensagens): ").strip()
        if not target_id.startswith('-'):
            print("❌ ID do grupo deve começar com '-' (ex: -1001234567890)")
            continue
        try:
            int(target_id)
            break
        except ValueError:
            print("❌ ID inválido! Use apenas números após o '-'")
    
    return int(source_id), int(target_id)

def get_first_message_link():
    """Coleta o link da primeira mensagem"""
    print("\n🔗 CONFIGURAÇÃO DA PRIMEIRA MENSAGEM")
    print("-" * 50)
    print("Para obter o link da primeira mensagem:")
    print("1. Vá até a primeira mensagem que deseja clonar")
    print("2. Clique com botão direito na mensagem")
    print("3. Selecione 'Copiar link da mensagem'")
    print("4. Cole o link aqui")
    print("-" * 50)
    
    while True:
        link = input("\n🔗 Cole o link da primeira mensagem: ").strip()
        if not link.startswith('https://t.me/'):
            print("❌ Link deve começar com 'https://t.me/'")
            continue
        if '/c/' not in link and '/s/' not in link:
            print("❌ Link parece inválido. Certifique-se de copiar o link correto.")
            continue
        break
    
    return link

def choose_transfer_mode():
    """Escolhe o modo de transferência"""
    print("\n⚡ MODO DE TRANSFERÊNCIA")
    print("-" * 50)
    print("1. MODO RÁPIDO - Transfere sem intervalo (recomendado para grupos pequenos)")
    print("2. MODO LENTO - 1 álbum por hora (recomendado para evitar limitações)")
    print("-" * 50)
    
    while True:
        choice = input("\nEscolha o modo (1 ou 2): ").strip()
        if choice == "1":
            return False  # slow_mode = False
        elif choice == "2":
            return True   # slow_mode = True
        else:
            print("❌ Opção inválida! Digite 1 ou 2.")

def backup_original_file():
    """Cria backup do arquivo original"""
    original_file = "Eros_free.py"
    backup_file = "Eros_free.py.backup"
    
    if os.path.exists(original_file) and not os.path.exists(backup_file):
        try:
            with open(original_file, 'r', encoding='utf-8') as f:
                content = f.read()
            with open(backup_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Backup criado: {backup_file}")
            return True
        except Exception as e:
            print(f"❌ Erro criando backup: {e}")
            return False
    return True

def update_script_file(api_id, api_hash, source_id, target_id, first_message_link, slow_mode):
    """Atualiza o arquivo do script com as configurações"""
    script_file = "Eros_free.py"
    
    try:
        with open(script_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Atualizar credenciais
        content = re.sub(
            r'READER_API_ID = \d+',
            f'READER_API_ID = {api_id}',
            content
        )
        content = re.sub(
            r'READER_API_HASH = "[^"]*"',
            f'READER_API_HASH = "{api_hash}"',
            content
        )
        content = re.sub(
            r'SENDER_API_ID = \d+',
            f'SENDER_API_ID = {api_id}',
            content
        )
        content = re.sub(
            r'SENDER_API_HASH = "[^"]*"',
            f'SENDER_API_HASH = "{api_hash}"',
            content
        )
        
        # Atualizar IDs dos grupos
        content = re.sub(
            r'SOURCE_CHAT_ID = -?\d+',
            f'SOURCE_CHAT_ID = {source_id}',
            content
        )
        content = re.sub(
            r'TARGET_CHAT_ID = -?\d+',
            f'TARGET_CHAT_ID = {target_id}',
            content
        )
        
        # Atualizar link da primeira mensagem
        content = re.sub(
            r'first_message_link = "[^"]*"',
            f'first_message_link = "{first_message_link}"',
            content
        )
        
        # Salvar arquivo atualizado
        with open(script_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Arquivo {script_file} atualizado com sucesso!")
        return True
        
    except Exception as e:
        print(f"❌ Erro atualizando arquivo: {e}")
        return False

def save_config_json(api_id, api_hash, source_id, target_id, first_message_link, slow_mode):
    """Salva configuração em arquivo JSON para backup"""
    config = {
        "api_id": api_id,
        "api_hash": api_hash,
        "source_chat_id": source_id,
        "target_chat_id": target_id,
        "first_message_link": first_message_link,
        "slow_mode": slow_mode,
        "configured_at": str(Path().resolve()),
    }
    
    try:
        with open("config_backup.json", 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        print("✅ Configuração salva em config_backup.json")
        return True
    except Exception as e:
        print(f"❌ Erro salvando configuração: {e}")
        return False

def show_summary(api_id, api_hash, source_id, target_id, first_message_link, slow_mode):
    """Mostra resumo das configurações"""
    print("\n" + "="*60)
    print("📋 RESUMO DAS CONFIGURAÇÕES")
    print("="*60)
    print(f"API ID: {api_id}")
    print(f"API Hash: {api_hash[:8]}...{api_hash[-4:]}")  # Mascarar parcialmente
    print(f"Grupo de origem: {source_id}")
    print(f"Grupo de destino: {target_id}")
    print(f"Primeira mensagem: {first_message_link}")
    print(f"Modo: {'LENTO (1h entre envios)' if slow_mode else 'RÁPIDO (sem intervalo)'}")
    print("="*60)
    
    confirm = input("\n✅ Confirma essas configurações? (s/n): ").strip().lower()
    return confirm in ['s', 'sim', 'y', 'yes']

def show_final_instructions():
    """Mostra instruções finais"""
    print("\n" + "="*60)
    print("🎉 CONFIGURAÇÃO CONCLUÍDA!")
    print("="*60)
    print("\n📋 PRÓXIMOS PASSOS:")
    print("\n1. Para iniciar a transferência:")
    print("   python Eros_free.py")
    
    print("\n2. Arquivos importantes:")
    print("   • Eros_free.py - Script configurado")
    print("   • Eros_free.py.backup - Backup do original")
    print("   • config_backup.json - Backup das configurações")
    print("   • transfer_progress_ErosFree.db - Progresso (criado automaticamente)")
    print("   • transfer.log - Log de execução")
    
    print("\n3. Dicas importantes:")
    print("   • Mantenha o computador ligado durante a transferência")
    print("   • Não feche o terminal enquanto o script estiver rodando")
    print("   • Se interromper, pode retomar de onde parou")
    print("   • Verifique o arquivo transfer.log em caso de erros")
    
    print("\n⚠️  SEGURANÇA:")
    print("   • NUNCA compartilhe seu API ID e API Hash!")
    print("   • Mantenha os arquivos .session em segurança")
    
    print("="*60 + "\n")

def main():
    """Função principal do configurador"""
    print_header()
    
    # Verificar se o arquivo principal existe
    if not os.path.exists("Eros_free.py"):
        print("❌ Arquivo Eros_free.py não encontrado!")
        print("Certifique-se de estar na pasta correta do projeto.")
        return False
    
    try:
        # Coletar informações
        api_id, api_hash = get_telegram_credentials()
        source_id, target_id = get_chat_ids()
        first_message_link = get_first_message_link()
        slow_mode = choose_transfer_mode()
        
        # Mostrar resumo e confirmar
        if not show_summary(api_id, api_hash, source_id, target_id, first_message_link, slow_mode):
            print("\n❌ Configuração cancelada.")
            return False
        
        # Criar backup
        if not backup_original_file():
            print("\n⚠️  Continuando sem backup...")
        
        # Atualizar arquivo
        if not update_script_file(api_id, api_hash, source_id, target_id, first_message_link, slow_mode):
            print("\n❌ Erro atualizando arquivo. Configuração cancelada.")
            return False
        
        # Salvar backup da configuração
        save_config_json(api_id, api_hash, source_id, target_id, first_message_link, slow_mode)
        
        # Mostrar instruções finais
        show_final_instructions()
        
        return True
        
    except KeyboardInterrupt:
        print("\n\n❌ Configuração cancelada pelo usuário.")
        return False
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        return False

if __name__ == "__main__":
    try:
        success = main()
        if not success:
            exit(1)
    except Exception as e:
        print(f"❌ Erro fatal: {e}")
        exit(1)