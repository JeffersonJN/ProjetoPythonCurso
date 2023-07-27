"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os


palavra_secreta = "perfume"
numero_tentativas = 0
letra_acertada = ''
while True:

    

    letra_informada = input('Informe uma letra. ')
    numero_tentativas += 1

    if len(letra_informada) > 1:
        print('Numero de letra excedente. ')
        continue
    
    if letra_informada in palavra_secreta:
        letra_acertada += letra_informada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print("Palavra formada: ", palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print("VOCÊ GANHOU!!! PARABÉNS!!!")
        print('A palavra  era ', palavra_secreta)
        print('Tentativas, ', numero_tentativas)
        numero_tentativas = 0
        letra_acertada = ''
        break