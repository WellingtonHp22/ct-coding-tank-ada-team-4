#!/usr/bin/env python3
"""
Script de instalação automática do Knowledge Base CLI
Gerado em: 2025-06-03 20:19:04
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
        url = f"{base_url}/{filename}"
        try:
            urllib.request.urlretrieve(url, filename)
            print(f"  ✅ {filename}")
        except Exception as e:
            print(f"  ❌ {filename}: {e}")
    
    print("\n✅ Instalação concluída!")
    print("\n🎯 Execute: python cli.py")

if __name__ == "__main__":
    download_and_install()
