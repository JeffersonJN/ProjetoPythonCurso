import contas

class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
        self.endereco = []

    def inserir_endereco(self, rua, numero):
        self.endereco.append((rua, numero))

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome
    @property
    def idade(self):
        return self._idade
    @idade.setter 
    def idade(self, idade: int):
        self._idade = idade

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attss = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{attss}'

class Cliete(Pessoa):
    def __init__(self, nome: str, idade: int):
        super().__init__(nome, idade)
        self.conta: contas.Contas | None= None


if __name__ == '__main__':
    c1= Cliete("Jefferson", 28)
    c1.conta = contas.ContaCorrente(2546, 25246, 100, 600)
    print(c1)
    print(c1.conta)