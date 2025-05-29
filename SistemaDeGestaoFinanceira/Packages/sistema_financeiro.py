from .serializacao import salvar_dados, carregar_dados, remover_dados
from .transacao import Transacao

class GerenciadorTransacoes:
    def __init__(self):
        self.transacoes, saldo_inicial = carregar_dados()
        self.saldo = saldo_inicial

    def adicionar_transacao(self, transacao: Transacao):
        self.transacoes.append(transacao)
        if transacao.tipo == "ENTRADA":
            self.saldo += transacao.valor
        else:
            self.saldo -= transacao.valor
        salvar_dados(self.transacoes, self.saldo)

    def remover_transacao(self, id_transacao: str):
        transacao = next((t for t in self.transacoes if t.id == id_transacao), None)
        if transacao:
            self.transacoes.remove(transacao)
            if transacao.tipo == "ENTRADA":
                self.saldo -= transacao.valor
            else:
                self.saldo += transacao.valor
            salvar_dados(self.transacoes, self.saldo)










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