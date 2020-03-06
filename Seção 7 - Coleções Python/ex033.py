""" Faça um programa que leia um vetor de 15 posições e o compacte, ou seja, elimine as posições com valor zero."""
from random import randint
lista = [randint(0, 10) for _ in range(1, 16)]
print(f'Lista original {lista}')
for valor in lista:
    if valor == 0:
        lista.remove(valor)
print(f'Lista compactada(sem zeros) {lista}')
