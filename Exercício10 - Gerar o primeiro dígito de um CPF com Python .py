"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7

"""
'''
# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)
cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)


'''
"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""
# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)
"""
cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)"""

import re
import sys
cpf_informado = "aaaaa"
cpf_novo = []
soma = 0
indice = 10
contagem = 11
cpf_novo1 = ''

entrada_sequencial = cpf_informado == cpf_informado[0] * len(cpf_informado)

if entrada_sequencial:
    print('Dados sequeciais')
    sys.exit()

elif cpf_informado.isdigit() and len(cpf_informado) == 11:

    # cpf_sendo_verificado = int(cpf_informado)
    for i in cpf_informado[0:9]:
        calculo = indice * int(i)
        cpf_novo.append(int(i))
        soma += calculo
        indice -= 1

    digito = (soma * 10) % 11 
    novo_digito = digito if digito < 9 else 0
    cpf_novo.append(novo_digito)
    soma = 0

    for j in cpf_informado[0:10]:
        calculo = indice * int(j)
        soma += calculo
        contagem -= 1

    digito = (soma * 10) % 11 
    novo_digito = digito if digito < 9 else 0
    cpf_novo.append(novo_digito)

    cpf_novo = str(cpf_novo)
    cpf_novo1 = re.sub(r'[^0-9]', '', cpf_novo)

    if cpf_novo1 == cpf_informado:
    
        print(f'{cpf_novo1} cpf valido')

    else:
        print('Cpf Invalido')


else:
    print('CPF digitado incorretamente. ')