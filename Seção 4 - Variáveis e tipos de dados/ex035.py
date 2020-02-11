""" Sejam A e B os catetos de um triângulo. Faça um programa que receba os valores de a e b e calcule o valor da
hipotenusa através de sua equação."""
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor da cateto adjacente: '))
""" Este exercício pode ser feito de duas formas:
--> Matematicamente:
    hip = ((co ** 2) + (ca ** 2)) ** (1/2)
--> Utilizando um módulo:
    import math
    math.hypot(co, ca)
"""
hip = ((co ** 2) + (ca ** 2)) ** (1/2)
print(f'Um triângulo com os catetos {co} e {ca} tem hipotenusa igual a {hip:.2f}')
