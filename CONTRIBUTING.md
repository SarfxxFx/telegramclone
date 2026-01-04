# 🤝 Contribuindo para o TelegramCloneHot

Obrigado por considerar contribuir para o TelegramCloneHot! Este documento fornece diretrizes para contribuições.

## 📋 Índice

- [Como Contribuir](#como-contribuir)
- [Reportando Bugs](#reportando-bugs)
- [Sugerindo Melhorias](#sugerindo-melhorias)
- [Desenvolvimento](#desenvolvimento)
- [Padrões de Código](#padrões-de-código)
- [Processo de Pull Request](#processo-de-pull-request)

## 🚀 Como Contribuir

### Tipos de Contribuições

Aceitamos vários tipos de contribuições:

- 🐛 **Correção de bugs**
- ✨ **Novas funcionalidades**
- 📚 **Melhorias na documentação**
- 🎨 **Melhorias na interface**
- ⚡ **Otimizações de performance**
- 🧪 **Testes**

## 🐛 Reportando Bugs

### Antes de Reportar

1. Verifique se o bug já foi reportado nas [Issues](https://github.com/arthurxavieerr/telegramclonehot/issues)
2. Teste com a versão mais recente
3. Verifique se seguiu corretamente o guia de instalação

### Como Reportar

Use o template de bug report e inclua:

- **Descrição clara** do problema
- **Passos para reproduzir** o bug
- **Comportamento esperado** vs **comportamento atual**
- **Ambiente**: SO, versão do Python, versão do projeto
- **Logs relevantes** (sem expor credenciais)
- **Screenshots** se aplicável

## 💡 Sugerindo Melhorias

### Antes de Sugerir

1. Verifique se a sugestão já existe nas Issues
2. Considere se a funcionalidade é útil para a maioria dos usuários
3. Pense em como implementar de forma simples

### Como Sugerir

Use o template de feature request e inclua:

- **Descrição clara** da funcionalidade
- **Justificativa** - por que é útil
- **Exemplos de uso**
- **Possível implementação** (opcional)

## 🛠️ Desenvolvimento

### Configuração do Ambiente

1. **Fork** o repositório
2. **Clone** seu fork:
   ```bash
   git clone https://github.com/SEU_USUARIO/telegramclonehot.git
   cd telegramclonehot
   ```

3. **Instale** as dependências:
   ```bash
   python install.py
   ```

4. **Crie** uma branch para sua feature:
   ```bash
   git checkout -b feature/nome-da-feature
   ```

### Estrutura do Projeto

```
telegramclonehot/
├── Eros_free.py          # Motor principal
├── run.py                # Launcher/Menu
├── config.py             # Configurador
├── install.py            # Instalador
├── requirements.txt      # Dependências
├── README.md             # Documentação principal
├── INICIO_RAPIDO.md      # Guia rápido
├── GUIA_COMPLETO.md      # Tutorial detalhado
└── docs/                 # Documentação adicional
```

### Testando

Antes de submeter:

1. **Teste** sua funcionalidade
2. **Verifique** se não quebrou funcionalidades existentes
3. **Execute** os comandos de diagnóstico:
   ```bash
   python -c "import telethon; print('OK')"
   python run.py  # Teste o menu
   ```

## 📝 Padrões de Código

### Python

- **PEP 8** para estilo de código
- **Type hints** quando possível
- **Docstrings** para funções públicas
- **Nomes descritivos** para variáveis e funções

### Exemplo:

```python
async def download_album_safe(self, album: AlbumInfo) -> bool:
    """
    Baixa um álbum de forma segura com retry automático.
    
    Args:
        album: Informações do álbum a ser baixado
        
    Returns:
        True se sucesso, False caso contrário
        
    Raises:
        TelegramError: Em caso de erro na API
    """
    self.logger.info(f"Iniciando download do álbum {album.grouped_id}")
    # ... implementação
```

### Logs

- Use o logger configurado: `self.logger`
- Níveis apropriados: `INFO`, `WARNING`, `ERROR`
- Mensagens claras e úteis
- **NUNCA** logue credenciais

### Tratamento de Erros

- Use try/except específicos
- Log erros com contexto
- Retry automático quando apropriado
- Falhe graciosamente

## 🔄 Processo de Pull Request

### Antes de Submeter

1. ✅ **Teste** localmente
2. ✅ **Documente** mudanças
3. ✅ **Atualize** CHANGELOG.md se necessário
4. ✅ **Commit** com mensagens claras

### Mensagens de Commit

Use o padrão:
```
tipo(escopo): descrição breve

Descrição mais detalhada se necessário.

Fixes #123
```

**Tipos:**
- `feat`: nova funcionalidade
- `fix`: correção de bug
- `docs`: documentação
- `style`: formatação
- `refactor`: refatoração
- `test`: testes
- `chore`: manutenção

### Exemplo:
```
feat(download): adiciona retry automático para downloads

Implementa sistema de retry com backoff exponencial
para downloads que falham por problemas de rede.

Fixes #45
```

### Submissão

1. **Push** para sua branch
2. **Abra** Pull Request
3. **Descreva** as mudanças
4. **Aguarde** review
5. **Responda** aos comentários

### Template de PR

```markdown
## Descrição
Breve descrição das mudanças.

## Tipo de Mudança
- [ ] Bug fix
- [ ] Nova funcionalidade
- [ ] Breaking change
- [ ] Documentação

## Como Testar
1. Passo 1
2. Passo 2
3. Resultado esperado

## Checklist
- [ ] Código testado localmente
- [ ] Documentação atualizada
- [ ] CHANGELOG.md atualizado
- [ ] Sem credenciais expostas
```

## 🎯 Áreas que Precisam de Ajuda

- 📱 **Interface mobile** - melhorar experiência em dispositivos móveis
- 🌐 **Internacionalização** - tradução para outros idiomas
- 🧪 **Testes automatizados** - criar suite de testes
- 📊 **Métricas** - adicionar estatísticas de transferência
- 🔒 **Segurança** - auditoria de segurança
- 📚 **Documentação** - tutoriais em vídeo

## ❓ Dúvidas

Se tiver dúvidas:

1. Verifique a [documentação](README.md)
2. Procure nas [Issues](https://github.com/arthurxavieerr/telegramclonehot/issues)
3. Abra uma nova Issue com a tag `question`

## 📜 Código de Conduta

- Seja respeitoso e construtivo
- Aceite críticas construtivas
- Foque no que é melhor para a comunidade
- Ajude outros contribuidores

---

**Obrigado por contribuir! 🙏**

Toda contribuição, por menor que seja, é valiosa para o projeto.