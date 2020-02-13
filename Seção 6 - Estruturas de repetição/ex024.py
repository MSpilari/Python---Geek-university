""" Escreva um programa que leia um número inteiro e calule a soma de todos os divisores desse número com exceção dele
mesmo."""
somador = 0
numero = int(input('Informe um nº para saber a soma de seus divisores: '))
print(f'Os divisores do Nº \033[1;36m{numero}\033[m são', end=' ')
for divisores in range(1, numero):
    if numero % divisores == 0:
        print(f'\033[1;32m{divisores}\033[m', end='   ')
        somador = somador + divisores
print(f'\nA soma dos divisores é igual a \033[1;33m{somador}\033[m')