""" Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre na tela os valores lidos em ordem reversa."""
from random import randint
lista = list()
while len(lista) != 6:
    numero = randint(0, 100)
    if numero % 2 == 0:
        lista.append(numero)
print(f'A lista apenas com pares em ordem original é {lista}')
lista.reverse()
print(f'A lista de números pares em ordem reversa é {lista}')
