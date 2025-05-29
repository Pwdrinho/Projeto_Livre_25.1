# Projeto_Livre_25.1

## Sistema de Gestão Financeira
Atividade Livre utilizando linguagem **python** e seus paradigmas de programação Orientado à Objetos, persistência de dados via serialização e interface gráfica simples utilizando o `tkinter` e `json` para armazenamento de dados.

---
### 📌 Descrição
Este sistema permite **gerenciar receitas e despesas**, oferecendo uma visão clara do orçamento pessoal. O usuário poderá **cadastrar transações** financeiras, **visualizar relatórios** e manter controle sobre seus gastos.

---
### 🎴 Casos de Uso




---
### ✅ Funcionalidades (escopo inicial)

- [x]Cadastro de transações (receitas e despesas).
- [ ]Visualização de transações.
- [ ]Resumo financeiro (saldo, total de receitas e despesas).
- [ ]Alertas financeiros (ex.: Saldo Negativo).
- [ ]Serialização dos dados (salvar/carregar). num arquivo JSON
- [ ]Interface gráfica com `tkinter`.

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
- `os` / `datetime` — Utilitários

### 📂 Estrtura do Projeto
```yaml
Sistema de Gestão Financeira/
├── Packages
│   ├── sistema_financeiro.py
│   ├── transacao.py
│   ├── orcamento.py
│   ├── categoria.py
│   ├── serializacao.py   # Funções para salvar e carregar dados com JSON
│   └── alertas.py
├── Gui/
│   ├── __init__.py
│   └── app_gui.py
├── Data/
│   └── transacoes.json   # Arquivo onde os dados serão salvos
├── README.md  <- Você está aqui!
├── main.py # Ponto de entrada, inicia a GUI
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
>


📦 packages/
Contém as classes principais que modelam a lógica do negócio:

transacao.py
Define a classe Transacao e suas subclasses Receita e Despesa.
Cada transação terá atributos como valor, data, categoria e descrição.

orcamento.py
Gerencia o conjunto de transações e calcula totais e saldo.
Essa classe será responsável por adicionar, remover e listar transações, além de aplicar filtros.

categoria.py
Define e gerencia as categorias possíveis para as transações, como “Alimentação”, “Transporte”, “Salário”, etc.

alertas.py
Implementa a lógica de alertas financeiros, como avisar quando o usuário ultrapassa um limite definido em alguma categoria ou no orçamento total.

🖥️ gui/
Arquivos relacionados à interface gráfica com tkinter:

main_window.py
Define a janela principal da aplicação, que exibirá o resumo financeiro, lista de transações e botões para ações.

adicionar_transacao.py
Tela/formulário para o usuário inserir uma nova transação (receita ou despesa), com campos para valor, categoria, data e descrição.

📁 data/
transacoes.json
Arquivo onde todas as transações serão armazenadas e carregadas em formato JSON.

serializacao.py
Contém funções para salvar e carregar os dados do sistema usando JSON.
Funções como salvar_em_json(objeto, arquivo) e carregar_de_json(arquivo) estarão aqui.

Arquivos principais fora das pastas:
main.py
Arquivo de entrada do programa. Inicializa a aplicação, carrega dados, e chama a interface gráfica.

README.md
Documentação do projeto.



📂 Sistema de Gestão Financeira
├── packages/
✅ Responsável pela lógica principal do sistema — modelagem das entidades.

__init__.py
Torna packages um pacote Python. Não terá muita lógica, mas possibilita importar facilmente as classes.

transacao.py

Define a classe Transacao (classe base).

Define subclasses como Receita e Despesa usando herança e polimorfismo.

Atributos: valor, data, categoria, descricao.

orcamento.py

Classe Orcamento que compõe várias transações.

Métodos: adicionar, remover e listar transações.

Calcula saldo, total de despesas e total de receitas.

categoria.py

Define classe Categoria.

Pode ter atributos como: nome, limite.

Útil para organizar e agrupar transações por tipo.

alertas.py

Lógica para verificar condições de alerta, como:
➡️ Gastos acima de limite da categoria.
➡️ Orçamento estourado.

Pode implementar Mixins ou classes utilitárias para adicionar esse comportamento.

├── gui/
✅ Interface gráfica com o usuário, usando tkinter.

__init__.py
Marca gui como pacote.

main_window.py

Define a janela principal:
➡️ Resumo do orçamento.
➡️ Lista de transações.
➡️ Botões para adicionar/remover transações.

adicionar_transacao.py

Define a janela/modal para o usuário cadastrar uma nova transação.

Campos: valor, data, categoria, descrição.

├── data/

serializacao.py

Funções para salvar e carregar os dados:
➡️ salvar_em_json(objeto, caminho_arquivo)
➡️ carregar_de_json(caminho_arquivo)

Utiliza o módulo padrão json.

Facilita a persistência de dados.

✅ Armazenamento físico dos dados.

transacoes.json

Arquivo onde ficam salvos todos os dados: receitas, despesas, categorias etc.

Utilizado pelo utils/serializacao.py.

├── README.md
✅ Documentação do projeto, explicando:

Objetivo.

Estrutura.

Como executar.

├── main.py
✅ Arquivo principal do sistema.

Inicializa o programa.

Carrega dados do JSON.

Executa a interface gráfica (gui/main_window.py).

✅ Resumo:
Pasta	Função Principal
packages	Modelagem das classes de domínio (negócio)
utils	Suporte para serialização e utilitários
gui	Interface gráfica com o usuário
data	Persistência de dados em JSON
Arquivos raiz	Documentação e execução (README.md, main.py)