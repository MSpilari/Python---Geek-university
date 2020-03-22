class Quadrado:
    def __init__(self, lado, area=None, perimetro=None):
        self.__lado = lado
        self.__area = area
        self.__perimetro = perimetro

    def calcular_area(self):
        self.__area = pow(self.__lado, 2)
        print('A área foi calculada...')

    def calcular_perimetro(self):
        self.__perimetro = 4 * self.__lado
        print('O perímetro foi calculado...')

    def imprimir(self):
        if self.__area is not None and self.__perimetro is not None:
            print('==Todos os dados do Quadrado==\n'
                  f'O lado do quadrado mede {self.__lado}m\n'
                  f'A área mede {self.__area}m²\n'
                  f'O perímetro mede {self.__perimetro}m')
        else:
            print(f'Apenas o lado foi de {self.__lado}m foi informado. '
                  f'Não foram executados cálculos de área nem perímetro.')
