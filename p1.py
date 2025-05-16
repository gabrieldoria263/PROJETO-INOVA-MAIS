def paciente_existe(cartao_SUS):
    with open(ARQ_PACIENTES, newline='') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[0] == cartao_SUS:
                return True
    return False

def obter_nome_paciente(cartao_SUS):
    with open(ARQ_PACIENTES, newline='') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[0] == cartao_SUS:
                return row[1]
    return None

def cadastrar_paciente():
    print("\n--- Cadastro de Paciente ---")
    cartao_SUS = input("Número do Cartão SUS do paciente: ")

    if paciente_existe(cartao_SUS):
        print(f"Erro: Paciente com Cartão SUS {cartao_SUS} já existe.")
        return

    nome = input("Nome: ")
    idade = input("Idade: ")
    if not idade.isdigit():
        print("Erro: Idade deve ser um número.")
        return

    sexo = input("Sexo (M/F): ").upper()
    if sexo not in ["M", "F"]:
        print("Erro: Sexo deve ser 'M' ou 'F'.")
        return

    with open(ARQ_PACIENTES, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([cartao_SUS, nome, idade, sexo])
    print("Paciente cadastrado com sucesso!")
