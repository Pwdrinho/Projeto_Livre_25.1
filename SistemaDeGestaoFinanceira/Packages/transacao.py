from datetime import datetime
import random
from .categoria import Categoria

class Transacao: #classe base
    TIPOS = ["Entrada", "Saida"]

    def __init__(self, valor: float, categoria: str, tipo: str, id= None, data = None):

        self.id = id if id is not None else self._gerar_id_hex()

        self.valor = self._validar_valor(valor)
        self.data = data if data is not None else datetime.now()
        self.categoria = self._validar_categoria(categoria)
        self.tipo = self._validar_tipo(tipo)

    @staticmethod
    def _gerar_id_hex():
        """Gera um ID de 4 dígitos em hexadecimal."""
        return f"{random.randint(0, 65535):04X}"

    @staticmethod
    def _validar_valor(valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor deve ser numérico.")
        if valor <= 0:
            raise ValueError("Valor deve ser positivo.")
        return float(valor)

    @staticmethod
    def _validar_categoria(categoria):
        if not isinstance(categoria, str) or not categoria.strip():
            raise ValueError("Categoria não pode ser vazia.")
        
        categoria_padronizada = Categoria.registrar(categoria)

        print(f"Categoria '{categoria_padronizada}' adicionada ao registro.")
        
        return categoria_padronizada

    @staticmethod
    def _validar_tipo(tipo):
        tipo = tipo.lower().capitalize()
        if tipo not in Transacao.TIPOS:
            raise ValueError("Tipo deve ser 'Entrada' ou 'Saida'.")
        return tipo
    
    def to_dict(self) -> dict:
        """Converte o objeto Transacao em um dicionário para serialização."""
        return {
            'id': self.id,
            'valor': self.valor,
            'data': self.data.isoformat(),  # Serializa a data como string ISO
            'categoria': self.categoria,
            'tipo': self.tipo
        }

    @classmethod
    def from_dict(cls, data):
        """Cria um objeto Transacao a partir de um dicionário."""
        data_obj = datetime.fromisoformat(data['data'])
        return cls(
            valor=data['valor'],
            data=data_obj,
            categoria=data['categoria'],
            tipo=data['tipo'],
            id=data['id']
        )

    def __str__(self):
        return (f"Transação n°{self.id}: {self.valor:.2f} "
                f"em {self.data.strftime('%Y-%m-%d')} "
                f"[{self.categoria}] - {self.tipo}")


# trocar valuerrror
#while True:
#   valor = input("valor: "))
#   if valor not in (int, float):
#       print("Valor deve ser numérico. Tente novamente.")
#   if (valor <= 0):
#       print("Valor deve ser positivo. Tente novamente.")
#   break
#valor = (int(input("Valor: ")))
#categoria = input("Categoria: ")    
#tipo = input("Tipo: ")

#obj = Transacao(valor, categoria, tipo)
#print(obj)