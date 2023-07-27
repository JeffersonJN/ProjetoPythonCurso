# import re
# import math

'''17-Faça um Programa que peça um número correspondente a um determinado ano e
em seguida informe se este ano é ou não bissexto.'''

# ano = input('Informe um ano para saber se ele e bissexto ou não. ')


# def bissexto(valor):
#     if valor[-2:] == "00":
#         valore = valor
#         valores = int(valore)
#         if valores % 400 == 0:
#             return f"Ano {valor} é bissexto."
#         return f"Ano {valor} NÂO é bissexto."
#     else:
#         valores = valor[-2:]
#         valore = int(valores)
#         if valore / 4 != 0 and valore % 4 == 0:
#             return f"Ano {valor} é bissexto."
#         return f"Ano {valor} NÂO é bissexto."


# print(bissexto(ano))


"""16-Faça um programa que calcule as raízes de uma equação do segundo grau, na
forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as
consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo.
grau
 e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais.
Informe
ao
 usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao
usuário;"""

# while True:
#     num_4 = input('informer um numero A. ')
#     num_1 = int(num_4)
#     if num_1 == 0:
#         print('O valor de "A" e igual a 0 não sendo possivel calcular')
#         break
#     num_5 = input('informer um numero B. ')
#     num_2 = int(num_5)
#     num_6 = input('informer um numero C. ')
#     num_3 = int(num_6)

#     def equation(a, b, c):
#         D = b ** 2 - 4*a*c
#         if D < 0:
#             retouns = "Delta negativo sendo assim a a equação",
#             f"não possui raizes reais seu o Delta {D}. \n Finalizando
# Progama"
#             return retouns
#         x1 = (((-1)*b + (D ** 0.5))/(2*a))
#         x2 = (((-1)*b - (D ** 0.5))/(2*a))
#         if D == 0:
#             return f'A equação possui apenas uma raiz real {x1}.'
#         if D > 0:
#             return f'A equação possui duas raiz reais {x1}, {x2}'

#     print(equation(num_1, num_2, num_3))
#     break

"""15-Faça um Programa que peça os 3 lados de um triângulo. O programa deverá
informar se os valores podem ser um triângulo. Indique, caso os lados formem um
triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior
que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;"""

# lados_um = input("Informe um lado. ")
# lados_dois = input("Informe dois lado. ")
# lados_tres = input("Informe tres lado. ")


# def triangulo(valor, num, lado):
#     if valor ==  num == lado:
#         return 'E um Triângulo Equilátero: '
#     if valor ==  num or valor == lado or num == lado:
#         return 'Triângulo Isósceles: '
#     if valor !=  num != lado:
#         return 'E um Triângulo Escaleno: '

# print(triangulo(lados_um, lados_dois, lados_tres))


"""14-Faça um programa que lê as duas notas parciais obtidas por um aluno numa
disciplina ao longo de um semestre, e calcule a sua média. A atribuição de
conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e
a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito
for D ou E.
"""
# nota_a = input('Informe primeira nota. ')
# nota_b = input('Informe segunda nota. ')
# nota_a, nota_b = float(nota_a), float(nota_b)
# def media(num, valor):
#     return(num + valor )/ 2

# def conseito(valor):
#     if valor >=9 and valor <= 10:
#         return "Sua nota e 'A' Você foi APROVADO."
#     if valor >=7.5 and valor <= 9:
#         return "Sua nota e 'B' Você foi APROVADO."
#     if valor >=6 and valor <= 7.5:
#         return "Sua nota e 'C' Você foi APROVADO."
#     if valor >=4 and valor <= 6:
#         return "Sua nota e 'D' Você foi REPROVADO."
#     if valor >=0 and valor <= 4:
#         return "Sua nota e 'E' Você foi REPROVADO."
#     return 'Favor informa nota valida'

# nota_total = media(nota_a, nota_b)

# print(conseito(nota_total))

"""13-Faça um Programa que leia um número e exiba o dia correspondente da
semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor
inválido."""

# semana = input('Favor informe um numero correspondente ao numero da semana.')


# def week(value):
#     if value == "1":
#         return 'Domingo'
#     if value == "2":
#         return 'Segunda'
#     if value == "3":
#         return 'Terça'
#     if value == "4":
#         return 'Quarta'
#     if value == "5":
#         return 'Quinta'
#     if value == "6":
#         return 'Sexta'
#     if value == "7":
#         return 'Sabado'
#     return 'valor inválido'


# print(week(semana))

"""12-Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
descontos são do Imposto de Renda, que depende do salário bruto (conforme
tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido
corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao
usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a
quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00"""

# salario: int | float = input("Informe salario atual. ")

# salario = float(salario)


# def desconto_ir(valor: float):
#     if valor <= 900:
#         return 0
#     if valor <= 1500:
#         return valor * 0.05
#     if valor <= 2500:
#         return valor * 0.10
#     if valor >= 2500:
#         return valor * 0.20


# def fgts(valor):
#     return valor * 0.11


# def inss(valor: float):
#     return valor * 0.10


# def desconte(valor: float, val: float):
#     return valor + val


# print(f'Salário Bruto:                  : R$ {salario:.2f}')
# print(f'(-) IR (5%)                     : R$ {desconto_ir(salario):.2f}')
# print(f'(-) INSS ( 10%)                 : R$ {inss(salario):.2f}')
# print(f'FGTS (11%)                      : R$ {fgts(salario):.2f}')
# print(
#     f'Total de descontos              : R$ {desconte(desconto_ir(salario),
# inss(salario)):.2f}')
# print(
#     f'Salário Liquido                 : R$ {(salario - desconte(desconto_ir(
# salario), inss(salario))):.2f}')


# print(
#     f'Salário Bruto:                  : R$ {salario}'
#     f'(-) IR (5%)                     : R$ {desconto_ir(salario)}\n' /
#     f'(-) INSS ( 10%)                 : R$ {inss(salario)}\n'
#     f'FGTS (11%)                      : R$ {fgts(salario)}\n'
#     f'Total de descontos              : R$ {desconte(desconto_ir(
# salario),
#  inss(salario))}n'
#     f'Salário Liquido                  : R${desconte(fgts(salario),
#  inss(salario))}'
# )

"""11-As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhe contraram para desenvolver o programa que calculará os
reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo
o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado,
informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento."""

# salario: int | float = input("Informe salario atual. ")


# def aumento_salario(valor: float):
#     valor = float(valor)
#     if valor <= 280 and valor >= 0:
#         return f'O salário antes do reajuste: R$ {valor:.2f} \n' \
#             f'O percentual de aumento aplicado: 20%.\n'\
#             f'O valor do aumento R$ {valor*0.20:.2f}\n' \
#             F'o novo salário R$ {valor*1.20:.2f}, após o aumento.\n'
#     if valor <= 700:
#         return f'O salário antes do reajuste: R$ {valor:.2f} \n' \
#             f'O percentual de aumento aplicado: 15%.\n'\
#             f'O valor do aumento R$ {valor*0.15:.2f}\n' \
#             F'o novo salário R$ {valor*1.15:.2f}, após o aumento.\n'
#     if valor <= 1500:
#         return f'O salário antes do reajuste: R$ {valor:.2f} \n' \
#             f'O percentual de aumento aplicado: 10%.\n'\
#             f'O valor do aumento R$ {valor*0.10:.2f}\n' \
#             F'o novo salário R$ {valor*1.10:.2f}, após o aumento.\n'

#     return f'O salário antes do reajuste: R$ {valor:.2f} \n' \
#         f'O percentual de aumento aplicado: 5%\n'\
#         f'O valor do aumento R$ {valor*0.05:.2f}\n' \
#         F'o novo salário R$ {valor*1.05:.2f}, após o aumento.\n'


# print(aumento_salario(salario))


'''10-Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem
"Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme
o caso.
'''

# turno = input('Informe M-matutino ou V-Vespertino ou N- Noturno. ')


# def turnos(valor: str):
#     valor.lower
#     if valor == "m":
#         return "Bom Dia!"
#     if valor == "v":
#         return "Boa Tarde!"
#     if valor == "n":
#         return "Boa Noite!"
#     return "Valor Inválido!"


# print(turnos(turno))

"""
9-Faça um Programa que leia três números e mostre-os em ordem decrescente."""

# # produto: float = input('Informe o valor do produto. ')
# # produto2: float = input('Informe o valor do produto. ')
# # produto3: float = input('Informe o valor do produto. ')


# # lista = [produto, produto2, produto3]
# # lista = sorted(lista, reverse=True)
# # lista.sort (produto, produto2, produto2)
# # print(f'{lista}')

'''
8-Faça um programa que pergunte o preço de três produtos e informe qual
produto você deve comprar, sabendo que a decisão é sempre pelo mais
barato'''

# produto: float = input('Informe o valor do produto. ')
# produto2: float = input('Informe o valor do produto. ')
# produto3: float = input('Informe o valor do produto. ')


# lista = [produto, produto2, produto3]
# lista = sorted(lista)
# # lista.sort (produto, produto2, produto2)
# print(f'O valor do produto mais barato é {lista[0]}')

"""
7-Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
# num: str|float = input('Informe um numeros: ')
# num1 = input('Informe um numeros: ')
# num2 = input('Informe 3 numeros: ')

# def maior(value: int|float, value1: int|float, value2: int|float):
#     if value == value1 == value2:
#         return 'Valores iguais'
#     elif value > value1 and value > value2 and value1 > value2:
#             return f'{value} e o maior e o menor é {value2}'
#     elif value > value1 and value > value2 and value1 > value2:
#         return f'{value} e o maior e o menor é {value1}'
#     elif value1 > value and value1 > value2 and value < value2:
#         return f'{value1} e o maior e o menor é {value}'
#     elif value1 > value and value1 > value2 and value > value2:
#         return f'{value1} e o maior e o menor é {value2}'
#     elif value2 > value and value2 > value1 and value < value1:
#         return f'{value2} e o maior e o menor é {value}'

#     return f'{value2} e o maior e o menor é {value1}'

# print(maior(num, num1, num2))


"""
6-Faça um Programa que leia três números e mostre o maior deles."""

# num: str|float = input('Informe um numeros: ')
# num1 = input('Informe um numeros: ')
# num2 = input('Informe 3 numeros: ')

# def maior(value: int|float, value1: int|float, value2: int|float):
#     if value == value1 == value2:
#         return 'Valores iguais'
#     if value > value1 or value > value2:
#         return f'{value} e o maior'
#     if value1 > value and value1 > value2:
#         return f'{value1} e o maior'
#     return f'{value2} e o maior'


# print(maior(num, num1, num2))

"""
5-Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez."""

# note = input('Informe sua nota do primeiro bimestre. ')
# note2 = input('Informe sua nota do segunda bimestre. ')
# notes = note
# note22 = note2

# note = re.sub(r'[^0-9]', '', note)
# note2 = re.sub(r'[^0-9]', '', note2)

# def note_total(note, value):
#     media = (note + value) / 2
#     if media == 10:
#         return f"Sua media é {media} é Voce foi Aprovado com Distinção. "
#     elif media >= 7 and media < 10:
#         return f"Sua media é {media} é Voce foi Aprovado. "
#     return f"Sua media é {media} é Voce foi Reprovado. "

# if note.isdigit() and note2.isdigit():
#     notes = float(notes)
#     note22 = float(note22)

#     print(f'{note_total(notes, note22)}')

# else:
#     print("Favor informar numeros validos. ")


"""
4-Faça um Programa que verifique se uma letra digitada é vogal ou consoante."""

# vogal = input('Favor informar uma letra. ')
# vogal = re.sub(r'[^a-zA-Z]', '', vogal )
# def vogais(valor):
#     if valor == "a" or valor == "e" or valor == "i" or valor == "o" or
# valor == "u":
#         return 'Vogal'
#     return 'Consoante'

# if not vogal.isdigit() and len(vogal) > 1:
#     vogal = vogal.lower()
#     for k in vogal:
#         print(f'{k}, {vogais(k)}')
# else:
#     print('Favor informar dados validos')


"""
3-Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido"""

# verifica = input("Favor informar [F]eminino ou [M]asculino. ")

# def sexo(valor):
#     if valor == 'f':
#         return 'Sexo Feminino'
#     if valor == 'm':
#         return 'Sexo Masculino'
#     return "Sexo Inválido"


# if not verifica.isdigit():
#     verifica = verifica.lower()
#     print(sexo(verifica))

# else:
#     print('Favor informar dados validos. ')

"""
2-Faça um Programa que peça um valor e mostre na tela se o valor é
positivo ou negativo."""

# num = input("Favor informe um  numero. ")
# nums = num
# num = re.sub(r'[^0-9]', '', num)

# def posi(num):
#     if num >= 0:
#         return f'O numero {num} é positivo. '
#     return f'O numero {num} é negativo. '

# if num.isdigit():
#     nums = float(nums)
#     print(posi(nums))
# else:
#     print('Favor informar um valor valido. ')


"""
1-Faça um Programa que peça dois números e imprima o maior deles."""

# um = input('Favor informe um numero. ')
# dois = input('Favor informe mais um numero. ')
# uns = um
# doises = dois

# um = re.sub(r'[^0-9]', '', um)
# dois = re.sub(r'[^0-9]', '', dois)

# def maior(num, valor):
#     if num == valor:
#         return "São iguais"
#     elif num > valor:
#         return f"O maior é {num}"
#     elif num < valor:
#         return f"O maior é {valor}"

# if um.isdigit() and dois.isdigit():
#     uns = int(uns)
#     doises = int(doises)
#     print(maior(uns, doises))
# else:
#     print('Favor informar um valor valido. ')
