### Desafio - Knowledge Base CLI

Sua equipe foi incumbida de criar uma aplicação para gerenciar uma base de conhecimento (Knowledge Base).
Esta base de conhecimento é composta por múltiplos arquivos dispostos numa pasta.

### [FEATURE-001] [25pt] Buscar conteúdo exato (ID-0003) ou dentro de um range (ID-0001 até ID-0004)

O sistema vai ser composto dos seguintes módulos:

Implementar uma busca eficiente por um ou mais registros em um arquivo grande de texto, utilizando **busca binária** com 
base nos **IDs**.

Você receberá um arquivo de texto (`fictional_books.txt`), contendo registros de livros em linhas fixas.

Cada linha possui:

```
ID-000123 | Dom Casmurro | Machado de Assis | uma frase aleatória com conteúdo complementar
```

- Cada linha tem exatamente **200 caracteres** (preenchida com espaços se necessário).
- Os registros estão **ordenados por ID**, mas **não são sequenciais** (ex: `ID-000123`, `ID-000128`, `ID-000135`, ...).
- O conteúdo textual extra serve apenas como complemento (para simular um arquivo realista).

Você deve implementar duas funcionalidades aqui
- **Busca por ID exato**
Seu programa deve receber um ID como entrada (ex: `ID-001234`) e localizar ele no arquivo, imprimindo seu 
conteúdo completo separado por uma quebra de linha no seguinte formato:

```
id: 000123
----
titulo: Dom Casmurro
autor: Machado de Assis
code: **random text**
```

Após solicitado o comando você irá imprimir:

- `id:` seguido de um espaço seguido do id

Ao encontrar um elemento você deve imprimir:

- '----' sem as aspas que é um separador de inicio 
- 'titulo:' seguido de um espaço seguido do titulo (2 parametro)
- 'autor:' seguido de um espaço seguido do autor (3 parametro)
- 'code:' seguido de um espaço seguido do código (4 parametro )

- **Busca por intervalo de IDs**
Seu programa deve receber dois IDs (ex: `ID-005000` até `ID-005100`) e imprimir **todas as linhas** com IDs dentro desse
intervalo, inclusive os limites se existirem. Exemplo:

```
ids: 000123-00130
----
id: 000123
titulo: Dom Casmurro
autor: Machado de Assis
code: **random text**
----
id: 000124
titulo: Livro 2
autor: Autor 2
code: **random text**
----
id: 000125
titulo: Livro 3
autor: Autor 3
code: **random text**
```

Após solicitado o comando você irá imprimir:

- `id:` seguido de um espaço seguido do id

Ao encontrar um elemento você deve imprimir:

- '----' sem as aspas que é um separador de inicio 
- 'titulo:' seguido de um espaço seguido do titulo (2 parametro)
- 'autor:' seguido de um espaço seguido do autor (3 parametro)
- 'code:' seguido de um espaço seguido do código (4 parametro )

**Regras:** 

- **Você deve usar busca binária**: o arquivo é grande e ordenado — soluções com leitura linear serão penalizadas.
- **Você deve simular paginação**: cada linha tem tamanho fixo (200 caracteres), então você pode acessar diretamente usando `f.seek(linha * 200)`.
- Não é permitido carregar o arquivo inteiro na memória.

Uma dica é usar a função `seek` para acessar diretamente uma linha do arquivo:

```python
f.seek(index * 200)
linha = f.read(200)
```
