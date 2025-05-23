import csv
from arquivos import ARQ_ATENDIMENTOS, carregar_dados
from pacientes import ler_data

def registrar_atendimento_manual():
    print("\n--- Registro de Atendimento ---")
    data = ler_data("Data do atendimento (DD/MM/AAAA): ").strftime("%d/%m/%Y")
    cartao_sus = input("Cartão SUS do paciente: ")
    pacientes, _ = carregar_dados()
    if cartao_sus not in pacientes:
        print("Cartão SUS não encontrado. Registre o paciente primeiro.")
        return
    tipo = input("Tipo de atendimento (consulta, vacinação, etc.): ")
    observacoes = input("Observações (opcional): ")
    with open(ARQ_ATENDIMENTOS, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([data, cartao_sus, tipo, observacoes])
    print("Atendimento registrado.")

def importar_atendimentos_csv():
    caminho = input("Digite o caminho do arquivo .csv com os atendimentos: ")
    try:
        with open(caminho, 'r', encoding='utf-8') as f_in, open(ARQ_ATENDIMENTOS, 'a', newline='', encoding='utf-8') as f_out:
            reader = csv.reader(f_in)
            next(reader)
            writer = csv.writer(f_out)
            for row in reader:
                if len(row) != 4:
                    print(f"Linha ignorada (formato inválido): {row}")
                    continue
                writer.writerow(row)
        print("Atendimentos importados com sucesso.")
    except Exception as e:
        print(f"Erro ao importar: {e}")
