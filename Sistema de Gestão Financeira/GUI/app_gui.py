import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestão Financeira")
        self.geometry("800x600")
        self.configure(bg="#D8D7D7")
        # Configurações adicionais da janela principal
        self.create_widgets()

    def create_widgets(self):
        # Aqui você pode adicionar widgets como botões, labels, etc.
        label = tk.Label(self, text="Bem-vindo ao Sistema de Gestão Financeira", font=("Arial", 16))
        label.pack(pady=20)
        # Outros widgets podem ser adicionados aqui

janela = MainWindow()
janela.mainloop()