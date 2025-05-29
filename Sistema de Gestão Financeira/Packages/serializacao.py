import json
import os
from datetime import datetime
from transacao import Transacao

Caminho_arquivo = "data/transacoes.json"

def salvar_dados(transacoes: list[Transacao], saldo: float) -> None:
    """Salva as transações e o saldo em um arquivo JSON."""
    dados = {
        "saldo": saldo,
        transacoes: [transacao.to_dict() for transacao in transacoes]
    }
    with open(Caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

def carregar_dados() -> tuple[list[Transacao], float]:
    """Carrega as transações e o saldo de um arquivo JSON."""
    if not os.path.exists(Caminho_arquivo):
        return [], 0.0

    with open(Caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    saldo = dados.get("saldo", 0.0)
    transacoes_dicts = dados.get("transacoes", [])
    transacoes = []
    for transacao_dict in transacoes_dicts:
        try:
            transacao = Transacao.from_dict(transacao_dict)
            transacoes.append(transacao)
        except Exception as e:
            print(f"Erro ao carregar transação: {e} - Dados: {transacao_dict}")
    return transacoes, saldo