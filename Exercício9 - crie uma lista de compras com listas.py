"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
# lista = ['Maria', 'Helena', 'Luiz']
# lista.append('João')

# for indice, nome in enumerate(lista):
#     print(indice, nome, lista[indice])

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)


# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')

lista = []

while True:

    botao = input(
        'Selecione uma opcão abaixo: \n'
        '[i]nserir, [a]pagar, [l]istar e [s]air: '
                  )
    
    if botao.lower() == 'i': 
        item = (input('Insira um iten: '))
        lista.append(item)

        # for indice, nome in enumerate(lista, start=1):
        #     ...
    elif botao.lower() == 'l'and lista == []:
        print('Nenhum iten adicionado.')

    elif botao.lower() == 'l':
        print('Valores encontrado na lista: ')
        for indice, nome in enumerate(lista, start=1):
            print(indice, nome,)
    elif botao.lower() == 'a' and lista == []:
        print('Nenhum item encontrado para ser apagado. ')

    elif botao.lower() == 'a':

        valor_apagado = input(
            'Favor selecione numero da '\
            'lista do item que deseja ser apagado. '
            )
        try:
            indicess = int(valor_apagado)

            lista.pop(indicess - 1 )
        except:

            print('Informer um valor em numeros ou que contem na lista. ')
    
    elif botao.lower() == 's':
        print("Finalizando programa. ")

        break

    else:
        print('Informer um valor da acordo comforme o valor a cima. ')


        ...