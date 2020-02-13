""" Faça um programa que converta a velocidade em km/h para m/s e vice versa. Você deve criar um menu com as duas opções
de conversão e com uma opção para finalizar o programa. O usuário poderá fazer quantas conversões desejar, sendo que o
programa só será finalizado quando a opção de finalizar for escolhida."""
lista = ['De Km/h para M/s', 'De M/s para Km/h']
while True:
    print('=' * 40)
    print(f'{"CONVERSOR DE VELOCIDADES":^40}')
    print('=' * 40)
    print(f'{"Código":<10}{"Velocidade":<20}')
    for indice, tipo in enumerate(lista):
        print(f'{indice + 1:<10} {tipo:<20}')
    print('=' * 40)
    resposta = int(input('Qual conversão deseja realizar ? '))
    while resposta != 1 and resposta != 2:
        print('Opção inválida. Digite 1 ou 2. Tente novamente.')
        resposta = int(input('Qual conversão deseja realizar ? '))
    if resposta == 1:
        vkm = float(input('Qual a velocidade em Km/h ? '))
        vfinal = vkm / 3.6
        print(f'A velocidade de {vkm}Km/h é igual a {vfinal}M/s')
    elif resposta == 2:
        vms = float(input('Qual a velocidade em M/s ? '))
        vfinal = vms * 3.6
        print(f'A velocidade de {vms}M/s é igual a {vfinal}Km/h')
    continua = str(input('Deseja continuar ? [S/N] ')).strip().upper()
    while continua != 'S' and continua != 'N':
        print('Opção inválida. Digite S ou N. Tente novamente.')
        continua = str(input('Deseja continuar ? [S/N] ')).strip().upper()
    if continua == 'N':
        print('Programa encerrado. Volte sempre !!')
        break
