""" Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem
decrescente."""
numero = int(input('Informe um número: '))
for contagem in range(numero, -1, -1):
    print(contagem, '->' if contagem > 0 else '-> FIM', end=' ')
