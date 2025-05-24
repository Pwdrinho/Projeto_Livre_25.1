# Projeto_Livre_25.1

## Sistema de Gestão Financeira
Atividade Livre utilizando linguagem **python** e seus paradigmas de programação Orientado à Objetos, persistência de dados via serialização e interface gráfica simples utilizando o `tkinter` e `json` para armazenamento de dados.

---
### 📌 Descrição
Este sistema permite **gerenciar receitas e despesas**, oferecendo uma visão clara do orçamento pessoal. O usuário poderá **cadastrar transações** financeiras, **visualizar relatórios** e manter controle sobre seus gastos.

---

### ✅ Funcionalidades (escopo inicial)

- [ ]Cadastro de transações (receitas e despesas).
- [ ]Visualização de transações.
- [ ]Resumo financeiro (saldo, total de receitas e despesas).
- [ ]Filtros por categoria e data.
- [ ]Alertas financeiros (ex.: ultrapassagem de limites).
- [ ]Serialização dos dados (salvar/carregar).
- [ ]Interface gráfica com `tkinter`.
- [ ]Relatórios gráficos com `matplotlib`.

---

### ☁️ Persistência de Dados

Os dados são armazenados em um arquivo JSON localizado na pasta `data/`.

- **Salvar:** Todas as transações realizadas são automaticamente salvas no arquivo `transacoes.json`.
- **Carregar:** Ao iniciar o sistema, os dados são carregados do arquivo JSON para manter a continuidade.

---

### 🛠️ Tecnologias utilizadas

- Python 3.11.9
- `tkinter` — Interface gráfica
- `json` — Serialização
- `matplotlib` — Gráficos (opcional)
- `os` / `datetime` — Utilitários

### 📂 Estrtura do Projeto
```yaml
Sistema de Gestão Financeira/
├── packages/
│   ├── __init__.py
│   ├── transacao.py
│   ├── orcamento.py
│   ├── categoria.py
│   ├── alertas.py
├── utils/
│   ├── __init__.py
│   ├── serializacao.py   # Funções para salvar e carregar dados com JSON
├── gui/
│   ├── __init__.py
│   ├── main_window.py
│   ├── adicionar_transacao.py
├── data/
│   └── transacoes.json   # Arquivo onde os dados serão salvos
├── README.md  <- Você está aqui!
├── main.py







```





<!--
⚠️ deu ruim
🔧 consertando
⚙️ funcionando
🪛 arrumando
🧻 deu merda
📦 pacotes
📧 email
🔌 se ligar é sorte
💾 salvando
⭐ commit normal
☁️ cloud
🎴 cartinha do tigrinho
>