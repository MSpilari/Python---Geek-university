""" Faça um programa que leia um vetor de 8 posições, em seguida, leia também dois valores X e Y quaisquer
correspondentes a duas poisções no vetor. Ao final seu programa deverá escrever a soma dos valores encontrados nas
respectivas posições X e Y."""
from random import randint
lista = list()
while len(lista) != 8:
    lista.append(randint(0, 100))
print(f'A lista sorteada foi {lista}')
print('Vou somar dois valores dessa lista, diga para mim quais posições, entre 1 e 8, deseja.')
p1 = int(input('Informe a posição do 1º número: '))
p2 = int(input('Informe a posição do 2º número: '))
print(f'A soma entre {lista[p1 - 1]} e {lista[p2 - 1]} é igual a {lista[p1 - 1] + lista[p2 - 1]}')
