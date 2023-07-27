# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'

# C:\Users\JEFFERSON_PC\Pictures
import os
caminho = os.path.join('/Users','JEFFERSON_PC', 'Pictures')

for iten in os.listdir(caminho):
    print(iten)
    caminho_completo = os.path.join(caminho, iten)

    if not os.path.isdir(caminho_completo):
        continue
    for pasta in os.listdir(caminho_completo):
        print('        ',pasta)
