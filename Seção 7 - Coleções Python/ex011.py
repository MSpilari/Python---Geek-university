""" Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a quantidade de números negativos e a
soma dos números positivos desse vetor."""
from random import randint
contador = somador = 0
lista = [randint(-100, 100) for _ in range(1, 11)]
for elemento in lista:
    if elemento < 0:
        contador += 1
    else:
        somador += elemento
print(f'A lista final é {lista}')
print(f'Ela possui {contador} elementos NEGATIVOS.')
print(f'A soma dos elementos positivos é {somador}')