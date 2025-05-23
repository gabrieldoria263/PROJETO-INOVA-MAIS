# 🏥  Inova Mais - sistema de cadastramento

## 📋 Descrição do Projeto

Este projeto é um sistema simples para gerenciamento de **pacientes**, **atendimentos** e **relatórios médicos** utilizando arquivos CSV. É uma solução leve e prática para pequenas unidades de saúde, clínicas ou postos de atendimento.

---

## 📋 Funcionalidades

- Cadastro, edição e exclusão de pacientes
- Registro manual de atendimentos
- Importação de atendimentos via arquivo `.csv`
- Geração de relatórios:
  - Pacientes atendidos em um período
  - Quantidade por tipo de atendimento
  - Atendimentos por bairro
  - Histórico completo de um paciente
- Exportação de relatórios em `.csv` ou `.txt`

---

## 📂 Estrutura do Projeto

SistemaAtendimento/
├── main.py                 # Ponto de entrada do sistema
├── arquivos.py             # Inicialização e manipulação de arquivos CSV
├── pacientes.py            # Cadastro, edição e exclusão de pacientes
├── atendimentos.py         # Registro manual ou importação de atendimentos
├── relatorios.py           # Geração de relatórios diversos
├── pacientes.csv           # Arquivo com dados dos pacientes
├── atendimentos.csv        # Arquivo com dados dos atendimentos
└── relatorios/             # Diretório onde os relatórios são salvos

---
## 📁 Estrutura dos Arquivos

- `pacientes.csv`: Contém os dados dos pacientes
- `atendimentos.csv`: Registra os atendimentos realizados
- `relatorios/`: Pasta onde são salvos os relatórios gerados

---

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Módulos padrão:
  - `csv`
  - `datetime`
  - `os`

---

## 🚀 Como Usar

1. **Clone o repositório:**

``bash
git clone https://github.com/gabrieldoria263/PROJETO-INOVA-MAIS.git
cd sistema-pacientes

2.**Execute o sistema:**

python main.py

3. Siga o menu interativo no terminal.

4. **Você também pode executar o sistema localmente utilizando o **Visual Studio Code (VS Code)**, siga os seguintes passos:**

-  Certifique-se de ter o **Python** e o **pip** instalados em sua máquina.
-  Abra o VS Code e clone este repositório utilizando a função "Clone Git Repository...".
-  Abra a pasta do projeto no VS Code ("File" > "Open Folder...").
-   Abra o terminal integrado do VS Code ("Terminal" > "New Terminal").
-  No terminal, navegue até o diretório onde se encontra o arquivo principal do sistema (ex: `main.py` ou similar).
-  Execute o sistema utilizando o comando: `python nome_do_arquivo_principal.py` (substitua `nome_do_arquivo_principal.py` pelo nome real do arquivo).

**Dica para VS Code:** Você pode configurar um ambiente de execução (Run and Debug) no VS Code para facilitar o debug e a execução do seu projeto Python diretamente no terminal. Consulte a documentação do VS Code para Python para mais detalhes.

## 🖼️ Exemplo de Uso
Ao rodar o script, você verá um menu interativo como este:

--- MENU PRINCIPAL ---
1. Cadastrar paciente
2. Editar paciente
3. Excluir paciente
4. Registrar atendimento manual
5. Importar atendimentos via CSV
6. Relatórios
7. Sair

## 🧪 Teste com Arquivo de Importação
Você pode importar atendimentos com um arquivo .csv no seguinte formato:

Data,CartaoSUS,Tipo,Observacoes
12/05/2024,123456789012345,Consulta,Gripe
15/05/2024,987654321098765,Vacinação,Influenza

## 📌 Observações
- O Cartão SUS deve ser único para cada paciente.

- As datas devem estar no formato DD/MM/AAAA.

- Os dados são persistidos em arquivos .csv, então não é necessário banco de dados.

## 🧑‍💻 Autores
Desenvolvido por Alunos do IFS: Rosevaldo, Gabriel, Willian, Antonio, Josivaio, Jailton, Geilson e Cristiano

Contribuições são bem-vindas!
