# Knowledge Base CLI - Sistema de Busca Inteligente

## Visão Geral

O Knowledge Base CLI é um sistema avançado de busca e gerenciamento de bases de conhecimento, projetado para lidar eficientemente com grandes volumes de dados textuais estruturados.

## Características Principais

### 🔍 Busca Binária Otimizada
- Complexidade O(log n) para buscas em arquivos grandes
- Acesso direto usando seek() para máxima performance
- Suporte a linhas de tamanho fixo (200 caracteres)

### 📊 Dados Estruturados
- Formato padronizado: `ID-XXXXXX | Título | Autor | Descrição`
- IDs ordenados mas não sequenciais
- Busca por ID exato ou intervalo de IDs

### 📚 Biblioteca Digital
- Acervo de literatura brasileira clássica
- Obras de Machado de Assis, José de Alencar, Aluísio Azevedo
- Metadados completos para cada obra

## Funcionalidades Implementadas

### FEATURE-001: Busca por Conteúdo Exato e Intervalos
- **Busca por ID Exato**: Localiza registro específico pelo identificador
- **Busca por Intervalo**: Retorna todos os registros dentro de um range
- **Performance Garantida**: Usa busca binária em todas as operações
- **Formato Padronizado**: Saída estruturada e consistente

## Arquitetura Técnica

```
┌─────────────────────────────────────┐
│           CLI Interface             │
├─────────────────────────────────────┤
│        Knowledge Base Core          │
│  ┌─────────────┬─────────────────┐  │
│  │ Binary      │ File Management │  │
│  │ Search      │ & Indexing      │  │
│  └─────────────┴─────────────────┘  │
├─────────────────────────────────────┤
│        Structured Data Files        │
│    (fictional_books.txt + books/)   │
└─────────────────────────────────────┘
```

## Casos de Uso

1. **Pesquisa Acadêmica**: Localização rápida de obras literárias
2. **Análise Literária**: Comparação entre autores e períodos
3. **Catalogação**: Gerenciamento de acervos bibliográficos
4. **Educação**: Ferramenta didática para estudo de literatura

## 🚀 Deploy e Colaboração

### Opções de Repositório

**Repositório Principal (requer permissão):**
```
https://github.com/moroni646/ct-coding-tank-ada-team-4
```

**Alternativas para Deploy:**

1. **Fork do Repositório**: Criar fork para sua conta
2. **Novo Repositório**: Criar repositório próprio
3. **Colaboração**: Solicitar acesso como colaborador
4. **Bundle Git**: Criar arquivo bundle para transferência

### Scripts Disponíveis

- `deploy_github.py` - Deploy automático (requer permissão)
- `setup_git.py` - Configuração inicial do repositório
- `create_fork.py` - Criar fork ou novo repositório
- `bundle_project.py` - Gerar bundle para transferência

## Próximos Passos

- ✅ FEATURE-001: Busca binária implementada
- 🚧 FEATURE-002: Indexação de texto completo
- 📋 FEATURE-003: Interface web para acesso remoto
- 🔄 FEATURE-004: Sincronização multi-arquivo

## Começando

Execute o sistema com:
```bash
python cli.py
```

Comandos disponíveis:
- `search ID-000001` - Busca por ID específico
- `range ID-000001 ID-000050` - Busca por intervalo
- `help` - Ajuda completa