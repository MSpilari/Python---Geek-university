"""Faça um programa para ler as dimensões de um terreno(comprimento c e largura l), bem como o preço do metro de tela p.
Imprima o custo para cercar este mesmo terreno com tela."""
compr = float(input('Qual o comprimento do terreno, em metros ? '))
larg = float(input('Qual a largura do terreno, em metros ? '))
preco = float(input('Qual o preço do metro da tela ? R$'))
custo_total = ((compr * preco) + (larg * preco)) * 2
print(f'O custo total para cercar o terreno será de R${custo_total:.2f}')
