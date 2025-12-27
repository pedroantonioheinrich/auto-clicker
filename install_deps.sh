#!/bin/bash

# Nome padrão do ambiente virtual (com ponto para ser oculto)
VENV_NAME=".venv"

echo "=== Ajustando e instalando dependências do Auto-Clicker ==="

# 1. Se existir uma pasta 'venv' sem ponto, vamos renomear para '.venv'
if [ -d "venv" ] && [ ! -d ".venv" ]; then
    echo "Renomeando pasta 'venv' para '.venv' para seguir o padrão..."
    mv venv .venv
fi

# 2. Instala dependências do sistema
sudo apt update && sudo apt install -y python3-tk python3-venv python3-dev libx11-dev libxtst-dev

# 3. Cria o ambiente virtual se não existir
if [ ! -d "$VENV_NAME" ]; then
    python3 -m venv "$VENV_NAME"
fi

# 4. Instala os pacotes
echo "Instalando pacotes no ambiente $VENV_NAME..."
./$VENV_NAME/bin/pip install --upgrade pip
./$VENV_NAME/bin/pip install -r requirements.txt

echo "----------------------------------------------------"
echo "Pronto! Agora use sempre:"
echo "source .venv/bin/activate"
echo "----------------------------------------------------"