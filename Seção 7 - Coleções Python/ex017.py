""" Leia um vetor de 10 posições e atribua valor 0 para todos os elementos que possuírem valores negativos."""
from random import randint
lista = [randint(-100, 100) for _ in range(1, 11)]
print(f'Lista original {lista}')
for chave, valor in enumerate(lista):
    if valor < 0:
        lista[chave] = 0
        chave += 1
print(f'Lista somente com números positivos é {lista}')
