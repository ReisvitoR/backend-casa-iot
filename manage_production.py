#!/usr/bin/env python
"""
Script de gerenciamento para produção usando Uvicorn para melhor performance ASGI.
"""
import os
import sys

if __name__ == '__main__':
    """Run administrative tasks with production settings."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config-admin.settings_production')
    
    if len(sys.argv) > 1 and sys.argv[1] == 'runserver':
        # Para produção, usar Uvicorn em vez do runserver
        print("🚀 Iniciando servidor de produção com Uvicorn...")
        print("📍 Acesse: http://localhost:8000")
        print("🛑 Pare com Ctrl+C")
        
        # Executar com Uvicorn
        import subprocess
        subprocess.run([
            sys.executable, '-m', 'uvicorn', 
            'config-admin.asgi:application',
            '--host', '0.0.0.0',
            '--port', '8000',
            '--reload'  # Remove em produção real
        ])
    else:
        # Para outros comandos Django
        try:
            from django.core.management import execute_from_command_line
        except ImportError as exc:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            ) from exc
        execute_from_command_line(sys.argv)
