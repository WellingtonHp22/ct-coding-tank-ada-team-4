#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de demonstração do Knowledge Base CLI
Executa exemplos das funcionalidades principais
"""

import os
import sys
from knowledge_base_cli import KnowledgeBaseCLI


def criar_dados_exemplo():
    """Cria dados de exemplo para demonstração"""
    
    # Cria diretório info se não existir
    if not os.path.exists("info"):
        os.makedirs("info")
    
    # Cria arquivo fictional_books.txt de exemplo se não existir
    fictional_books_path = "info/fictional_books.txt"
    if not os.path.exists(fictional_books_path):
        books_data = [
            "ID-000001 | Dom Casmurro | Machado de Assis | Romance classico da literatura brasileira sobre ciume e narrativa                                            ",
            "ID-000005 | O Cortico | Aluisio Azevedo | Obra naturalista que retrata a vida em um cortico carioca                                                      ",
            "ID-000010 | Memorias Postumas | Machado de Assis | Romance inovador narrado por um defunto autor                                                         ",
            "ID-000015 | O Ateneu | Raul Pompeia | Romance de formacao que critica o sistema educacional brasileiro                                                     ",
            "ID-000020 | Iracema | Jose de Alencar | Romance indianista que narra o amor entre india e portugues                                                       ",
            "ID-000025 | Senhora | Jose de Alencar | Romance urbano sobre Aurora que compra um marido por dinheiro                                                      ",
            "ID-000030 | Casa de Pensao | Aluisio Azevedo | Drama naturalista sobre pensao familiar e relacoes sociais                                              ",
            "ID-000035 | O Guarani | Jose de Alencar | Romance indianista sobre amor entre Peri e Ceci                                                                ",
            "ID-000040 | A Escrava Isaura | Bernardo Guimaraes | Romance abolicionista sobre escrava que luta pela liberdade                                         ",
            "ID-000045 | O Seminarista | Bernardo Guimaraes | Romance sobre jovem seminarista dividido entre vocacao e amor                                          "
        ]
        
        with open(fictional_books_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(books_data))
    
    # Cria diretório books se não existir
    if not os.path.exists("books"):
        os.makedirs("books")
    
    # Cria arquivos de exemplo na pasta books
    exemplo1 = """Este e um livro sobre amor e paixao.
O amor e um sentimento profundo e transformador.
Nao ha nada mais belo que o amor verdadeiro.
A paixao consome e transforma as pessoas.
Final do primeiro livro de exemplo."""
    
    exemplo2 = """Jardim das flores coloridas estava vazio.
No nosso jardim havia flores de todas as cores.
As flores perfumavam o ar matinal da primavera.
O jardim era o lugar favorito da familia inteira.
Fim do segundo livro sobre jardins."""
    
    exemplo3 = """Historia sobre aventuras e grandes descobertas.
Os exploradores viajaram por mares nunca navegados.
Descobriram terras novas e povos diferentes.
A aventura durou muitos anos perigosos.
Retornaram como herois de grandes feitos."""
    
    with open("books/01_exemplo_amor.txt", 'w', encoding='utf-8') as f:
        f.write(exemplo1)
    
    with open("books/02_exemplo_jardim.txt", 'w', encoding='utf-8') as f:
        f.write(exemplo2)
    
    with open("books/03_exemplo_aventura.txt", 'w', encoding='utf-8') as f:
        f.write(exemplo3)


def demonstrar_feature_001():
    """Demonstra a Feature 001 - Busca por ID"""
    print("=" * 60)
    print("           DEMONSTRAÇÃO FEATURE 001 - BUSCA POR ID")
    print("=" * 60)
    
    kb_cli = KnowledgeBaseCLI()
    
    print("\n🔍 Teste 1: Busca por ID exato")
    print("Comando: Buscar ID-000010")
    print("-" * 40)
    
    result = kb_cli.binary_search_id("info/fictional_books.txt", "ID-000010")
    if result:
        print("id: 000010")
        print(kb_cli.format_book_output(result))
    else:
        print("ID não encontrado")
    
    print("\n🔍 Teste 2: Busca por intervalo de IDs")
    print("Comando: Buscar de ID-000005 até ID-000020")
    print("-" * 40)
    
    results = kb_cli.search_id_range("info/fictional_books.txt", "ID-000005", "ID-000020")
    if results:
        start_num = "000005"
        end_num = "000020"
        print(f"ids: {start_num}-{end_num}")
        for result in results:
            print(kb_cli.format_book_output(result))
    else:
        print("Nenhum ID encontrado no intervalo")
    
    print("\n🔍 Teste 3: Busca por ID inexistente")
    print("Comando: Buscar ID-999999")
    print("-" * 40)
    
    result = kb_cli.binary_search_id("info/fictional_books.txt", "ID-999999")
    if result:
        print("id: 999999")
        print(kb_cli.format_book_output(result))
    else:
        print("id: 999999")
        print("----")
        print("ID não encontrado")


def demonstrar_feature_003():
    """Demonstra a Feature 003 - Busca de Texto"""
    print("\n\n" + "=" * 60)
    print("        DEMONSTRAÇÃO FEATURE 003 - BUSCA DE TEXTO")
    print("=" * 60)
    
    kb_cli = KnowledgeBaseCLI()
    
    testes = [
        ("o amor", "Busca simples por 'o amor'"),
        ("no nosso jardim havia flores", "Busca por frase que atravessa linha"),
        ("am.r", "Busca com caractere curinga"),
        ("texto inexistente", "Busca por texto que não existe")
    ]
    
    for i, (frase, descricao) in enumerate(testes, 1):
        print(f"\n🔍 Teste {i}: {descricao}")
        print(f"Comando: Buscar '{frase}'")
        print("-" * 40)
        
        print(f'frase: "{frase}"')
        results = kb_cli.search_text_in_books(frase)
        
        if results:
            for filename, start_line, end_line in results:
                print("----")
                print(f"arquivo: {filename}")
                if start_line == end_line:
                    print(f"linha: {start_line}-{start_line}")
                else:
                    print(f"linha: {start_line}-{end_line}")
        else:
            print("----")
            print("nao encontrado")


def demonstrar_trie():
    """Demonstra o funcionamento da estrutura Trie"""
    print("\n\n" + "=" * 60)
    print("           DEMONSTRAÇÃO DA ESTRUTURA TRIE")
    print("=" * 60)
    
    from knowledge_base_cli import Trie
    
    trie = Trie()
    
    # Insere palavras
    palavras = ["amor", "amar", "amargo", "casa", "casamento", "python", "programa"]
    
    print("\n📝 Inserindo palavras na Trie:")
    for palavra in palavras:
        trie.insert(palavra)
        print(f"  + {palavra}")
    
    print("\n🔍 Testando buscas:")
    
    # Testa buscas
    testes_busca = ["amor", "casa", "java", "prog"]
    
    for palavra in testes_busca:
        existe = trie.search(palavra)
        print(f"  Buscar '{palavra}': {'✅ Encontrada' if existe else '❌ Não encontrada'}")
    
    print("\n🔍 Testando prefixos:")
    
    # Testa prefixos
    prefixos = ["am", "cas", "py", "xyz"]
    
    for prefixo in prefixos:
        tem_prefixo = trie.starts_with(prefixo)
        print(f"  Prefixo '{prefixo}': {'✅ Existe' if tem_prefixo else '❌ Não existe'}")


def demonstrar_normalizacao():
    """Demonstra a normalização de texto"""
    print("\n\n" + "=" * 60)
    print("         DEMONSTRAÇÃO DA NORMALIZAÇÃO DE TEXTO")
    print("=" * 60)
    
    kb_cli = KnowledgeBaseCLI()
    
    exemplos = [
        "Olá, José! Como está?",
        "Programação em Python é fácil.",
        "Dom Casmurro... um clássico!!!",
        "   Texto    com     espaços   múltiplos   "
    ]
    
    print("\n📝 Exemplos de normalização:")
    
    for texto in exemplos:
        normalizado = kb_cli.normalize_text(texto)
        print(f"Original : '{texto}'")
        print(f"Normalizado: '{normalizado}'")
        print()


def main():
    """Função principal da demonstração"""
    print("🚀 KNOWLEDGE BASE CLI - DEMONSTRAÇÃO COMPLETA")
    print("Team 4 - Coding Tank ADA")
    print("=" * 60)
    
    # Cria dados de exemplo
    print("📁 Criando dados de exemplo...")
    criar_dados_exemplo()
    print("✅ Dados criados com sucesso!")
    
    # Executa demonstrações
    try:
        demonstrar_feature_001()
        demonstrar_feature_003()
        demonstrar_trie()
        demonstrar_normalizacao()
        
        print("\n\n" + "=" * 60)
        print("           ✅ DEMONSTRAÇÃO CONCLUÍDA COM SUCESSO!")
        print("=" * 60)
        print("\nPara usar o sistema interativo, execute:")
        print("  python knowledge_base_cli.py")
        print("\nPara executar testes automatizados:")
        print("  python test_knowledge_base.py")
        
    except Exception as e:
        print(f"\n❌ Erro durante a demonstração: {e}")
        return False
    
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
