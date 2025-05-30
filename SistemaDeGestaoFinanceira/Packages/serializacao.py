import json
import os
from .transacao import Transacao
from .categoria import Categoria
from .orcamento import Orcamento

class Serializador:
    CAMINHO_ARQUIVO = os.path.join(os.path.dirname(__file__), "../Data/transacoes.json")

    @classmethod
    def salvar_dados(cls, transacoes: list[Transacao], saldo: float) -> None:
        # Salva as transações e o saldo em um arquivo JSON.
        dados = {
            "saldo": saldo,
            "transacoes": [transacao.to_dict() for transacao in transacoes]
        }
        os.makedirs(os.path.dirname(cls.CAMINHO_ARQUIVO), exist_ok=True)  # Garante que o diretório exista
        with open(cls.CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    @classmethod
    def carregar_dados(cls) -> tuple[list[Transacao], float]:
        # Carrega as transações e o saldo de um arquivo JSON.
        if not os.path.exists(cls.CAMINHO_ARQUIVO):
            print("Erro - Caminho não existe.")
            return [], 0.0
        try:
            with open(cls.CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
                print("[JSON] Abrindo arquivo...")
                conteudo = arquivo.read().strip()
                print("[JSON] Lendo arquivo...")
                if not conteudo:  # Verifica se o arquivo está vazio
                    # print("Erro - Não foi possível ler o arquivo.")
                    return [], 0.0
                dados = json.loads(conteudo)
                print("[JSON] Carregando dados...")
        except (json.JSONDecodeError, FileNotFoundError):
            # print("Erro - Não foi possível abrir JSON.")
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

    @classmethod
    def remover_dados(cls, id_transacao: str)-> bool:
        transacoes, saldo = cls.carregar_dados()
        transacao_removida = None
        for transacao in transacoes:
            if transacao.id == id_transacao:
                transacao_removida = transacao
                break
        if not transacao_removida:
            return False # Não encontrou a transação com o ID fornecido
            
        orcamento = Orcamento(saldo)
        orcamento.remover_transacao(transacao_removida)
        transacoes = [transacao for transacao in transacoes if transacao.id != id_transacao]
        cls.salvar_dados(transacoes, orcamento.saldo_atual())
        return True