
def consultar_historico():
    print("\n--- Consultar Histórico do Paciente ---")
    id_paciente = input("ID do paciente: ")

    nome = obter_nome_paciente(id_paciente)
    if not nome:
        print(f"Paciente com ID {id_paciente} não encontrado.")
        return

    print(f"\nHistórico de atendimentos do paciente {nome} (ID: {id_paciente}):\n")

    with open(ARQ_ATENDIMENTOS, newline='') as f:
        reader = csv.reader(f)
        next(reader)
        encontrados = False
        for row in reader:
            if row[0] == id_paciente:
                print(f"Data: {row[1]} - Descrição: {row[2]}")
                encontrados = True

        if not encontrados:
            print("Nenhum atendimento encontrado para este paciente.")