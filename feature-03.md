### Desafio - Knowledge Base CLI

Sua equipe foi incumbida de criar uma aplicação para gerenciar uma base de conhecimento (Knowledge Base).
Esta base de conhecimento é composta por múltiplos arquivos dispostos numa pasta.

### [FEATURE-003] [25pt] Busca um texto específico dentro de vários livros

Este modulo vai olhar os arquivos na pasta `livros`, que é um diretório com arquivos .txt, cada um contendo múltiplas 
linhas de texto já normalizadas (é garantido que cada linha é separada por um `\n` e terá no máximo `200 caracteres`).

Você receberá da entrada padrão uma frase que pode conter caracteres curingas representados por um '.' onde este '.'
representa qualquer caractere.

O objetivo é encontrar quais destas frases aparecem nos arquivos, mesmo que a frase esteja dividida em linhas consecutivas, 
mas sem pular linhas (se uma palavra foi encontrada na linha n, a próxima tem que estar na linha n ou no máximo na linha n+1
ela não pode estar na linha n+2 ou superior).

**Regras:**
- As frases devem ser normalizadas (tudo em minúsculas, sem acentuação, sem pontuação).
- Uma frase pode começar em uma linha e terminar na próxima, mas nunca pode pular linhas.
- Todas as palavras da frase devem estar presentes, em ordem ou seja uma palavra da frase de entrada não pode vir antes 
de outra da mesma frase.
- É garantido que as frases não irão conter palavras repetidas nem pontuação e o espaço será meramente um separador da entrada
- Não é permitido ler todo o livro, por isso você deve se limitar a ler seções deles, sendo que estas seções não devem 
exceder 2 linhas máximas (400 caracteres)

Após solicitado o comando você irá imprimir:

- `frase:` seguido de um espaço e a frase entre aspas duplas usada de entrada

Ao encontrar uma frase, você deve imprimir:

- '----' sem as aspas que é um separador de inicio 
- 'arquivo:' seguido de um espaço e o nome do arquivo
- 'linha:' seguida de um espaço e a linha considerando o número da linha começando em um e cada linha separado por um '\n'
sendo que aqui deve ser apresentado um range como em '1-10'. No caso de ser uma mesma linha mostrar o mesmo número

Caso não encontre em nenhum arquivo imprimir:

- '----' sem as aspas que é um separador de inicio
- `nao encontrado`

Exemplo de saída linha única e arquivo único:
```
frase: "no nosso jardim havia flores"
----
arquivo: 03_book_vo000009.txt
linha: 190-190
```

Exemplo de saída multiplos arquivos:
```
frase: "o amor"
----
arquivo: 13_book_vo000006.txt
linha: 118-118
----
arquivo: 14_book_jp000001.txt
linha: 593-593
```

Exemplo de saída multiplos arquivos:
```
frase: "nao e para achar"
----
nao encontrado
```

Você deve usar uma Trie para indexar as frases e otimizar a busca dentro do texto bruto dos arquivos.

Não é preciso indexar todo o livro com uma Trie, mas você pode indexar para fazer consultas mais rapidamente. 
A Trie é obrigatória para a entrada.

Caso queira você pode extender a funcionalidade para diferentes padrões basta que a sua extensão não comprometa a 
funcionalidade principal.
