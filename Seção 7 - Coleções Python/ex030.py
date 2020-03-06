""" Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a intersecção entre os dois vetores
anteriores."""
from random import randint
conjuntoA = set()
conjuntoB = set()
conjuntoC = set()
while len(conjuntoA) != 10:
    conjuntoA.add(randint(0, 20))
while len(conjuntoB) != 10:
    conjuntoB.add(randint(0, 20))
conjuntoC = conjuntoA.intersection(conjuntoB)
print(f'O vetor A é o {conjuntoA}')
print(f'O vetor B é o {conjuntoB}')
print(f'A intersecção entre os conjuntos é igual a {conjuntoC}')
