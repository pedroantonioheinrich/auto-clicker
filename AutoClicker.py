import pyautogui 
from pynput import mouse 
import time
import threading
import customtkinter as ct

class App(ct.CTk):
    clicking = False
    posicao_x = 0
    posicao_y = 0
    contador = 0
    tempoInterval = 0
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.title("AutoClick by @streetegist")

        def loop_clique():
            self.clicking, self.posicao_x, self.posicao_y, self.contador, self.tempoInterval
            
            # Armazena a posição onde o clique deveria ocorrer
            alvo_x, alvo_y = self.posicao_x, self.posicao_y   
            # Margem de erro (pixels) para evitar que tremores parem o script
            tolerancia = 10 
            while self.clicking:
                # Pega a posição ATUAL do mouse no exato momento
                atual_x, atual_y = pyautogui.position()
                
                # Verifica se o mouse saiu da posição alvo
                if abs(atual_x - alvo_x) > tolerancia or abs(atual_y - alvo_y) > tolerancia:
                    parar_tudo()
                    break
                    
                pyautogui.click(alvo_x, alvo_y)
                contador_status.configure(text=f'clique: {self.contador}')
                self.contador = self.contador + 1
                print(f'Clicado em {alvo_x} e {alvo_y}')
                time.sleep(capturar_texto()) # Intervalo

        def parar_tudo():
            self.clicking, self.contador, self.posicao_x,  self.posicao_y
            self.clicking = False
            self.contador = 0
            self.posicao_x = 0
            self.posicao_y = 0
            contador_status.pack_forget()
            label_status4.pack_forget()
            btn_fechar.pack_forget()
            label_status3.pack_forget()
            label_status.pack(pady=5)
            label_status.configure(text="Status: STOPED")
            btn_start.configure(text="Restart", state="normal")

        def ao_clicar(x, y, botao, pressionado):
            self.posicao_x, self.posicao_y, self.clicking
            if pressionado:
                label_input.pack_forget()
                inputTime.pack_forget()
                label_status.pack_forget()
                label_status4.pack()
                contador_status.pack()
                btn_start.pack()
                btn_fechar.pack_forget()
                label_status3.pack(pady=1)
                self.posicao_x, self.posicao_y = x, y
                self.clicking = True
                label_status4.configure(text=f"Target defined (x:{x} e y:{y})\nIs Running...\nDon't Move the Cursor!")
                btn_start.configure(text="Running...", state="disabled")
                # Dispara os cliques em uma linha de execução separada (Thread)
                threading.Thread(target=loop_clique, daemon=True).start()
                
                # Retorna False para fechar o Listener (ele já cumpriu o papel de pegar a coordenada)
                return False

        def coordenadas():
            with mouse.Listener(on_click=ao_clicar) as ouvinte:
                ouvinte.join() # escuta o evento de click do mouse pra pegar a posição
                print(f'Ouvinte: {ouvinte}')

        def preparar_captura():
            label_status.configure(text="CLICK SOMEWHERE ON THE SCREEN")
            label_status2 = ct.CTkLabel(master=self, text="")
            label_status2.pack(pady=1)
            btn_start.pack_forget()
            btn_fechar.pack_forget()
            label_input.pack_forget()
            inputTime.pack_forget()

            # Inicia o ouvinte em background
            threading.Thread(target=coordenadas, daemon=True).start()

        def fechar():
            self.destroy()

        def capturar_texto():
            global tempoInterval
            texto = inputTime.get()
            tempoInterval = texto
            return int(tempoInterval)

        label_input = ct.CTkLabel(master=self, text='Click Interval in Minutes\n(Numbers Only)')
        label_input.pack(pady=7)
        inputTime = ct.CTkEntry(master=self, width=30)
        inputTime.pack()

        label_status = ct.CTkLabel(master=self, text="1. Click START and 'Select The Area'\n2. Click Wherever You Want The AutoClick")
        label_status.pack(pady=10)

        label_status4 = ct.CTkLabel(master=self)

        contador_status = ct.CTkLabel(master=self)

        label_status3 = ct.CTkLabel(master=self, text="Move the cursor to STOP the program!")

        btn_start = ct.CTkButton(master=self, text="Start", command=preparar_captura, corner_radius=32, fg_color='blue')
        btn_start.pack(pady=5)

        btn_fechar = ct.CTkButton(master=self, text="Close", command=fechar, corner_radius=32, fg_color='grey')
        btn_fechar.pack()


app = App()
app.mainloop()
