#!/usr/bin/env python3
"""
Script para criar bundle Git do projeto Knowledge Base CLI
Útil quando não há permissão para push direto no repositório
"""

import os
import subprocess
import sys
import shutil
import zipfile
from datetime import datetime
from pathlib import Path


class ProjectBundler:
    def __init__(self):
        self.project_name = "knowledge-base-cli"
        self.timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        
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
    
    def create_git_bundle(self):
        """Cria bundle Git com todo o histórico"""
        bundle_name = f"{self.project_name}-git-{self.timestamp}.bundle"
        
        print(f"📦 Criando bundle Git: {bundle_name}")
        
        success, _ = self.run_command(f"git bundle create {bundle_name} --all")
        
        if success:
            size = os.path.getsize(bundle_name) / (1024 * 1024)  # MB
            print(f"✅ Bundle Git criado: {bundle_name} ({size:.1f} MB)")
            
            # Instruções de uso
            print("\n📋 Como usar o bundle:")
            print(f"1. git clone {bundle_name} {self.project_name}")
            print(f"2. cd {self.project_name}")
            print("3. git remote set-url origin <NEW_REPO_URL>")
            print("4. git push -u origin main")
            
            return bundle_name
        else:
            print("❌ Erro ao criar bundle Git")
            return None
    
    def create_source_zip(self):
        """Cria arquivo ZIP com código fonte"""
        zip_name = f"{self.project_name}-source-{self.timestamp}.zip"
        
        print(f"📦 Criando arquivo ZIP: {zip_name}")
        
        # Lista de arquivos importantes
        important_files = [
            "cli.py",
            "knowledge_base.py",
            "fictional_books.txt",
            "introduction.md",
            "feature-01.md", 
            "feature-03.md",
            "setup_git.py",
            "deploy_github.py",
            "create_fork.py",
            "bundle_project.py",
            "requirements.txt",
            "LICENSE",
            "README.md",
            ".gitignore"
        ]
        
        # Pastas importantes
        important_dirs = [
            "books",
            "docs",
            "tests"
        ]
        
        try:
            with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                # Adiciona arquivos
                for file_path in important_files:
                    if os.path.exists(file_path):
                        zipf.write(file_path)
                        print(f"  ✅ {file_path}")
                
                # Adiciona pastas
                for dir_path in important_dirs:
                    if os.path.exists(dir_path):
                        for root, dirs, files in os.walk(dir_path):
                            for file in files:
                                file_path = os.path.join(root, file)
                                arcname = os.path.relpath(file_path)
                                zipf.write(file_path, arcname)
                        print(f"  ✅ {dir_path}/")
            
            size = os.path.getsize(zip_name) / (1024 * 1024)  # MB
            print(f"✅ Arquivo ZIP criado: {zip_name} ({size:.1f} MB)")
            
            return zip_name
            
        except Exception as e:
            print(f"❌ Erro ao criar ZIP: {e}")
            return None
    
    def create_deployment_package(self):
        """Cria pacote completo para deployment"""
        package_name = f"{self.project_name}-deploy-{self.timestamp}"
        package_dir = Path(package_name)
        
        print(f"📦 Criando pacote de deployment: {package_name}")
        
        try:
            # Cria diretório
            package_dir.mkdir(exist_ok=True)
            
            # Lista de arquivos para copiar
            files_to_copy = [
                "cli.py",
                "knowledge_base.py", 
                "fictional_books.txt",
                "requirements.txt",
                "LICENSE"
            ]
            
            # Copia arquivos principais
            for file_path in files_to_copy:
                if os.path.exists(file_path):
                    shutil.copy2(file_path, package_dir)
                    print(f"  ✅ {file_path}")
            
            # Copia pasta books se existir
            if os.path.exists("books"):
                shutil.copytree("books", package_dir / "books", dirs_exist_ok=True)
                print("  ✅ books/")
            
            # Cria README para deployment
            readme_content = f"""# Knowledge Base CLI - Deployment Package

## Quick Start

1. Instale Python 3.8+ se necessário
2. Execute o sistema:
   ```bash
   python cli.py
   ```

## Comandos Básicos

- `search ID-000001` - Busca por ID específico
- `range ID-000001 ID-000020` - Busca por intervalo  
- `books termo` - Busca nos livros
- `help` - Ajuda completa

## Arquivos Incluídos

- `cli.py` - Interface principal
- `knowledge_base.py` - Engine de busca
- `fictional_books.txt` - Dados estruturados
- `books/` - Biblioteca de livros
- `requirements.txt` - Dependências (opcional)

## Características

- ✅ Busca binária O(log n)
- ✅ {len([f for f in os.listdir('books') if f.endswith('.txt')]) if os.path.exists('books') else 0} livros incluídos
- ✅ Sem dependências externas
- ✅ Interface CLI intuitiva

## Repositório Original

https://github.com/moroni646/ct-coding-tank-ada-team-4

Gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
            
            with open(package_dir / "README.md", "w", encoding="utf-8") as f:
                f.write(readme_content)
            
            # Cria ZIP do pacote
            shutil.make_archive(package_name, 'zip', package_dir)
            
            # Remove diretório temporário
            shutil.rmtree(package_dir)
            
            zip_file = f"{package_name}.zip"
            size = os.path.getsize(zip_file) / (1024 * 1024)  # MB
            print(f"✅ Pacote criado: {zip_file} ({size:.1f} MB)")
            
            return zip_file
            
        except Exception as e:
            print(f"❌ Erro ao criar pacote: {e}")
            return None
    
    def create_installation_script(self):
        """Cria script de instalação automática"""
        script_name = f"install-{self.project_name}.py"
        
        script_content = f'''#!/usr/bin/env python3
"""
Script de instalação automática do Knowledge Base CLI
Gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

import os
import urllib.request
import zipfile
import sys

def download_and_install():
    """Baixa e instala o Knowledge Base CLI"""
    print("🚀 Knowledge Base CLI - Instalação")
    print("="*40)
    
    # URLs dos arquivos (ajustar conforme necessário)
    base_url = "https://github.com/SEU_USUARIO/SEU_REPOSITORIO/raw/main"
    files_to_download = [
        "cli.py",
        "knowledge_base.py",
        "fictional_books.txt",
        "requirements.txt"
    ]
    
    print("📥 Baixando arquivos...")
    for filename in files_to_download:
        url = f"{{base_url}}/{{filename}}"
        try:
            urllib.request.urlretrieve(url, filename)
            print(f"  ✅ {{filename}}")
        except Exception as e:
            print(f"  ❌ {{filename}}: {{e}}")
    
    print("\\n✅ Instalação concluída!")
    print("\\n🎯 Execute: python cli.py")

if __name__ == "__main__":
    download_and_install()
'''
        
        with open(script_name, "w", encoding="utf-8") as f:
            f.write(script_content)
        
        print(f"✅ Script de instalação criado: {script_name}")
        return script_name
    
    def show_summary(self, created_files):
        """Mostra resumo dos arquivos criados"""
        print("\n" + "="*60)
        print("📦 ARQUIVOS CRIADOS")
        print("="*60)
        
        total_size = 0
        for file_path in created_files:
            if file_path and os.path.exists(file_path):
                size = os.path.getsize(file_path) / (1024 * 1024)  # MB
                total_size += size
                print(f"📄 {file_path} ({size:.1f} MB)")
        
        print("="*60)
        print(f"📊 Total: {len(created_files)} arquivo(s), {total_size:.1f} MB")
        print("\n💡 Dicas:")
        print("• Use o bundle Git para preservar histórico")
        print("• Use o ZIP source para código completo")  
        print("• Use o pacote deploy para distribuição")
        print("• Compartilhe via email, drive, ou transfer")
        print("="*60)
    
    def run(self):
        """Executa criação de todos os bundles"""
        print("📦 Knowledge Base CLI - Criador de Bundles")
        print("="*50)
        
        created_files = []
        
        # Verifica se está em repositório Git
        if os.path.exists('.git'):
            bundle_file = self.create_git_bundle()
            if bundle_file:
                created_files.append(bundle_file)
        else:
            print("⚠️ Não é um repositório Git - pulando bundle Git")
        
        # Cria ZIP com código fonte
        zip_file = self.create_source_zip()
        if zip_file:
            created_files.append(zip_file)
        
        # Cria pacote de deployment
        deploy_file = self.create_deployment_package()
        if deploy_file:
            created_files.append(deploy_file)
        
        # Cria script de instalação
        install_script = self.create_installation_script()
        if install_script:
            created_files.append(install_script)
        
        # Mostra resumo
        self.show_summary(created_files)
        
        return len(created_files) > 0


def main():
    """Função principal"""
    bundler = ProjectBundler()
    
    try:
        success = bundler.run()
        if success:
            sys.exit(0)
        else:
            print("❌ Nenhum bundle foi criado")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n⏸️ Operação cancelada")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
