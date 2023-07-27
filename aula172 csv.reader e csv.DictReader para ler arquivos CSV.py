# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula173.csv'

with open(CAMINHO_CSV, 'r')as arquivo:
    # leitor = csv.reader(arquivo)
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(linha['Nome'], linha['Idade'], linha['Endereco'])
        # print(linha[0])
        # print(linha[1])
        # print(linha[2])
    # print(next(leitor))
