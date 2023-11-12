import customtkinter as ctk
from customtkinter import*

class calculadora (ctk.CTk):
    def __init__(self):
        super().__init__()
        self.block = True
        self.title("Calculadora")
        self.geometry('350x475')
        # Definir a cor de fundo da janela
        self.configure(fg_color="#1f1f1f")
        self.entrada = ctk.StringVar()
        self.entradal = ctk.CTkEntry(self, textvariable=self.entrada, width=350, height=50, border_color='#1f1f1f', justify="right", fg_color='#1f1f1f', font=('Arial', 25), state="readonly").grid(row = 0, columnspan=4, pady=10)
        self.limpar_entry = False
        botoes = [
            '%', 'CE', 'C',"<",
            '7', '8', '9', '/',
            '4', '5', '6', 'x',
            '1', '2', '3', '-',
            '+/-', '0', ',', '+'
            ]
        row_val = 2
        col_val = 0
        for botao in botoes:
            ctk.CTkButton(self, text=botao, font=("Arial", 20), fg_color="green", hover_color="light green", text_color="black", width=85, height=65, command=lambda tecla=botao: self.pressionar_tecla(tecla)).grid(row=row_val, column=col_val, pady=1, padx=1)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
        self.botaototal = ctk.CTkButton(self, text="=", font=("Arial", 20), fg_color="#0e3e62", hover_color="#135688", text_color="black", width=85, height=65, command=self.calcular).grid(row=8, column=3, pady=1)
    

    def pressionar_tecla(self, tecla):
        self.entrada_atual = self.entrada.get()
    
        # Verifica se o usuário obteve um resultado e está começando uma nova operação
        if self.limpar_entry:
            self.entrada.set(tecla)
            self.limpar_entry = False
        else:
            if tecla == 'CE':
                self.entrada.set('')
            elif tecla == 'C':
                self.entrada.set('')
            elif tecla == '<':
                self.entrada.set(self.entrada_atual[:-1])
            elif tecla == 'x':
                self.entrada.set(self.entrada_atual + '*')
            elif tecla == '%':
                self.entrada.set(self.entrada_atual + '%')
            elif tecla == '+/-':
                if self.entrada_atual and self.entrada_atual[0] == '-':
                    self.entrada.set(self.entrada_atual[1:])  # Torna positivo
                else:
                    self.entrada.set('-' + self.entrada_atual)  # Torna negativo
            else:
                self.entrada.set(self.entrada_atual + tecla)
        

    def calcular(self):
        try:
            expressao = self.entrada.get()
            resultado = eval(expressao)
            self.entrada.set(str(resultado))
            self.limpar_entry = True
        except Exception as e:
            self.entrada.set("Erro")

if __name__ == "__main__":
    app = calculadora()
    app.mainloop()