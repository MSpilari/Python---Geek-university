""" Crie uma classe para representar uma pessoa, com os atributos privados de nome, idade e altura. Crie métodos
públicos necessários para sets e gets e também um método para imprimir os dados de uma pessoa."""


class Pessoa:

    def __init__(self, nome, idade=0, altura=0.0):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, name):
        self.__nome = name

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, age):
        self.__idade = age

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, height):
        self.__altura = height

    def mostra_tudo(self):
        print(f'Nome: {self.nome}\nIdade: {self.idade}\nAltura: {self.altura}')


user1 = Pessoa('Matheus', 26, 1.70)
user1.mostra_tudo()
