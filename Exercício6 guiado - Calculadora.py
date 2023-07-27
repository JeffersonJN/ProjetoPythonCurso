""" Calculadora com while """
while True:
    numero_um = input("informe um numero. ")
    numero_dois = input("informe outro numero. ")
    operador = input('Digite um operador. + adição, - subtração, * multiplicação, / divisão. ')

    numeros_validados = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_um)
        num_2_float = float(numero_dois)
        numeros_validados = True

    except:
        numeros_validados = None

    if numeros_validados is None:
        print("Um ou ambos são dos numeros NÃO são validos.")
        continue

    operados_permitidos = '+-*/'

    if operador not in operados_permitidos:
        print("Operador Invalido. ")
        continue
    if len(operador) > 1:
        print("Digite apenas um. ")
    
    print("Realizando sua conta a baixo confira o resultado. ")
    if operador == "+":
        print(num_1_float + num_2_float)
    elif operador == "-":
        print(num_1_float - num_2_float)
    elif operador == "*":
        print(num_1_float * num_2_float)
    elif operador == "/":
        print(num_1_float / num_2_float)

    else:
        print("Não deveria chagara aqui. ")


    sair = input("Quer Sair. [S]air. ").lower().startswith('s')

    if sair is True:
        break