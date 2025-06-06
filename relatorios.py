import csv
import os
from datetime import datetime
from arquivos import carregar_dados
from pacientes import ler_data

def salvar_relatorio(dados, colunas, nome_base):
    formato = input("Deseja salvar como (1) .txt ou (2) .csv? ")
    nome_arquivo = f"{nome_base}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    os.makedirs("relatorios", exist_ok=True)

    if formato == '1':
        caminho = os.path.join("relatorios", f"{nome_arquivo}.txt")
        with open(caminho, 'w', encoding='utf-8') as f:
            largura = 30
            f.write("".join(f"{c:<{largura}}" for c in colunas) + "\n")
            f.write("-" * (largura * len(colunas)) + "\n")
            for linha in dados:
                f.write("".join(f"{str(linha.get(c, '')):<{largura}}" for c in colunas) + "\n")
    elif formato == '2':
        caminho = os.path.join("relatorios", f"{nome_arquivo}.csv")
        with open(caminho, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=colunas)
            writer.writeheader()
            for linha in dados:
                writer.writerow(linha)
    else:
        print("Formato inválido. Relatório não salvo.")
        return

    print(f"Relatório salvo como: {caminho}")

# Função para gerar relatório de atendimentos por paciente
def relatorio_pacientes_por_periodo():
    pacientes, atendimentos = carregar_dados()
    data_inicio = ler_data("Data inicial (DD/MM/AAAA): ")
    data_fim = ler_data("Data final (DD/MM/AAAA): ")

    cartoes_exibidos = set()
    relatorio = []

    atendimentos_ordenados = sorted(
        (at for at in atendimentos if data_inicio <= datetime.strptime(at['Data'], "%d/%m/%Y") <= data_fim),
        key=lambda x: datetime.strptime(x['Data'], "%d/%m/%Y"),
        reverse=True
    )
# Conta os atendimentos por paciente
    for at in atendimentos_ordenados:
        cartao = at['CartaoSUS']
        if cartao not in cartoes_exibidos:
            p = pacientes.get(cartao, {'Nome': 'Desconhecido'})
            relatorio.append({
                'Nome': p['Nome'],
                'CartaoSUS': cartao,
                'DataAtendimento': at['Data']
            })
            cartoes_exibidos.add(cartao)

    if not relatorio:
        print("Nenhum paciente encontrado no período especificado.")
        return

    for item in relatorio:
        print(f"{item['DataAtendimento']} - {item['Nome']} - Cartão SUS: {item['CartaoSUS']}")

    if input("Deseja salvar o relatório? (s/n): ").lower() == 's':
        salvar_relatorio(relatorio, ['Nome', 'CartaoSUS', 'DataAtendimento'], 'relatorio_pacientes_periodo')

def relatorio_tipo_atendimento():
    _, atendimentos = carregar_dados()
    contagem = {}
    for at in atendimentos:
        tipo = at['Tipo']
        contagem[tipo] = contagem.get(tipo, 0) + 1

    relatorio = [{'Tipo': tipo, 'Quantidade': qtd} for tipo, qtd in contagem.items()]
    for item in relatorio:
        print(f"{item['Tipo']}: {item['Quantidade']}")

    if input("Deseja salvar o relatório? (s/n): ").lower() == 's':
        salvar_relatorio(relatorio, ['Tipo', 'Quantidade'], 'relatorio_tipos')

def relatorio_atendimentos_por_bairro():
    pacientes, atendimentos = carregar_dados()
    contagem = {}
    for at in atendimentos:
        paciente = pacientes.get(at['CartaoSUS'])
        if paciente:
            bairro = paciente['Bairro']
            contagem[bairro] = contagem.get(bairro, 0) + 1

    relatorio = [{'Bairro': b, 'Atendimentos': qtd} for b, qtd in contagem.items()]
    for item in relatorio:
        print(f"{item['Bairro']}: {item['Atendimentos']}")

    if input("Deseja salvar o relatório? (s/n): ").lower() == 's':
        salvar_relatorio(relatorio, ['Bairro', 'Atendimentos'], 'relatorio_bairros')

def relatorio_historico_paciente():
    cartao = input("Informe o número do cartão SUS do paciente (15 dígitos): ").strip()
    if not cartao.isdigit() or len(cartao) != 15:
        print("Erro: Cartão SUS inválido.")
        return

    pacientes, atendimentos = carregar_dados()
    paciente = pacientes.get(cartao)
    if not paciente:
        print("Paciente não encontrado.")
        return

    historico = [at for at in atendimentos if at['CartaoSUS'] == cartao]
    if not historico:
        print("Nenhum atendimento encontrado para este paciente.")
        return

    historico.sort(key=lambda x: datetime.strptime(x['Data'], "%d/%m/%Y"))

    dados_formatados = []
    print(f"\n--- Histórico de atendimentos para {paciente['Nome']} ---")
    for at in historico:
        registro = {
            'Nome': paciente['Nome'],
            'CartaoSUS': paciente['CartaoSUS'],
            'Nascimento': paciente['Nascimento'],
            'Bairro': paciente['Bairro'],
            'Tipo': at['Tipo'],
            'DataAtendimento': at['Data']
        }
        dados_formatados.append(registro)
        print(f"{registro['DataAtendimento']} - {registro['Tipo']} - "
              f"{registro['Nome']}, Cartão SUS: {registro['CartaoSUS']}, "
              f"Nasc.: {registro['Nascimento']}, Bairro: {registro['Bairro']}")

    if input("Deseja salvar o relatório? (s/n): ").lower() == 's':
        salvar_relatorio(dados_formatados,
                         ['Nome', 'CartaoSUS', 'Nascimento', 'Bairro', 'Tipo', 'DataAtendimento'],
                         f"historico_{cartao}")


# Função para exibir o menu de relatórios
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
