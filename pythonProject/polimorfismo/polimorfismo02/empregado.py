from pessoa import *
from abc import ABC, abstractmethod

class Empregado(Pessoa, ABC):

    def __init__(self, nome, endereco, telefone, codigo_setor: int, salario_base:float, imposto: float):
        super().__init__(nome,endereco,telefone)
        self.__codigo_setor = codigo_setor
        self.salarioBase = salario_base
        self.imposto = imposto

    @abstractmethod
    def calcularSalario(self):
        salario_descontado = self.salarioBase - (self.salarioBase * self.imposto)
        return salario_descontado
    @property
    def imposto(self):
        return self.__imposto

    @imposto.setter
    def imposto(self, imposto):

        self.__imposto = imposto

    @property
    def codigoSetor(self):
        return self.__codigo_setor

    @property
    def salarioBase(self):
        return self.__salarioBase

    @salarioBase.setter
    def salarioBase(self, novo_salario):
        self.__salarioBase = novo_salario

    def __str__(self):
        return f"""
{self.__class__.__name__}
        {super().__str__()}
        Código do Setor: {self.codigoSetor}
        Salário Base: {self.salarioBase}
        Taxa de imposto: {self.imposto}
        """

