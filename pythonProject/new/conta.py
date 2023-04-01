import time
class ContaCorrente:

    def __init__(self, nome_titular: str, numero: int, saldo: float):
        self.nome_titular = nome_titular
        self.__numero = numero
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo
    @property
    def numero(self):
        return self.__numero
    @property
    def nome(self):
        return self.nome_titular
    @nome.setter
    def nome(self,novo):
        self.__nome_titular = novo
    def depositar(self, depositar):
        self.__saldo += depositar

    def sacar(self, saque):
        if self.saldo - saque < 0:
            print(f'Saldo Insuficiênte Para o Saque de R$ {saque:.2f}.')
            return False
        else:
            self.__saldo -= saque
            print(f'Saque R$ {saque:.2f} Realizado com Sucesso.')
            return True

    def __str__(self):
        return f'''
        Titular: {self.nome_titular}
        Número da Conta: {self.numero}
        Saldo: {self.__saldo:.2f}
        '''

    def menu_operacao(self):
            return f'''+---------------------------------+
    [1] - Depositar valores
    [2] - Realizar Saque
    [3] - Saldo da conta
    [4] - Encerrar Operações
+---------------------------------+
    '''


