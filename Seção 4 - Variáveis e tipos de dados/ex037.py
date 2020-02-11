""" Faça um programa que leia o valor de um produto e imprima o valor com desconto informado pelo usuário."""
produto = float(input('Informe o valor do produto: R$'))
desconto = float(input('Informe a taxa de desconto em porcentagem(%): '))
valorf = produto - (produto * (desconto/100))
print(f'O preço inicial era de R${produto:.2f} com desconto de {desconto:.1f}%, o valor passou a ser de R${valorf:.2f}')
