
def editar_paciente():
    print("\n--- Editar Paciente ---")
    cartao_SUS = input("Cartão SUS do paciente a editar: ")

    if not paciente_existe(cartao_SUS):
        print(f"Paciente com Cartão SUS {cartao_SUS} não encontrado.")
        return

    pacientes = []
    with open(ARQ_PACIENTES, newline='') as f:
        reader = csv.reader(f)
        pacientes = list(reader)

    for i, row in enumerate(pacientes):
        if row[0] == cartao_SUS:
            print(f"Dados atuais: Nome: {row[1]}, Idade: {row[2]}, Sexo: {row[3]}")
            novo_nome = input("Novo nome (deixe em branco para manter): ")
            nova_idade = input("Nova idade (deixe em branco para manter): ")
            novo_sexo = input("Novo sexo (M/F - deixe em branco para manter): ").upper()

            if novo_nome:
                row[1] = novo_nome
            if nova_idade:
                if nova_idade.isdigit():
                    row[2] = nova_idade
                else:
                    print("Idade inválida. Mantendo a anterior.")
            if novo_sexo in ["M", "F"]:
                row[3] = novo_sexo
            elif novo_sexo:
                print("Sexo inválido. Mantendo o anterior.")
            pacientes[i] = row
            break

    with open(ARQ_PACIENTES, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(pacientes)

    print("Paciente atualizado com sucesso!")

def excluir_paciente():
    print("\n--- Excluir Paciente ---")
    cartao_SUS = input("Cartão SUS do paciente a excluir: ")

    if not paciente_existe(cartao_SUS):
        print(f"Paciente com Cartão SUS {cartao_SUS} não encontrado.")
        return

    confirmacao = input(f"Tem certeza que deseja excluir o paciente {cartao_SUS} e seus atendimentos? (S/N): ").upper()
    if confirmacao != "S":
        print("Operação cancelada.")
        return

    with open(ARQ_PACIENTES, newline='') as f:
        pacientes = [row for row in csv.reader(f) if row[0] != cartao_SUS or row[0] == "Cartao_SUS"]

    with open(ARQ_PACIENTES, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(pacientes)

    with open(ARQ_ATENDIMENTOS, newline='') as f:
        atendimentos = [row for row in csv.reader(f) if row[0] != cartao_SUS or row[0] == "Cartao_SUS"]

    with open(ARQ_ATENDIMENTOS, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(atendimentos)

    print(f"Paciente {cartao_SUS} e seus atendimentos foram excluídos com sucesso.")