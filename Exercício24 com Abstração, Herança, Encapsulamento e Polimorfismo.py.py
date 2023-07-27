"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Clente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

from typing import Any


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
        self._endereco = []

    def inserir_endereco(self, rua, numero):
        self._endereco.append((rua, numero))

class Cliete(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self._banco = None
        self._conta = None

class Contas:
    def __init__(self, agencia, conta, saldo=0) -> None:
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo
    def saldo(self, saldo):
        self._saldo = saldo
        return self._saldo
    
    def deposito(self, valor):
        self._saldo = self._saldo + valor
        return self._saldo
    
    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo = self._saldo - valor
            return self._saldo
        return 'Saldo insuficiente'
    
class ContaPoupanca(Contas):
    def __init__(self, agencia, conta, saldo=0) -> None:
        super().__init__(agencia, conta, saldo)

class ContaCorrente(Contas):
    def __init__(self, agencia, conta, saldo=0) -> None:
        super().__init__(agencia, conta, saldo)

    def limite_extra(self, valor):
        if self._saldo <= valor:
            return valor


class Banco(Cliete, Contas):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def agencia():
        ...
    def criar_conta():
        ...
    @classmethod
    def autencic():
        ...





cliente1 = Pessoa('Jefferson', 28)
# cliente1.inserir_endereco('7 de setembro', 93)
print(vars(cliente1))

conta = Contas("0001", "202526-6")
conta.deposito(2000)
conta.sacar(3000)
print(vars(conta))





