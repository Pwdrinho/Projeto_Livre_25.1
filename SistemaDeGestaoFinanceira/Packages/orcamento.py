from .transacao import Transacao

class Orcamento:
    # Classe responsável por gerenciar o saldo financeiro
    # O saldo é atualizado automaticamente conforme as transações são adicionadas ou removidas.
    def __init__(self, saldo_inicial: float = 0.0):
        # Inicializa o orçamento com um saldo inicial.
        self.saldo = saldo_inicial

    def adicionar_transacao(self, transacao: Transacao):
        # Adiciona uma transação ao orçamento.
        if transacao.tipo.lower() == 'entrada':
            self.saldo += transacao.valor
        elif transacao.tipo.lower() == 'saida':
            self.saldo -= transacao.valor
        else:
            raise ValueError("Tipo de transação inválido. Deve ser 'Entrada' ou 'Saida'.")

    def remover_transacao(self, transacao: Transacao):
        # Remove uma transação do orçamento pelo ID.
        if transacao.tipo.lower() == 'entrada':
            self.saldo -= transacao.valor
        elif transacao.tipo.lower() == 'saida':
            self.saldo += transacao.valor
        else:
            raise ValueError("Tipo de transação inválido. Deve ser 'Entrada' ou 'Saida'.")

    def saldo_atual(self):
        # Retorna o saldo atual do orçamento.
        return self.saldo

    def __str__(self):
        return f"Saldo atual: R$ {self.saldo:.2f}"