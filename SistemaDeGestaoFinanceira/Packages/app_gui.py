import customtkinter as ctk
from .serializacao import Serializador
from .transacao import Transacao
from .orcamento import Orcamento
from .alertas import Alerta

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestão Financeira")
        self.geometry("800x600")
        self.resizable(False, False)

        # Dados iniciais
        self.transacoes, self.saldo = Serializador.carregar_dados()
        self.orcamento = Orcamento(self.saldo)
        for t in self.transacoes:
            self.orcamento.adicionar_transacao(t)
        self.alerta = Alerta(self.orcamento)

        # Saldo sempre visível
        self.saldo_label = ctk.CTkLabel(self, text="", font=("Arial", 22, "bold"))
        self.saldo_label.pack(pady=10)
        self.atualizar_saldo()

        # Botões de navegação
        nav_frame = ctk.CTkFrame(self)
        nav_frame.pack(pady=5)
        ctk.CTkButton(nav_frame, text="Adicionar", command=self.mostrar_adicionar).pack(side="left", padx=5)
        ctk.CTkButton(nav_frame, text="Remover", command=self.mostrar_remover).pack(side="left", padx=5)
        ctk.CTkButton(nav_frame, text="Extrato", command=self.mostrar_extrato).pack(side="left", padx=5)

        # Frame principal para trocar o conteúdo
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(expand=True, fill="both", pady=10)

        self.mostrar_extrato()  # Mostra extrato ao iniciar

    def atualizar_saldo(self):
        self.saldo_label.configure(text=f"Saldo Atual: R$ {self.orcamento.saldo_atual():.2f}")
        alerta_msg =self.alerta.negativo()
        if alerta_msg:
            self.mostrar_alerta(alerta_msg)

    def limpar_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def mostrar_adicionar(self):
        self.limpar_main_frame()
        ctk.CTkLabel(self.main_frame, text="Adicionar Transação", font=("Arial", 16, "bold")).pack(pady=5)
        valor_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Valor")
        valor_entry.pack(pady=5)
        
        # OptionMenu para tipo
        tipo_var = ctk.StringVar(value="Entrada")
        tipo_menu = ctk.CTkOptionMenu(self.main_frame, variable=tipo_var, values=["Entrada", "Saida"])
        tipo_menu.pack(pady=5)
        
        categoria_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Categoria")
        categoria_entry.pack(pady=5)
        msg_label = ctk.CTkLabel(self.main_frame, text="")
        msg_label.pack(pady=5)
    
        def adicionar():
            try:
                valor = float(valor_entry.get())
                tipo = tipo_var.get()
                categoria = categoria_entry.get()
                nova = Transacao(valor=valor, tipo=tipo, categoria=categoria)
                self.transacoes.append(nova)
                self.orcamento.adicionar_transacao(nova)
                Serializador.salvar_dados(self.transacoes, self.orcamento.saldo_atual())
                self.atualizar_saldo()
                msg_label.configure(text="Transação adicionada!", text_color="green")
            except Exception as e:
                msg_label.configure(text=f"Erro: {e}", text_color="red")
    
        ctk.CTkButton(self.main_frame, text="Adicionar", command=adicionar).pack(pady=10)

    def mostrar_remover(self):
        self.limpar_main_frame()
        ctk.CTkLabel(self.main_frame, text="Remover Transação", font=("Arial", 16, "bold")).pack(pady=5)
        id_entry = ctk.CTkEntry(self.main_frame, placeholder_text="ID da Transação")
        id_entry.pack(pady=5)
        msg_label = ctk.CTkLabel(self.main_frame, text="")
        msg_label.pack(pady=5)

        def remover():
            id_remover = id_entry.get().strip().upper()
            print(id_remover)
            if Serializador.remover_dados(id_remover):
                self.transacoes, saldo = Serializador.carregar_dados()
                self.orcamento = Orcamento(saldo)
                self.atualizar_saldo()
                msg_label.configure(text="Transação removida!", text_color="green")
            else:
                msg_label.configure(text="ID não encontrado.", text_color="red")

        ctk.CTkButton(self.main_frame, text="Remover", command=remover).pack(pady=10)

    def mostrar_extrato(self):
        self.limpar_main_frame()
        ctk.CTkLabel(self.main_frame, text="Extrato de Transações", font=("Arial", 16, "bold")).pack(pady=5)
        transacoes, _ = Serializador.carregar_dados()
        if not transacoes:
            ctk.CTkLabel(self.main_frame, text="Nenhuma transação registrada.").pack(pady=10)
        else:
            for t in transacoes:
                ctk.CTkLabel(
                    self.main_frame,
                    text=f"ID: {t.id} | Valor: R$ {t.valor:.2f} | Tipo: {t.tipo} | Categoria: {t.categoria}"
                ).pack(anchor="w", padx=10)

    def mostrar_alerta(self, mensagem):
        popup = ctk.CTkToplevel(self)
        popup.title("Alerta de Saldo Negativo")
        popup.geometry("350x120")
        popup.attributes("-topmost", True)
        popup.grab_set()

        self.update_idletasks()
        x = self.winfo_x() + (self.winfo_width() // 2) - (350 // 2)
        y = self.winfo_y() + (self.winfo_height() // 2) - (120 // 2)
        popup.geometry(f"+{x}+{y}")

        ctk.CTkLabel(popup, text="⚠️", text_color="black", font=("Arial", 40, "bold")).pack(pady=5)
        ctk.CTkLabel(popup, text=mensagem, text_color="red", font=("Arial", 14, "bold")).pack(pady=5)
        ctk.CTkButton(popup, text="OK", command=popup.destroy).pack(pady=5)

if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    app = MainApp()
    app.mainloop()