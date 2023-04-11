from empregado import *

class Vendedor(Empregado):

    def __init__(self, nome, endereco, telefone, codigo_setor: int, salario_base:float, imposto: float, valor_vendas:float, comissao:float):
        super().__init__(nome,endereco,telefone,codigo_setor,salario_base,imposto)
        self.comissao = comissao # porcentagem de comissão
        self.valor_vendas = valor_vendas # valor total dos artigos vendidos

    def calcularSalario(self):
        return super().calcularSalario() + (self.comissao * self.valor_vendas) / 100

    @property
    def valor_vendas(self):
        return self.__valor_vendas

    @valor_vendas.setter
    def valor_vendas(self,vendas):
        self.__valor_vendas = vendas

    @property
    def comissao(self):
        return self.__comissao

    @comissao.setter
    def comissao(self,comissao):
        assert 0 < comissao < 100, "Comissão deve ser de 0 a 100% "
        self.__comissao = comissao

    def __str__(self):
        return f"""
        {super().__str__()}
        Vendas totais: {self.valor_vendas}
        Comissão: {self.comissao} %
        """

