""" Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem
crescente."""
while True:
    numero = int(input('Digite um número par: '))
    if numero % 2 == 1:
        print('ERRO ! Este número é ímpar. Tente novamente.')
        continue
    else:
        break
for contagem in range(0, numero + 1, 2):
    print(contagem, '->' if contagem < numero else '-> FIM', end=' ')
