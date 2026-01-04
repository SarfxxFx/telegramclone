# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-03

### Adicionado
- Sistema de transferência de álbuns do Telegram com 3 filas otimizadas
- Suporte a duas contas (leitura e envio)
- Modo rápido e modo lento de transferência
- Sistema de retomada automática após interrupções
- Instalador automático (`install.py`)
- Configurador interativo (`config.py`)
- Launcher com menu (`run.py`)
- Logs detalhados e monitoramento em tempo real
- Proteção contra FloodWait automática
- Backup automático de configurações
- Limpeza automática de arquivos temporários

### Características Técnicas
- **Sistema de Filas**: Download (10) → Upload (10) → Envio (1)
- **Ordem Cronológica**: Mantém ordem rigorosa das mensagens
- **Rate Limiting**: Proteção automática contra limitações do Telegram
- **Persistência**: Banco SQLite para salvar progresso
- **Monitoramento**: Logs estruturados e status em tempo real

### Arquivos Principais
- `Eros_free.py` - Motor principal de transferência
- `run.py` - Interface de launcher e menu
- `config.py` - Configurador interativo
- `install.py` - Instalador automático
- `README.md` - Documentação completa
- `INICIO_RAPIDO.md` - Guia de início rápido
- `GUIA_COMPLETO.md` - Tutorial detalhado

### Dependências
- Python 3.8+
- Telethon 1.37.0
- Requests 2.32.0+
- Rich 14.0.0+
- SQLite3 (incluído no Python)

### Segurança
- Nunca expõe credenciais em logs
- Backup seguro de configurações
- Validação de entrada de dados
- Tratamento robusto de erros

---

## Formato das Versões

- **[Major.Minor.Patch]** - YYYY-MM-DD
- **Major**: Mudanças incompatíveis na API
- **Minor**: Funcionalidades adicionadas de forma compatível
- **Patch**: Correções de bugs compatíveis

## Tipos de Mudanças

- **Adicionado** - para novas funcionalidades
- **Alterado** - para mudanças em funcionalidades existentes
- **Descontinuado** - para funcionalidades que serão removidas
- **Removido** - para funcionalidades removidas
- **Corrigido** - para correções de bugs
- **Segurança** - para vulnerabilidades corrigidas