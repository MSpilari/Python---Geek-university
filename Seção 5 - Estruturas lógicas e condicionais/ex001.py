""" Faça um programa que receba dois números e mostre qual deles é o maior."""
n1 = float(input('Informe o 1º número: '))
n2 = float(input('Informe o 2º número: '))
if n1 > n2:
    print(f'O número {n1} é MAIOR que o {n2}.')
elif n1 == n2:
    print('Os números são iguais.')
else:
    print(f'O número {n2} é MAIOR que o {n1}.')
