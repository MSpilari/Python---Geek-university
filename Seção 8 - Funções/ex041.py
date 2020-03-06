""" Faça uma função que receba um vetor de inteiros e retorne o maior valor."""
from random import randint
lista = [randint(0, 100) for _ in range(10)]


def maior_valor(*args):
    """
    -> Função que recebe um vetor e informa qual é o maior valor deste.
    :param args: Vetor informado pelo usuário.
    :return: Retorna o maior valor encontrado no vetor.
    """
    print(f'A lista sorteada foi {lista}')
    return f'O maior valor da lista é o {max(args)}'


print(maior_valor(*lista))
