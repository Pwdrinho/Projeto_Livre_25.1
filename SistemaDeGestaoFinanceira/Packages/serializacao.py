import json
import os
from datetime import datetime
from .transacao import Transacao
from .categoria import Categoria

Caminho_arquivo = "SistemaDeGestaoFinanceira/Data/transacoes.json"

def salvar_dados(transacoes: list[Transacao], saldo: float) -> None:
    """Salva as transações e o saldo em um arquivo JSON."""
    dados = {
        "saldo": saldo,
        "transacoes": [transacao.to_dict() for transacao in transacoes]
    }
    os.makedirs(os.path.dirname(Caminho_arquivo), exist_ok=True)  # Garante que o diretório exista
    with open(Caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

def carregar_dados() -> tuple[list[Transacao], float]:
    """Carrega as transações e o saldo de um arquivo JSON."""
    if not os.path.exists(Caminho_arquivo):
        return [], 0.0
    try:
        with open(Caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read().strip()
            if not conteudo:  # Verifica se o arquivo está vazio
                return [], 0.0
            dados = json.load(arquivo)
    except (json.JSONDecodeError, FileNotFoundError):
        return [], 0.0

    saldo = dados.get("saldo", 0.0)
    transacoes_dicts = dados.get("transacoes", [])
    transacoes = []
    for transacao_dict in transacoes_dicts:
        try:
            Categoria.registrar(transacao_dict['categoria'])  # Registra a categoria no sistema global de categorias
            transacao = Transacao.from_dict(transacao_dict)
            transacoes.append(transacao)
        except Exception as e:
            print(f"Erro ao carregar transação: {e} - Dados: {transacao_dict}")
    return transacoes, saldo