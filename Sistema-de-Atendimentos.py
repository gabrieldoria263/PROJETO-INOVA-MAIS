import csv
import os
ARQ_PACIENTES = "pacientes.csv"
ARQ_ATENDIMENTOS = "atendimentos.csv"
def menu():
print("\n--- Menu Principal ---")
print("1. Cadastrar novo paciente")
print("2. Registrar novo atendimento")
print("3. Importar atendimentos via CSV")
print("4. Consultar histórico de atendimentos")
print("5. Gerar relatório de todos os atendimentos")
print("6. Editar paciente")
print("7. Excluir paciente")
print("8. Sair")
def inicializar_arquivos():
if not os.path.exists(ARQ_PACIENTES):
with open(ARQ_PACIENTES, 'w', newline='') as f:
writer = csv.writer(f)
writer.writerow(["Cartao_SUS", "Nome", "Idade", "Sexo"])
if not os.path.exists(ARQ_ATENDIMENTOS):
with open(ARQ_ATE…
colocar em Codigo_completo.py
Usuário: Jailtonmoraes
jailton va no github e cole isso em Sistema-de-Atendimentos.py
import csv
import os
from datetime import datetime
Arquivos de dados principais
ARQ_PACIENTES = 'pacientes.csv'
ARQ_ATENDIMENTOS = 'atendimentos.csv'
Cria os arquivos se não existirem
def inicializar_arquivos():
for arquivo, cabecalho in [(ARQ_PACIENTES, ['Nome', 'CartaoSUS', 'Nascimento', 'Bairro']),
(ARQ_ATENDIMENTOS, ['Data', 'CartaoSUS', 'Tipo', 'Observacoes'])]:
if not os.path.exists(arquivo):
with open(arquivo, 'w', newline='', encoding='utf-8') as f:
writer = csv.writer(f)
writer.writerow(cabecalho)
Lê uma data no formato DD/MM/AAAA
def ler_data(msg):
while True:
data_str = input(msg)
try:
return datetime.strptime(data_str, "%d/%m/%Y")
except ValueError:
print("Formato inválido. Use DD/MM/AAAA.")
Salva relatório em .txt ou .csv
def salvar_relatorio(dados, colunas, nome_base):
formato = input("Deseja salvar como (1) .txt ou (2) .csv? ")
nome_arquivo = f"{nome_base}{datetime.now().strftime('%Y%m%d%H%M%S')}"
os.makedirs("relatorios", exist_ok=True)
if formato == '1':
    caminho = os.path.join("relatorios", f"{nome_arquivo}.txt")
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(" | ".join(colunas) + "\n")
        f.write("-" * (len(colunas) * 15) + "\n")
        for linha in dados:
            f.write(" | ".join(str(linha.get(c, '')) for c in colunas) + "\n")
elif formato == '2':
    caminho = os.path.join("relatorios", f"{nome_arquivo}.csv")
    with open(caminho, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=colunas)
        writer.writeheader()
        for linha in dados:
            writer.writerow(linha)
else:
    print("Formato inválido. Relatório não salvo.")
    return

print(f"Relatório salvo como: {caminho}")

    
Cadastra um novo paciente
def cadastrar_paciente():
print("\n--- Cadastro de Paciente ---")
nome = input("Nome completo: ")
cartao_sus = input("Número do cartão SUS: ")
# Verifica se o Cartão SUS já está cadastrado
with open(ARQ_PACIENTES, 'r', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        if row['CartaoSUS'] == cartao_sus:
            print("Paciente com este cartão SUS já está cadastrado.")
            return

nascimento = ler_data("Data de nascimento (DD/MM/AAAA): ").strftime("%d/%m/%Y")
bairro = input("Bairro: ")

# Salva novo paciente
with open(ARQ_PACIENTES, 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow([nome, cartao_sus, nascimento, bairro])
print("Paciente cadastrado com sucesso!")

    
Edita dados de um paciente
def editar_paciente():
cartao = input("Informe o Cartão SUS do paciente a editar: ")
pacientes, _ = carregar_dados()
paciente = pacientes.get(cartao)
if not paciente:
print("Paciente não encontrado.")
return
print(f"Editando paciente: {paciente['Nome']}")
# Campos com valor padrão mantêm o valor antigo se não houver entrada
novo_nome = input(f"Novo nome [{paciente['Nome']}]: ") or paciente['Nome']
novo_nascimento = input(f"Nova data de nascimento [{paciente['Nascimento']}]: ") or paciente['Nascimento']
novo_bairro = input(f"Novo bairro [{paciente['Bairro']}]: ") or paciente['Bairro']

pacientes[cartao] = {
    'Nome': novo_nome,
    'CartaoSUS': cartao,
    'Nascimento': novo_nascimento,
    'Bairro': novo_bairro
}

# Atualiza arquivo de pacientes
with open(ARQ_PACIENTES, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['Nome', 'CartaoSUS', 'Nascimento', 'Bairro'])
    writer.writeheader()
    for p in pacientes.values():
        writer.writerow(p)
print("Dados atualizados com sucesso.")

    
Exclui um paciente e seus atendimentos
def excluir_paciente():
cartao = input("Informe o Cartão SUS do paciente a excluir: ")
pacientes, atendimentos = carregar_dados()
if cartao not in pacientes:
print("Paciente não encontrado.")
return
confirm = input(f"Tem certeza que deseja excluir {pacientes[cartao]['Nome']}? (s/n): ")
if confirm.lower() != 's':
    return

del pacientes[cartao]
atendimentos = [a for a in atendimentos if a['CartaoSUS'] != cartao]

# Atualiza os arquivos
with open(ARQ_PACIENTES, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['Nome', 'CartaoSUS', 'Nascimento', 'Bairro'])
    writer.writeheader()
    for p in pacientes.values():
        writer.writerow(p)

with open(ARQ_ATENDIMENTOS, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['Data', 'CartaoSUS', 'Tipo', 'Observacoes'])
    writer.writeheader()
    for a in atendimentos:
        writer.writerow(a)
print("Paciente e seus atendimentos foram removidos.")

    
Registra um novo atendimento manualmente
def registrar_atendimento_manual():
print("\n--- Registro de Atendimento ---")
data = ler_data("Data do atendimento (DD/MM/AAAA): ").strftime("%d/%m/%Y")
cartao_sus = input("Cartão SUS do paciente: ")
pacientes, _ = carregar_dados()
if cartao_sus not in pacientes:
print("Cartão SUS não encontrado. Registre o paciente primeiro.")
return
tipo = input("Tipo de atendimento (consulta, vacinação, etc.): ")
observacoes = input("Observações (opcional): ")
with open(ARQ_ATENDIMENTOS, 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow([data, cartao_sus, tipo, observacoes])
print("Atendimento registrado.")

    
Importa atendimentos a partir de um arquivo CSV externo
def importar_atendimentos_csv():
caminho = input("Digite o caminho do arquivo .csv com os atendimentos: ")
try:
with open(caminho, 'r', encoding='utf-8') as f_in, open(ARQ_ATENDIMENTOS, 'a', newline='', encoding='utf-8') as f_out:
reader = csv.reader(f_in)
next(reader)  # Ignora o cabeçalho
writer = csv.writer(f_out)
for row in reader:
if len(row) != 4:
print(f"Linha ignorada (formato inválido): {row}")
continue
writer.writerow(row)
print("Atendimentos importados com sucesso.")
except Exception as e:
print(f"Erro ao importar: {e}")
Carrega os dados de pacientes e atendimentos dos arquivos
def carregar_dados():
pacientes = {}
with open(ARQ_PACIENTES, 'r', encoding='utf-8') as f:
reader = csv.DictReader(f)
for row in reader:
pacientes[row['CartaoSUS']] = row
atendimentos = []
with open(ARQ_ATENDIMENTOS, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        atendimentos.append(row)
return pacientes, atendimentos

    
Relatório de pacientes atendidos em determinado período
def relatorio_pacientes_por_periodo():
pacientes, atendimentos = carregar_dados()
data_inicio = ler_data("Data inicial (DD/MM/AAAA): ")
data_fim = ler_data("Data final (DD/MM/AAAA): ")
print("\n--- Pacientes atendidos no período ---")
cartoes_exibidos = set()
relatorio = []
for at in atendimentos:
    data_at = datetime.strptime(at['Data'], "%d/%m/%Y")
    if data_inicio <= data_at <= data_fim and at['CartaoSUS'] not in cartoes_exibidos:
        p = pacientes.get(at['CartaoSUS'], {'Nome': 'Desconhecido'})
        print(f"{p['Nome']} - Cartão SUS: {at['CartaoSUS']}")
        relatorio.append({'Nome': p['Nome'], 'CartaoSUS': at['CartaoSUS']})
        cartoes_exibidos.add(at['CartaoSUS'])

if input("Deseja salvar o relatório? (s/n): ").lower() == 's':
    salvar_relatorio(relatorio, ['Nome', 'CartaoSUS'], 'relatorio_pacientes_periodo')

    
Relatório de atendimentos por tipo (contagem)
def relatorio_tipo_atendimento():
_, atendimentos = carregar_dados()
contagem = {}
for at in atendimentos:
tipo = at['Tipo']
contagem[tipo] = contagem.get(tipo, 0) + 1
relatorio = [{'Tipo': tipo, 'Quantidade': qtd} for tipo, qtd in contagem.items()]

print("\n--- Quantidade por tipo de atendimento ---")
for item in relatorio:
    print(f"{item['Tipo']}: {item['Quantidade']}")

if input("Deseja salvar o relatório? (s/n): ").lower() == 's':
    salvar_relatorio(relatorio, ['Tipo', 'Quantidade'], 'relatorio_tipos')

    
Relatório de atendimentos agrupados por bairro
def relatorio_atendimentos_por_bairro():
pacientes, atendimentos = carregar_dados()
contagem = {}
for at in atendimentos:
paciente = pacientes.get(at['CartaoSUS'])
if paciente:
bairro = paciente['Bairro']
contagem[bairro] = contagem.get(bairro, 0) + 1
relatorio = [{'Bairro': b, 'Atendimentos': qtd} for b, qtd in contagem.items()]

print("\n--- Atendimentos por bairro ---")
for item in relatorio:
    print(f"{item['Bairro']}: {item['Atendimentos']}")

if input("Deseja salvar o relatório? (s/n): ").lower() == 's':
    salvar_relatorio(relatorio, ['Bairro', 'Atendimentos'], 'relatorio_bairros')

    
Histórico de todos os atendimentos de um paciente
def relatorio_historico_paciente():
cartao = input("Informe o número do cartão SUS do paciente: ")
pacientes, atendimentos = carregar_dados()
paciente = pacientes.get(cartao)
if not paciente:
print("Paciente não encontrado.")
return
print(f"\n--- Histórico de atendimentos para {paciente['Nome']} ---")
historico = [at for at in atendimentos if at['CartaoSUS'] == cartao]
historico.sort(key=lambda x: datetime.strptime(x['Data'], "%d/%m/%Y"))
for at in historico:
    print(f"{at['Data']} - {at['Tipo']} - {at['Observacoes']}")

if input("Deseja salvar o relatório? (s/n): ").lower() == 's':
    salvar_relatorio(historico, ['Data', 'Tipo', 'Observacoes'], f"historico_{cartao}")

    
Menu principal do sistema
def menu():
inicializar_arquivos()
while True:
print("\n--- MENU PRINCIPAL ---")
print("1. Cadastrar paciente")
print("2. Editar paciente")
print("3. Excluir paciente")
print("4. Registrar atendimento manual")
print("5. Importar atendimentos via CSV")
print("6. Relatórios")
print("7. Sair")
opcao = input("Escolha uma opção: ")
    if opcao == '1':
        cadastrar_paciente()
    elif opcao == '2':
        editar_paciente()
    elif opcao == '3':
        excluir_paciente()
    elif opcao == '4':
        registrar_atendimento_manual()
    elif opcao == '5':
        importar_atendimentos_csv()
    elif opcao == '6':
        menu_relatorios()
    elif opcao == '7':
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida.")

    
Submenu de relatórios
def menu_relatorios():
while True:
print("\n--- RELATÓRIOS ---")
print("1. Pacientes atendidos em período")
print("2. Quantidade por tipo de atendimento")
print("3. Número de atendimentos por bairro")
print("4. Histórico por paciente")
print("5. Voltar")
opcao = input("Escolha uma opção: ")
    if opcao == '1':
        relatorio_pacientes_por_periodo()
    elif opcao == '2':
        relatorio_tipo_atendimento()
    elif opcao == '3':
        relatorio_atendimentos_por_bairro()
    elif opcao == '4':
        relatorio_historico_paciente()
    elif opcao == '5':
        break
    else:
        print("Opção inválida.")

    
Ponto de entrada do programa
if name == "main":
menu()
