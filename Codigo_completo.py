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
        with open(ARQ_ATENDIMENTOS, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Cartao_SUS", "Data", "Descrição"])

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

def importar_atendimentos_csv():
    print("\n--- Importar Atendimentos via CSV ---")
    caminho = input("Caminho do arquivo CSV: ")
    try:
        with open(caminho, newline='') as f:
            reader = csv.reader(f)
            next(reader)

            with open(ARQ_ATENDIMENTOS, 'a', newline='') as f_out:
                writer = csv.writer(f_out)
                importados = 0
                ignorados = 0
                for row in reader:
                    if len(row) != 3:
                        print(f"Formato inválido ignorado: {row}")
                        ignorados += 1
                        continue
                    if paciente_existe(row[0]):
                        writer.writerow(row)
                        importados += 1
                    else:
                        print(f"Cartão SUS inválido ignorado: {row[0]}")
                        ignorados += 1

        print(f"Importação concluída: {importados} atendimentos importados, {ignorados} ignorados.")
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado. Verifique o caminho informado.")

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

def gerar_relatorio():
    print("\n--- Relatório de Todos os Atendimentos ---")
    escolha = input("Salvar relatório em (1) .txt ou (2) .csv? ")
    nome_arquivo = input("Nome do arquivo (sem extensão): ")

    with open(ARQ_ATENDIMENTOS, newline='') as f:
        reader = list(csv.reader(f))
        cabecalho = reader[0]
        dados = reader[1:]

    if escolha == "1":
        with open(f"{nome_arquivo}.txt", 'w') as f_out:
            f_out.write("Relatório de Atendimentos\n\n")
            for linha in dados:
                nome_paciente = obter_nome_paciente(linha[0]) or "Desconhecido"
                f_out.write(f"Paciente: {nome_paciente} (Cartão SUS: {linha[0]}) | Data: {linha[1]} | Descrição: {linha[2]}\n")
        print("Relatório salvo como .txt com sucesso!")
    elif escolha == "2":
        with open(f"{nome_arquivo}.csv", 'w', newline='') as f_out:
            writer = csv.writer(f_out)
            writer.writerow(cabecalho)
            writer.writerows(dados)
        print("Relatório salvo como .csv com sucesso!")
    else:
        print("Opção inválida.")

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

def main():
    inicializar_arquivos()
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_paciente()
        elif opcao == "2":
            registrar_atendimento()
        elif opcao == "3":
            importar_atendimentos_csv()
        elif opcao == "4":
            consultar_historico()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "6":
            editar_paciente()
        elif opcao == "7":
            excluir_paciente()
        elif opcao == "8":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
