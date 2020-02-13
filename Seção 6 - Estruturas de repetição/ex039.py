""" Faça um programa que calcule a área de um triângulo, cuja a base e altura são fornecidas pelo usuário. Este programa
não pode permitir a entrada de dados inválidos, ou seja, menores ou iguais a 0."""

base = float(input('Qual a medida da base do triângulo em metros ? '))
while base <= 0:
    print('ERRO ! O valor da base tem que ser MAIOR que 0.')
    base = float(input('Qual a medida da base do triângulo em metros ? '))
altura = float(input('Qual a medida da altura do triângulo em metros ? '))
while altura <= 0:
    print('ERRO ! O valor da altura tem que ser MAIOR que 0.')
    altura = float(input('Qual a medida da altura do triângulo em metros ? '))
area = (base * altura) / 2
print(f'A área do triângulo tem medidas de {area} m²')


