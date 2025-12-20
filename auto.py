import pyautogui 
import tkinter as tk
from pynput import mouse 
import time
import threading


janela = tk.Tk()
janela.title("AutoClick by @streetegist") 
janela.geometry("400x200")


clicking = False
posicao_x = 0
posicao_y = 0
contador = 0

def loop_clique():
    global clicking, posicao_x, posicao_y, contador
    
    # Armazena a posição onde o clique deveria ocorrer
    alvo_x, alvo_y = posicao_x, posicao_y   
    # Margem de erro (pixels) para evitar que tremores parem o script
    tolerancia = 10 
    while clicking:
        # Pega a posição ATUAL do mouse no exato momento
        atual_x, atual_y = pyautogui.position()
        
        # Verifica se o mouse saiu da posição alvo
        if abs(atual_x - alvo_x) > tolerancia or abs(atual_y - alvo_y) > tolerancia:
            parar_tudo()
            break
            
        pyautogui.click(alvo_x, alvo_y)
        contador_status.config(text=f'clique: {contador}', fg="black")
        contador = contador + 1
        print(f'Clicado em {alvo_x} e {alvo_y}')
        time.sleep(5) # Intervalo

def parar_tudo():
    global clicking, contador, posicao_x, posicao_y
    clicking = False
    contador = 0
    posicao_x = 0
    posicao_y = 0
    contador_status.pack_forget()
    label_status4.pack_forget()
    btn_fechar.pack_forget()
    label_status3.pack_forget()
    label_status.pack(pady=5)
    label_status.config(text="Status: STOPED", fg="red")
    btn_start.config(text="Restart", bg="blue",fg="white", state="normal")

def ao_clicar(x, y, botao, pressionado):
    global posicao_x, posicao_y, clicking
    if pressionado:
        label_status.pack_forget()
        label_status4.pack()
        contador_status.pack()
        btn_start.pack()
        btn_fechar.pack_forget()
        label_status3.pack(pady=1)
        posicao_x, posicao_y = x, y
        clicking = True
        label_status4.config(text=f"Target defined (x:{x} e y:{y})\nIs Running...\nDon't Move the Cursor!", fg="red")
        btn_start.config(text="Running...", bg="green", fg="white", state="disabled")
        # Dispara os cliques em uma linha de execução separada (Thread)
        threading.Thread(target=loop_clique, daemon=True).start()
        
        # Retorna False para fechar o Listener (ele já cumpriu o papel de pegar a coordenada)
        return False

def coordenadas():
    with mouse.Listener(on_click=ao_clicar) as ouvinte:
        ouvinte.join() # escuta o evento de click do mouse pra pegar a posição
        print(f'Ouvinte: {ouvinte}')

def preparar_captura():
    label_status.config(text="CLICK SOMEWHERE ON THE SCREEN", fg="black", bg="yellow")
    label_status2 = tk.Label(janela, text="")
    label_status2.pack(pady=1)
    btn_start.pack_forget()
    btn_fechar.pack_forget()

    # Inicia o ouvinte em background
    threading.Thread(target=coordenadas, daemon=True).start()


label_status = tk.Label(janela, text="1. Click START and 'Select The Area'\n2. Click Wherever You Want The AutoClick", fg="blue")
label_status.pack(pady=10)

label_status4 = tk.Label()

contador_status = tk.Label(janela)

label_status3 = tk.Label(janela, text="Move the cursor to STOP the program!")

btn_start = tk.Button(janela, text="Start", command=preparar_captura, bg="blue")
btn_start.pack(pady=1)

btn_fechar = tk.Button(janela, text="Close", command=parar_tudo, bg="grey")
btn_fechar.pack(pady=1)

janela.mainloop()
