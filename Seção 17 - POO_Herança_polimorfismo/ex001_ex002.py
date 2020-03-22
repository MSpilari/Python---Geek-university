""" Escreva um código que apresente a classe Pessoa com os atributos nome, endereço, telefone e o método imprimir. O
método imprimir deve mostrar na tela os valores de todos os atributos.
Baseando-se no exercício enunciado acima, adicione um método construtor que permita a definição de todos os atributos no
momento da instanciação do objeto."""


class Pessoa:
    def __init__(self, nome, endereco, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    def imprimir_dados(self):
        print(f'Seu nome é {self.__nome}\nLogradouro {self.__endereco}\nNº de telefone {self.__telefone}')


p1 = Pessoa('Matheus', 'Avenida Martim Francisco', '(11)0000-0000')
p1.imprimir_dados()
