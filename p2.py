def registrar_atendimento_manual():
    print("\n--- Registro de Atendimento ---")
    data = input("Data do atendimento (DD/MM/AAAA): ")
    cartao_sus = input("Cartão SUS do paciente: ")
    tipo = input("Tipo de atendimento (consulta, vacinação, etc.): ")
    observacoes = input("Observações (opcional): ")

    with open(ARQ_ATENDIMENTOS, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([data, cartao_sus, tipo, observacoes])
    print("Atendimento registrado.")
