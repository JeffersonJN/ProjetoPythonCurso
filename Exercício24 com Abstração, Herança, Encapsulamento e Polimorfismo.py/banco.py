import contas
import pessoas


class Banco:
    def __init__(
            self, 
            agencias: list[int] | None = None, 
            clintes: list[pessoas.Pessoa] | None = None, 
            contas: list[contas.Conta] | None = None,
    ) -> None:
        self.agencias = agencias or []
        self.clientes = clintes or []
        self.contas = contas or []


    def _checar_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False

    def _checar_cliente(self, clinte):
        if clinte in self.clientes:
            return True
        return False

    def _checar_conta(self, conta):
        if conta in self.contas:
            return True
        return False
    
    def _checar_se_conta_e_do_cliente(self, cliente, conta):
        if conta in cliente.conta:
            return True
        return False

    def autencicar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        return self._checar_agencia(conta) and self._checar_cliente(cliente) and self._checar_conta(conta)
   
   
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attss = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attss}'
    

if __name__ == '__main__':

    c1= pessoas.Cliete("Jefferson", 28)
    cc1 = contas.ContaCorrente(2546, 25246, 10000, 60000)
    c1.conta == cc1
    c2= pessoas.Cliete("Ana", 20)
    cp2 = contas.ContaPoupanca(2546, 35347, 5000)
    c2.conta == cp2
    c3= pessoas.Cliete("Robson", 59)
    cc3 = contas.ContaCorrente(2647, 23286, 5000, 6000)
    c3.conta == cc3
    c4= pessoas.Cliete("Maria", 35)
    cp4 = contas.ContaPoupanca(2445, 87259, 1000)
    c4.conta == cp4
    c5= pessoas.Cliete("Beatriz", 40)
    cc5 = contas.ContaCorrente(2748, 12871, 1000, 3000)
    c5.conta == cc5
    c6= pessoas.Cliete("Marcelo", 26)
    cp6 = contas.ContaPoupanca(2344, 87369, 3000)
    c6.conta == cp6

    banco = Banco()
    banco.clientes.extend([c1, c2, c3, c4, c5, c6])
    banco.contas.extend([cc1, cp2, cc3, cp4, cc5, cp6])
    banco.agencias.extend([2344, 2445, 2546, 2647, 2748])

    print(banco)
    print(banco.autencicar(c1, cc1))