""" Faça uma função e um programa de teste para o cálculo do volume de uma esfera. Sendo que o raio é passado por
parâmetro."""


def volume_esfera(radius):
    """
    -> Função que calcula o volume de uma esfera.
    :param radius: Raio da esfera, em metros, que se deseja calcular o volume.
    :return: Retorna o volume da esfera.
    """
    from math import pi
    return f'O volume da esfera é {(4 * pi * (radius ** 3) / 3):.2f} m³.'  # Fórmula do volume da esfera.


print(volume_esfera(int(input('Informe o raio da esfera em metros: '))))
