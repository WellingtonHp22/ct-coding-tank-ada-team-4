# Knowledge Base CLI - Team 4

Sistema de gerenciamento de base de conhecimento desenvolvido para o Coding Tank ADA.

## 📋 Descrição

Este projeto implementa uma aplicação CLI para gerenciar uma base de conhecimento composta por múltiplos arquivos. O sistema oferece duas funcionalidades principais:

- **FEATURE-001**: Busca eficiente por ID usando busca binária
- **FEATURE-003**: Busca de texto em múltiplos livros usando estrutura Trie

## 🚀 Funcionalidades

### Feature 001 - Busca por ID
- Busca por ID exato em arquivo de livros ficcionais
- Busca por intervalo de IDs
- Implementação usando busca binária para eficiência O(log n)
- Suporte a arquivos grandes sem carregar tudo na memória

### Feature 003 - Busca de Texto
- Busca de frases em múltiplos arquivos de livros
- Suporte a caracteres curinga ('.')
- Busca pode atravessar até 2 linhas consecutivas
- Implementação usando estrutura de dados Trie para otimização
- Normalização automática de texto (remove acentos, pontuação)

## 📁 Estrutura do Projeto

```
Knowledge-Base-CLI/
├── knowledge_base_cli.py      # Sistema principal
├── test_knowledge_base.py     # Testes automatizados
├── README.md                  # Este arquivo
├── requirements.txt           # Dependências Python
├── info/
│   └── fictional_books.txt    # Base de dados de livros (Feature 001)
└── books/                     # Diretório com arquivos de texto (Feature 003)
    ├── 01_book_*.txt
    ├── 02_book_*.txt
    └── ...
```

## 🛠️ Instalação e Execução

### Pré-requisitos
- Python 3.7 ou superior
- Sistema operacional: Windows, Linux ou macOS

### Instalação
1. Clone ou baixe o repositório
2. Navegue até o diretório do projeto
3. Execute o sistema:

```bash
python knowledge_base_cli.py
```

### Execução com Argumentos
```bash
# Busca direta por ID
python knowledge_base_cli.py --feature 001 --id ID-000123

# Busca direta por frase
python knowledge_base_cli.py --feature 003 --phrase "o amor"
```

## 📖 Guia de Uso

### Menu Principal
Ao executar o sistema, você verá o menu principal com as seguintes opções:

```
=== MENU PRINCIPAL ===
1. Feature 001 - Busca por ID
2. Feature 003 - Busca de Texto
3. Sair
```

### Feature 001 - Busca por ID

#### Busca por ID Exato
1. Selecione a opção 1 no menu principal
2. Escolha "Buscar ID exato"
3. Digite o ID no formato `ID-XXXXXX`
4. O sistema retornará:

```
id: 000123
----
titulo: Dom Casmurro
autor: Machado de Assis
code: Romance classico brasileiro
```

#### Busca por Intervalo
1. Selecione a opção 1 no menu principal
2. Escolha "Buscar intervalo de IDs"
3. Digite o ID inicial e final
4. O sistema retornará todos os livros no intervalo

### Feature 003 - Busca de Texto

1. Selecione a opção 2 no menu principal
2. Digite a frase para buscar
3. Use '.' como caractere curinga para qualquer caractere
4. O sistema retornará:

```
frase: "o amor"
----
arquivo: 01_book_test.txt
linha: 2-2
----
arquivo: 03_book_example.txt
linha: 15-16
```

## 🧪 Execução de Testes

Para executar os testes automatizados:

```bash
python test_knowledge_base.py
```

Os testes cobrem:
- ✅ Funcionalidade da estrutura Trie
- ✅ Busca binária por ID
- ✅ Busca por intervalo de IDs
- ✅ Busca de texto em arquivos
- ✅ Normalização de texto
- ✅ Suporte a caracteres curinga
- ✅ Integração entre componentes

## 🏗️ Arquitetura Técnica

### Classe KnowledgeBaseCLI
**Responsabilidade**: Classe principal que coordena todas as funcionalidades

**Métodos principais**:
- `binary_search_id()`: Implementa busca binária por ID
- `search_id_range()`: Busca por intervalo usando busca binária
- `search_text_in_books()`: Coordena busca de texto usando Trie
- `normalize_text()`: Normaliza texto removendo acentos e pontuação

### Classe Trie
**Responsabilidade**: Estrutura de dados para busca eficiente de palavras

**Características**:
- Inserção O(m) onde m é o tamanho da palavra
- Busca O(m) onde m é o tamanho da palavra
- Suporte a prefixos para otimização

### Algoritmos Utilizados

#### Busca Binária (Feature 001)
- **Complexidade**: O(log n)
- **Vantagem**: Eficiente para arquivos grandes ordenados
- **Implementação**: Usa `seek()` para acesso direto às linhas

#### Trie + Pattern Matching (Feature 003)
- **Complexidade**: O(m) para busca, onde m é o tamanho da frase
- **Vantagem**: Busca rápida de padrões complexos
- **Suporte**: Caracteres curinga e busca entre linhas

## 📝 Formato dos Dados

### Arquivo fictional_books.txt (Feature 001)
```
ID-XXXXXX | Título do Livro | Nome do Autor | Descrição complementar...
```
- Cada linha tem exatamente 200 caracteres
- IDs são ordenados numericamente
- Separador: ` | ` (espaço, pipe, espaço)

### Arquivos de Livros (Feature 003)
- Arquivos .txt na pasta `books/`
- Máximo 200 caracteres por linha
- Encoding UTF-8
- Separação por `\n`

## 🔧 Configurações

### Parâmetros Configuráveis
```python
# Em knowledge_base_cli.py
self.books_dir = "books"                    # Diretório dos livros
self.fictional_books_file = "info/fictional_books.txt"  # Arquivo de IDs
self.line_size = 200                        # Tamanho fixo das linhas
```

## 🎯 Exemplos de Uso

### Exemplo 1: Busca por ID Específico
```python
# Via código
kb_cli = KnowledgeBaseCLI()
result = kb_cli.binary_search_id("info/fictional_books.txt", "ID-000123")
```

### Exemplo 2: Busca de Texto com Curinga
```python
# Busca "am.r" encontrará "amor"
results = kb_cli.search_text_in_books("am.r")
```

### Exemplo 3: Busca por Intervalo
```python
results = kb_cli.search_id_range("info/fictional_books.txt", "ID-000100", "ID-000200")
```

## 🐛 Tratamento de Erros

O sistema trata os seguintes cenários:
- ❌ Arquivo não encontrado
- ❌ ID inexistente
- ❌ Formato de linha inválido
- ❌ Erro de encoding
- ❌ Frase não encontrada

## 📊 Performance

### Feature 001 (Busca Binária)
- **Arquivo 1MB**: ~10 comparações
- **Arquivo 100MB**: ~27 comparações
- **Arquivo 1GB**: ~30 comparações

### Feature 003 (Busca com Trie)
- **Indexação**: O(n) onde n é o número de palavras
- **Busca**: O(m) onde m é o tamanho da frase
- **Memória**: Eficiente, processa apenas 2 linhas por vez

## 👥 Equipe

**Team 4 - Coding Tank ADA**
- Desenvolvido para avaliação do curso
- Implementação das Features 001 e 003
- Testes automatizados incluídos

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais no âmbito do Coding Tank ADA.

---

**Nota**: Este sistema foi desenvolvido seguindo os requisitos específicos do desafio, priorizando clareza, eficiência e facilidade de manutenção.
