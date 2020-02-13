""" Faça um programa que receba um número inteiro maior do que 1, e verifique se o número fornecido é primo ou não."""
contador = 0
numero = int(input('Digite um número para saber se ele é primo ou não: '))
for sequencia in range(1, numero + 1):
    if numero % sequencia == 0:
        print(f'\033[1;31m{sequencia}\033[m', end='  ')
        contador = contador + 1
    else:
        print(f'\033[1;34m{sequencia}\033[m', end='  ')
print(f'\nOs números em \033[1;31mVERMELHO\033[m são os divisores de {numero}; já em \033[1;34mAZUL\033[m são os não divisores')
if contador > 2:
    print(f'O número {numero} não é primo.')
else:
    print(f'O número {numero} É PRIMO.')
