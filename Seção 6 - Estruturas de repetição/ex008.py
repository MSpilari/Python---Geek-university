""" Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido."""
maior = menor = 0
for contagem in range(1, 11):
    numero = int(input(f'Informe o {contagem}º valor: '))
    if contagem == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
print(f'Entre os números informados, o maior é {maior} e o menor é {menor}.')
