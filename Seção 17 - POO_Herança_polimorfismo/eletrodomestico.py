class Eletrodomestico:
    def __init__(self, ligado=False):
        self.__ligado = ligado

    @property
    def ligado(self):
        return self.__ligado

    def ligar_desligar(self):
        if self.__ligado is False:
            self.__ligado = True
            print('Ligando o eletrodoméstico...')
            print('=' * 30)
        else:
            self.__ligado = False
            print('Desligando o eletrodoméstico...')
            print('=' * 30)

    def imprimir(self):
        print('--Dados do eletrodoméstico--\n'
              f'Situação: {"Ligado" if self.__ligado==True else "Desligado"}')
        print('=' * 30)
