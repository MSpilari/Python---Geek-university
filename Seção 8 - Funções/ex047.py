""" Faça uma função que receba uma matriz 4x4 e retorne quantos valores maiores que 10 ela possui."""
from random import randint


def maiores10(*args):
    """
    -> Função que calula quantos elementos maiores que 10 existem dentro de uma matriz.
    :param args: Matriz passa pelo usuário
    :return: Retorna a quantidade de valores maiores do que 10.
    """
    contador = 0
    for listas in args:
        for valores in listas:
            if valores > 10:
                contador += 1
    return f'Existem {contador} números maiores que DEZ na matriz.'


matriz = [[randint(0, 20)for _ in range(4)], [randint(0, 20)for _ in range(4)],
          [randint(0, 20)for _ in range(4)], [randint(0, 20)for _ in range(4)]]  # Matriz 4x4
for listas in matriz:  # Mostrando a matriz de maneira organizada.
    for valores in listas:
        print(f'{valores:^5}', end='')
    print()
print(maiores10(*matriz))
