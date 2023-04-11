from empregado import *

class Administrador(Empregado):

    def __init__(self, nome, endereco, telefone, codigo_setor: int, salario_base: float, imposto: float, ajuda_de_custo: float):
        super().__init__(nome,endereco,telefone,codigo_setor,salario_base,imposto)
        self.ajuda_de_custos = ajuda_de_custo

    def calcularSalario(self):
        return super().calcularSalario() + self.ajuda_de_custos

    def __str__(self):
        return f"""
        {super().__str__()} 
        """



