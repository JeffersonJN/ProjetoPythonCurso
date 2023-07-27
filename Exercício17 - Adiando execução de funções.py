# Exercício - Adiando execução de funções
def soma(x, y):

    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, *args):
    return funcao(*args)

# soma_com_cinco = criar_funcao(soma, 5)
# multiplica_por_dez = criar_funcao(multiplica, 10)

soma_com_cinco1 = criar_funcao(
    lambda y: lambda x: x + y, 5
)
print(soma_com_cinco1(7))

multiplica_por_dez1 = criar_funcao(
    lambda y: lambda x: x * y, 10
)
print(multiplica_por_dez1(10))


def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x,y)
    return interna

soma_com_cinco1 = criar_funcao(soma, 5)
multiplica_por_dez1 = criar_funcao(multiplica, 10)

print(soma_com_cinco1(50))
print(multiplica_por_dez1(20))