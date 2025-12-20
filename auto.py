import pyautogui 
import tkinter as tk
from pynput import mouse 
import time
import threading


janela = tk.Tk()
janela.title("AutoClick by Pedro") 
janela.geometry("400x200")

clicking = False
posicao_x = 0
posicao_y = 0

def loop_clique():
    global clicking, posicao_x, posicao_y
    
    # Armazena a posição onde o clique deveria ocorrer
    alvo_x, alvo_y = posicao_x, posicao_y
    
    # Margem de erro (pixels) para evitar que tremores parem o script
    tolerancia = 10 
    print(f'Posições iniciais: {posicao_x} e {posicao_y}')
    print(f'Clicking Bool fora do while: {clicking}')
    while clicking:
        print(f'Clicking Bool dentro do while: {clicking}')
        # Pega a posição ATUAL do mouse no exato momento
        atual_x, atual_y = pyautogui.position()
        
        # Verifica se o mouse saiu da posição alvo
        if abs(atual_x - alvo_x) > tolerancia or abs(atual_y - alvo_y) > tolerancia:
            print("Movimento detectado! Parando autoclick por segurança.")
            clicking = False 
            posicao_x = 0
            posicao_y = 0
            parar_tudo()
            print(f'Depois do movimento do mouse, Clicking é {clicking}, X: {posicao_x}, Y: {posicao_y}')
            break
            
        pyautogui.click(alvo_x, alvo_y)
        print(f'Clicado em {alvo_x} e {alvo_y}')
        time.sleep(5) # Intervalo

def parar_tudo():
    global clicking
    clicking = False
    label_status.config(text="Status: PARADO", fg="red")

def ao_clicar(x, y, botao, pressionado):
    global posicao_x, posicao_y, clicking
    if pressionado:
        posicao_x, posicao_y = x, y
        clicking = True
        label_status.config(text=f"Alvo definido em {x}, {y}\nIniciando...", fg="green")
        
        # Dispara os cliques em uma linha de execução separada (Thread)
        threading.Thread(target=loop_clique, daemon=True).start()
        
        # Retorna False para fechar o Listener (ele já cumpriu o papel de pegar a coordenada)
        return False

def coordenadas():
    with mouse.Listener(on_click=ao_clicar) as ouvinte:
        ouvinte.join() # escuta o evento de click do mouse pra pegar a posição
        print(f'Ouvinte: {ouvinte}')


    
def preparar_captura():
    label_status.config(text="CLIQUE ONDE DESEJA O AUTOCLICK", fg="orange")
    # Inicia o ouvinte em background
    threading.Thread(target=coordenadas, daemon=True).start()


print("Monitorando cliques... (Pressione Ctrl+C no terminal para parar)")

label_status = tk.Label(janela, text="1. Clique em 'Selecionar Área'\n2. Clique onde deseja o AutoClick", fg="blue")
label_status.pack(pady=10)

btn_coordenadas = tk.Button(janela, text="Posição X,Y", command=preparar_captura, bg="lightgreen")
btn_coordenadas.pack(pady=5)

btn_fechar = tk.Button(janela, text="Fechar Programa", command=parar_tudo)
btn_fechar.pack(pady=5)

janela.mainloop()
