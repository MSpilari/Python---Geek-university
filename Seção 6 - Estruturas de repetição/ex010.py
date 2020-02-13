""" Faça um programa que calcule e mostre a soma dos 50 primeiros números pares."""
numero = somador = contador = 0
while True:
    if numero % 2 == 0:
        somador = somador + numero
        contador = contador + 1
    numero = numero + 1
    if contador == 51:
        break
print(f'A soma dos números PARES é {somador}')
