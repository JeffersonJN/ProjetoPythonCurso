# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

# def refazer(iten, lista=None):
#     if lista is None:
#         lista = []
#     lista.append(iten)
#     return lista

# def desfazer(iten, lista1=None):
#         if lista1 is None:
#             lista1 = []
#         lista1.pop(iten)
#         return lista1


def refazer(iten, lista=None):
    def desfazer(iten, lista1=None):
        if lista1 is None:
            lista1 = []
        lista1.pop(iten)
        return desfazer
    if lista is None:
        lista = []
    lista.append(iten)
    return lista




# def desfazer(iten, lista=None):
#     def refazer(iten, lista1=None):
#         if lista1 is None:
#            lista1 = [] 
#         lista1.append(iten)
#         return refazer
#     if lista is None:
#         lista = []
#     lista.pop(iten)
#     return lista


# lista = []
# lista_dois = []

# while True:
    
#     itens = input(
#         "\nComados: [L]istar, [R]efazer, [D]esfazer, [S]air.\n" \
#         "Favor informe itens da lista ou comados. " \
#         )
#     itens.lower()

#     if itens == 'listar' or itens == 'l':

#         if lista20 == []:
#             print('Nada a listado.\n ')

#         print(f'Tarefas: ', refazer(*lista20))

#         for k, i in  enumerate(lista, start=1):
            
#             print(f'[{k}] {i}')
#         for i in  lista:
#             print(f'{i}')

#     elif itens == 'refazer' or itens == 'r':
        
#         if lista20 != []:
#             refazer(lista20[-1])
#             desfazer(lista21.pop())
#             if lista20 == []:
#                 print('Nada a refazer.\n ')
#         elif lista == [] or lista_dois == []:
#             print('Nada a refazer.\n ')
        
            

#     elif itens == 'desfazer' or itens  == 'd':

#         if  lista20 == []:
#             print('Nada a desfazer.\n ')
#         else:
#             refazer((lista20[-1]))

            
#     elif itens == "s" or itens == 'sair':

#         print("Saindo....")
#         break   
    
#     else:
#         print(f'Adicionando {itens}.')
#         lista20 = refazer()
        # lista21 = desfazer(itens)


# lista = []
# lista_dois = []

# while True:
    
#     itens = input(
#         "\nComados: [L]istar, [R]efazer, [D]esfazer, [S]air.\n" \
#         "Favor informe itens da lista ou comados. " \
#         )
#     itens.lower()

#     if itens == 'listar' or itens == 'l':

#         if lista == []:
#             print('Nada a listado.\n ')

#         print(f'Tarefas: ')

#         for k, i in  enumerate(lista, start=1):
            
#             print(f'[{k}] {i}')
#         # for i in  lista:
#         #     print(f'{i}')

#     elif itens == 'refazer' or itens == 'r':
#         if lista_dois != []:
#             lista.append(lista_dois[-1])
#             lista_dois.pop()
#             if lista_dois == []:
#                 print('Nada a refazer.\n ')
#         elif lista == [] or lista_dois == []:
#             print('Nada a refazer.\n ')
        
            

#     elif itens == 'desfazer' or itens  == 'd':

#         if lista == []:
#             print('Nada a desfazer.\n ')
#         else:
#             lista_dois.append(lista[-1])
#             lista.pop()
            
#     elif itens == "s" or itens == 'sair':

#         print("Saindo....")
#         break   
    
#     else:
#         print(f'Adicionando {itens}.')
#         lista.append(itens)

# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'clear':
        os.system('clear')
        continue
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue