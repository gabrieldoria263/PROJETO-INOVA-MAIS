from arquivos import inicializar_arquivos
from pacientes import cadastrar_paciente, editar_paciente, excluir_paciente
from atendimentos import registrar_atendimento_manual, importar_atendimentos_csv
from relatorios import (
    relatorio_pacientes_por_periodo,
    relatorio_tipo_atendimento,
    relatorio_atendimentos_por_bairro,
    relatorio_historico_paciente
)

def menu_relatorios():
    while True:
        print("\n--- RELATÓRIOS ---")
        print("1. Pacientes atendidos em período")
        print("2. Quantidade por tipo de atendimento")
        print("3. Número de atendimentos por bairro")
        print("4. Histórico por paciente")
        print("5. Voltar")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            relatorio_pacientes_por_periodo()
        elif opcao == '2':
            relatorio_tipo_atendimento()
        elif opcao == '3':
            relatorio_atendimentos_por_bairro()
        elif opcao == '4':
            relatorio_historico_paciente()
        elif opcao == '5':
            break
        else:
            print("Opção inválida.")

def menu_principal():
    inicializar_arquivos()
    while True:
        print("\n=== MENU PRINCIPAL ===")
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
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu_principal()

