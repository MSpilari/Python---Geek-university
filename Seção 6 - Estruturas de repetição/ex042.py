""" Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e escreva para cada valor, o
quadrado, cubo e a raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero."""
from math import sqrt
while True:
    print('Números negativos ou zero encerram o programa.')
    numero = int(input('Informe um número: '))
    print('=' * 40)
    if numero <= 0:
        print('Programa encerrado. Volte sempre.')
        break
    else:
        print(f'O quadadro de {numero} é igual a {pow(numero, 2)}')
        print('-' * 40)
        print(f'O cubo de {numero} é igual a {pow(numero, 3)}')
        print('-' * 40)
        print(f'A raiz quadrada de {numero} é igual a {sqrt(numero):.2f}')
        print('=' * 40)
