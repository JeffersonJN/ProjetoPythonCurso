import json
from execicio22_a import CAMINHA_ARQUIVO, Pessoa

with open(CAMINHA_ARQUIVO, 'r', encoding="UTF-8") as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])
    p4 = Pessoa(**pessoas[3])

    print(p1.nome)
    print(p2.nome)
    print(p3.nome)
    print(p4.nome)