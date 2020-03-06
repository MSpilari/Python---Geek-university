""" Faça uma função que receba a altura e o raio de um cilindro circular reto e retorne o volume do cilindro."""


def volume_cilindro(height, radius):
    from math import pi
    return f'O volume do cilindro é {pi * (radius ** 2) * height:.2f} m³.'


print(volume_cilindro(float(input('Informe a altura do cilindro em metros: ')),
                      float(input('Informe o raio do cilindro: '))))
