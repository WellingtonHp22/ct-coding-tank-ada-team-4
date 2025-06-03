#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testes automatizados para o Knowledge Base CLI

Este arquivo contém testes para validar as duas features principais:
- Feature 001: Busca por ID usando busca binária
- Feature 003: Busca de texto usando Trie

Execução: python test_knowledge_base.py
"""

import unittest
import os
import tempfile
import shutil
from knowledge_base_cli import KnowledgeBaseCLI, Trie, TrieNode


class TestTrie(unittest.TestCase):
    """
    Testes para a estrutura de dados Trie
    """
    
    def setUp(self):
        self.trie = Trie()
    
    def test_insert_and_search(self):
        """Testa inserção e busca básica na Trie"""
        self.trie.insert("python")
        self.trie.insert("programa")
        
        self.assertTrue(self.trie.search("python"))
        self.assertTrue(self.trie.search("programa"))
        self.assertFalse(self.trie.search("java"))
    
    def test_starts_with(self):
        """Testa funcionalidade de prefixo"""
        self.trie.insert("programacao")
        self.trie.insert("programa")
        
        self.assertTrue(self.trie.starts_with("prog"))
        self.assertTrue(self.trie.starts_with("programa"))
        self.assertFalse(self.trie.starts_with("java"))
    
    def test_empty_trie(self):
        """Testa Trie vazia"""
        self.assertFalse(self.trie.search("qualquer"))
        self.assertFalse(self.trie.starts_with("qual"))


class TestKnowledgeBaseCLI(unittest.TestCase):
    """
    Testes para o sistema Knowledge Base CLI
    """
    
    def setUp(self):
        """Configuração inicial para cada teste"""
        self.kb_cli = KnowledgeBaseCLI()
        
        # Cria diretório temporário para testes
        self.test_dir = tempfile.mkdtemp()
        self.books_dir = os.path.join(self.test_dir, "books")
        self.info_dir = os.path.join(self.test_dir, "info")
        
        os.makedirs(self.books_dir)
        os.makedirs(self.info_dir)
        
        # Atualiza caminhos do CLI para usar diretório temporário
        self.kb_cli.books_dir = self.books_dir
        self.kb_cli.fictional_books_file = os.path.join(self.info_dir, "fictional_books.txt")
        
        # Cria arquivo de teste para Feature 001
        self.create_test_fictional_books()
        
        # Cria arquivos de teste para Feature 003
        self.create_test_books()
    
    def tearDown(self):
        """Limpeza após cada teste"""
        shutil.rmtree(self.test_dir)
    
    def create_test_fictional_books(self):
        """Cria arquivo de teste para busca por ID"""
        content = ""
        books_data = [
            ("ID-000001", "Dom Casmurro", "Machado de Assis", "Romance classico brasileiro"),
            ("ID-000005", "O Cortico", "Aluisio Azevedo", "Obra naturalista carioca"),
            ("ID-000010", "Memorias Postumas", "Machado de Assis", "Romance inovador defunto"),
            ("ID-000015", "O Ateneu", "Raul Pompeia", "Romance de formacao critico"),
            ("ID-000020", "Iracema", "Jose de Alencar", "Romance indianista amor"),
        ]
        
        for book_id, title, author, description in books_data:
            line = f"{book_id} | {title} | {author} | {description}"
            # Preenche com espaços até 200 caracteres
            line = line.ljust(200)
            content += line + "\n"
        
        with open(self.kb_cli.fictional_books_file, 'w', encoding='utf-8') as f:
            f.write(content.rstrip('\n'))  # Remove última quebra de linha
    
    def create_test_books(self):
        """Cria arquivos de teste para busca de texto"""
        
        # Livro 1
        book1_content = """Este e um livro sobre amor e paixao.
O amor e um sentimento profundo.
Nao ha nada mais belo que o amor verdadeiro.
A paixao consome e transforma pessoas.
Final do primeiro livro."""
        
        with open(os.path.join(self.books_dir, "01_book_test.txt"), 'w', encoding='utf-8') as f:
            f.write(book1_content)
        
        # Livro 2
        book2_content = """Jardim das flores coloridas estava vazio.
No nosso jardim havia flores de todas as cores.
As flores perfumavam o ar matinal.
O jardim era o lugar favorito da familia.
Fim do segundo livro."""
        
        with open(os.path.join(self.books_dir, "02_book_test.txt"), 'w', encoding='utf-8') as f:
            f.write(book2_content)
        
        # Livro 3
        book3_content = """Historia sobre aventuras e descobertas.
Os exploradores viajaram por mares desconhecidos.
Descobriram terras novas e povos diferentes.
A aventura durou muitos anos.
Retornaram como herois."""
        
        with open(os.path.join(self.books_dir, "03_book_test.txt"), 'w', encoding='utf-8') as f:
            f.write(book3_content)
    
    def test_normalize_text(self):
        """Testa normalização de texto"""
        # Teste com acentos
        result = self.kb_cli.normalize_text("Olá, José! Como está?")
        expected = "ola jose como esta"
        self.assertEqual(result, expected)
        
        # Teste com pontuação
        result = self.kb_cli.normalize_text("Um texto... com! muita? pontuação.")
        expected = "um texto com muita pontuacao"
        self.assertEqual(result, expected)
        
        # Teste com espaços múltiplos
        result = self.kb_cli.normalize_text("Texto    com     espaços   múltiplos")
        expected = "texto com espacos multiplos"
        self.assertEqual(result, expected)
    
    def test_binary_search_existing_id(self):
        """Testa busca binária por ID existente"""
        result = self.kb_cli.binary_search_id(self.kb_cli.fictional_books_file, "ID-000010")
        self.assertIsNotNone(result)
        self.assertIn("Memorias Postumas", result)
        self.assertIn("Machado de Assis", result)
    
    def test_binary_search_non_existing_id(self):
        """Testa busca binária por ID inexistente"""
        result = self.kb_cli.binary_search_id(self.kb_cli.fictional_books_file, "ID-999999")
        self.assertIsNone(result)
    
    def test_search_id_range(self):
        """Testa busca por intervalo de IDs"""
        results = self.kb_cli.search_id_range(
            self.kb_cli.fictional_books_file, 
            "ID-000005", 
            "ID-000015"
        )
        
        self.assertEqual(len(results), 3)  # Deve encontrar IDs 005, 010, 015
        
        # Verifica se os IDs corretos foram encontrados
        ids_found = []
        for result in results:
            parts = result.split('|')
            if len(parts) >= 1:
                ids_found.append(parts[0].strip())
        
        self.assertIn("ID-000005", ids_found)
        self.assertIn("ID-000010", ids_found)
        self.assertIn("ID-000015", ids_found)
    
    def test_format_book_output(self):
        """Testa formatação de saída do livro"""
        test_line = "ID-000001 | Dom Casmurro | Machado de Assis | Romance classico"
        result = self.kb_cli.format_book_output(test_line)
        
        expected = """----
titulo: Dom Casmurro
autor: Machado de Assis
code: Romance classico"""
        
        self.assertEqual(result, expected)
    
    def test_search_text_exact_match(self):
        """Testa busca de texto - correspondência exata"""
        results = self.kb_cli.search_text_in_books("o amor")
        
        # Deve encontrar pelo menos uma ocorrência
        self.assertGreater(len(results), 0)
        
        # Verifica se encontrou no arquivo correto
        filenames = [result[0] for result in results]
        self.assertIn("01_book_test.txt", filenames)
    
    def test_search_text_phrase_across_lines(self):
        """Testa busca de frase que atravessa linhas"""
        results = self.kb_cli.search_text_in_books("no nosso jardim havia flores")
        
        # Deve encontrar a frase no segundo livro
        self.assertGreater(len(results), 0)
        
        # Verifica arquivo e linha
        found = False
        for filename, start_line, end_line in results:
            if filename == "02_book_test.txt" and start_line == 2:
                found = True
                break
        
        self.assertTrue(found)
    
    def test_search_text_not_found(self):
        """Testa busca de texto inexistente"""
        results = self.kb_cli.search_text_in_books("texto que nao existe em lugar nenhum")
        self.assertEqual(len(results), 0)
    
    def test_search_text_wildcard(self):
        """Testa busca com caractere curinga"""
        results = self.kb_cli.search_text_in_books("am.r")
        
        # Deve encontrar "amor"
        self.assertGreater(len(results), 0)
    
    def test_word_matches_with_wildcard(self):
        """Testa correspondência de palavra com curinga"""
        # Teste com curinga
        self.assertTrue(self.kb_cli._word_matches("amor", "am.r"))
        self.assertTrue(self.kb_cli._word_matches("casa", "c.sa"))
        
        # Teste sem curinga
        self.assertTrue(self.kb_cli._word_matches("amor", "amor"))
        self.assertFalse(self.kb_cli._word_matches("amor", "casa"))
        
        # Teste com tamanhos diferentes
        self.assertFalse(self.kb_cli._word_matches("amor", "am."))
        self.assertFalse(self.kb_cli._word_matches("am", "amor"))


class TestIntegration(unittest.TestCase):
    """
    Testes de integração para validar o sistema completo
    """
    
    def setUp(self):
        self.kb_cli = KnowledgeBaseCLI()
    
    def test_system_initialization(self):
        """Testa inicialização do sistema"""
        self.assertIsNotNone(self.kb_cli)
        self.assertEqual(self.kb_cli.line_size, 200)
        self.assertEqual(self.kb_cli.books_dir, "books")
    
    def test_trie_integration(self):
        """Testa integração da Trie com o sistema"""
        trie = Trie()
        
        # Simula indexação de palavras
        words = ["python", "programacao", "codigo", "algoritmo"]
        for word in words:
            trie.insert(word)
        
        # Verifica se todas as palavras foram inseridas
        for word in words:
            self.assertTrue(trie.search(word))
        
        # Verifica prefixos
        self.assertTrue(trie.starts_with("prog"))
        self.assertTrue(trie.starts_with("cod"))
        self.assertFalse(trie.starts_with("java"))


def run_tests():
    """
    Executa todos os testes
    """
    print("=" * 60)
    print("    EXECUTANDO TESTES DO KNOWLEDGE BASE CLI")
    print("=" * 60)
    
    # Carrega todas as suítes de teste
    test_suite = unittest.TestSuite()
    
    # Adiciona testes da Trie
    test_suite.addTest(unittest.makeSuite(TestTrie))
    
    # Adiciona testes do CLI
    test_suite.addTest(unittest.makeSuite(TestKnowledgeBaseCLI))
    
    # Adiciona testes de integração
    test_suite.addTest(unittest.makeSuite(TestIntegration))
    
    # Executa os testes
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Relatório final
    print("\n" + "=" * 60)
    print("    RELATÓRIO FINAL DOS TESTES")
    print("=" * 60)
    print(f"Testes executados: {result.testsRun}")
    print(f"Falhas: {len(result.failures)}")
    print(f"Erros: {len(result.errors)}")
    
    if result.failures:
        print("\nFALHAS:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback}")
    
    if result.errors:
        print("\nERROS:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback}")
    
    if result.wasSuccessful():
        print("\n✅ TODOS OS TESTES PASSARAM COM SUCESSO!")
        return True
    else:
        print(f"\n❌ {len(result.failures + result.errors)} TESTE(S) FALHARAM!")
        return False


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
