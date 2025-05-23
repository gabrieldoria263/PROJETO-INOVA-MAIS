# Relatório de pacientes atendidos em determinado período
def relatorio_pacientes_por_periodo():
    pacientes, atendimentos = carregar_dados()
    data_inicio = ler_data("Data inicial (DD/MM/AAAA): ")
    data_fim = ler_data("Data final (DD/MM/AAAA): ")

    print("\n--- Pacientes atendidos no período ---")
    cartoes_exibidos = set()
    relatorio = []
    for at in atendimentos:
        data_at = datetime.strptime(at['Data'], "%d/%m/%Y")
        if data_inicio <= data_at <= data_fim and at['CartaoSUS'] not in cartoes_exibidos:
            p = pacientes.get(at['CartaoSUS'], {'Nome': 'Desconhecido'})
            print(f"{p['Nome']} - Cartão SUS: {at['CartaoSUS']}")
            relatorio.append({'Nome': p['Nome'], 'CartaoSUS': at['CartaoSUS']})
            cartoes_exibidos.add(at['CartaoSUS'])

    if input("Deseja salvar o relatório? (s/n): ").lower() == 's':
        salvar_relatorio(relatorio, ['Nome', 'CartaoSUS'], 'relatorio_pacientes_periodo')

# Relatório de atendimentos por tipo (contagem)
def relatorio_tipo_atendimento():
    _, atendimentos = carregar_dados()
    contagem = {}
    for at in atendimentos:
        tipo = at['Tipo']
        contagem[tipo] = contagem.get(tipo, 0) + 1

    relatorio = [{'Tipo': tipo, 'Quantidade': qtd} for tipo, qtd in contagem.items()]

    print("\n--- Quantidade por tipo de atendimento ---")
    for item in relatorio:
        print(f"{item['Tipo']}: {item['Quantidade']}")

    if input("Deseja salvar o relatório? (s/n): ").lower() == 's':
        salvar_relatorio(relatorio, ['Tipo', 'Quantidade'], 'relatorio_tipos')

# Relatório de atendimentos agrupados por bairro
def relatorio_atendimentos_por_bairro():
    pacientes, atendimentos = carregar_dados()
    contagem = {}
    for at in atendimentos:
        paciente = pacientes.get(at['CartaoSUS'])
        if paciente:
            bairro = paciente['Bairro']
            contagem[bairro] = contagem.get(bairro, 0) + 1

    relatorio = [{'Bairro': b, 'Atendimentos': qtd} for b, qtd in contagem.items()]

    print("\n--- Atendimentos por bairro ---")
    for item in relatorio:
        print(f"{item['Bairro']}: {item['Atendimentos']}")

    if input("Deseja salvar o relatório? (s/n): ").lower() == 's':
        salvar_relatorio(relatorio, ['Bairro', 'Atendimentos'], 'relatorio_bairros')

# Histórico de todos os atendimentos de um paciente
def relatorio_historico_paciente():
    cartao = input("Informe o número do cartão SUS do paciente: ")
    pacientes, atendimentos = carregar_dados()
    paciente = pacientes.get(cartao)
    if not paciente:
        print("Paciente não encontrado.")
        return

    print(f"\n--- Histórico de atendimentos para {paciente['Nome']} ---")
    historico = [at for at in atendimentos if at['CartaoSUS'] == cartao]
    historico.sort(key=lambda x: datetime.strptime(x['Data'], "%d/%m/%Y"))
    for at in historico:
        print(f"{at['Data']} - {at['Tipo']} - {at['Observacoes']}")

    if input("Deseja salvar o relatório? (s/n): ").lower() == 's':
        salvar_relatorio(historico, ['Data', 'Tipo', 'Observacoes'], f"historico_{cartao}")
