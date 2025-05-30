from .transacao import Transacao
from .mixinlog import LogConsoleMixin

class Orcamento(LogConsoleMixin):
    # Classe responsável por gerenciar o saldo financeiro
    # O saldo é atualizado automaticamente conforme as transações são adicionadas ou removidas.
    def __init__(self, saldo_inicial: float = 0.0):
        # Inicializa o orçamento com um saldo inicial.
        self.saldo = saldo_inicial
        self.mostrar_log(f"Orcamento iniciado com saldo R$ {self.saldo:.2f}")

    def adicionar_transacao(self, transacao: Transacao):
        # Adiciona uma transação ao orçamento.
        if transacao.tipo == 'Entrada':
            self.saldo += transacao.valor
        elif transacao.tipo == 'Saida':
            self.saldo -= transacao.valor
        else:
            raise ValueError("Tipo de transação inválido. Deve ser 'Entrada' ou 'Saida'.")
        self.mostrar_log(f"Transação adicionada: {transacao}")

    def remover_transacao(self, transacao: Transacao):
        # Remove uma transação do orçamento pelo ID.
        if transacao.tipo == 'Entrada':
            self.saldo -= transacao.valor
        elif transacao.tipo == 'Saida':
            self.saldo += transacao.valor
        else:
            raise ValueError("Tipo de transação inválido. Deve ser 'Entrada' ou 'Saida'.")
        self.mostrar_log(f"Transação removida: {transacao}")

    def saldo_atual(self):
        # Retorna o saldo atual do orçamento.
        return self.saldo

    def __str__(self):
        return f"Saldo atual: R$ {self.saldo:.2f}"