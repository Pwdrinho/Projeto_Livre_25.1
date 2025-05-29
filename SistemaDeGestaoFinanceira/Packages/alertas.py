from .orcamento import Orcamento

class Alerta:
    def __init__(self, orcamento: Orcamento):
        self.orcamento = orcamento

    def negativo(self) -> str | None:
        #Verifica se o orçamento está negativo e retorna um alerta.
        saldo = self.orcamento.saldo_atual()
        if saldo < 0:
            return f"Alerta: O orçamento está negativo! R$ {saldo:.2f}"
        return None