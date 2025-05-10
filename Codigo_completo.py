import csv
import os
from datetime import datetime

ARQ_PACIENTES = 'pacientes.csv'
ARQ_ATENDIMENTOS = 'atendimentos.csv'

def inicializar_arquivos():
    for arquivo, cabecalho in [(ARQ_PACIENTES, ['Nome', 'CartaoSUS', 'Nascimento', 'Bairro']),
                               (ARQ_ATENDIMENTOS, ['Data', 'CartaoSUS', 'Tipo', 'Observacoes'])]:
        if not os.path.exists(arquivo):
            with open(arquivo, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(cabecalho)

def cadastrar_paciente():
    print("\n--- Cadastro de Paciente ---")
    nome = input("Nome completo: ")
    cartao_sus = input("Número do cartão SUS: ")
    nascimento = input("Data de nascimento (DD/MM/AAAA): ")
    bairro = input("Bairro: ")

    with open(ARQ_PACIENTES, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([nome, cartao_sus, nascimento, bairro])
    print("Paciente cadastrado com sucesso!")
