# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


# def multi(*args):
#     total = 1
#     for numero in args:
#         total *= numero

#     if total % 2 == 0:
#         print('par')
#     else:
#         print('impar')
#     return total

# print(multi(1, 3, ))




# def multi(*args):
#     total = 1
# Exercício11 com funções + Solução (prepare-se para pausar)    for numero in args:
#         total *= numero



#     def asd(par="Par" ,impar='impar'):
        

#         if total % 2 == 0:
#             return par
    
#         return impar 
        
#     asd(par="par", impar="impar")
        
#     return total
# print(multi(1, 4, ))
# print(asd('asd'))
###################################################################
def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


multiplicação = multiplicar(10, 2, 3, 4, 5)
print(multiplicação)


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'


outro_par_impar = par_impar
dois_e_par = outro_par_impar(2)
print(dois_e_par)
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))

print(par_impar is outro_par_impar)