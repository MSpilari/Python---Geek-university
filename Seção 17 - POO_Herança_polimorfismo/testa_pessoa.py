from Secao17_POO_Heranca_Polimorfismo.classes.pessoa import Pessoa


class TestaPessoa(Pessoa):
    def __init__(self, codigo, nome, idade):
        super().__init__(codigo, nome, idade)

    def exibe(self, number=1):
        if number == 1:
            print('--Dados da Pessoa--\n'
                  f'Código: {self._Pessoa__codigo}\n'
                  f'Nome: {self._Pessoa__nome}\n'
                  f'Idade: {self._Pessoa__idade}')
        else:
            print('--Dados da Pessoa--\n'
                  f'Código: {self._Pessoa__codigo}\n'
                  f'Nome: {self._Pessoa__nome}')
