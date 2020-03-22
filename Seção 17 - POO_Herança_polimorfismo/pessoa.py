class Pessoa:
    def __init__(self, codigo, nome, idade):
        self.__codigo = codigo
        self.__nome = nome
        self.__idade = idade
        print('Construtor Padrão.')  # Retorna no local da instanciação.

    def exibe(self):
        print('--Dados da Pessoa--\n'
              f'Código: {self.__codigo}\n'
              f'Nome: {self.__nome}\n'
              f'Idade: {self.__idade}')

