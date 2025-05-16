def paciente_existe(id_paciente):
    with open(ARQ_PACIENTES, newline='') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[0] == id_paciente:
                return True
    return False

def obter_nome_paciente(id_paciente):
    with open(ARQ_PACIENTES, newline='') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[0] == id_paciente:
                return row[1]
    return None

def cadastrar_paciente():
    print("\n--- Cadastro de Paciente ---")
    id_paciente = input("ID do paciente: ")

    if paciente_existe(id_paciente):
        print(f"Erro: Paciente com ID {id_paciente} já existe.")
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
        writer.writerow([id_paciente, nome, idade, sexo])
    print("Paciente cadastrado com sucesso!")
