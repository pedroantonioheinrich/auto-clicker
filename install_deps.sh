#!/bin/bash

# Nome do ambiente virtual
VENV_NAME=".venv"

echo "=== Iniciando instalação do projeto Auto-Clicker ==="

# 1. Instala dependências do sistema Ubuntu necessárias para GUI e Automação
echo "Instalando dependências do sistema (sudo)..."
sudo apt update
sudo apt install -y python3-tk python3-venv python3-dev libx11-dev libxtst-dev

# 2. Cria o ambiente virtual
if [ ! -d "$VENV_NAME" ]; then
    echo "Criando ambiente virtual..."
    python3 -m venv "$VENV_NAME"
fi

# 3. Atualiza o pip e instala as dependências do arquivo requirements.txt
echo "Instalando pacotes Python dentro do venv..."
./$VENV_NAME/bin/pip install --upgrade pip
./$VENV_NAME/bin/pip install -r requirements.txt

echo ""
echo "----------------------------------------------------"
echo "Sucesso! Tudo foi instalado corretamente."
echo "Para ativar o ambiente e rodar o projeto:"
echo "source $VENV_NAME/bin/activate"
echo "python3 seu_arquivo_principal.py"
echo "----------------------------------------------------"