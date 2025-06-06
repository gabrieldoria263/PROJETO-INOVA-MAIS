import os
import csv

ARQ_PACIENTES = 'pacientes.csv'
ARQ_ATENDIMENTOS = 'atendimentos.csv'

def inicializar_arquivos():
    for arquivo, cabecalho in [(ARQ_PACIENTES, ['Nome', 'CartaoSUS', 'Nascimento', 'Bairro']),
                               (ARQ_ATENDIMENTOS, ['Data', 'CartaoSUS', 'Tipo', 'Observacoes'])]:
        if not os.path.exists(arquivo):
            with open(arquivo, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(cabecalho)

def carregar_dados():
    pacientes = {}
    with open(ARQ_PACIENTES, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            pacientes[row['CartaoSUS']] = row

    atendimentos = []
    with open(ARQ_ATENDIMENTOS, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            atendimentos.append(row)
    return pacientes, atendimentos
