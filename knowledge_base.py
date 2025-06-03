import os
import glob


class KnowledgeBase:
    def __init__(self, filename="fictional_books.txt"):
        """
        Inicializa o sistema de Knowledge Base para busca binária
        
        Args:
            filename: Caminho para o arquivo de dados estruturado
        """
        self.filename = filename
        self.line_size = 200  # Tamanho fixo de cada linha
        self.books_dir = "books"
        
        # Verifica se o arquivo existe
        if not os.path.exists(self.filename):
            raise FileNotFoundError(f"Arquivo {self.filename} não encontrado!")
    
    def _get_file_size(self):
        """Retorna o tamanho do arquivo em bytes"""
        return os.path.getsize(self.filename)
    
    def _get_total_lines(self):
        """Calcula o número total de linhas baseado no tamanho fixo"""
        file_size = self._get_file_size()
        return file_size // self.line_size
    
    def _read_line_at_index(self, index):
        """
        Lê uma linha específica usando seek para acesso direto
        
        Args:
            index: Índice da linha (0-based)
            
        Returns:
            str: Conteúdo da linha sem espaços extras
        """
        with open(self.filename, 'r', encoding='utf-8') as f:
            f.seek(index * self.line_size)
            line = f.read(self.line_size).strip()
            return line
    
    def _extract_id_from_line(self, line):
        """
        Extrai o ID numérico de uma linha estruturada
        
        Args:
            line: Linha no formato "ID-000123 | ..."
            
        Returns:
            str: ID numérico sem o prefixo "ID-"
        """
        if '|' in line:
            id_part = line.split('|')[0].strip()
            if id_part.startswith('ID-'):
                return id_part[3:]  # Remove 'ID-' prefix
        return None
    
    def _parse_line(self, line):
        """
        Converte uma linha em dicionário com os campos estruturados
        
        Args:
            line: Linha no formato "ID-000123 | Título | Autor | Descrição"
            
        Returns:
            dict: Dicionário com os campos parseados
        """
        parts = [part.strip() for part in line.split('|')]
        if len(parts) >= 4:
            return {
                'id': parts[0][3:] if parts[0].startswith('ID-') else parts[0],
                'titulo': parts[1],
                'autor': parts[2],
                'code': parts[3]
            }
        return None
    
    def _binary_search_exact(self, target_id):
        """
        Busca binária por ID exato
        
        Args:
            target_id: ID alvo (sem prefixo "ID-")
            
        Returns:
            str: Linha completa se encontrada, None caso contrário
        """
        total_lines = self._get_total_lines()
        left, right = 0, total_lines - 1
        
        while left <= right:
            mid = (left + right) // 2
            line = self._read_line_at_index(mid)
            current_id = self._extract_id_from_line(line)
            
            if current_id is None:
                return None
                
            # Comparação numérica dos IDs
            if current_id == target_id:
                return line
            elif current_id < target_id:
                left = mid + 1
            else:
                right = mid - 1
                
        return None
    
    def _binary_search_range_start(self, start_id):
        """
        Encontra o primeiro índice no range usando busca binária
        
        Args:
            start_id: ID inicial do range
            
        Returns:
            int: Índice da primeira ocorrência >= start_id, -1 se não encontrar
        """
        total_lines = self._get_total_lines()
        left, right = 0, total_lines - 1
        result_index = -1
        
        while left <= right:
            mid = (left + right) // 2
            line = self._read_line_at_index(mid)
            current_id = self._extract_id_from_line(line)
            
            if current_id is None:
                break
                
            if current_id >= start_id:
                result_index = mid
                right = mid - 1  # Continua buscando à esquerda
            else:
                left = mid + 1
                
        return result_index
    
    def _binary_search_range_end(self, end_id):
        """
        Encontra o último índice no range usando busca binária
        
        Args:
            end_id: ID final do range
            
        Returns:
            int: Índice da última ocorrência <= end_id, -1 se não encontrar
        """
        total_lines = self._get_total_lines()
        left, right = 0, total_lines - 1
        result_index = -1
        
        while left <= right:
            mid = (left + right) // 2
            line = self._read_line_at_index(mid)
            current_id = self._extract_id_from_line(line)
            
            if current_id is None:
                break
                
            if current_id <= end_id:
                result_index = mid
                left = mid + 1  # Continua buscando à direita
            else:
                right = mid - 1
                
        return result_index
    
    def search_exact(self, target_id):
        """
        Busca por ID exato e imprime resultado conforme especificação
        
        Args:
            target_id: ID a ser buscado (com ou sem prefixo "ID-")
        """
        # Remove 'ID-' prefix se presente
        if target_id.startswith('ID-'):
            target_id = target_id[3:]
            
        # Imprime o ID conforme especificação
        print(f"id: {target_id}")
        
        # Realiza busca binária
        line = self._binary_search_exact(target_id)
        
        if line:
            data = self._parse_line(line)
            if data:
                # Formato exato conforme especificação
                print("----")
                print(f"titulo: {data['titulo']}")
                print(f"autor: {data['autor']}")
                print(f"code: {data['code']}")
            else:
                print("Erro ao processar linha encontrada")
        else:
            print("ID não encontrado")
    
    def search_range(self, start_id, end_id):
        """
        Busca por range de IDs e imprime resultados conforme especificação
        
        Args:
            start_id: ID inicial do range (com ou sem prefixo "ID-")
            end_id: ID final do range (com ou sem prefixo "ID-")
        """
        # Remove 'ID-' prefix se presente
        if start_id.startswith('ID-'):
            start_id = start_id[3:]
        if end_id.startswith('ID-'):
            end_id = end_id[3:]
            
        # Imprime IDs conforme especificação
        print(f"ids: {start_id}-{end_id}")
        
        # Encontra os índices inicial e final usando busca binária
        start_index = self._binary_search_range_start(start_id)
        end_index = self._binary_search_range_end(end_id)
        
        # Verifica se encontrou registros no intervalo
        if start_index == -1 or end_index == -1 or start_index > end_index:
            print("Nenhum registro encontrado no intervalo especificado")
            return
        
        # Percorre todos os registros no intervalo
        for i in range(start_index, end_index + 1):
            line = self._read_line_at_index(i)
            data = self._parse_line(line)
            
            if data:
                # Formato exato conforme especificação
                print("----")
                print(f"id: {data['id']}")
                print(f"titulo: {data['titulo']}")
                print(f"autor: {data['autor']}")
                print(f"code: {data['code']}")
    
    def search_books(self, query):
        """
        Busca em texto completo nos livros da pasta books/
        
        Args:
            query: Termo a ser buscado
        """
        print(f"Buscando por: '{query}' nos livros...")
        
        if not os.path.exists(self.books_dir):
            print("Pasta 'books/' não encontrada")
            return
        
        book_files = glob.glob(os.path.join(self.books_dir, "*.txt"))
        
        if not book_files:
            print("Nenhum livro encontrado na pasta 'books/'")
            return
        
        found_any = False
        query_lower = query.lower()
        
        for book_file in book_files:
            try:
                with open(book_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if query_lower in content.lower():
                        filename = os.path.basename(book_file)
                        print("----")
                        print(f"arquivo: {filename}")
                        
                        # Encontra contexto da primeira ocorrência
                        lines = content.split('\n')
                        for i, line in enumerate(lines):
                            if query_lower in line.lower():
                                # Mostra algumas linhas de contexto
                                start = max(0, i - 1)
                                end = min(len(lines), i + 3)
                                context_lines = lines[start:end]
                                context = '\n'.join(context_lines)
                                
                                # Limita o contexto a 300 caracteres
                                if len(context) > 300:
                                    context = context[:300] + "..."
                                    
                                print(f"contexto: {context}")
                                found_any = True
                                break
            except (IOError, UnicodeDecodeError) as e:
                print(f"Erro ao ler arquivo {book_file}: {e}")
                continue
        
        if not found_any:
            print("Nenhuma ocorrência encontrada nos livros")
    
    def list_books(self):
        """Lista todos os livros disponíveis na pasta books/"""
        print("=== Livros Disponíveis ===")
        
        if not os.path.exists(self.books_dir):
            print("Pasta 'books/' não encontrada")
            return
        
        book_files = glob.glob(os.path.join(self.books_dir, "*.txt"))
        
        if not book_files:
            print("Nenhum livro encontrado na pasta 'books/'")
            return
        
        book_files.sort()
        for i, book_file in enumerate(book_files, 1):
            filename = os.path.basename(book_file)
            # Extrai informações do nome do arquivo se possível
            if filename.startswith("01_book_bn000167.txt"):
                title = "Memórias Póstumas de Brás Cubas"
                author = "Machado de Assis"
                print(f"{i:2d}. {title} - {author} ({filename})")
            else:
                print(f"{i:2d}. {filename}")
        
        print(f"\nTotal: {len(book_files)} livro(s)")
    
    def get_stats(self):
        """
        Retorna estatísticas do sistema
        
        Returns:
            dict: Estatísticas do sistema
        """
        total_lines = self._get_total_lines()
        file_size = self._get_file_size()
        
        # Conta livros disponíveis
        book_count = 0
        if os.path.exists(self.books_dir):
            book_files = glob.glob(os.path.join(self.books_dir, "*.txt"))
            book_count = len(book_files)
        
        return {
            'filename': self.filename,
            'total_records': total_lines,
            'file_size_bytes': file_size,
            'line_size': self.line_size,
            'estimated_max_comparisons': total_lines.bit_length(),  # log2(n)
            'books_available': book_count,
            'books_directory': self.books_dir
        }
