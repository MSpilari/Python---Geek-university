""" Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números maiores que 0."""
contador = 0
for multiplos in range(1, 100):
    if multiplos % 3 == 0:
        print(multiplos)
        contador = contador + 1
        if contador == 5:
            break
