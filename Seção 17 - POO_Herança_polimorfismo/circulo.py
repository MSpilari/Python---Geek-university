class Circulo:
    def __init__(self, raio, area=None, comp_circunferencia=None):
        self.__raio = raio
        self.__area = area
        self.__comp_circunferencia = comp_circunferencia

    def calcular_area(self):
        from math import pi
        self.__area = pi * pow(self.__raio, 2)
        print('Calculando a área da circunferência...')

    def calcular_comp_circunf(self):
        from math import pi
        self.__comp_circunferencia = 2 * pi * self.__raio
        print('Calculando o comprimento da circunferência...')

    def imprimir(self):
        if self.__area is not None and self.__comp_circunferencia is not None:
            print('==Dados da circunferência==\n'
                  f'O raio da circunferência é {self.__raio}m.\n'
                  f'A área da circunferência é {self.__area:.2f}m².\n'
                  f'O comprimento da circunferência é {self.__comp_circunferencia:.2f}m.')
        elif self.__area is None and self.__comp_circunferencia is not None:
            print('Ainda não calculei a área.')
        elif self.__area is not None and self.__comp_circunferencia is None:
            print('Ainda não calculei o comprimento da circunferência.')
        else:
            print('Ainda não calculei a área, nem o comprimento da circunferência.')