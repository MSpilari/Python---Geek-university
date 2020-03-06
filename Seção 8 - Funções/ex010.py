""" Faça uma função que receba dois números e retorne qual deles é o maior."""
from random import randint


def maior_menor(first, second):
    print(f'Primeiro número {first}, segundo número {second}')
    return f'O maior número é o {max(first, second)}'


print(maior_menor(randint(0, 10), randint(0, 10)))
