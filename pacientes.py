import csv
from datetime import datetime
from arquivos import ARQ_PACIENTES, ARQ_ATENDIMENTOS, carregar_dados

def ler_data(msg):
    while True:
        data_str = input(msg).strip()
        try:
            return datetime.strptime(data_str, "%d/%m/%Y")
        except ValueError:
            print("Formato inválido. Use DD/MM/AAAA.")

# Função para cadastrar um novo paciente
def cadastrar_paciente():
    print("\n--- Cadastro de Paciente ---")

    while True:
        nome = input("Nome completo: ").strip()
        if nome:
            break
        print("Erro: O nome não pode ficar em branco.")

# Cadastra e valida o Cartão SUS
    while True:
        cartao_sus = input("Número do cartão SUS (15 dígitos): ").strip()
        if not (cartao_sus.isdigit() and len(cartao_sus) == 15):
            print("Erro: O cartão SUS deve conter exatamente 15 dígitos numéricos.")
            continue

# Registra o novo paciente
        with open(ARQ_PACIENTES, 'r', encoding='utf-8') as f:
            for row in csv.DictReader(f):
                if row['CartaoSUS'] == cartao_sus:
                    print("Erro: Este cartão SUS já está cadastrado.")
                    break
            else:
                break

    nascimento = ler_data("Data de nascimento (DD/MM/AAAA): ").strftime("%d/%m/%Y")

    while True:
        bairro = input("Bairro: ").strip()
        if bairro:
            break
        print("Erro: O bairro não pode ficar em branco.")

    with open(ARQ_PACIENTES, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([nome, cartao_sus, nascimento, bairro])
    print("Paciente cadastrado com sucesso!")

# Função para editar os dados de um paciente
def editar_paciente():
    cartao = input("Informe o Cartão SUS do paciente a editar (15 dígitos): ").strip()
# Valida o Cartão SUS
    if not cartao.isdigit() or len(cartao) != 15:
        print("Erro: Cartão SUS inválido.")
        return

    pacientes, _ = carregar_dados()
    paciente = pacientes.get(cartao)
    if not paciente:
        print("Paciente não encontrado.")
        return

    print(f"Editando paciente: {paciente['Nome']}")
    novo_nome = input(f"Novo nome [{paciente['Nome']}]: ").strip() or paciente['Nome']
    if not novo_nome:
        print("Erro: Nome não pode ficar em branco.")
        return

    nova_data_nasc = input(f"Nova data de nascimento [{paciente['Nascimento']}]: ").strip()
    if nova_data_nasc:
        try:
            datetime.strptime(nova_data_nasc, "%d/%m/%Y")
        except ValueError:
            print("Erro: Data de nascimento inválida.")
            return
    else:
        nova_data_nasc = paciente['Nascimento']

    novo_bairro = input(f"Novo bairro [{paciente['Bairro']}]: ").strip()
    if not novo_bairro:
        print("Erro: O bairro não pode ficar em branco.")
        return

    pacientes[cartao] = {
        'Nome': novo_nome,
        'CartaoSUS': cartao,
        'Nascimento': nova_data_nasc,
        'Bairro': novo_bairro
    }

# Se o paciente foi encontrado, reescreve o arquivo com os dados atualizados
    with open(ARQ_PACIENTES, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['Nome', 'CartaoSUS', 'Nascimento', 'Bairro'])
        writer.writeheader()
        for p in pacientes.values():
            writer.writerow(p)
    print("Dados atualizados com sucesso.")


# Função para excluir um paciente
def excluir_paciente():
    cartao = input("Informe o Cartão SUS do paciente a excluir: ").strip()
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

# Se o paciente foi encontrado, reescreve o arquivo sem ele
    with open(ARQ_ATENDIMENTOS, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['Data', 'CartaoSUS', 'Tipo', 'Observacoes'])
        writer.writeheader()
        for a in atendimentos:
            writer.writerow(a)
    print("Paciente e seus atendimentos foram removidos.")
