from arquivos import inicializar_arquivos
from pacientes import cadastrar_paciente, editar_paciente, excluir_paciente
from atendimentos import registrar_atendimento_manual, importar_atendimentos_csv, listar_atendimentos
from relatorios import menu_relatorios

def autenticar_usuario():
    """Autentica o usuário no sistema e retorna o nome de usuário."""
    usuarios = {
        "admin": "UBS2025",
        "funcionario": "fubs2025"
    }

    print("=== Sistema de Gestão de Pacientes ===")
    for _ in range(3):
        usuario = input("Usuário: ").strip()
        senha = input("Senha: ").strip()
        if usuario in usuarios and senha == usuarios[usuario]:
            print("Acesso concedido.")
            return usuario
        else:
            print("Usuário ou senha incorretos.\n")
    print("Número de tentativas excedido. Encerrando o programa.")
    return None

def menu(usuario):
    inicializar_arquivos()
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Cadastrar paciente")
        print("2. Editar paciente")
        print("3. Excluir paciente")
        print("4. Registrar atendimento manual")
        print("5. Importar atendimentos via CSV")
        print("6. Listar atendimentos (com nome)")
        print("7. Relatórios")
        print("8. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_paciente()
        elif opcao == '2':
            editar_paciente()
        elif opcao == '3':
            excluir_paciente()
        elif opcao == '4':
            registrar_atendimento_manual(usuario)
        elif opcao == '5':
            importar_atendimentos_csv(usuario)
        elif opcao == '6':
            listar_atendimentos()
        elif opcao == '7':
            menu_relatorios(usuario)
        elif opcao == '8':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    usuario_logado = autenticar_usuario()
    if usuario_logado:
        menu(usuario_logado)
