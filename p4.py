def consultar_historico():
    print("\n--- Consultar Histórico do Paciente ---")
    cartao_SUS = input("Cartão SUS do paciente: ")

    nome = obter_nome_paciente(cartao_SUS)
    if not nome:
        print(f"Paciente com Cartão SUS {cartao_SUS} não encontrado.")
        return

    print(f"\nHistórico de atendimentos do paciente {nome} (Cartão SUS: {cartao_SUS}):\n")

    with open(ARQ_ATENDIMENTOS, newline='') as f:
        reader = csv.reader(f)
        next(reader)
        encontrados = False
        for row in reader:
            if row[0] == cartao_SUS:
                print(f"Data: {row[1]} - Descrição: {row[2]}")
                encontrados = True

        if not encontrados:
            print("Nenhum atendimento encontrado para este paciente.")
