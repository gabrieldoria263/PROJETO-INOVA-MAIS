#🏥 Sistema de Gestão de Pacientes - UBS
Este é um sistema simples de gerenciamento de pacientes e atendimentos desenvolvido em Python, com armazenamento em arquivos .csv. Ele é voltado para pequenas unidades de saúde (como UBS) que precisam registrar dados de pacientes e atendimentos de forma organizada e segura.

##📂 Estrutura do Projeto

PROJETO-INOVA-MAIS/
│
├── arquivos.py             # Inicialização e manipulação de arquivos CSV
├── pacientes.py            # Cadastro, edição e exclusão de pacientes
├── atendimentos.py         # Registro, importação e exclusão de atendimentos
├── relatorios.py           # Geração de relatórios diversos
├── main.py                 # Interface principal e menu do sistema
├── pacientes.csv           # Armazena dados dos pacientes
├── atendimentos.csv        # Armazena registros de atendimentos
└── relatorios/             # Pasta gerada automaticamente com os relatórios salvos

##✅ Funcionalidades
👤 Pacientes
- Cadastro de novos pacientes

- Edição dos dados de pacientes existentes

- Exclusão de pacientes e seus atendimentos

🩺 Atendimentos
- Registro manual de atendimentos

- Importação de atendimentos via arquivo .csv

- Exclusão individual de atendimentos por Cartão SUS e data

📊 Relatórios
- Pacientes atendidos em um período específico

- Contagem por tipo de atendimento (ex: consulta, vacina)

- Número de atendimentos por bairro

- Histórico completo de atendimentos de um paciente

  ##🔒 Autenticação
Ao iniciar o sistema, o usuário deve fazer login com as seguintes credenciais:

- Usuário: admin

- Senha: UBS2025

Limite de 3 tentativas antes do encerramento automático do programa.

##▶️ Como executar
1- Certifique-se de que você possui Python 3 instalado.

2- Instale o projeto em um diretório local.

3- Execute o arquivo principal:
python main.py

4- **Você também pode executar o sistema localmente utilizando o **Visual Studio Code (VS Code)**, siga os seguintes passos:**

-  Certifique-se de ter o **Python** e o **pip** instalados em sua máquina.
-  Abra o VS Code e clone este repositório utilizando a função "Clone Git Repository...".
-  Abra a pasta do projeto no VS Code ("File" > "Open Folder...").
-   Abra o terminal integrado do VS Code ("Terminal" > "New Terminal").
-  No terminal, navegue até o diretório onde se encontra o arquivo principal do sistema (ex: `main.py` ou similar).
-  Execute o sistema utilizando o comando: `python nome_do_arquivo_principal.py` (substitua `nome_do_arquivo_principal.py` pelo nome real do arquivo).

**Dica para VS Code:** Você pode configurar um ambiente de execução (Run and Debug) no VS Code para facilitar o debug e a execução do seu projeto Python diretamente no terminal. Consulte a documentação do VS Code para Python para mais detalhes.

##📝 Requisitos
- Python 3.6 ou superior

- Sistema operacional compatível com arquivos .csv (Windows, Linux, MacOS)

##📦 Exemplo de Importação de Atendimentos (.csv)
O arquivo CSV para importação deve seguir o seguinte formato (com cabeçalho):

swift
Data,CartaoSUS,Tipo,Observacoes
01/05/2025,123456789012345,Consulta,Paciente com dor de cabeça
03/05/2025,987654321098765,Vacinação,Dose de reforço aplicada

##📁 Relatórios
Os relatórios gerados são salvos na pasta relatorios/, podendo ser exportados em .csv ou .txt com formatação adequada para impressão ou análise.

##💡 Objetivo do Projeto
Este sistema foi desenvolvido como parte de um projeto acadêmico para a disciplina de Gerenciamento de Projetos, com foco em inovação e uso de tecnologias simples e acessíveis para facilitar o atendimento à população em unidades de saúde públicas.

##👨‍💻 Autores
Nome: Rosevaldo, Gabriel, Willian, Antonio, Josivanio, Jailton, Geilson e Cristiano
Instituição: Instituto Federal de Sergipe (IFS)
Ano: 2025
