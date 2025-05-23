
import csv
from arquivos import ARQ_PACIENTES, ARQ_ATENDIMENTOS, carregar_dados

def ler_data(msg):
    from datetime import datetime
    while True:
        data_str = input(msg)
        try:
            return datetime.strptime(data_str, "%d/%m/%Y")
        except ValueError:
            print("Formato inválido. Use DD/MM/AAAA.")

def cadastrar_paciente():
    print("\n--- Cadastro de Paciente ---")
    nome = input("Nome completo: ")
    cartao_sus = input("Número do cartão SUS: ")
    with open(ARQ_PACIENTES, 'r', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            if row['CartaoSUS'] == cartao_sus:
                print("Paciente com este cartão SUS já está cadastrado.")
                return
    nascimento = ler_data("Data de nascimento (DD/MM/AAAA): ").strftime("%d/%m/%Y")
    bairro = input("Bairro: ")
    with open(ARQ_PACIENTES, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([nome, cartao_sus, nascimento, bairro])
    print("Paciente cadastrado com sucesso!")

def editar_paciente():
    cartao = input("Informe o Cartão SUS do paciente a editar: ")
    pacientes, _ = carregar_dados()
    paciente = pacientes.get(cartao)
    if not paciente:
        print("Paciente não encontrado.")
        return
    print(f"Editando paciente: {paciente['Nome']}")
    novo_nome = input(f"Novo nome [{paciente['Nome']}]: ") or paciente['Nome']
    novo_nascimento = input(f"Nova data de nascimento [{paciente['Nascimento']}]: ") or paciente['Nascimento']
    novo_bairro = input(f"Novo bairro [{paciente['Bairro']}]: ") or paciente['Bairro']
    pacientes[cartao] = {
        'Nome': novo_nome,
        'CartaoSUS': cartao,
        'Nascimento': novo_nascimento,
        'Bairro': novo_bairro
    }
    with open(ARQ_PACIENTES, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['Nome', 'CartaoSUS', 'Nascimento', 'Bairro'])
        writer.writeheader()
        for p in pacientes.values():
            writer.writerow(p)
    print("Dados atualizados com sucesso.")

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