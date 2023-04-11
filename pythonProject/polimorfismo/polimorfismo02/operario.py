from empregado import *

class Operario(Empregado):

    def __init__(self, nome, endereco, telefone, codigo_setor: int, salario_base:float, imposto: float,valor_producao:float, comissao:float):
        super().__init__(nome,endereco,telefone,codigo_setor,salario_base,imposto)
        self.valor_producao = valor_producao
        self.comissao = comissao

    def calcularSalario(self):
        return super().calcularSalario() + (self.comissao * self.valor_producao) / 100

    @property
    def valor_producao(self):
        return self.__valor_producao

    @valor_producao.setter
    def valor_producao(self, valor_producao):
        self.__valor_producao = valor_producao

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
        valor monetário dos artigos: {self.valor_producao}
        comissao: {self.comissao} %
        """


