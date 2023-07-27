# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy

import os
import shutil
HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Pictures')
WARPPER = os.path.join(DESKTOP, 'wallpaper - Copia')
NOVA_PASTA = os.path.join(DESKTOP, 'Nova_Pasta')

# os.unlink(NOVA_PASTA)
shutil.rmtree(NOVA_PASTA, ignore_errors=True)
shutil.copytree(WARPPER, NOVA_PASTA)

shutil.move(NOVA_PASTA, NOVA_PASTA + '_eita',)


# os.makedirs(NOVA_PASTA, exist_ok=True)

# print(NOVA_PASTA)

# for root, dirs, files in os.walk(WARPPER):
#     for file_ in files:
#         caminho_atual = os.path.join(root, file_)
#         caminho_novo = os.path.join(root.replace(WARPPER,NOVA_PASTA), file_)
#         print(caminho_novo)
#         shutil.copy(caminho_atual, caminho_novo)


# # os + shutil - Copiando arquivos com Python
# # Vamos copiar arquivos de uma pasta para outra.
# # Copiar -> shutil.copy
# # import os
# # import shutil

# # HOME = os.path.expanduser('~')
# # DESKTOP = os.path.join(HOME, 'Desktop')
# # PASTA_ORIGINAL = os.path.join(DESKTOP, 'EXEMPLO')
# # NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')

# # os.makedirs(NOVA_PASTA, exist_ok=True)

# # for root, dirs, files in os.walk(PASTA_ORIGINAL):
# #     for dir_ in dirs:
# #         caminnho_novo_diretorio = os.path.join(
# #             root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
# #         )
# #         os.makedirs(caminnho_novo_diretorio, exist_ok=True)

# #     for file in files:
# #         caminho_arquivo = os.path.join(root, file)
# #         caminnho_novo_arquivo = os.path.join(
# #             root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
# #         )
# #         shutil.copy(caminho_arquivo, caminnho_novo_arquivo)