from Secao17_POO_Heranca_Polimorfismo.classes.eletrodomestico import Eletrodomestico


class Televisor(Eletrodomestico):
    def __init__(self, max_volume=10, max_canais=5, canal_atual=0, volume_atual=0, ligado=False):
        super().__init__(ligado)
        self._canal_inicial = 0  # Canal 0 é considerado um canal
        self.__numero_max_canais = max_canais
        self.__canal_atual = canal_atual
        self.__volume_atual = volume_atual
        self.__volume_min = 0
        self.__max_volume = max_volume

    def imprimir(self):
        print('--Dados do Televisor--\n'
              f'Situação: {"Ligado" if self.ligado==True else "Desligado"}\n'
              f'Canal atual: {self.__canal_atual}\n'
              f'Volume atual: {self.__volume_atual}\n'
              f'Nº max de canais: {self.__numero_max_canais}\n'
              f'Volume max: {self.__max_volume}')
        print('=' * 30)

    def aumentar_canal(self):
        if self.ligado:
            if self.__canal_atual == self.__numero_max_canais:
                self._canal_inicial = -1
            print('Aumentando o nº do canal...')
            self.__canal_atual = self._canal_inicial + 1
            self._canal_inicial = self.__canal_atual
            print('=' * 30)
        else:
            print('Não é possível mudar de canal com o Televisor Desligado.')
            print('=' * 30)

    def abaixar_canal(self):
        if self.ligado:
            if self.__canal_atual == 0:
                self._canal_inicial = self.__numero_max_canais + 1
            self.__canal_atual = self._canal_inicial - 1
            self._canal_inicial = self.__canal_atual
            print('Diminuindo o nº do canal...')
            print('=' * 30)
        else:
            print('Não é possivel mudar de canal com o Televisor Desligado.')
            print('=' * 30)

    def aumentar_volume(self):
        if self.ligado:
            if self.__volume_atual < self.__max_volume:
                self.__volume_atual = self.__volume_min + 1
                self.__volume_min = self.__volume_atual
                print('Aumentando o volume...')
                print('=' * 30)
            else:
                print('Não é possível aumentar mais o volume, pois chegamos ao valor máximo.')
                print('=' * 30)
        else:
            print('Não é possível manipular o volume com o Televisor desligado.')
            print('=' * 30)

    def abaixar_volume(self):
        if self.ligado:
            if self.__volume_atual > 0:
                self.__volume_atual = self.__volume_min - 1
                self.__volume_min = self.__volume_atual
                print('Diminuindo o volume...')
                print('=' * 30)
            else:
                print('Não é possível diminuir mais o volume, pois chegamos ao volume mínimo.')
                print('=' * 30)
        else:
            print('Não é possível manipular o volume com o Televisor desligado.')
            print('=' * 30)
