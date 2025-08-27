# 🏥 Sistema de Gestão de Pacientes - UBS

Este projeto é um **sistema de gestão de pacientes e atendimentos** voltado para **Unidades Básicas de Saúde (UBS)**.  
Ele permite cadastrar pacientes, registrar atendimentos, importar dados em lote, gerar relatórios e manter as informações tanto em **arquivos CSV** quanto em um **banco de dados SQLite**.

---

## 📌 Funcionalidades

- 🔑 **Autenticação de usuário** (admin / funcionário).  
- 👤 **Gestão de Pacientes**:
  - Cadastrar novos pacientes (com validações de nome, cartão SUS e data de nascimento).
  - Editar informações já cadastradas.
  - Excluir pacientes (e seus atendimentos vinculados).
- 🩺 **Gestão de Atendimentos**:
  - Registrar atendimento manual.
  - Importar atendimentos em lote via CSV (evitando duplicatas).
  - Listar atendimentos com nome do paciente.
- 📊 **Relatórios**:
  - Pacientes atendidos em um período.
  - Quantidade por tipo de atendimento.
  - Número de atendimentos por bairro.
  - Histórico completo por paciente.
  - Opção de exportar relatórios em **TXT** ou **CSV**.
- 💾 **Armazenamento Híbrido**:
  - Dados salvos em **SQLite (banco.db)**.
  - Dados duplicados em **CSV** (`pacientes.csv` e `atendimentos.csv`) para compatibilidade e portabilidade.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **SQLite3** (persistência de dados)
- **CSV** (armazenamento paralelo)
- Estrutura modular em múltiplos arquivos:
  - `main.py` → Menu principal e autenticação.
  - `pacientes.py` → Cadastro, edição e exclusão de pacientes.
  - `atendimentos.py` → Registro e importação de atendimentos.
  - `arquivos.py` → Controle de CSVs.
  - `banco.py` → Acesso ao banco SQLite.
  - `relatorios.py` → Geração de relatórios.
  - `auxiliares.py` → Funções auxiliares (ex.: leitura de datas).

---

## ▶️ Como Executar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/gabrieldoria263/PROJETO-INOVA-MAIS.git
   ```

2. **(Opcional) Crie um ambiente virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Instale as dependências** (se necessário):
   ```bash
   pip install -r requirements.txt
   ```
   *(Atualmente o projeto só depende da biblioteca padrão do Python).*

4. **Execute o sistema**:
   ```bash
   python main.py
   ```

5. **Você também pode executar o sistema localmente utilizando o Visual Studio Code (VS Code), seguindo os seguintes passos:

- se de ter o Python certifique-se de que o pip esteja instalado em sua máquina.
- Abra o VS Code e clone este repositório utilizando a função "Clone Git Repository...".
- Abra a pasta do projeto no VS Code ("Arquivo" > "Abrir Pasta...").
- Abra o terminal integrado do VS Code ("Terminal" > "Novo Terminal").
- No terminal, navegue até o diretório onde se encontra o arquivo principal do sistema (ex: main.pyou similar).
- Execute o sistema utilizando o comando: python nome_do_arquivo_principal.py(substitua nome_do_arquivo_principal.pypelo nome real do arquivo).

Dica para VS Code: Você pode configurar um ambiente de execução (Run and Debug) no VS Code para facilitar o debug e a execução do seu projeto Python diretamente no terminal. Consulte a documentação do VS Code para Python para obter mais detalhes.
---

## 🔐 Usuários e Senhas

O sistema vem com dois perfis pré-configurados (em `main.py`):

- **Admin** → usuário: `admin`, senha: `UBS2025`  
- **Funcionário** → usuário: `funcionario`, senha: `fubs2025`

---

## 📂 Estrutura de Arquivos

```
📦 sistema-ubs
├── main.py
├── pacientes.py
├── atendimentos.py
├── arquivos.py
├── banco.py
├── auxiliares.py
├── relatorios.py
├── pacientes.csv
├── atendimentos.csv
├── banco.db
└── importacoes/         # pasta usada para importar CSVs em lote
```

---

## 📝 Exemplos de Uso

- **Cadastrar paciente** → Opção 1 no menu principal.  
- **Registrar atendimento manual** → Opção 4.  
- **Importar atendimentos via CSV** → Coloque o arquivo na pasta `importacoes/` e use a opção 5.  
- **Gerar relatórios** → Acesse a opção 7 no menu principal.

---

## 📌 Observações

- O sistema mantém dados em **duplicidade** (Banco SQLite + CSV) para garantir portabilidade e compatibilidade.  
- Ao excluir um paciente, todos os seus atendimentos também são removidos.  
- Relatórios são salvos na pasta `relatorios/` com nome identificando usuário e data/hora.  

---

## 📄 Licença

Este projeto é distribuído sob a licença **MIT**.  
Sinta-se à vontade para usar, modificar e contribuir.

---

👨‍💻 **Desenvolvido para fins acadêmicos e de aprendizado.**

Autores - Antônio Oliveira, Cristiano dos Santos, Gabriel Henrique, Geilson Santos, Jailton Santos, Josivanio Rodrigues, José Rosevaldo, Willian Aragão
Instituto Federal de Sergipe - Campus Propriá
