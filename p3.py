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
