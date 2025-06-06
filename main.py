from arquivos import inicializar_arquivos
from pacientes import cadastrar_paciente, editar_paciente, excluir_paciente
from atendimentos import registrar_atendimento_manual, importar_atendimentos_csv
from relatorios import menu_relatorios

# Menu de autenticação e inicialização

def autenticar_usuario():
    print("=== Sistema de Gestão de Pacientes ===")
    for _ in range(3):
        usuario = input("Usuário: ").strip()
        senha = input("Senha: ").strip()
        if usuario == "admin" and senha == "UBS2025":
            print("Acesso concedido.")
            return True
        else:
            print("Usuário ou senha incorretos.\n")
    print("Número de tentativas excedido. Encerrando o programa.")
    return False

def menu():
    inicializar_arquivos()
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Cadastrar paciente")
        print("2. Editar paciente")
        print("3. Excluir paciente")
        print("4. Registrar atendimento manual")
        print("5. Importar atendimentos via CSV")
        print("6. Relatórios")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_paciente()
        elif opcao == '2':
            editar_paciente()
        elif opcao == '3':
            excluir_paciente()
        elif opcao == '4':
            registrar_atendimento_manual()
        elif opcao == '5':
            importar_atendimentos_csv()
        elif opcao == '6':
            menu_relatorios()
        elif opcao == '7':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida.")

if _name_ == "_main_":
    if autenticar_usuario():
        menu()
