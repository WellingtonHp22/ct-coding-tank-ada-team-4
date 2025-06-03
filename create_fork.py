#!/usr/bin/env python3
"""
Script para criar fork ou novo repositório quando não há permissão de push
Knowledge Base CLI - Alternativas de Deploy

Este script oferece várias opções quando você não tem permissão para
fazer push no repositório original.
"""

import os
import subprocess
import sys
import json
from datetime import datetime


class GitHubAlternative:
    def __init__(self):
        self.original_repo = "https://github.com/moroni646/ct-coding-tank-ada-team-4"
        self.original_owner = "moroni646"
        self.original_name = "ct-coding-tank-ada-team-4"
        
    def run_command(self, command, capture_output=False):
        """Executa comando no shell"""
        try:
            if capture_output:
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                return result.returncode == 0, result.stdout.strip()
            else:
                result = subprocess.run(command, shell=True)
                return result.returncode == 0, ""
        except Exception as e:
            print(f"❌ Erro: {e}")
            return False, str(e)
    
    def check_gh_cli(self):
        """Verifica se GitHub CLI está instalado"""
        success, output = self.run_command("gh --version", capture_output=True)
        if success:
            print(f"✅ GitHub CLI encontrado: {output.split()[0]}")
            return True
        else:
            print("⚠️ GitHub CLI não encontrado")
            print("   Instale em: https://cli.github.com/")
            return False
    
    def check_git_auth(self):
        """Verifica autenticação do Git"""
        success, output = self.run_command("gh auth status", capture_output=True)
        if success and "Logged in" in output:
            print("✅ Autenticado no GitHub")
            return True
        else:
            print("⚠️ Não autenticado no GitHub")
            print("   Execute: gh auth login")
            return False
    
    def create_fork(self):
        """Cria fork do repositório original"""
        print(f"🍴 Criando fork de {self.original_repo}...")
        
        # Tenta criar fork
        success, output = self.run_command(f"gh repo fork {self.original_repo} --clone=false", capture_output=True)
        
        if success:
            print("✅ Fork criado com sucesso!")
            # Obtém URL do fork
            success, username = self.run_command("gh api user --jq .login", capture_output=True)
            if success:
                fork_url = f"https://github.com/{username}/{self.original_name}"
                print(f"📂 Fork disponível em: {fork_url}")
                return fork_url
        else:
            print(f"❌ Erro ao criar fork: {output}")
            return None
    
    def create_new_repo(self, repo_name=None):
        """Cria novo repositório"""
        if not repo_name:
            repo_name = f"knowledge-base-cli-{datetime.now().strftime('%Y%m%d')}"
        
        print(f"🆕 Criando novo repositório: {repo_name}...")
        
        # Cria repositório
        success, output = self.run_command(
            f'gh repo create {repo_name} --public --description "Knowledge Base CLI - Sistema de Busca Inteligente"',
            capture_output=True
        )
        
        if success:
            print("✅ Repositório criado com sucesso!")
            success, username = self.run_command("gh api user --jq .login", capture_output=True)
            if success:
                new_repo_url = f"https://github.com/{username}/{repo_name}"
                print(f"📂 Repositório disponível em: {new_repo_url}")
                return new_repo_url
        else:
            print(f"❌ Erro ao criar repositório: {output}")
            return None
    
    def update_remote(self, new_repo_url):
        """Atualiza remote origin para novo repositório"""
        print(f"🔗 Atualizando remote para: {new_repo_url}")
        
        # Remove remote atual
        self.run_command("git remote remove origin")
        
        # Adiciona novo remote
        success, _ = self.run_command(f"git remote add origin {new_repo_url}")
        
        if success:
            print("✅ Remote atualizado com sucesso!")
            return True
        else:
            print("❌ Erro ao atualizar remote")
            return False
    
    def push_to_new_repo(self, repo_url):
        """Faz push para o novo repositório"""
        print(f"🚀 Fazendo push para {repo_url}...")
        
        success, _ = self.run_command("git push -u origin main")
        
        if success:
            print("✅ Push realizado com sucesso!")
            print(f"🌐 Acesse: {repo_url}")
            return True
        else:
            print("❌ Erro no push")
            return False
    
    def create_bundle(self):
        """Cria bundle Git para transferência manual"""
        bundle_name = f"knowledge-base-cli-{datetime.now().strftime('%Y%m%d-%H%M%S')}.bundle"
        
        print(f"📦 Criando bundle: {bundle_name}")
        
        success, _ = self.run_command(f"git bundle create {bundle_name} --all")
        
        if success:
            print(f"✅ Bundle criado: {bundle_name}")
            print("📋 Para usar o bundle:")
            print(f"   git clone {bundle_name} knowledge-base-cli")
            print("   cd knowledge-base-cli")
            print("   git remote set-url origin <NEW_REPO_URL>")
            print("   git push -u origin main")
            return bundle_name
        else:
            print("❌ Erro ao criar bundle")
            return None
    
    def show_manual_steps(self):
        """Mostra passos manuais para deploy"""
        print("\n" + "="*60)
        print("📋 PASSOS MANUAIS PARA DEPLOY")
        print("="*60)
        print("\n1. 🍴 CRIAR FORK (Recomendado):")
        print(f"   • Acesse: {self.original_repo}")
        print("   • Clique em 'Fork' no canto superior direito")
        print("   • Aguarde a criação do fork")
        print("   • Copie a URL do seu fork")
        print("\n2. 🔗 ATUALIZAR REMOTE:")
        print("   git remote set-url origin <SEU_FORK_URL>")
        print("\n3. 🚀 FAZER PUSH:")
        print("   git push -u origin main")
        print("\n4. 🆕 CRIAR NOVO REPOSITÓRIO:")
        print("   • Acesse: https://github.com/new")
        print("   • Nome: knowledge-base-cli")
        print("   • Descrição: Sistema de Busca Inteligente")
        print("   • Tipo: Público")
        print("   • Clique em 'Create repository'")
        print("\n5. 📞 SOLICITAR COLABORAÇÃO:")
        print("   • Contate o dono do repositório original")
        print("   • Solicite acesso como colaborador")
        print("   • Aguarde convite por email")
        print("\n" + "="*60)
    
    def show_menu(self):
        """Mostra menu de opções"""
        print("\n🔧 SOLUÇÕES PARA PROBLEMA DE PERMISSÃO")
        print("="*50)
        print("1. 🍴 Criar fork do repositório original")
        print("2. 🆕 Criar novo repositório")
        print("3. 📦 Criar bundle para transferência")
        print("4. 📋 Ver passos manuais")
        print("5. ❌ Sair")
        print("="*50)
        
        choice = input("\nEscolha uma opção (1-5): ").strip()
        return choice
    
    def run(self):
        """Executa o script principal"""
        print("🚀 Knowledge Base CLI - Soluções de Deploy")
        print(f"⚠️ Problema: Sem permissão para {self.original_repo}")
        print("="*60)
        
        # Verifica se está em um repositório Git
        if not os.path.exists('.git'):
            print("❌ Não estamos em um repositório Git!")
            print("   Execute primeiro: python setup_git.py")
            return False
        
        while True:
            choice = self.show_menu()
            
            if choice == "1":
                # Criar fork
                if self.check_gh_cli() and self.check_git_auth():
                    fork_url = self.create_fork()
                    if fork_url:
                        if self.update_remote(fork_url):
                            self.push_to_new_repo(fork_url)
                else:
                    print("⚠️ GitHub CLI necessário para esta opção")
                    self.show_manual_steps()
                break
                
            elif choice == "2":
                # Criar novo repositório
                if self.check_gh_cli() and self.check_git_auth():
                    repo_name = input("Nome do repositório (Enter para auto): ").strip()
                    new_repo_url = self.create_new_repo(repo_name or None)
                    if new_repo_url:
                        if self.update_remote(new_repo_url):
                            self.push_to_new_repo(new_repo_url)
                else:
                    print("⚠️ GitHub CLI necessário para esta opção")
                    self.show_manual_steps()
                break
                
            elif choice == "3":
                # Criar bundle
                self.create_bundle()
                break
                
            elif choice == "4":
                # Passos manuais
                self.show_manual_steps()
                break
                
            elif choice == "5":
                # Sair
                print("👋 Saindo...")
                break
                
            else:
                print("❌ Opção inválida! Tente novamente.")
        
        return True


def main():
    """Função principal"""
    alternative = GitHubAlternative()
    
    try:
        success = alternative.run()
        if success:
            sys.exit(0)
        else:
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n⏸️ Operação cancelada")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
