import abc

class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float=0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    @abc.abstractclassmethod
    def sacar(self, valor: float) -> float: ...

    def deposito(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'Depositando {valor}')
        return self.saldo
    
    def detalhes(self, msg: str = '') -> None:
        print(f'o seu saldo e {self.saldo:.2f} {msg}')

    def saldos(self, saldo):
        self.saldo = saldo
        return self.saldo
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attss = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attss}'
    

class ContaPoupanca(Conta):
     def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'Sacando {valor:.2f}')
            return self.saldo
        print('Não foi possivel sacar valor desejado')
        self.detalhes(f'Saque negado {valor:.2f}')
        return self.saldo

class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float=0, limite: float=0) -> None:
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite    

        
        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'Sacando {valor:.2f}')
            return self.saldo
        print('Não foi possivel sacar valor desejado')
        print(f'Seu limite é {limite_maximo:.2f}')
        self.detalhes(f'Saque negado {valor:.2f}')
        return self.saldo
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attss = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, {self.limite!r})'
        return f'{class_name}{attss}'


if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222, 0)
    cp1.sacar(500)
    cp1.deposito(2000)
    cp1.sacar(500)
    cp1.deposito(2000)

    print('#' * 20)
    cc1 = ContaCorrente(333, 665, 0, 1000)
    cc1.sacar(250)
    cc1.deposito(1200)
    cc1.sacar(350)
    cc1.deposito(3900)
    cc1.sacar(4650)
    cc1.sacar(200)

