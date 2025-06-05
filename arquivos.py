
import os
import csv

# Caminho do arquivo de pacientes
ARQ_PACIENTES = 'pacientes.csv'
# Caminho do arquivo de atendimentos
ARQ_ATENDIMENTOS = 'atendimentos.csv'

# Função para inicializar os arquivos CSV, criando-os se não existirem
def inicializar_arquivos():
    for arquivo, cabecalho in [(ARQ_PACIENTES, ['Nome', 'CartaoSUS', 'Nascimento', 'Bairro']),
                               (ARQ_ATENDIMENTOS, ['Data', 'CartaoSUS', 'Tipo', 'Observacoes'])]:
# Cria o arquivo de atendimentos com cabeçalho, se não existir
        if not os.path.exists(arquivo):
            with open(arquivo, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(cabecalho)

# Função para carregar os dados dos arquivos CSV
def carregar_dados():
    pacientes = {}
# Carrega os dados de pacientes
    with open(ARQ_PACIENTES, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            pacientes[row['CartaoSUS']] = row

    atendimentos = []
# Carrega os dados de atendimentos
    with open(ARQ_ATENDIMENTOS, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            atendimentos.append(row)
    return pacientes, atendimentos