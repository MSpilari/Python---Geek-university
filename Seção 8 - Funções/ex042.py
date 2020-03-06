""" Faça uma função que receba um vetor de reais e retorne a média dele."""
from random import randint
from statistics import mean
lista = [randint(0, 10) for _ in range(6)]
print(f'Vetor original {lista}')


def media_vetor(*args):
    return f'A média dos valores do vetor CALCULADA POR DEF é {sum(args) / len(args):.2f}'


print(media_vetor(*lista))

# Existe um outro modo de calcular a média do vetor usando menos linhas e importando statistics.
print(f'A média dos valores CALCULADOS POR MEAN é {mean(lista):.2f}')
