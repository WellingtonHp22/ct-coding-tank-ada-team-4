#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Knowledge Base CLI - Sistema de Gerenciamento de Base de Conhecimento

Este sistema implementa duas funcionalidades principais:
1. FEATURE-001: Busca por ID exato ou intervalo usando busca binária
2. FEATURE-003: Busca de texto específico em múltiplos livros usando Trie

Autores: Team 4 - Coding Tank ADA
Data: 2025
"""

import os
import sys
import re
from typing import List, Tuple, Optional, Dict
import unicodedata
import argparse


class TrieNode:
    """
    Nó da estrutura Trie para busca eficiente de palavras
    """
    def __init__(self):
        self.children = {}
        self.is_end_word = False
        self.word = ""


class Trie:
    """
    Implementação de Trie para busca eficiente de frases
    """
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        """Insere uma palavra na Trie"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_word = True
        node.word = word
    
    def search(self, word: str) -> bool:
        """Busca uma palavra na Trie"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_word
    
    def starts_with(self, prefix: str) -> bool:
        """Verifica se existe alguma palavra com o prefixo dado"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


class KnowledgeBaseCLI:
    """
    Classe principal do sistema Knowledge Base CLI
    """
    
    def __init__(self):
        self.books_dir = "books"
        self.fictional_books_file = "info/fictional_books.txt"
        self.line_size = 200  # Tamanho fixo de cada linha
    
    def normalize_text(self, text: str) -> str:
        """
        Normaliza texto removendo acentos, pontuação e convertendo para minúsculas
        """
        # Remove acentos
        text = unicodedata.normalize('NFD', text)
        text = ''.join(char for char in text if unicodedata.category(char) != 'Mn')
        
        # Converte para minúsculas
        text = text.lower()
        
        # Remove pontuação, mantém apenas letras, números e espaços
        text = re.sub(r'[^\w\s.]', ' ', text)
        
        # Remove espaços múltiplos
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    def binary_search_id(self, file_path: str, target_id: str) -> Optional[str]:
        """
        Busca binária por ID específico no arquivo
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                # Calcula o número total de linhas
                f.seek(0, 2)  # Vai para o final do arquivo
                file_size = f.tell()
                total_lines = file_size // self.line_size
                
                left, right = 0, total_lines - 1
                
                while left <= right:
                    mid = (left + right) // 2
                    
                    # Posiciona no início da linha
                    f.seek(mid * self.line_size)
                    line = f.read(self.line_size).strip()
                    
                    if not line:
                        break
                    
                    # Extrai o ID da linha
                    parts = line.split('|')
                    if len(parts) >= 4:
                        line_id = parts[0].strip()
                        
                        if line_id == target_id:
                            return line
                        elif line_id < target_id:
                            left = mid + 1
                        else:
                            right = mid - 1
                
                return None
                
        except FileNotFoundError:
            print(f"Erro: Arquivo {file_path} não encontrado.")
            return None
        except Exception as e:
            print(f"Erro ao ler arquivo: {e}")
            return None
    
    def search_id_range(self, file_path: str, start_id: str, end_id: str) -> List[str]:
        """
        Busca por intervalo de IDs usando busca binária
        """
        results = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                # Calcula o número total de linhas
                f.seek(0, 2)
                file_size = f.tell()
                total_lines = file_size // self.line_size
                
                # Encontra a primeira posição do intervalo
                left, right = 0, total_lines - 1
                start_pos = -1
                
                while left <= right:
                    mid = (left + right) // 2
                    f.seek(mid * self.line_size)
                    line = f.read(self.line_size).strip()
                    
                    if not line:
                        break
                    
                    parts = line.split('|')
                    if len(parts) >= 4:
                        line_id = parts[0].strip()
                        
                        if line_id >= start_id:
                            start_pos = mid
                            right = mid - 1
                        else:
                            left = mid + 1
                
                # Se encontrou posição inicial, coleta todos os IDs no intervalo
                if start_pos != -1:
                    current_pos = start_pos
                    
                    while current_pos < total_lines:
                        f.seek(current_pos * self.line_size)
                        line = f.read(self.line_size).strip()
                        
                        if not line:
                            break
                        
                        parts = line.split('|')
                        if len(parts) >= 4:
                            line_id = parts[0].strip()
                            
                            if line_id > end_id:
                                break
                            
                            if start_id <= line_id <= end_id:
                                results.append(line)
                        
                        current_pos += 1
                
        except FileNotFoundError:
            print(f"Erro: Arquivo {file_path} não encontrado.")
        except Exception as e:
            print(f"Erro ao ler arquivo: {e}")
        
        return results
    
    def format_book_output(self, line: str) -> str:
        """
        Formata a saída de um registro de livro
        """
        parts = line.split('|')
        if len(parts) >= 4:
            book_id = parts[0].strip().replace('ID-', '')
            title = parts[1].strip()
            author = parts[2].strip()
            code = parts[3].strip()
            
            return f"""----
titulo: {title}
autor: {author}
code: {code}"""
        
        return "Formato inválido"
    
    def search_text_in_books(self, phrase: str) -> List[Tuple[str, int, int]]:
        """
        Busca uma frase nos livros da pasta books usando Trie
        """
        # Normaliza a frase de entrada
        normalized_phrase = self.normalize_text(phrase)
        words = normalized_phrase.split()
        
        # Cria Trie com as palavras da frase
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        results = []
        books_path = self.books_dir
        
        if not os.path.exists(books_path):
            return results
        
        # Processa cada arquivo de livro
        for filename in sorted(os.listdir(books_path)):
            if filename.endswith('.txt'):
                file_path = os.path.join(books_path, filename)
                matches = self._search_in_file(file_path, words, trie)
                
                for start_line, end_line in matches:
                    results.append((filename, start_line, end_line))
        
        return results
    
    def _search_in_file(self, file_path: str, words: List[str], trie: Trie) -> List[Tuple[int, int]]:
        """
        Busca palavras em um arquivo específico
        """
        matches = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
                for i in range(len(lines)):
                    # Lê no máximo 2 linhas consecutivas (400 caracteres)
                    if i + 1 < len(lines):
                        text_block = lines[i] + lines[i + 1]
                        max_end_line = i + 2
                    else:
                        text_block = lines[i]
                        max_end_line = i + 1
                    
                    # Normaliza o bloco de texto
                    normalized_text = self.normalize_text(text_block)
                    
                    # Verifica se a sequência de palavras está presente
                    if self._matches_phrase_pattern(normalized_text, words):
                        # Determina as linhas exatas onde a frase foi encontrada
                        start_line = i + 1  # +1 porque linhas começam em 1
                        end_line = min(max_end_line, len(lines))
                        
                        # Verifica se a frase está toda na primeira linha
                        first_line_normalized = self.normalize_text(lines[i])
                        if self._matches_phrase_pattern(first_line_normalized, words):
                            end_line = start_line
                        
                        matches.append((start_line, end_line))
        
        except Exception as e:
            print(f"Erro ao ler arquivo {file_path}: {e}")
        
        return matches
    
    def _matches_phrase_pattern(self, text: str, words: List[str]) -> bool:
        """
        Verifica se o texto contém a sequência de palavras na ordem correta
        Suporta caracteres curinga '.'
        """
        text_words = text.split()
        
        if len(words) == 0:
            return False
        
        # Encontra todas as posições onde a primeira palavra pode estar
        for start_idx in range(len(text_words)):
            if self._word_matches(text_words[start_idx], words[0]):
                # Verifica se as palavras seguintes estão na sequência
                if self._check_sequence(text_words, start_idx, words):
                    return True
        
        return False
    
    def _word_matches(self, text_word: str, pattern_word: str) -> bool:
        """
        Verifica se uma palavra do texto corresponde ao padrão (com suporte a '.')
        """
        if len(text_word) != len(pattern_word):
            return False
        
        for i in range(len(pattern_word)):
            if pattern_word[i] != '.' and pattern_word[i] != text_word[i]:
                return False
        
        return True
    
    def _check_sequence(self, text_words: List[str], start_idx: int, pattern_words: List[str]) -> bool:
        """
        Verifica se a sequência de palavras do padrão está presente no texto
        """
        current_idx = start_idx
        pattern_idx = 0
        
        while pattern_idx < len(pattern_words) and current_idx < len(text_words):
            if self._word_matches(text_words[current_idx], pattern_words[pattern_idx]):
                pattern_idx += 1
                if pattern_idx == len(pattern_words):
                    return True
            current_idx += 1
        
        return pattern_idx == len(pattern_words)
    
    def run_feature_001(self):
        """
        Executa a Feature 001 - Busca por ID
        """
        print("=== FEATURE-001: Busca por ID ===")
        
        while True:
            print("\nOpções:")
            print("1. Buscar ID exato")
            print("2. Buscar intervalo de IDs")
            print("3. Voltar ao menu principal")
            
            choice = input("\nEscolha uma opção (1-3): ").strip()
            
            if choice == "1":
                id_input = input("Digite o ID (ex: ID-000123): ").strip()
                print(f"id: {id_input.replace('ID-', '')}")
                
                result = self.binary_search_id(self.fictional_books_file, id_input)
                if result:
                    print(self.format_book_output(result))
                else:
                    print("----\nID não encontrado")
            
            elif choice == "2":
                start_id = input("Digite o ID inicial (ex: ID-000123): ").strip()
                end_id = input("Digite o ID final (ex: ID-000130): ").strip()
                
                start_num = start_id.replace('ID-', '')
                end_num = end_id.replace('ID-', '')
                print(f"ids: {start_num}-{end_num}")
                
                results = self.search_id_range(self.fictional_books_file, start_id, end_id)
                
                if results:
                    for result in results:
                        print(self.format_book_output(result))
                else:
                    print("----\nNenhum ID encontrado no intervalo")
            
            elif choice == "3":
                break
            else:
                print("Opção inválida!")
    
    def run_feature_003(self):
        """
        Executa a Feature 003 - Busca de texto
        """
        print("=== FEATURE-003: Busca de Texto ===")
        
        while True:
            phrase = input("\nDigite a frase para buscar (ou 'quit' para sair): ").strip()
            
            if phrase.lower() == 'quit':
                break
            
            print(f'frase: "{phrase}"')
            
            results = self.search_text_in_books(phrase)
            
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
    
    def run(self):
        """
        Método principal para executar o sistema
        """
        print("=" * 50)
        print("    KNOWLEDGE BASE CLI - Team 4")
        print("=" * 50)
        
        while True:
            print("\n=== MENU PRINCIPAL ===")
            print("1. Feature 001 - Busca por ID")
            print("2. Feature 003 - Busca de Texto")
            print("3. Sair")
            
            choice = input("\nEscolha uma opção (1-3): ").strip()
            
            if choice == "1":
                self.run_feature_001()
            elif choice == "2":
                self.run_feature_003()
            elif choice == "3":
                print("\nObrigado por usar o Knowledge Base CLI!")
                break
            else:
                print("Opção inválida! Tente novamente.")


def main():
    """
    Função principal do programa
    """
    # Suporte para argumentos de linha de comando
    parser = argparse.ArgumentParser(description='Knowledge Base CLI')
    parser.add_argument('--feature', choices=['001', '003'], 
                       help='Executar feature específica diretamente')
    parser.add_argument('--id', help='ID para busca direta (Feature 001)')
    parser.add_argument('--phrase', help='Frase para busca direta (Feature 003)')
    
    args = parser.parse_args()
    
    kb_cli = KnowledgeBaseCLI()
    
    # Se argumentos específicos foram fornecidos
    if args.feature == '001' and args.id:
        print(f"id: {args.id.replace('ID-', '')}")
        result = kb_cli.binary_search_id(kb_cli.fictional_books_file, args.id)
        if result:
            print(kb_cli.format_book_output(result))
        else:
            print("----\nID não encontrado")
    elif args.feature == '003' and args.phrase:
        print(f'frase: "{args.phrase}"')
        results = kb_cli.search_text_in_books(args.phrase)
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
    else:
        # Executa o menu interativo
        kb_cli.run()


if __name__ == "__main__":
    main()
