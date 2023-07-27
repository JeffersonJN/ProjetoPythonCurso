# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertou = 0
errou = 0

for i in perguntas:
    print('Pergunta: ', i['Pergunta'], '\n')
    print('Opções: ',)
    rs1 = i['Resposta']
    resposta_ceta = 0   
    resposta_ceta2 = 0
    for k , i  in enumerate(i['Opções']):
        print(f'{k})', i)
        if i == rs1:
            
            resposta_ceta += k
            resposta_ceta2 += int(i)
        
    resposta = input('escolha uma reposta: ')

    coisa = '#' * 30
    repes = int(resposta)
    if resposta_ceta  == repes :
        print(f'{coisa}\nAcertou miseravil!!!!\n')
        acertou += 1
    
    else:
        print(f"{coisa}\nErrou mizeravil!!!!\n")
        errou += 1
    
print(f'Você Acertou {acertou} é Errou {errou}. ')


qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')