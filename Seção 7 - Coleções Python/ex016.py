""" Faça um programa que leia um vetor de 5 posições para números reais e , depois um código inteiro. Se o código for 0,
finalize o programa, se for 1, mostre o vetor na ordem direta, se for 2 mostre o vetor na ordem inversa. Caso o código
for diferente de 1 ou 2 escreva uma mensagem informando código inválido."""
from random import randint
lista = [randint(0, 100) for _ in range(1, 6)]
tupla = ('Finalize o programa', 'Vetor na ordem direta', 'Vetor na ordem inversa')
while True:
    print(f'{"Código":^10}{"Operação":^20}')
    for k, v in enumerate(tupla):
        print(f'{k:^10}{v:^20}')
    resposta = int(input('Qual o código da operação que deseja ? '))
    if resposta == 0:
        print('Programa encerrado. Volte sempre !')
        break
    elif resposta == 1:
        print(f'Vetor na ordem direta {lista}')
    elif resposta == 2:
        lista.reverse()
        print(f'Vetor na ordem inversa {lista}')
        lista.reverse()
    else:
        print('Código inválido. Tente novamente.')
