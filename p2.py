def registrar_atendimento():
    print("\n--- Registro de Atendimento ---")
    cartao_SUS = input("Cartão SUS do paciente: ")

    if not paciente_existe(cartao_SUS):
        print(f"Erro: Paciente com Cartão SUS {cartao_SUS} não encontrado.")
        return

    data = input("Data do atendimento (DD/MM/AAAA): ")
    descricao = input("Descrição do atendimento: ")

    with open(ARQ_ATENDIMENTOS, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([cartao_SUS, data, descricao])
    print("Atendimento registrado com sucesso!")
