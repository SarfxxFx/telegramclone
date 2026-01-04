# 🚀 TelegramCloneHot - Clone de Álbuns do Telegram

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Telethon](https://img.shields.io/badge/Telethon-1.37.0-green.svg)](https://github.com/LonamiWebs/Telethon)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)]()

**TelegramCloneHot** é uma ferramenta Python avançada para transferir álbuns e mensagens de grupos do Telegram de forma automatizada, com sistema de filas otimizado e retomada automática após interrupções.

## ✨ Características Principais

- 🔄 **Sistema de 3 Filas**: Download (10) → Upload (10) → Envio (1) com ordem cronológica rigorosa
- ⚡ **Dois Modos**: Rápido (sem intervalo) e Lento (1 álbum/hora)
- 🔁 **Retomada Automática**: Continue de onde parou após interrupções
- 📱 **Duas Contas**: Uma para leitura e outra para envio
- 🛡️ **Rate Limit**: Proteção automática contra FloodWait
- 📊 **Monitoramento**: Logs detalhados e progresso em tempo real
- 🎯 **Interface Amigável**: Instalação e configuração simplificadas

## 🚀 Instalação Rápida

### 1. Clone o Repositório
```bash
git clone https://github.com/sarfxxfx/telegramclone.git
cd telegramclone
```

### 2. Instalação Automática
```bash
python install.py
```

### 3. Configuração Interativa
```bash
python config.py
```

### 4. Executar
```bash
python run.py
```

## 📋 Pré-requisitos

### Sistema
- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **Conta do Telegram** ativa
- **Acesso aos grupos** de origem e destino

### Credenciais Necessárias
- **API ID e API Hash** - Obtenha em [my.telegram.org](https://my.telegram.org)
- **ID do grupo de origem** - Use @userinfobot no grupo
- **ID do grupo de destino** - Use @userinfobot no grupo
- **Link da primeira mensagem** - Clique direito → Copiar link

## 🛠️ Arquitetura do Sistema

### Componentes Principais

| Arquivo | Função | Descrição |
|---------|--------|-----------|
| `Eros_free.py` | Script Principal | Motor de transferência com sistema de filas |
| `run.py` | Launcher | Interface de menu e gerenciamento |
| `config.py` | Configurador | Assistente interativo de configuração |
| `install.py` | Instalador | Instalação automática de dependências |

### Sistema de Filas

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Download  │───▶│   Upload    │───▶│    Envio    │
│  (10 slots) │    │ (10 slots)  │    │  (1 slot)   │
└─────────────┘    └─────────────┘    └─────────────┘
```

- **Download**: Baixa até 10 álbuns simultaneamente
- **Upload**: Processa até 10 álbuns simultaneamente  
- **Envio**: Envia 1 álbum por vez (ordem cronológica rigorosa)

## 🎮 Modos de Operação

### ⚡ Modo Rápido (Padrão)
- Transfere álbuns sem intervalo
- Ideal para grupos pequenos (< 1000 mensagens)
- Máxima velocidade de transferência

### 🐌 Modo Lento
- 1 álbum a cada 1 hora
- Ideal para grupos grandes (> 1000 mensagens)
- Evita limitações do Telegram

## 📊 Monitoramento e Logs

### Arquivos de Status
```
transfer.log                    # Log detalhado em tempo real
transfer_progress_ErosFree.db   # Banco de dados de progresso
config_backup.json             # Backup das configurações
*.session                      # Sessões do Telegram
```

### Comandos de Monitoramento
```bash
# Ver status completo
python run.py  # Opção 4

# Acompanhar logs em tempo real
tail -f transfer.log           # Linux/Mac
Get-Content transfer.log -Wait # Windows

# Verificar instalação
python -c "import telethon; print('✅ OK')"
```

## 🔧 Solução de Problemas

### Problemas Comuns

| Erro | Solução |
|------|---------|
| `ModuleNotFoundError: telethon` | Execute `python install.py` |
| `Script não configurado` | Execute `python config.py` |
| `FloodWaitError` | Use modo lento ou aguarde automaticamente |
| `Arquivo não encontrado` | Delete `transfer_progress_ErosFree.db` |

### Comandos de Diagnóstico
```bash
# Verificar dependências
python install.py

# Reconfigurar
python config.py

# Limpar arquivos temporários
python run.py  # Opção 5

# Ver logs de erro
python run.py  # Opção 4
```

## 🔒 Segurança e Boas Práticas

### ✅ Recomendações
- Nunca compartilhe API ID/Hash
- Mantenha arquivos `.session` seguros
- Teste com grupos pequenos primeiro
- Use modo lento para grupos grandes
- Faça backup das configurações

### ⚠️ Avisos Importantes
- Use apenas em grupos onde tem permissão
- Respeite direitos autorais
- Siga os Termos de Serviço do Telegram
- Não abuse das APIs do Telegram

## 📚 Documentação Adicional

- [Issues](https://github.com/sarfxxfx/telegramclone/issues) - Suporte e bugs
- [Discussions](https://github.com/sarfxxfx/telegramclone/discussions) - Perguntas e discussões

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🙏 Agradecimentos

- [Telethon](https://github.com/LonamiWebs/Telethon) - Biblioteca Python para Telegram
- Comunidade Python - Pelas ferramentas e bibliotecas
- Contribuidores - Por melhorias e feedback

## 📞 Suporte

- 🐛 **Bugs**: [Abra uma issue](https://github.com/sarfxxfx/telegramclone/issues)
- 💡 **Sugestões**: [Discussions](https://github.com/sarfxxfx/telegramclonehot/discussions)
- 📧 **Contato**: Através das issues do GitHub

---

<div align="center">

**Feito com ❤️ por [Clown](https://github.com/SarfxxFx)**

⭐ Se este projeto te ajudou, considere dar uma estrela!

</div>
