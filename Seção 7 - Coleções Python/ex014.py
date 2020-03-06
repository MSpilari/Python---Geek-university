""" Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais e os escreva na tela."""
from random import randint
lista = list()
repetidos = list()
for _ in range(1, 11):
    numero = randint(0, 15)
    if numero in lista and numero not in repetidos:
        lista.append(numero)
        repetidos.append(numero)
    else:
        lista.append(numero)
print(f'Lista original {lista}')
print(f'Lista com os repetidos {repetidos}')
