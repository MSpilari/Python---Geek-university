""" Leia um vetor com 20 números inteiros. Escreva os elementos do vetor eliminando elementos repetidos."""
from random import randint
lista = [randint(0, 50) for _ in range(1, 21)]
lista.sort()
print(f'Vetor original, ordenado, com todos elementos {lista}')
print(f'Vetor só com elementos únicos {set(lista)}')
