""" Leia uma matriz 4x4, conte e escreva quantos valores maiores que 10 ela possui."""
from random import randint
maiores10 = 0
contador = 1
matriz = [[randint(0, 20) for _ in range(1, 5)], [randint(0, 20) for _ in range(1, 5)],
          [randint(0, 20) for _ in range(1, 5)], [randint(0, 20) for _ in range(1, 5)]]  # Matriz 4 x 4.
print('Matriz 4 x 4')
for listas in matriz:
    for numeros in listas:
        print(f'{numeros:>5}', end='' '\n' if contador % 4 == 0 and contador != 0 else '')
        contador += 1
        if numeros > 10:
            maiores10 += 1
print(f'Essa matriz possui {maiores10} valores maiores que dez.')