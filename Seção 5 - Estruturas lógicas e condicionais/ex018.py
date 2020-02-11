""" Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas. O usuário escolhe uma das
opções e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultado e saindo."""
while True:
    n1 = float(input('Informe o 1º número: '))
    n2 = float(input('Informe o 2º número: '))
    print(""" Escolha qual operação deseja realizar :
              1 -> Somar
              2 -> Subtrair
              3 -> Multiplicar
              4 -> Dividir
              5 -> Encerrar o programa.""")
    escolha = int(input('Qual operção deseja ? '))
    if escolha == 5:
        print('Programa encerrado. Volte sempre !!')
        break
    elif escolha == 1:
        print(f'A soma entre {n1} + {n2} = {n1 + n2}')
    elif escolha == 2:
        print(f'A subtração entre {n1} - {n2} = {n1 - n2}')
    elif escolha == 3:
        print(f'A multiplicação entre {n1} x {n2} = {n1 * n2}')
    elif escolha == 4:
        print(f'A divisão entre {n1} / {n2} = {n1 / n2}')
    else:
        print('Opção inválida. Tente novamente.')
