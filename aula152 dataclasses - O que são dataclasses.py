# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, asdict, astuple, field, fields

# @dataclass
# class Pessoa:
#     nome: str
#     idade: int  

"""
 frozen= deixa as inmutaveis
order= ordena lista

"""

# @dataclass(init=False)
# class Pessoa:
#     nome: str
#     sobrenome: str  
#     def __init__(self, nome, sobrenome) -> None:
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.nomecompleto = f'{self.nome} {self.sobrenome}'
#     def __post_init__(self):
#         print('oi')

# @dataclass
# class Pessoa:
#     nome: str
#     sobrenome: str  

#     def __post_init__(self):
#         self.nomecompleto = f'{self.nome} {self.sobrenome}'

    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'
    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)
# @dataclass(order=True)
# class Pessoa:
#     nome: str
#     sobrenome: str  

#     def __post_init__(self):
#         self.nomecompleto = f'{self.nome} {self.sobrenome}'

@dataclass(order=False)
class Pessoa:
    nome: str
    sobrenome: str  
    idade: int = 28
    endereco: list[str] = field(default_factory=list)


    def __post_init__(self):
        self.nomecompleto = f'{self.nome} {self.sobrenome}'

if __name__ == '__main__':

    p2 = Pessoa('Jefferson', 'Jose', )
    # # p2 = Pessoa('Ana', 'Maria Jesus')
    # # p2.nome_completo = 'Ana Maria Jesus'
    # # print(p2.nomecompleto)
    # lista = [Pessoa('A', 'X'), Pessoa('B', 'Y'), Pessoa('C', 'Z')]

    # # ordenadas = sorted(lista, reverse=True)
    # # print(ordenadas)
    # ordenadas = sorted(lista, reverse=False, key=lambda p:p.nome)
    # print(ordenadas)
    # ordenadas1 = sorted(lista, reverse=True, key=lambda p:p.sobrenome)
    # print(ordenadas1)
    # print(asdict(p2))
    # print(asdict(p2).keys())
    # print(asdict(p2).values())
    # print(asdict(p2).items())
    # print(astuple(p2))
    # print(astuple(p2)[0])
    # print(astuple(p2)[1])
    print(p2)
    print(fields(p2))