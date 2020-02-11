""" Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
-> O número digitado ao quadrado.
-> A raiz quadrada do número digitado."""
numero = float(input('Informe um número: '))
if numero >= 0:
    quadrado = pow(numero, 2)
    raiz = numero ** (1/2)
    print(f'O quadrado de {numero} é {quadrado} e sua raiz é {raiz:.1f}')
else:
    print('Número inválido.')
