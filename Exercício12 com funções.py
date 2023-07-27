# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.


def cria_multiplicado(multiplicado):

    def multiplicar(numero):
        return numero * multiplicado
        
    return multiplicar

duplicar = cria_multiplicado(2)
print(duplicar(2))
triplicar = cria_multiplicado(3)
print(triplicar(2))
quadruplicar = cria_multiplicado(4)
print(quadruplicar(2))