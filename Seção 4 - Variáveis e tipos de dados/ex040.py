""" Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite o número de dias trabalhados
pelo encanador e imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda.
"""
dias = int(input('Quantos dias o encanador trabalhou ? '))
pagamento = (30 * dias) * 0.92
print(f'O pagamento líquido do encanador será de R${pagamento:.2f}')
