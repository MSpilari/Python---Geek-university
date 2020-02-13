""" Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem
crescente."""
numero = int(input('Informe um número: '))
for contagem in range(0, numero + 1):
    print(contagem, '->' if contagem < numero else '-> FIM', end=' ')
