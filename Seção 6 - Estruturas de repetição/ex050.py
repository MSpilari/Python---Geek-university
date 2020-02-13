""" Chico tem 1,50m e cresce 2cm por ano, enquanto Zé tem 1,10m e cresce 3cm por ano. Escreva um programa que calcule e
imprima quantos anos serão necessários para que Zé seja maior que Chico."""
ano = 0
altura_chico = 150
altura_ze = 110
while altura_chico >= altura_ze:
    altura_chico = altura_chico + 2
    altura_ze = altura_ze + 3
    ano = ano + 1
print(f'Com {ano} anos a idade deles será igual, então com {ano + 1} anos, a altura de Zé será maior.')
