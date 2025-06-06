import csv
from datetime import datetime
from arquivos import ARQ_ATENDIMENTOS, carregar_dados
from pacientes import ler_data

def registrar_atendimento_manual():
    print("\n--- Registro de Atendimento ---")

    while True:
        data = ler_data("Data do atendimento (DD/MM/AAAA): ")
        if data.date() > datetime.today().date():
            print("Erro: datas futuras não são aceitas.")
        else:
            break

    data_str = data.strftime("%d/%m/%Y")
    cartao_sus = input("Cartão SUS do paciente (15 dígitos): ").strip()
    if not cartao_sus.isdigit() or len(cartao_sus) != 15:
        print("Erro: Cartão SUS inválido.")
        return

    pacientes, _ = carregar_dados()
    if cartao_sus not in pacientes:
        print("Cartão SUS não encontrado. Registre o paciente primeiro.")
        return

    tipo = input("Tipo de atendimento (consulta, vacinação, etc.): ").strip()
    observacoes = input("Observações (opcional): ").strip()

    with open(ARQ_ATENDIMENTOS, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([data_str, cartao_sus, tipo, observacoes])
    print("Atendimento registrado.")

def importar_atendimentos_csv():
    caminho = input("Digite o caminho do arquivo .csv com os atendimentos: ").strip()
    pacientes, _ = carregar_dados()
    registros_importados = 0
    registros_ignorados = 0

    try:
        with open(caminho, 'r', encoding='utf-8') as f_in, open(ARQ_ATENDIMENTOS, 'a', newline='', encoding='utf-8') as f_out:
            reader = csv.reader(f_in)
            next(reader)
            writer = csv.writer(f_out)
            for row in reader:
                if len(row) != 4:
                    registros_ignorados += 1
                    continue
                data, cartao_sus, tipo, obs = [r.strip() for r in row]
                try:
                    datetime.strptime(data, "%d/%m/%Y")
                except ValueError:
                    registros_ignorados += 1
                    continue
                if not cartao_sus.isdigit() or len(cartao_sus) != 15 or cartao_sus not in pacientes:
                    registros_ignorados += 1
                    continue
                writer.writerow([data, cartao_sus, tipo, obs])
                registros_importados += 1
        print(f"Importação concluída: {registros_importados} registros importados, {registros_ignorados} ignorados.")
    except Exception as e:
        print(f"Erro ao importar: {e}")
