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

## 🚀 Deploy no GitHub

### Repositório Oficial
```
https://github.com/moroni646/ct-coding-tank-ada-team-4
```

### Scripts de Deploy
- `deploy_github.py` - Upload automático para GitHub
- `setup_git.py` - Configuração inicial do repositório
- `requirements.txt` - Dependências do projeto

### Como fazer deploy:
```bash
# 1. Configurar repositório
python setup_git.py

# 2. Upload para GitHub
python deploy_github.py

# 3. Ou usar comandos Git tradicionais
git add .
git commit -m "Knowledge Base CLI - Sistema completo"
git push origin main
```