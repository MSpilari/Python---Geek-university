""" Faça um programa que receba do usuário dois vetores A e B, com 10 números inteiros cada. Crie um novo vetor
denominado C calculando C = A - B. Mostre na tela os dados do vetor C."""
from random import randint
conjuntoA = set()
conjuntoB = set()
conjuntoC = set()
while len(conjuntoA) != 10:
    conjuntoA.add(randint(0, 20))
while len(conjuntoB) != 10:
    conjuntoB.add(randint(0, 20))
conjuntoC = conjuntoA.difference(conjuntoB)
print(f'O conjunto A é igual a {conjuntoA}')
print(f'O conjunto B é igual a {conjuntoB}')
print(f'O conjunto C = A - B fica igual a {conjuntoC}')
