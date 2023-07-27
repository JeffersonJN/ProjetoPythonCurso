# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela



class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Motor:
    def __init__(self, nome):
        self.nome = nome



class Fabricante:
    def __init__(self, nome):
        self.nome = nome

gol = Carro('Gol')
volkswagen = Fabricante('Volkswagen')
mt = Motor('V8 1.8')
gol.fabricante = volkswagen
gol.motor = mt


print(gol.nome, gol.fabricante.nome, gol.motor.nome)
# class Fabricante:
#     def __init__(self, nome):
#         self.fabricante = nome
#         self.motor = []

#     def lista(self, carro, motor):
#         self.carros = carro
#         self.motor = motor


# class Motor:
#     def __init__(self, nome):
#         self.motor = nome
#         self.carros = []

#     def inserir_carro(self, carro):
#         self.carros.append(Carro(carro))

#     def lista_carro(self):
#         self.motor = nome
#         for carro in self.carros:
#             self.motor = nome
#             print(carro.carros, self.motor)
#         return carro.carros

# class Carro:
#     def __init__(self, carro):
#         self.carros = carro



# fb = Fabricante("volkswagen")
# mt = Motor("V8 1.8")
# mt.inserir_carro('Gol')
# mt.inserir_carro('Palio')
# mt.inserir_carro('Vectra')
# mt.inserir_carro('Astra')
# mt.inserir_carro('Monsa')


# print(mt.motor, mt.lista_carro())

# print(mt.motor)
# print(fb.lista(mt.motor, mt.lista_carro()))