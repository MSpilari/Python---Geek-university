""" Faça um programa que leia o valor da hora de trabalho(em reais) e o número de horas trabalhadas no mês. Imprima o
valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado."""
valor_da_hora = float(input('Quanto custa sua hora de trabalho ? R$'))
horas_mes = float(input('Quantas horas você trabalhou neste mês ?'))
pagamento = (valor_da_hora * horas_mes) * 1.10  # Pagamento com 10% do valor adicionado.
print(f'O seu pagamento é de R${pagamento:.2f}')
