#!/usr/bin/env python3
"""
Deploy automático para GitHub - Knowledge Base CLI
Repositório: https://github.com/moroni646/ct-coding-tank-ada-team-4

Este script automatiza o processo de upload do projeto para o GitHub,
incluindo configuração de repositório, commit e push.
"""

import os
import subprocess
import sys
from datetime import datetime


class GitHubDeployer:
    def __init__(self):
        self.repo_url = "https://github.com/moroni646/ct-coding-tank-ada-team-4"
        self.repo_name = "ct-coding-tank-ada-team-4"
        self.branch = "main"
        self.project_root = os.path.dirname(os.path.abspath(__file__))
        
    def run_command(self, command, capture_output=False):
        """Executa comando no shell"""
        try:
            print(f"🔧 Executando: {command}")
            if capture_output:
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                return result.returncode == 0, result.stdout.strip()
            else:
                result = subprocess.run(command, shell=True)
                return result.returncode == 0, ""
        except Exception as e:
            print(f"❌ Erro ao executar comando: {e}")
            return False, str(e)
    
    def check_git_installed(self):
        """Verifica se Git está instalado"""
        success, output = self.run_command("git --version", capture_output=True)
        if success:
            print(f"✅ Git encontrado: {output}")
            return True
        else:
            print("❌ Git não está instalado! Por favor, instale o Git primeiro.")
            print("   Download: https://git-scm.com/downloads")
            return False
    
    def check_git_config(self):
        """Verifica configuração do Git"""
        success, user_name = self.run_command("git config --global user.name", capture_output=True)
        success2, user_email = self.run_command("git config --global user.email", capture_output=True)
        
        if not success or not success2 or not user_name or not user_email:
            print("⚠️ Configuração do Git incompleta!")
            print("Configure suas credenciais:")
            print('   git config --global user.name "Seu Nome"')
            print('   git config --global user.email "seu.email@exemplo.com"')
            return False
        
        print(f"✅ Git configurado para: {user_name} <{user_email}>")
        return True
    
    def initialize_repo(self):
        """Inicializa repositório Git se necessário"""
        if os.path.exists('.git'):
            print("✅ Repositório Git já existe")
            return True
        
        print("🆕 Inicializando repositório Git...")
        success, _ = self.run_command("git init")
        if not success:
            print("❌ Falha ao inicializar repositório")
            return False
        
        # Configura branch principal
        success, _ = self.run_command(f"git branch -M {self.branch}")
        return success
    
    def add_remote(self):
        """Adiciona remote origin se necessário"""
        success, output = self.run_command("git remote -v", capture_output=True)
        
        if "origin" in output:
            print("✅ Remote origin já configurado")
            return True
        
        print("🔗 Adicionando remote origin...")
        success, _ = self.run_command(f"git remote add origin {self.repo_url}")
        if not success:
            print("❌ Falha ao adicionar remote")
            return False
        
        return True
    
    def create_gitignore(self):
        """Cria arquivo .gitignore se não existir"""
        gitignore_path = ".gitignore"
        
        if os.path.exists(gitignore_path):
            print("✅ .gitignore já existe")
            return
        
        print("📝 Criando .gitignore...")
        gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Project specific
*.log
temp/
cache/
backup/

# Sensitive data
config.ini
secrets.json
"""
        
        with open(gitignore_path, 'w', encoding='utf-8') as f:
            f.write(gitignore_content)
        
        print("✅ .gitignore criado")
    
    def create_readme(self):
        """Cria README.md se não existir"""
        readme_path = "README.md"
        
        if os.path.exists(readme_path):
            print("✅ README.md já existe")
            return
        
        print("📝 Criando README.md...")
        readme_content = f"""# Knowledge Base CLI - Sistema de Busca Inteligente

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
git clone {self.repo_url}
cd {self.repo_name}

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

### v1.0.0 - {datetime.now().strftime('%Y-%m-%d')}
- ✅ Implementação da busca binária
- ✅ Interface CLI completa
- ✅ Acervo de literatura brasileira
- ✅ Documentação completa
- ✅ Scripts de deploy automatizado

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👥 Equipe

- **Desenvolvimento**: Ada Coding Tank Team 4
- **Repositório**: {self.repo_url}
- **Documentação**: [Ver docs/](docs/)

## 📞 Suporte

- **Issues**: [GitHub Issues]({self.repo_url}/issues)
- **Documentação**: [Wiki]({self.repo_url}/wiki)
- **Email**: team4@codingtak.ada.tech

---

⭐ Se este projeto te ajudou, considere dar uma estrela no GitHub!
"""
        
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        print("✅ README.md criado")
    
    def stage_files(self):
        """Adiciona arquivos ao staging"""
        print("📦 Adicionando arquivos...")
        
        # Lista de arquivos importantes
        important_files = [
            "cli.py",
            "knowledge_base.py", 
            "fictional_books.txt",
            "README.md",
            ".gitignore",
            "introduction.md",
            "feature-01.md",
            "feature-03.md",
            "deploy_github.py",
            "setup_git.py",
            "requirements.txt"
        ]
        
        # Adiciona arquivos que existem
        for file in important_files:
            if os.path.exists(file):
                success, _ = self.run_command(f"git add {file}")
                if success:
                    print(f"  ✅ {file}")
                else:
                    print(f"  ❌ {file}")
        
        # Adiciona pasta books se existir
        if os.path.exists("books"):
            success, _ = self.run_command("git add books/")
            if success:
                print("  ✅ books/")
        
        return True
    
    def commit_changes(self):
        """Faz commit das mudanças"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        commit_message = f"Knowledge Base CLI - Deploy automático {timestamp}"
        
        print(f"💾 Fazendo commit: {commit_message}")
        success, _ = self.run_command(f'git commit -m "{commit_message}"')
        
        if not success:
            print("⚠️ Nada para commitar ou erro no commit")
            return False
        
        return True
    
    def push_to_github(self):
        """Faz push para o GitHub"""
        print(f"🚀 Fazendo push para {self.repo_url}...")
        success, _ = self.run_command(f"git push -u origin {self.branch}")
        
        if not success:
            print("❌ Falha no push. Verifique suas credenciais do GitHub")
            print("   Você pode precisar de um Personal Access Token")
            print("   https://github.com/settings/tokens")
            return False
        
        return True
    
    def deploy(self):
        """Executa o deploy completo"""
        print("🚀 Iniciando deploy para GitHub...")
        print("=" * 50)
        
        # Verifica pré-requisitos
        if not self.check_git_installed():
            return False
        
        if not self.check_git_config():
            return False
        
        # Configura repositório
        if not self.initialize_repo():
            return False
        
        if not self.add_remote():
            return False
        
        # Cria arquivos necessários
        self.create_gitignore()
        self.create_readme()
        
        # Faz deploy
        if not self.stage_files():
            return False
        
        if not self.commit_changes():
            print("⚠️ Continuando sem commit...")
        
        if not self.push_to_github():
            return False
        
        print("=" * 50)
        print("🎉 Deploy concluído com sucesso!")
        print(f"📂 Repositório: {self.repo_url}")
        print(f"🌐 Acesse: {self.repo_url}")
        print("=" * 50)
        
        return True


def main():
    """Função principal"""
    print("🚀 Knowledge Base CLI - Deploy para GitHub")
    print("Repositório: https://github.com/moroni646/ct-coding-tank-ada-team-4")
    print()
    
    deployer = GitHubDeployer()
    
    try:
        success = deployer.deploy()
        if success:
            sys.exit(0)
        else:
            print("❌ Deploy falhou!")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n⏸️ Deploy cancelado pelo usuário")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
