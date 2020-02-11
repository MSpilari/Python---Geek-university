""" Receba o salário base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que esse funcionário tem
uma gratificação de 5% sobre o salário base. Além disso ele paga 7% de imposto sobre o salário base."""
salario_base = float(input('Informe seu salário base: '))
salariof = (salario_base * 1.05) * 0.93
print(f'O salário final a receber já deduzidos os impostos é de {salariof}')