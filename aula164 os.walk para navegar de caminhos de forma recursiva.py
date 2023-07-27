# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os
from itertools import count

caminho = os.path.join('/Users','JEFFERSON_PC', 'Pictures')
couter = count()
for root, dirs, files in os.walk(caminho):
    the_couter = next(couter)
    print(the_couter, "pasta atual", root)

    for dir_ in dirs:
        print("  ", the_couter, "DIR", dir_)
    for file_ in files:
        print("  ", the_couter, "FILE", file_)