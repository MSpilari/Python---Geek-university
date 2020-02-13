""" Faça um programa que leia 10 números inteiros positivos, ignorando os não positivos e imprima sua média."""
somador = positivos = 0
for contador in range(1, 11):
    numeros = int(input(f'Informe o {contador}º número: '))
    if numeros >= 0:
        somador = somador + numeros
        positivos = positivos + 1
print(f'Você digitou {positivos} números positivos e a soma entre eles é {somador}')
