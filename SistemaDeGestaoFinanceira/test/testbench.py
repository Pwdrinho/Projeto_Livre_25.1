from Packages import Transacao
from Packages import carregar_dados, salvar_dados
from Packages import Orcamento

def pedir_transacao():
    """Pede ao usuário"""
    while True:
        try:
            valor = float(input("Digite o valor da transação: R$ "))
            tipo = input("Digite o tipo da transação (Entrada/Saída): ")
            categoria = input("Digite a categoria da transação: ")
            return Transacao(valor=valor, tipo=tipo, categoria=categoria)
        except ValueError:
            print("Valor inválido. Tente novamente.")    
        
    
if __name__ == "__main__":
    # Carrega os dados existentes
    transacoes, saldo_inicial = carregar_dados()
    orcamento = Orcamento(saldo_inicial)
    print(f"Saldo inicial carregado: R$ {orcamento.saldo_atual():.2f}")

    for i in range(3):
        print(f"\n Transação {i+1} de 3")
        nova = pedir_transacao()
        orcamento.adicionar_transacao(nova)
        transacoes.append(nova)
        print(f"Saldo após transação {i+1}: R$ {orcamento.saldo_atual():.2f}")
        salvar_dados(transacoes, orcamento.saldo_atual())
    
    # Cria o orçamento com o saldo inicial
    print("---------------------------------")
    print("3 Transação adicionada com sucesso!")
    print(f"Saldo final: R$ {orcamento.saldo_atual():.2f}")