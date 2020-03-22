class Televisao:
    i = 0

    def __init__(self):
        self.__canais = ('HDMI', 'AV', 'Cultura', 'SBT', 'Globo', 'Record', 'Gazeta', 'Band')
        self.__canal_inicial = self.__canais[Televisao.i]
        self.__volume_min = 0
        self.__volume_max = 2

    def aumentar_volume(self):
        if self.__volume_min < self.__volume_max:
            print('Aumentando o volume em UMA unidade.')
            self.__volume_min += 1
        else:
            print('Não foi possível aumentar o volume, pois a Televisão está com seu volume máximo.')

    def diminuir_volume(self):
        if self.__volume_min > 0:
            print('Diminuindo o volume em UMA unidade.')
            self.__volume_min -= 1
        else:
            print('Não foi possível diminuir o volume, pois a Televisão está com seu volume mínimo.')

    def zapeando_canais(self):
        while True:
            print('Digite "+" para AUMENTAR o canal e "-" para DIMINUIR o canal.')
            escolha = str(input('Digite "+" ou "-" : ')).strip()
            if escolha not in ('+', '-'):
                print('Digite um caractere válido "+" ou "-".')
                continue
            elif escolha == '+':
                if Televisao.i < len(self.__canais) - 1:
                    print('Avançando um canal...')
                    Televisao.i += 1
                    self.__canal_inicial = self.__canais[Televisao.i]
                else:
                    print('Não posso avançar mais, estamos no último canal.')
                break
            else:
                if Televisao.i > 0:
                    print('Regredindo um canal...')
                    Televisao.i -= 1
                    self.__canal_inicial = self.__canais[Televisao.i]
                else:
                    print('Não posso regredir mais, estamos no primeiro canal.')
            break

    def escolhendo_canal(self, number=0):
        try:
            self.__canal_inicial = self.__canais[number]
            if 0 > number or number > len(self.__canais):
                raise ValueError
        except ValueError:
            print(f'Não tenho este número de canal. Informe um Nº INTEIRO entre 0 e {len(self.__canais) - 1}.')

    def consulta_canal(self):
        print(f'O canal atual é o {self.__canal_inicial}')

    def consulta_volume(self):
        print(f'O volume atual é {self.__volume_min}')