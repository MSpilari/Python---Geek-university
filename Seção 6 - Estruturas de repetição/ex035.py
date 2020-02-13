""" Faça um programa que some os números ímpares contidos em um intervalo definido pelo usuário. O usuário define o
valor inicial e final do intervalo e o programa deve somar todos os números ímpares contidos neste intervalo. Caso o
usuário digite um intervalo inválido(começando por um valor maior que o valor final) deve ser escrito uma mensagem de
erro na tela, 'INTERVALO DE VALORES INVÁLIDO' e o programa termina. """
somador = 0

inicio = int(input('Informe o início do intervalo: '))
fim = int(input('Informe o fim do intevalo: '))
if inicio < fim:
    for valores in range(inicio, fim + 1):
        if valores % 2 == 1:
            somador = somador + valores
    print(f'A soma dos valores ímpares no intervalo de {inicio} até {fim} é igual a {somador}')
    print('Programa encerrado. Volte sempre.')
else:
    print('INTERVALO DE VALORES INVÁLIDO. Programa encerrado.')
