import re
import math

"""
18-Faça um programa que peça o tamanho de um arquivo para download 
(em MB) e a velocidade de um link de Internet (em Mbps), calcule e 
informe o tempo aproximado de download do arquivo usando este link 
(em minutos).
"""


velocidade1 = input('Informe a velocidade de sua internet em Mb. ')
arquivo1 = input('Informe o tamanho do arquivo que deseja fazer o dowloand em Mb. ')
velocidade = velocidade1
arquivo = arquivo1

velocidade1  = re.sub(r'[^0-9]', "", velocidade1 )
arquivo1 = re.sub(r'[^0-9]', "", arquivo1)

def dowloand(num, valor):
    return num / (valor/8)


if velocidade1.isdigit() and arquivo.isdigit():
    velocidade = float(velocidade)
    arquivo = float(arquivo)
    print(f'Tempo aproximado do dowloand do arquivo e de {math.ceil(dowloand(arquivo, velocidade))} segundos ou {(dowloand(arquivo, velocidade)//60)} minutos.  ')





else:
    print("Favor informa um numero valido. ")



"""
17-Faça um Programa para uma loja de tintas. O programa deverá pedir o 
tamanho em metros quadrados da área a ser pintada. Considere que a 
cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a 
tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões 
de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os 
respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, 
considere latas cheias.
"""

# area = input('Informe a quantidade de metros quadrados a ser pintada. ')
# area_total = area
# area = re.sub(r'[^0-9]', '', area)
# latas = 18 * 6
# galoes = 3.6 * 6
# def tinta_inteira(num, num2):
#     res = num // num2
#     rest = num / num2
#     tos = rest - res
#     if res == rest:
#         return rest
#     print(rest)
#     return tos

# def tinta_inteira(num, num2):
#     res = num // num2
#     return res

# def tinta_flolt(num, num2):
#     rest = num / num2
#     return rest

# if area.isdigit():
#     area_total = float(area_total)
#     qnt_latas = area_total / latas
#     qnt_galoes = area_total / galoes
#     qnt_latas = round((qnt_latas * 1.10)) 
#     qnt_galoes = round((qnt_galoes * 1.10))
#     qnt_lata = qnt_latas * 80.00
#     qnt_galoe = qnt_galoes * 25.00

#     if area_total <= (galoes * 4):
#         print(f'A quantidade necessaria de galoes são. {qnt_galoes}. valor total R$: {qnt_galoe:.2f}')
    
#     elif area_total > (galoes * 4) and area_total < (galoes * 5):
#         lata_total = tinta_flolt(area_total, latas)
#         lata_total = round(lata_total * 1.10)
#         print(f'A quantidade necessaria de latas são. {lata_total}. valor total R$: {qnt_lata:.2f}')

#         if tinta_inteira(area_total, latas) > 1 or tinta_inteira(area_total, latas) == tinta_flolt(area_total, latas):
#                 lata_total = tinta_flolt(area_total, latas)
#                 lata_total = round(lata_total * 1.10)
#                 print(f'A quantidade necessaria de latas são. {lata_total}. valor total R$: {qnt_lata:.2f}')

#     elif tinta_inteira(area_total, latas) == tinta_flolt(area_total, latas):
#                 lata_total = tinta_flolt(area_total, latas)
#                 lata_total = round(lata_total * 1.10)
#                 print(f'A quantidade necessaria de latas são. {lata_total}. valor total R$: {qnt_lata:.2f}')

#     else:
#         galoe_resto = tinta_flolt(area_total, latas) - tinta_inteira(area_total, latas)  
#         galoe_resto = round((galoe_resto * 1.10), 2)
#         galoe_resto = math.ceil(galoe_resto)
#         lata_total = tinta_inteira(area_total, latas)

#         print(f'A quantidade necessaria de latas são. {lata_total}. e de galoes são {galoe_resto}, valor total R$: {qnt_lata + galoe_resto * 25  :.2f}')
                 
# else:
#     print("Favor informa um numero valido. ")


"""
16-Faça um programa para uma loja de tintas. O programa deverá pedir o 
tamanho em metros quadrados da área a ser pintada. Considere que a 
cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a 
tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao 
usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
# area = input('Informe a quantidade de metros quadrados a ser pintada. ')
# area_total = area
# area = re.sub(r'[^0-9]', '', area)
# latas = 18 * 3

# def tinta():
#     ...

# if area.isdigit():
#     area_total =float(area_total)
#     qnt = area_total / latas
#     qnt = round(qnt + 0.5)
#     qnt_lata = qnt * 80.00
#     print(f'A quantidade necessaria de latas são. {qnt:.2f}. valor total R$: {qnt_lata:.2f}')

# else:
#     print("Favor informa um numero valido. ")


"""
15-Faça um Programa que pergunte quanto você ganha por hora e o 
número de horas trabalhadas no mês. Calcule e mostre o total do 
seu salário no referido mês, sabendo-se que são descontados 11% 
para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$

"""

# horas = input('Informer a quantidade de horas trabalhada no mês. ')
# saldos = input('Informer a valor de hora trabalhada. ')
# hora = horas
# saldo = saldos

# horas = re.sub(r'[^0-9]', '', horas)
# saldos = re.sub(r'[^0-9]', '', saldos)

# # def salario(traba, valor):
# #     return traba * valor

# # salarios = salario
# # def irs(valor, irss):
# #     vas = valor * irss
# #     return vas

# # ir = irs
# # def insss(valor):
# #     return valor * 0.08

# # inss = insss
# # def sind(valor):
# #     return valor * 0.05

# # sindc = sind

# if horas.isdigit() and saldos.isdigit():
#     hora = float(hora)
#     saldo = float(saldo)
#     salarios = hora * saldo

#     print(f'+ Salário Bruto :       R$ {salarios:.2f}\n' \
#           f'- IR (11%) :            R$ {salarios * 0.11:.2f}\n'\
#           f'- INSS (8%) :           R$ {salarios * 0.08:.2f}\n'\
#           f'- Sindicato ( 5%) :     R$ {salarios * 0.05:.2f}\n'\
#           f'= Total dos descontos : R$ {salarios * 0.24:.2f}\n'
#           f'= Salário Liquido :     R$ {salarios * 0.76:.2f}'
#           )


# else:
#     print("Favor informa um numero valido. ")

"""
14-João Papo-de-Pescador, homem de bem, comprou um microcomputador para 
controlar o rendimento diário de seu trabalho. Toda vez que ele traz 
um peso de peixes maior que o estabelecido pelo regulamento de pesca 
do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por 
quilo excedente. João precisa que você faça um programa que leia a 
variável peso (peso de peixes) e calcule o excesso. Gravar na variável 
excesso a quantidade de quilos além do limite e na variável multa o 
valor da multa que João deverá pagar. Imprima os dados do programa 
com as mensagens adequadas."""

# peixe = input('Informer a quantidade de peixes. ')
# peixe1 = peixe

# peixe = re.sub(r'[^0-9]', '', peixe)

# if peixe.isdigit():
#     peixe1 = float(peixe1)
#     if peixe1 <= 50:
#         print(f"A quantidade informada {peixe1} kg de peixes, não tem valor de excedente a ser paga. ")
#     elif peixe1 > 50:
#         multa = (peixe1 - 50) * 4
#         print(f'A quantidade de kilos excedentes foi de {peixe1-50:.2f} Kg sendo multa calculada no valor de R$ {multa:.2f}. ')

# else:
#     print("Favor informa um numero valido. ")

"""
13-Tendo como dado de entrada a altura (h) de uma pessoa, construa um 
algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7"""

# sexo = input("Informer 'H' para Homem ou 'M' para Mulher. ")
# sexo.lower
# altu = input('Favor informar sua altura. ')
# tura = altu
# altu = re.sub(r'[^0-9]', '', altu)


# def peso_ideal_valor(valor, altura):
#     if valor == "h":
#         return (72.7*altura) - 58
#     elif valor == 'm':
#         return (62.1*altura) - 44.7
    
# if altu.isdigit() and sexo == "h" or sexo == "m":
#     tura = float(tura)
#     print(f'O seu peso ideal é. {round(peso_ideal_valor(sexo, tura), 2)}')

# else:
#     print("Favor informa um numero valido. ")




"""
12-Tendo como dados de entrada a altura de uma pessoa, construa um 
algoritmo que calcule seu peso ideal, usando a seguinte fórmula: 
(72.7*altura) - 58
"""
# altu = input('Favor informar sua altura. ')
# tura = altu
# altu = re.sub(r'[^0-9]', '', altu)


# def peso_ideal(altura):
#     return (72.7*altura) - 58


# if altu.isdigit():
#     tura = float(tura)
#     print(f'O seu peso ideal é. {round(peso_ideal(tura), 2)}')

# else:
#     print("Favor informa um numero valido. ")

# try:
#     try:
#         def peso_ideal(altura):
#             return (72.7*altura) - 58
#     except TypeError:
#         print("Favor informa um numero valido. ")

#     if altu.isdecimal():
#         altu = float(altu)
    

#     print(f'O seu peso ideal é. {round(peso_ideal(altu), 2)}')
    
# except ValueError:
#     print("Favor informa um numero valido. ")

# else:
#     print("Favor informa um numero valido. ")

# altu = re.sub(r'[^A-Za-z]', '', altu)


# try:
#     if altu.isdigit():

#     print(f"{altu}")


"""11-Faça um Programa que peça 2 números inteiros e um número real. 
Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo."""

# num_1 = input('Favor informa um números inteiros. ')
# num_2 = input('Favor informa um números inteiros. ')
# num_3 = input('Favor informa um números real. ')

# def dobro(inteiro, real):
#     return (inteiro * 2) * (real / 2)

# def somar(inteiro, real):
#     return (inteiro * inteiro * inteiro) + real

# def cubo(real):
#     return real ** 2

# if num_1.isdigit() and num_2.isnumeric() and num_3.isnumeric():
#     num_4 = float(num_1)
#     num_5 = float(num_2)
#     num_6 = float(num_3)

#     print(f"O produto do dobro do primeiro com metade do segundo é. {dobro(num_4, num_5)}")
#     print(f"A soma do triplo do primeiro com o terceiro. {somar(num_4, num_6)}")
#     print(f"O terceiro elevado ao cubo. {cubo(num_6)}")

# else:
#     print("Favor informa numero validos. ")

"""
10-Faça um Programa que peça a temperatura em graus Celsius, 
transforme e mostre em graus Fahrenheit.
"""

# nun_celsius = input('Favor informar a temperatura em graus Celsius. ')

# def conversor_fahrenheit(numero):
#     return  (numero * 9 / 5) + 32

# if nun_celsius.isdigit():
#     nun_celsius = int(nun_celsius)
#     print(f"O grau em Fahrenheit e. {round(conversor_fahrenheit(nun_celsius), 1)}")
# else:
#     print("Favor informa apenas numeros validos. ")




"""
9-Faça um Programa que peça a temperatura em graus Fahrenheit, 
transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9)."""

# nun_fahren = input('Favor informar a temperatura em graus Fahrenheit. ')

# def conversor_celsius(numero):
#     return 5 * ((numero-32) / 9)

# if nun_fahren.isdigit():
#     nun_fahren = int(nun_fahren)
#     print(f"O grau em Celsius e. {round(conversor_celsius(nun_fahren), 1)}")
# else:
#     print("Favor informa apenas numeros validos. ")


"""8-Faça um Programa que pergunte quanto você ganha por hora e o 
número de horas trabalhadas no mês. Calcule e mostre o total 
do seu salário no referido mês."""

# nun_hora = input('Favor informar quantidade horas trabalhada. ')
# nun_traba = input('Favor informar valor das sua horas trabalhada. ')

# def hora(horas, preco):
#     return horas * preco

# if nun_hora.isdigit() and nun_traba.isdigit():
#     nun_traba = float(nun_traba)
#     nun_hora = float(nun_hora)
#     print(f'Seu salario e. {hora(nun_traba, nun_hora)}')
# else:
#     print("Favor informa apenas numeros validos. ")

"""7-Faça um Programa que calcule a área de um quadrado, 
em seguida mostre o dobro desta área para o usuário."""

# m = input('Informe um lado do quadrado: ')

# def quadrado(numero):
#     return numero * numero * 2

# if m.isdigit():
#     num = float(m)
#     print(f'o dobro drea do quadrado é. {quadrado(num)}')

# else:
#     print('Favor informa um nomero valido. ')



"""
6- Faça um Programa que peça o raio de um 
círculo, calcule e mostre sua área."""


# m = input('Informe um raio em centimentros PI sera considerado 3,14 : ')

# if m.isdigit():
#     c = 3.14 * (float(m)**2)
#     print(f"A area do circulo é {c} centimetro: ")
# else:
#     print("Favor informa apenas em numeros: ")






'''5-Faça um Programa que converta metros para centímetros.'''

# m = input('Informe a quantidade de metros: ')
# if m.isdigit():
#     c = float(m)*100
#     print(f"Os {m} metros são {c} centimetro: ")
# else:
#     print("Favou informa apenas em numeros: ")



"""
4-Faça um Programa que peça as 4 notas bimestrais e mostre a média."""

# def media(a, b, c, d):
#     if a.isdigit() and b.isdigit() and c.isdigit() and d.isdigit():
#         return (float(a) + float(b) + float(c) + float(d))/ 4
    
#     else:
#         return None


# a = input('Informe um numero: ')
# b = input('Informe um numero: ')
# c = input('Informe um numero: ')
# d = input('Informe um numero: ')

# if media == None:
#     print("Favor informar apenas numeros: ")
    

# else:
#     print("Sua media é: ", media(a, b, c, d))

'''3-Faça um Programa que peça dois números e imprima a soma.'''


# def soma(a, b):

#     if a.isdigit() and b.isdigit():
#         return int(a) + int(b)
#     else:
#         return "Por favor informar apenas numeros: "

# a = input('Informe um numero: ')
# b = input('Informe um numero: ')
# print("Sua soma é: ", soma(a,b))

'''2-Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
'''

# def ints(nun=""):
#     return nun

# numero = input('Informe o numero: ')

# print("O numero informado foi: ", ints(numero))



'''1-Faça um Programa que mostre a mensagem "Alo mundo" na tela.'''

# def ola(msg="Olá Mundo"):
#     return msg

# print(ola())
