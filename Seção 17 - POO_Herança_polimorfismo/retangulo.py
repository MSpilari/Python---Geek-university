class Retangulo:
    def __init__(self, comprimento, largura, area=None, perimetro=None):
        self.__comprimento = comprimento
        self.__largura = largura
        self.__area = area
        self.__perimetro = perimetro

    def calcular_area(self):
        self.__area = self.__comprimento * self.__largura
        print('A Área foi calculada...')

    def calcular_perimetro(self):
        self.__perimetro = ((self.__largura * 2) + (self.__comprimento * 2))
        print('O perímetro foi calculado...')

    def imprimir(self):
        if self.__area is not None and self.__perimetro is not None:
            print('==Dados do Retângulo==\n'
                  f'O comprimento é {self.__comprimento}m.\n'
                  f'A largura é {self.__largura}m.\n'
                  f'A área é {self.__area}m².\n'
                  f'O perímetro é {self.__perimetro}m.')
        elif self.__area is None and self.__perimetro is not None:
            print('Ainda não calculei a área...')
        elif self.__area is not None and self.__perimetro is None:
            print('Ainda não calculei o perímetro...')
        else:
            print(f'Só recebi comprimento {self.__comprimento}m e largura {self.__largura}m\n'
                  f'Não foi efetuado o calculo da área nem do perímetro.')
