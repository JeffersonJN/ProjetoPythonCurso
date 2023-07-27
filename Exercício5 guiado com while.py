"""
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])

nova_string = ''
nova_string += '*L*u*i*z* *O*t*á*v*i*o'

asterisco = "*"
nomes = "Jefferson Jose Nunes"
indice = 0

while indice < len(nomes):
    nova_str = asterisco + f'{nomes[indice]}'
    indice += 1
    print(nova_str, end="")


    """
Iterando strings com while
"""
#       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321


# nome = 'Maria Helena'  # Iteráveis

# indice = 0
# novo_nome = ''
# while indice < len(nome):
#     letra = nome[indice]
#     novo_nome += f'*{letra}'
#     indice += 1

# novo_nome += '*'
# print(novo_nome)