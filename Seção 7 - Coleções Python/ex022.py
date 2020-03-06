""" Faça um programa que leia dois vetores de 10 posições e calcule outro vetor contendo nas posições pares os valores
do primeiro e nas posições impares os valores do segundo."""
from random import randint
lista_par = [randint(0, 100) for _ in range(1, 11)]
lista_impar = [randint(0, 100) for _ in range(1, 11)]
lista_geral = list()
n = 0
f = 1
print(f'Primeiro Vetor {lista_par}')
print(f'Segundo Vetor {lista_impar}')
for numero in lista_par:
    lista_geral.insert(n, numero)
    n += 2
for elementos in lista_impar:
    lista_geral.insert(f, elementos)
    f += 2
print(f'Lista geral {lista_geral}')
