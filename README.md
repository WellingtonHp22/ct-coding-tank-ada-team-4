# Knowledge Base CLI - Sistema de Busca Inteligente

## 🎯 Visão Geral

Sistema avançado de busca e gerenciamento de bases de conhecimento com algoritmos de busca binária otimizada.

## ⚡ Características Principais

- **Busca Binária O(log n)**: Performance otimizada para arquivos grandes
- **Dados Estruturados**: Formato padronizado com IDs ordenados
- **CLI Intuitiva**: Interface de linha de comando fácil de usar
- **Literatura Brasileira**: Acervo com clássicos da literatura nacional

## 🚀 Quick Start

```bash
# Clone o repositório
git clone https://github.com/moroni646/ct-coding-tank-ada-team-4
cd ct-coding-tank-ada-team-4

# Execute o sistema
python cli.py

# Comandos básicos
kb> search ID-000001
kb> range ID-000001 ID-000020
kb> help
```

## 📚 Funcionalidades

### FEATURE-001: Busca por Conteúdo Exato e Intervalos ✅

- Busca por ID exato: `search ID-000001`
- Busca por intervalo: `range ID-000001 ID-000020`
- Performance garantida O(log n)
- Suporte a arquivos de qualquer tamanho

### FEATURE-002: Indexação de Texto Completo 🚧

- Busca em texto completo nos livros
- Índices otimizados para performance
- Suporte a múltiplos formatos

### FEATURE-003: Interface Web 📋

- API RESTful completa
- Interface responsiva
- Dashboard analytics
- Sistema de recomendações

## 🛠️ Tecnologias

- **Python 3.8+**: Linguagem principal
- **Algoritmos**: Busca binária, indexação
- **CLI**: Interface de linha de comando
- **Git**: Controle de versão

## 📁 Estrutura do Projeto

```
ct-coding-tank-ada-team-4/
├── cli.py                  # Interface principal
├── knowledge_base.py       # Engine de busca
├── fictional_books.txt     # Dados estruturados
├── books/                  # Biblioteca de livros
├── docs/                   # Documentação
├── tests/                  # Testes automatizados
└── README.md              # Este arquivo
```

## 🧪 Testes

```bash
# Executa testes básicos
python -m pytest tests/

# Teste manual das funcionalidades
python cli.py
```

## 📊 Performance

- **Complexidade**: O(log n) para busca exata
- **Memória**: O(1) - não carrega arquivo inteiro
- **Escalabilidade**: Suporte a arquivos de GB
- **Throughput**: Centenas de buscas/segundo

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📝 Changelog

### v1.0.0 - 2025-06-03
- ✅ Implementação da busca binária
- ✅ Interface CLI completa
- ✅ Acervo de literatura brasileira
- ✅ Documentação completa
- ✅ Scripts de deploy automatizado

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👥 Equipe

- **Desenvolvimento**: Ada Coding Tank Team 4
- **Repositório**: https://github.com/moroni646/ct-coding-tank-ada-team-4
- **Documentação**: [Ver docs/](docs/)

## 📞 Suporte

- **Issues**: [GitHub Issues](https://github.com/moroni646/ct-coding-tank-ada-team-4/issues)
- **Documentação**: [Wiki](https://github.com/moroni646/ct-coding-tank-ada-team-4/wiki)
- **Email**: team4@codingtak.ada.tech

---

⭐ Se este projeto te ajudou, considere dar uma estrela no GitHub!
