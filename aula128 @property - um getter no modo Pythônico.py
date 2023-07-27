# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código
class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta

    @property
    def cor_tampa(self):
        return 123456

###########################


caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tampa)

#####################################

# class Caneta:
#     def __init__(self, cor):
#         self.cor_tinta = cor

#     def get_cor(self):
#         print('GET COR')
#         return self.cor_tinta

# ###########################


# caneta = Caneta('Azul')
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
'''
Em Python, podemos usar o decorador @property para definir um método como um getter de um atributo de uma classe. O decorator @property torna o método como se fosse um atributo da classe, permitindo que o valor seja obtido sem a necessidade de usar parênteses para chamar o método.

Um exemplo de uso do @property:
'''
class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    @property
    def area(self):
        return self.comprimento * self.largura
"""
Neste exemplo, a classe Retangulo tem os atributos comprimento e largura. O método area é definido como um getter para o cálculo da área do retângulo. Ao usar o decorator @property, podemos acessar o valor da área usando a sintaxe de um atributo, sem a necessidade de chamar o método como uma função:
"""
r = Retangulo(4, 5)
print(r.comprimento)  # 4
print(r.largura)  # 5
print(r.area)  # 20