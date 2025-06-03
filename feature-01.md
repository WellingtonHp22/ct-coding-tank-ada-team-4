# FEATURE-001: Busca por Conteúdo Exato e Intervalos

## Status: ✅ IMPLEMENTADO

### Objetivos

Implementar sistema de busca eficiente utilizando algoritmo de busca binária para localizar registros por ID exato ou dentro de intervalos específicos em arquivos grandes de texto estruturado.

## Especificações Técnicas

### Estrutura dos Dados

**Formato padrão das linhas:**
```
ID-000123 | Dom Casmurro | Machado de Assis | uma frase aleatória com conteúdo complementar
```

**Características obrigatórias:**
- ✅ Linha fixa de **200 caracteres** (padding com espaços)
- ✅ Registros **ordenados por ID** numericamente
- ✅ IDs **não sequenciais** (ex: 001, 005, 010, 015...)
- ✅ Separador: ` | ` (pipe com espaços)
- ✅ 4 campos: ID, Título, Autor, Descrição

### Funcionalidades Implementadas

#### 1. Busca por ID Exato

**Comando:** `search <ID>`

**Entrada exemplo:**
```bash
kb> search ID-000001
```

**Saída esperada:**
```
id: 000001
----
titulo: Memorias Postumas de Bras Cubas
autor: Machado de Assis
code: Romance inovador narrado por um defunto autor com ironia mordaz
```

**Algoritmo:**
- Busca binária O(log n)
- Acesso direto via seek(index * 200)
- Comparação de IDs numericamente

#### 2. Busca por Intervalo

**Comando:** `range <ID1> <ID2>`

**Entrada exemplo:**
```bash
kb> range ID-000001 ID-000020
```

**Saída esperada:**
```
ids: 000001-000020
----
id: 000001
titulo: Memorias Postumas de Bras Cubas
autor: Machado de Assis
code: Romance inovador narrado por um defunto autor com ironia mordaz
----
id: 000005
titulo: Dom Casmurro
autor: Machado de Assis
code: Romance sobre ciumes e desconfianca narrado por Bento Santiago
----
id: 000010
titulo: O Cortico
autor: Aluisio Azevedo
code: Obra naturalista que retrata a vida em um cortico carioca do seculo XIX
----
id: 000015
titulo: Iracema
autor: Jose de Alencar
code: Romance indianista sobre o amor tragico entre Iracema e Martim
----
id: 000020
titulo: O Guarani
autor: Jose de Alencar
code: Historia epica de amor entre Ceci e Peri no Brasil colonial
```

## Implementação Técnica

### Algoritmo de Busca Binária

```python
def _binary_search_exact(self, filename, target_id):
    total_lines = self._get_total_lines(filename)
    left, right = 0, total_lines - 1
    
    while left <= right:
        mid = (left + right) // 2
        line = self._read_line_at_index(filename, mid)
        current_id = self._extract_id_from_line(line)
        
        if current_id == target_id:
            return line
        elif current_id < target_id:
            left = mid + 1
        else:
            right = mid - 1
    
    return None
```

### Acesso Direto por Seek

```python
def _read_line_at_index(self, filename, index):
    with open(filename, 'r', encoding='utf-8') as f:
        f.seek(index * 200)  # 200 chars por linha
        line = f.read(200).strip()
        return line
```

### Busca por Intervalo

```python
def search_range(self, start_id, end_id):
    # Encontra índice inicial
    start_index = self._binary_search_range_start(filename, start_id)
    # Encontra índice final  
    end_index = self._binary_search_range_end(filename, end_id)
    
    # Percorre intervalo
    for i in range(start_index, end_index + 1):
        line = self._read_line_at_index(filename, i)
        # Processa e exibe linha
```

## Validação e Testes

### Casos de Teste Executados

1. ✅ **Busca Exata Existente**
   - Input: `search ID-000001`
   - Output: Registro de "Memorias Postumas de Bras Cubas" encontrado

2. ✅ **Busca Exata Inexistente**
   - Input: `search ID-999999` 
   - Output: "ID não encontrado"

3. ✅ **Intervalo Válido**
   - Input: `range ID-000001 ID-000020`
   - Output: 5 registros encontrados

4. ✅ **Intervalo Vazio**
   - Input: `range ID-000002 ID-000004`
   - Output: "Nenhum registro encontrado"

5. ✅ **Performance O(log n)**
   - Arquivo com 20 registros: máximo 5 comparações
   - Busca instantânea mesmo em arquivos grandes

### Critérios de Aceitação

- ✅ Busca binária implementada corretamente
- ✅ Acesso direto usando seek() para eficiência
- ✅ Formato de saída exatamente conforme especificação
- ✅ Tratamento adequado de casos de erro
- ✅ Performance O(log n) garantida para busca exata
- ✅ Performance O(log n + k) para busca por intervalo
- ✅ Não carrega arquivo inteiro na memória
- ✅ Suporte a arquivos de qualquer tamanho

## Arquivo de Dados

**Local:** `fictional_books.txt`
**Conteúdo:** 20 obras da literatura brasileira
**Autores:** Machado de Assis, José de Alencar, Aluísio Azevedo, Eça de Queirós
**Formato:** Rigorosamente conforme especificação (200 chars/linha)

## Comandos CLI

```bash
# Busca por ID específico
kb> search ID-000001

# Busca por intervalo
kb> range ID-000001 ID-000050

# Ajuda
kb> help

# Listar fontes
kb> list

# Estatísticas
kb> stats
```

## Performance Garantida

- **Complexidade Temporal:** O(log n) para busca exata
- **Complexidade Espacial:** O(1) - memória constante
- **Escalabilidade:** Funciona com arquivos de qualquer tamanho
- **Throughput:** Centenas de buscas por segundo

## 🚀 Disponível no GitHub

**Repositório:** https://github.com/moroni646/ct-coding-tank-ada-team-4

**Branch principal:** `main`
**Tag da versão:** `v1.0.0-feature-001`
