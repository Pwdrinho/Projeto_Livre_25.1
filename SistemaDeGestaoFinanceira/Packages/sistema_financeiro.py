from .serializacao import Serializador
from .transacao import Transacao
from .mixinlog import LogConsoleMixin

class GerenciadorTransacoes(LogConsoleMixin):
    def __init__(self):
        self.transacoes, saldo_inicial = Serializador.carregar_dados()
        self.saldo = saldo_inicial
        self.mostrar_log("GerenciadorTransacoes iniciado.")

    def adicionar_transacao(self, transacao: Transacao):
        self.transacoes.append(transacao)
        if transacao.tipo == "Entrada":
            self.saldo += transacao.valor
        elif transacao.tipo == "Saida":
            self.saldo -= transacao.valor
        Serializador.salvar_dados(self.transacoes, self.saldo)
        self.mostrar_log(f"Transação adicionada: {transacao}")

    def remover_transacao(self, id_transacao: str):
        transacao = next((t for t in self.transacoes if t.id == id_transacao.upper()), None)
        if transacao:
            self.transacoes.remove(transacao)
            if transacao.tipo == "Entrada":
                self.saldo -= transacao.valor
            else:
                self.saldo += transacao.valor
            Serializador.salvar_dados(self.transacoes, self.saldo)
            self.mostrar_log(f"Transação removida: {transacao}")










# Gerar transação com classe Transacao
# Guardar valores do objeto criado
# Dar dump nesses valores num JSON com o seguinte formato:
# {
#   "id": "1234",
#   "valor": 100.0,
#   "data": "2023-10-01",
#   "categoria": "Alimentação",
#   "descricao": "Compra de supermercado"
#}