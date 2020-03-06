""" Crie um programa que lê 6 valores inteiros e em seguida, mostre na tela, os valores lidos."""
lista = list()
for sequencia in range(1, 7):
    lista.append(int(input(f'Informe o {sequencia}º valor: ')))
print(lista)