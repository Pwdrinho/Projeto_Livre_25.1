import os
import customtkinter as ctk
from .serializacao import Serializador
from .transacao import Transacao
from .orcamento import Orcamento
from .alertas import Alerta
from .mixinlog import LogConsoleMixin

class MainApp(ctk.CTk, LogConsoleMixin):
    def __init__(self):
        super().__init__()
        self.mostrar_log("Interface gráfica iniciada.")
        self.title("Sistema de Gestão Financeira")
        icon_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "Assets", "int-exp.ico")
        )
        self.iconbitmap(icon_path)
        self.geometry("800x600")
        self.resizable(False, False)

        # Dados iniciais
        self.transacoes, self.saldo = Serializador.carregar_dados()
        self.orcamento = Orcamento(self.saldo)
        for t in self.transacoes:
            self.orcamento.adicionar_transacao(t)
        self.alerta = Alerta(self.orcamento)
        self.alerta_aberto = False

        # Saldo sempre visível
        self.saldo_label = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 22, "bold"),
            width=100,
            height=60,
            fg_color="#D3D3D3",
            corner_radius=20
        )
        self.saldo_label.pack(pady=(5, 0))
        self.atualizar_saldo()

        # Barra de navegação horizontal
        nav_bar = ctk.CTkFrame(self, fg_color="transparent")
        nav_bar.pack(fill="x")
        nav_bar.pack_propagate (False)

        ctk.CTkFrame(nav_bar, width=0).pack(side="left", expand=True)

        # Container 1 - Transações
        container1 = ctk.CTkFrame(
                nav_bar, 
                fg_color="#D3D3D3",
                corner_radius=20,
                width=240,
                height=100
        )
        container1.pack_propagate(False)
        container1.pack(side="left", padx=(20, 10), pady=1)

        ctk.CTkLabel(
                container1,
                text="Transação",
                font=("Arial", 14, "bold"),
                text_color="Black"
        ).pack(pady=(7,0))

        nav_frame1 = ctk.CTkFrame(container1, fg_color="transparent")
        nav_frame1.pack(pady=(5, 5))
        ctk.CTkButton(nav_frame1, text="Adicionar", command=self.mostrar_adicionar, fg_color="#E400E4", hover_color="#D100D1", text_color="white", corner_radius=50, width=70, height=40).pack(side="left", padx=10)
        ctk.CTkButton(nav_frame1, text="Remover", command=self.mostrar_remover, fg_color="#E400E4", hover_color="#D100D1", text_color="white", corner_radius=50, width=70, height=40).pack(side="left", padx=10)

        # Container 2 - Extrato
        container2 = ctk.CTkFrame(
            nav_bar,
            fg_color="#D3D3D3",
            corner_radius=20,
            width=140,
            height=100
            )
        container2.pack_propagate(False)
        container2.pack(side="left", padx=(10, 20), pady=1)

        ctk.CTkLabel(
            container2,
            text="Extrato",
            font=("Arial", 14, "bold"),
            text_color="Black"
        ).pack(pady=(7,0))

        nav_frame2 = ctk.CTkFrame(container2, fg_color="transparent")
        nav_frame2.pack(pady=(5, 5))
        ctk.CTkButton(
            nav_frame2,
            text="Extrato",
            command=self.mostrar_extrato,
            fg_color="#E400E4",
            hover_color="#D100D1",
            text_color="white",
            corner_radius=50,
            width=70,
            height=40
        ).pack(side="left", padx=10)

        ctk.CTkFrame(nav_bar, width=0).pack(side="left", expand=True)

        # Frame principal para trocar o conteúdo
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(expand=True, fill="both")

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
        valor_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Valor",text_color="black" , border_color="#950EA7")
        valor_entry.pack(pady=5)
        
        # OptionMenu para tipo
        tipo_var = ctk.StringVar(value="Entrada")
        tipo_menu = ctk.CTkOptionMenu(self.main_frame, fg_color="#E400E4", text_color="white", dropdown_fg_color="#E400E4" ,dropdown_text_color="white",dropdown_hover_color="#D100D1",button_color="#BE00BE", button_hover_color="#D100D1",variable=tipo_var ,values=["Entrada", "Saida"])
        tipo_menu.pack(pady=5)
        
        categoria_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Categoria", text_color="black", border_color="#950EA7")
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
    
        ctk.CTkButton(self.main_frame, text="Adicionar", text_color="white",command=adicionar,fg_color="#E400E4", hover_color="#D100D1").pack(pady=5)

    def mostrar_remover(self):
        self.limpar_main_frame()
        ctk.CTkLabel(self.main_frame, text="Remover Transação", font=("Arial", 16, "bold")).pack(pady=5)
        id_entry = ctk.CTkEntry(self.main_frame, placeholder_text="ID da Transação",text_color="black" , border_color="#950EA7")
        id_entry.pack(pady=5)
        msg_label = ctk.CTkLabel(self.main_frame, text="")
        msg_label.pack(pady=5)

        def remover():
            id_remover = id_entry.get().strip().upper()
            if Serializador.remover_dados(id_remover):
                self.transacoes, saldo = Serializador.carregar_dados()
                self.orcamento = Orcamento(saldo)
                self.alerta = Alerta(self.orcamento)
                self.atualizar_saldo()
                msg_label.configure(text="Transação removida!", text_color="green")
            else:
                msg_label.configure(text="ID não encontrado.", text_color="red")

        ctk.CTkButton(self.main_frame, text="Remover", command=remover, text_color="white", fg_color="#E400E4", hover_color="#D100D1").pack(pady=5)

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
                    text=f"ID: {t.id} | Valor: R$ {t.valor:.2f} | Data: {t.data.strftime('%d/%m/%Y')} | Tipo: {t.tipo} | Categoria: {t.categoria}",
                    font=("Arial", 12),
                    anchor="center",
                    justify="center"    
                ).pack(padx=10, pady=2)

    def mostrar_alerta(self, mensagem):
        if self.alerta_aberto:
            return
        self.alerta_aberto = True
        popup = ctk.CTkToplevel(self)
        popup.overrideredirect(True)
        popup.title("Alerta de Saldo Negativo")
        popup.geometry("350x120")
        popup.attributes("-topmost", True)
        popup.grab_set()
        popup.protocol("WM_DELETE_WINDOW", lambda: None)

        self.update_idletasks()
        x = self.winfo_x() + (self.winfo_width() // 2) - (350 // 2)
        y = self.winfo_y() + (self.winfo_height() // 2) - (120 // 2)
        popup.geometry(f"+{x}+{y}")

        ctk.CTkLabel(popup, text="⚠️", text_color="black", font=("Arial", 40, "bold")).pack(pady=5)
        ctk.CTkLabel(popup, text=mensagem, text_color="red", font=("Arial", 14, "bold")).pack(pady=5)
        def fechar():
            self.alerta_aberto = False
            popup.destroy()
        ctk.CTkButton(popup, text="OK", text_color="white", fg_color="#E400E4", hover_color="#D100D1",command=fechar, width= 50, height=55).pack(pady=5)

if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    app = MainApp()
    app.mainloop()