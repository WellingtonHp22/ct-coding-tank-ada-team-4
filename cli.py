import sys
import os
from knowledge_base import KnowledgeBase


def print_help():
    """Imprime instruções de uso conforme especificação"""
    print("=== Knowledge Base CLI ===")
    print("Sistema de busca binária em base de conhecimento")
    print()
    print("Comandos disponíveis:")
    print("  search <ID>              - Busca por ID exato em dados estruturados")
    print("                            Exemplo: search ID-000001")
    print()
    print("  range <ID1> <ID2>        - Busca por intervalo de IDs")
    print("                            Exemplo: range ID-000001 ID-000010")
    print()
    print("  books <termo>            - Busca texto nos livros da pasta books/")
    print("                            Exemplo: books Dom Casmurro")
    print()
    print("  list                     - Lista todos os livros disponíveis")
    print("  stats                    - Mostra estatísticas do sistema")
    print("  help                     - Mostra esta ajuda")
    print("  quit                     - Sai do programa")
    print()
    print("Formato dos IDs: ID-XXXXXX (ex: ID-000001, ID-000050)")
    print("O sistema usa busca binária O(log n) para máxima eficiência.")
    print()


def print_welcome():
    """Imprime mensagem de boas-vindas"""
    print("=" * 60)
    print("    KNOWLEDGE BASE CLI - FEATURE-001")
    print("    Busca Binária por ID Exato e Intervalos")
    print("    + Busca em Texto Completo")
    print("=" * 60)
    print()


def print_stats(kb):
    """Imprime estatísticas do sistema"""
    stats = kb.get_stats()
    print("=== Estatísticas do Sistema ===")
    print(f"Arquivo principal: {stats['filename']}")
    print(f"Total de registros estruturados: {stats['total_records']}")
    print(f"Tamanho do arquivo: {stats['file_size_bytes']:,} bytes")
    print(f"Tamanho da linha: {stats['line_size']} caracteres")
    print(f"Máximo de comparações (busca binária): {stats['estimated_max_comparisons']}")
    print(f"Livros disponíveis: {stats['books_available']}")
    print(f"Diretório de livros: {stats['books_directory']}")
    print()


def validate_id_format(id_str):
    """
    Valida se o ID está no formato correto
    
    Args:
        id_str: String do ID a ser validada
        
    Returns:
        bool: True se válido, False caso contrário
    """
    if not id_str.startswith('ID-'):
        return False
    
    try:
        # Verifica se a parte numérica é válida
        numeric_part = id_str[3:]
        int(numeric_part)
        return len(numeric_part) == 6  # Exatamente 6 dígitos
    except ValueError:
        return False


def main():
    """Função principal do CLI"""
    # Verifica se o arquivo de dados existe
    data_file = "fictional_books.txt"
    
    if not os.path.exists(data_file):
        print("❌ ERRO: Arquivo 'fictional_books.txt' não encontrado!")
        print()
        print("Por favor, certifique-se de que o arquivo de dados está presente")
        print("no diretório atual com o formato correto:")
        print()
        print("ID-000001 | Título | Autor | Descrição (200 chars por linha)")
        print()
        sys.exit(1)
    
    # Inicializa o sistema
    try:
        kb = KnowledgeBase(data_file)
    except Exception as e:
        print(f"❌ ERRO ao inicializar sistema: {e}")
        sys.exit(1)
    
    # Interface principal
    print_welcome()
    
    # Mostra informações iniciais
    stats = kb.get_stats()
    print(f"✅ Sistema inicializado com sucesso!")
    print(f"📊 {stats['total_records']} registros estruturados carregados")
    print(f"📚 {stats['books_available']} livro(s) disponível(is)")
    print(f"🔍 Busca binária ativa (máx. {stats['estimated_max_comparisons']} comparações)")
    print()
    print("Digite 'help' para ver os comandos disponíveis")
    print()
    
    # Loop principal de comandos
    while True:
        try:
            command = input("kb> ").strip()
            
            if not command:
                continue
                
            parts = command.split()
            cmd = parts[0].lower()
            
            # Comandos de sistema
            if cmd in ["quit", "exit", "q"]:
                print("👋 Encerrando o sistema...")
                break
                
            elif cmd in ["help", "h", "?"]:
                print_help()
                
            elif cmd == "stats":
                print_stats(kb)
                
            elif cmd == "list":
                kb.list_books()
                print()
                
            # Comando de busca exata
            elif cmd == "search":
                if len(parts) != 2:
                    print("❌ Uso incorreto: search <ID>")
                    print("   Exemplo: search ID-000001")
                    continue
                
                target_id = parts[1].upper()  # Garante maiúsculas
                
                # Valida formato do ID
                if not validate_id_format(target_id):
                    print("❌ Formato de ID inválido!")
                    print("   Use o formato: ID-XXXXXX (ex: ID-000001)")
                    continue
                
                print()
                kb.search_exact(target_id)
                print()
                
            # Comando de busca por intervalo
            elif cmd == "range":
                if len(parts) != 3:
                    print("❌ Uso incorreto: range <ID1> <ID2>")
                    print("   Exemplo: range ID-000001 ID-000010")
                    continue
                
                start_id = parts[1].upper()  # Garante maiúsculas
                end_id = parts[2].upper()    # Garante maiúsculas
                
                # Valida formato dos IDs
                if not validate_id_format(start_id):
                    print("❌ Formato de ID inicial inválido!")
                    print("   Use o formato: ID-XXXXXX (ex: ID-000001)")
                    continue
                    
                if not validate_id_format(end_id):
                    print("❌ Formato de ID final inválido!")
                    print("   Use o formato: ID-XXXXXX (ex: ID-000010)")
                    continue
                
                # Verifica se o intervalo é válido
                start_num = int(start_id[3:])
                end_num = int(end_id[3:])
                
                if start_num > end_num:
                    print("❌ ID inicial deve ser menor ou igual ao ID final!")
                    continue
                
                print()
                kb.search_range(start_id, end_id)
                print()
                
            # Comando de busca nos livros
            elif cmd == "books":
                if len(parts) < 2:
                    print("❌ Uso incorreto: books <termo de busca>")
                    print("   Exemplo: books Dom Casmurro")
                    print("   Exemplo: books Machado de Assis")
                    continue
                
                query = " ".join(parts[1:])
                print()
                kb.search_books(query)
                print()
                
            # Comando desconhecido
            else:
                print(f"❌ Comando desconhecido: {cmd}")
                print("   Digite 'help' para ver os comandos disponíveis")
                print()
                
        except KeyboardInterrupt:
            print("\n👋 Encerrando o sistema...")
            break
            
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            print("   Digite 'help' para ver os comandos disponíveis")
            print()


if __name__ == "__main__":
    main()
