# Projeto_Livre_25.1

## Sistema de Gestão Financeira
Atividade Livre utilizando linguagem **python** e seus paradigmas de programação Orientado à Objetos, persistência de dados via serialização e interface gráfica simples utilizando o **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)** e `json` para armazenamento de dados.

---
### 📌 Descrição
Este sistema permite **gerenciar receitas e despesas pessoais** de forma simples e eficiente. Oferecendo uma visão clara do **orçamento pessoal**. O usuário poderá **cadastrar e excluir transações** financeiras, **visualizar extrato** com todas transações cadastradas, **saldo** atualiza em tempo real conforme as operações, **Alerta** quando saldo estiver *negativo* e manter controle sobre seus gastos.

Sistema simples, com possibilidade para ser expandido, permitindo fácil inclusão de novas funcionalidades como relatórios gráficos, filtros avançados, multiusuário e dashboard inicial.

---
### 🎴 Casos de Uso
 Nosso Ator Principal é um *Usuário* que gerencia suas finanças pessoais.
 1. **Registrar Transação**: Ator consegue registrar uma nova transação, informando.
    - **Id** (gerado automaticamente e codificado em **Hex**)
    - **Valor** (float)
    - **Data** (usando `datetime()`)
    - **Categoria** (validada e/ou registrada automaticamente)
    - **Tipo** (*"Entrada" ou "Saida"*)

2. **Extrato** (**Listar as Transações**): Ator visualiza uma lista com todas as transações cadastradas ordenadas por data.
    - Sistema carrega os dados salvos em *.json* e exibe em formato de listas.

3. **Excluir Transação**: Ator tem opção de remover uma transação especifica pelo **id**.

4. **Visualizar Categorias Registradas**: Ator pode consultar as categorias já existentes.

5. **Saldo e Alertas**: Ator consegue ver o *Saldo atualizado automaticamente* conforme adição e/ou remoção de transações. Caso Saldo fique *Negativado* exibe um alerta na tela.

---
### ✅ Funcionalidades (escopo inicial)

- [x] Cadastro de transações (receitas/entrada e despesas/saida).
- [x] Visualização de transações. (Extrato)
- [x] Resumo financeiro (saldo atual).
- [x] Alertas financeiros (Saldo Negativo).
- [x] Serialização dos dados (salvar/carregar). num arquivo JSON
- [x] Interface gráfica com **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)**.
- Em caso de Futuras Versões:
- [ ] Rellatórios e Gráficos usando `Matplotlib`
- [ ] Busca e Filtros Avançados
- [ ] Edição de Transações
- [ ] Multiusuário (Login/Senha)
- [ ] Dashboard Inicial (resumo rápido: saldo, últimas transações, gráfico de pizza de categorias)
---

### ☁️ Persistência de Dados

Os dados são armazenados em um arquivo JSON localizado na pasta `data/`.

- **Salvar:** Todas as transações realizadas são automaticamente salvas no arquivo `transacoes.json`.
- **Carregar:** Ao iniciar o sistema, os dados são carregados do arquivo JSON para manter a continuidade.
- **Remover:** Ao excluir uma transação pelo ID, ela é removida do arquivo `transacoes.json` e o **saldo** é atualizado automaticamente.

---

### 🛠️ Tecnologias utilizadas

- Python 3.11.9
- **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)** — Interface gráfica
- `json` -- Serialização
- `os` / `datetime` -- Utilitários
- `abc` -- mixin de log

### 📂 Estrtura do Projeto
```yaml
SistemaDeGestaoFinanceira/
├── Packages
│   ├── alertas.py
│   ├── app_gui.py
│   ├── categoria.py
│   ├── mixinlog.py
│   ├── transacao.py
│   ├── orcamento.py
│   ├── serializacao.py   # Funções para salvar e carregar dados com JSON
│   └── sistema_financeiro.py 
├── Data/
│   └── transacoes.json   # Arquivo onde os dados serão salvos
├── main.py # Ponto de entrada, inicia a GUI
├──.gitignore
├── README.md  <- Você está aqui!
├──UML_SDGF.png
├──UML_SDGF.drawio # Diagrama de classes utilizando .Drawio
```


### 📦 Dependências e Como Executar
1. **Clone o repositório:**

```cmd
git clone https://github.com/Pwdrinho/Projeto_Livre_25.1.git
cd Projeto_Livre_25.1/SistemaDeGestaoFinanceira
```

2. **Instale as dependências:**

```cmd
pip install customtkinter
```

3. **Execute o sistema:**

```cmd
python main.py
```
---

## 👤 Autor
<center><a href="https://github.com/Pwdrinho"> Pedro Lucas  </a></center>

- Estudante de Engenharia de Software - Universidade de Brasilia | UNB Campus Gama (FCTE)

- Projeto acadêmico de prática orientado à objetos em Python, utilizando JSON e Interface Gráfica simples(GUI).

---

<!-- infos para commit
⚠️ deu ruim
🔧 consertando: bugfix
⚙️ funcionando: feat
🪛 arrumando: bugfix / refactor
🧻 deu merda
📦 pacotes: chore
📧 email
🔌 se ligar é sorte
💾 salvando
⭐ commit normal
☁️ cloud
>

