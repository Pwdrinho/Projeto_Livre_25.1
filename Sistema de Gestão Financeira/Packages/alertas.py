from Packages.orcamento import Orcamento

class Alertas:
    def __init__(self, orcamento: Orcamento):
        self.orcamento = orcamento

    def alerta_orcamento_negativo(self) -> str | None:
        """Verifica se o orçamento está negativo e retorna um alerta."""
        saldo = self.orcamento.calcular_saldo()
        if saldo < 0:
            return "Alerta: O orçamento está negativo! (R$ {saldo:.2f})"
        return None
