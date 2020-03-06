""" Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui."""
from random import randint
contador = 0
lista = list()
while len(lista) != 10:
    lista.append(randint(0, 10))
print(f'Lista com todos os elementos {lista}')
for elemento in lista:
    if elemento % 2 == 0:
        contador = contador + 1
print(f'A lista possui {contador} valores pares.')
