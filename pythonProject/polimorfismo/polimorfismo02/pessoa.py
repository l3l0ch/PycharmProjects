class Pessoa:

    def __init__(self, nome: str, endereco: str, telefone: int):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, name):
        self.__nome = name

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    def __str__(self):
        return f"""
        Nome: {self.nome}
        Endereço: {self.endereco}
        Telefone: {self.telefone}
        """


