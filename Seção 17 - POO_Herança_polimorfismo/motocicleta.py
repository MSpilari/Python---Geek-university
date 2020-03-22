class Moto:
    def __init__(self, marca, modelo, cor, marcha=0, ligada=False):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__ligada = ligada
        self._marcha_inicial = marcha
        self.__marchas = {0: 'Neutro', 1: 'Primeira', 2: 'Segunda', 3: 'Terceira', 4: 'Quarta', 5: 'Quinta'}
        self.__marcha_atual = self.__marchas[marcha]

    def ligar_desligar(self):
        if self.__ligada is False:
            self.__ligada = True
            print('Ligando a moto...')
            print('=' * 23)
        else:
            self.__ligada = False
            print('Desligando a moto...')
            print('=' * 23)

    def imprimir(self):
        print('==Informações da Moto==\n'
              f'Motor: {"Ligado" if self.__ligada == True else "Desligado"}\n'
              f'Marca: {self.__marca}\n'
              f'Modelo: {self.__modelo}\n'
              f'Cor: {self.__cor}\n'
              f'Marcha atual: {self.__marcha_atual}')
        print('=' * 23)

    def marcha_acima(self):
        if self.__ligada:
            if self._marcha_inicial < 5:
                self._marcha_inicial += 1
                self.__marcha_atual = self.__marchas[self._marcha_inicial]
                print('Aumentando a marcha...')
                print('=' * 23)
            else:
                print('Não posso aumentar mais a marcha ! Cheguei até a marcha final.')
                print('=' * 23)
        else:
            print('Ligue a moto para aumentar a marcha.')
            print('=' * 23)

    def marcha_abaixo(self):
        if self.__ligada:
            if self._marcha_inicial > 0:
                self._marcha_inicial -= 1
                self.__marcha_atual = self.__marchas[self._marcha_inicial]
                print('Diminuindo a marcha...')
                print('=' * 23)
            else:
                print('Não posso abaixar mais a marcha ! Cheguei até a marcha inicial.')
                print('=' * 23)
        else:
            print('Ligue a moto para diminuir a marcha.')
            print('=' * 23)
