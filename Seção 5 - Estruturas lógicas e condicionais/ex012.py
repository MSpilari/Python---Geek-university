""" Ler um número inteiro. Se o número for negativo escreva 'número inválido'. Se o número for positivo, calcule o seu
logaritmo."""
from math import log
numero = int(input('Informe um número: '))
if numero > 0:
    logaritmo = log(numero, 10)
    print(f'O logaritmo do número {numero} na base 10 é {logaritmo:.2f}')
else:
    print(f'O número {numero} NÃO é válido, para o cálculo do logaritmo.')
