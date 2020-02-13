""" Faça um programa que simula o lançamento de dados d1 e d2, n vezes e tem como saída o número de cada dado e a
relação ente ele(>, <, =) de cada lançamento."""
from random import randint
while True:
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    print(f'O Nº sorteado no 1º dado foi {dado1}. Já no 2º dado foi {dado2}')
    if dado1 > dado2:
        print(f'O Nº {dado1} (dado 1) é MAIOR que o Nº {dado2} (dado 2)')
    elif dado1 < dado2:
        print(f'O Nº {dado2} (dado 2) é MAIOR que o Nº {dado1} (dado 1)')
    else:
        print('Os valores sorteados foram iguais.')
    resposta = str(input('Deseja continuar ? [S/N] ')).strip().upper()
    while resposta != 'N' and resposta != 'S':
        resposta = str(input('Deseja continuar ? [S/N] ')).strip().upper()
    if resposta == 'N':
        print('Progrma encerrado. Volte sempre !')
        break
