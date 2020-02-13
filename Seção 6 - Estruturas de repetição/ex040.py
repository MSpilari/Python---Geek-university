""" Elabore um programa que faça a leitura  de vários números inteiros, até que se digite um número negativo. O programa
tem que retornar o maior e o menor valor lido."""
contador = maior = menor = 0
while True:
    print('Números negativos encerram o programa.')
    numero = int(input('Informe um número: '))
    if numero < 0:
        break
    elif contador == 0:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    contador = contador + 1
print(f'O maior valor informado foi {maior} e o menor valor informado foi {menor}')
