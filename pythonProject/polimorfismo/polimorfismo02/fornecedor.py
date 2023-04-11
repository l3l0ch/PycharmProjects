from pessoa import *

class Fornecedor(Pessoa):

    def __init__(self, nome, endereco, telefone, valordivida: float, valorCredito: float):
        super().__init__(nome,endereco,telefone)
        self.valorDivida = valordivida
        self.valorCredito = valorCredito

    def obterSaldo(self):
        return self.valorCredito - self.valorDivida

    @property
    def valor_divida(self):
        return self.__valorDivida

    @valor_divida.setter
    def valor_divida(self, divida):
        self.__valorDivida = divida

    @property
    def valor_credito(self):
        self.__valorCredito

    @valor_credito.setter
    def valor_credito(self, credito):
        self.__valorCredito = credito

    def __str__(self):
        return f'''{self.__class__.__name__}
    {super().__str__()}
        Crédito: {self.valorCredito}
        Divida: {self.valorDivida}
    '''

