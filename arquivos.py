
import csv
import os

ARQ_PACIENTES = 'pacientes.csv'
ARQ_ATENDIMENTOS = 'atendimentos.csv'

def inicializar_arquivos():
    for arquivo, cabecalho in [
        (ARQ_PACIENTES, ['Nome', 'CartaoSUS', 'Nascimento', 'Bairro']),
        (ARQ_ATENDIMENTOS, ['Data', 'CartaoSUS', 'Tipo', 'Observacoes'])
    ]:
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

def salvar_relatorio(dados, colunas, nome_base):
    from datetime import datetime
    formato = input("Deseja salvar como (1) .txt ou (2) .csv? ")
    nome_arquivo = f"{nome_base}{datetime.now().strftime('%Y%m%d%H%M%S')}"
    os.makedirs("relatorios", exist_ok=True)

    if formato == '1':
        caminho = os.path.join("relatorios", f"{nome_arquivo}.txt")
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(" | ".join(colunas) + "\n")
            f.write("-" * (len(colunas) * 15) + "\n")
            for linha in dados:
                f.write(" | ".join(str(linha.get(c, '')) for c in colunas) + "\n")
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

    print(f"Relatório salvo como: {caminho}").