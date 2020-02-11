""" Leia o salário de um funcionário. Calule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de
25%"""
salario = float(input('Qual o valor do seu salário ?'))
novo_salario = salario * 1.25
print(f'O seu salário era de R${salario:.2f} com o aumento de 25% passou para R${novo_salario:.2f}')
