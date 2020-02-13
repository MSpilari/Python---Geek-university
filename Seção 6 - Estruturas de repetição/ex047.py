""" Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números:
-> Adição(opção 1) -> Subtração(opção 2) -> Multiplicação(opção 3) -> Divisão(opção 4) -> Saída(opção 5).
O programa deve possibilitar ao usuário a escolha da operação desejada a exibição do resultado e a volta do menu de
opções. O programa só termina quando for escolhida a opção de saída."""

lista = ['Adição', 'Subtração', 'Multiplicação', 'Divisão', 'Encerrar o programa']
while True:
    n1 = float(input('Informe o 1º número: '))
    n2 = float(input('Informe o 2º número: '))
    print('=' * 30)
    print(f'{"Código":<10}{"Operações":<20}')
    print('=' * 30)
    for indice, valores in enumerate(lista):
        print(f'{indice + 1:<10}{valores:<20}')
    while True:
        try:
            resposta = int(input('Qual o código da operação que deseja ? '))
        except ValueError:
            print('Escolha uma opção válida entre 1 e 5. Tente novamente.')
            continue
        else:
            break
    while resposta < 1 or resposta > 5:
        print('ERRO ! Escolha uma opção válida. Tente novamente.')
        resposta = int(input('Qual o código da operação que deseja ? '))
    if resposta == 1:
        print(f'A soma entre {n1} e {n2} é igual a {n1 + n2}')
    elif resposta == 2:
        print(f'A subtração entre {n1} e {n2} é igual a {n1 - n2}')
    elif resposta == 3:
        print(f'A multiplicação entre {n1} e {n2} é igual a {n1 * n2}')
    elif resposta == 4:
        try:
            divisao = n1 / n2
        except ZeroDivisionError:
            print('Não é possivel realizar uma divisão com o denominador valendo 0.')
        else:
            print(f'A divisão entre {n1} e {n2} é igual a {divisao}')
    else:
        print('Programa encerrado. Volte sempre !!')
        break
