""" Um funcionário recebe aumento anual. Em 1995 foi contratado por 2000 reais. Em 1996 recebeu aumento de 1.5%. A
partir de 1997, os aumentos sempre correspondem ao dobro do ano anterior. Faça o programa e determine o salário atual do
funcionário."""

salario_inicial = 2000
aumento_inicial = 0.015
print("""Comecei a trabalhar em 1995, ganhando R$2000.00; 
Em 1996 recebi um aumento de 1.5% e depois disso a taxa de aumento dobrava com o passar do anos.""")
ano = int(input('Informe o ano para saber meu salário: '))

for anos in range(0, ano - 1995):
    salario_inicial = salario_inicial + salario_inicial * aumento_inicial
    aumento_inicial = aumento_inicial * 2
print(f'O meu salário em no ano de {ano} era de R${salario_inicial:.2f}')
