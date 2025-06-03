#!/usr/bin/env python3
"""
Configuração inicial do Git para o projeto Knowledge Base CLI
Repositório: https://github.com/moroni646/ct-coding-tank-ada-team-4

Este script configura o ambiente Git local e prepara o projeto
para sincronização com o repositório remoto.
"""

import os
import subprocess
import sys


class GitSetup:
    def __init__(self):
        self.repo_url = "https://github.com/moroni646/ct-coding-tank-ada-team-4"
        self.repo_name = "ct-coding-tank-ada-team-4"
        
    def run_command(self, command, capture_output=False):
        """Executa comando no shell"""
        try:
            print(f"🔧 {command}")
            if capture_output:
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                return result.returncode == 0, result.stdout.strip()
            else:
                result = subprocess.run(command, shell=True)
                return result.returncode == 0, ""
        except Exception as e:
            print(f"❌ Erro: {e}")
            return False, str(e)
    
    def check_git(self):
        """Verifica se Git está disponível"""
        success, version = self.run_command("git --version", capture_output=True)
        if success:
            print(f"✅ {version}")
            return True
        else:
            print("❌ Git não encontrado!")
            print("   Instale em: https://git-scm.com/downloads")
            return False
    
    def configure_git(self):
        """Configura credenciais do Git"""
        print("\n🔧 Configurando Git...")
        
        # Verifica configuração atual
        success, current_name = self.run_command("git config --global user.name", capture_output=True)
        success2, current_email = self.run_command("git config --global user.email", capture_output=True)
        
        if success and success2 and current_name and current_email:
            print(f"✅ Git já configurado:")
            print(f"   Nome: {current_name}")
            print(f"   Email: {current_email}")
            
            resposta = input("\n🤔 Deseja alterar a configuração? (s/N): ").lower()
            if resposta not in ['s', 'sim', 'y', 'yes']:
                return True
        
        # Solicita dados do usuário
        print("\n📝 Digite suas credenciais do Git:")
        name = input("   Nome completo: ").strip()
        email = input("   Email: ").strip()
        
        if not name or not email:
            print("❌ Nome e email são obrigatórios!")
            return False
        
        # Configura Git
        success1, _ = self.run_command(f'git config --global user.name "{name}"')
        success2, _ = self.run_command(f'git config --global user.email "{email}"')
        
        if success1 and success2:
            print("✅ Git configurado com sucesso!")
            return True
        else:
            print("❌ Erro ao configurar Git")
            return False
    
    def setup_repository(self):
        """Configura repositório local"""
        print("\n📁 Configurando repositório local...")
        
        # Inicializa Git se necessário
        if not os.path.exists('.git'):
            print("🆕 Inicializando repositório...")
            success, _ = self.run_command("git init")
            if not success:
                return False
        else:
            print("✅ Repositório já existe")
        
        # Configura branch principal
        success, _ = self.run_command("git branch -M main")
        if not success:
            print("⚠️ Aviso: Não foi possível configurar branch main")
        
        # Adiciona remote se necessário
        success, remotes = self.run_command("git remote -v", capture_output=True)
        
        if "origin" not in remotes:
            print("🔗 Adicionando remote origin...")
            success, _ = self.run_command(f"git remote add origin {self.repo_url}")
            if not success:
                print("❌ Erro ao adicionar remote")
                return False
        else:
            print("✅ Remote origin já configurado")
        
        return True
    
    def create_requirements(self):
        """Cria arquivo requirements.txt"""
        requirements_path = "requirements.txt"
        
        if os.path.exists(requirements_path):
            print("✅ requirements.txt já existe")
            return
        
        print("📝 Criando requirements.txt...")
        requirements_content = """# Knowledge Base CLI - Dependências

# Core dependencies
# Nenhuma dependência externa necessária para a versão básica
# O projeto usa apenas a biblioteca padrão do Python

# Desenvolvimento (opcional)
pytest>=7.0.0
black>=22.0.0
flake8>=5.0.0

# Futuras funcionalidades (Feature-003)
# fastapi>=0.100.0
# uvicorn>=0.20.0
# redis>=4.5.0
# psycopg2-binary>=2.9.0
# elasticsearch>=8.0.0

# Deploy e CI/CD
# github3.py>=4.0.0
# python-dotenv>=1.0.0
"""
        
        with open(requirements_path, 'w', encoding='utf-8') as f:
            f.write(requirements_content)
        
        print("✅ requirements.txt criado")
    
    def create_license(self):
        """Cria arquivo LICENSE"""
        license_path = "LICENSE"
        
        if os.path.exists(license_path):
            print("✅ LICENSE já existe")
            return
        
        print("📝 Criando LICENSE (MIT)...")
        license_content = f"""MIT License

Copyright (c) 2024 Ada Coding Tank Team 4

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
        
        with open(license_path, 'w', encoding='utf-8') as f:
            f.write(license_content)
        
        print("✅ LICENSE criado")
    
    def show_next_steps(self):
        """Mostra próximos passos"""
        print("\n" + "="*50)
        print("🎉 Configuração concluída!")
        print("="*50)
        print("\n📋 Próximos passos:")
        print("1. Execute o deploy:")
        print("   python deploy_github.py")
        print()
        print("2. Ou use comandos Git manuais:")
        print("   git add .")
        print("   git commit -m 'Initial commit'")
        print("   git push -u origin main")
        print()
        print("3. Acesse o repositório:")
        print(f"   {self.repo_url}")
        print()
        print("4. Execute o sistema:")
        print("   python cli.py")
        print("="*50)
    
    def setup(self):
        """Executa configuração completa"""
        print("🛠️ Knowledge Base CLI - Configuração do Git")
        print(f"📂 Repositório: {self.repo_url}")
        print("="*50)
        
        # Verifica Git
        if not self.check_git():
            return False
        
        # Configura credenciais
        if not self.configure_git():
            return False
        
        # Configura repositório
        if not self.setup_repository():
            return False
        
        # Cria arquivos auxiliares
        self.create_requirements()
        self.create_license()
        
        # Mostra próximos passos
        self.show_next_steps()
        
        return True


def main():
    """Função principal"""
    setup = GitSetup()
    
    try:
        success = setup.setup()
        if success:
            sys.exit(0)
        else:
            print("❌ Configuração falhou!")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n⏸️ Configuração cancelada")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
