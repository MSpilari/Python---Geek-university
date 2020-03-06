""" Faça uma função que receba como parâmetro um vetor X de 30 elementos inteiros e retorne, também por parâmetro, dois
vetores A e B. O vetor A deve conter os elementos pares de X e o B os ímpares."""
from random import randint


def analisador_elementar(*args):
    """
    -> Função que separa os elementos pares e ímpares de um vetor
    :param args: Vetor passado pelo usuário.
    :return: Retorna duas listas uma par(A) e outra ímpar(B).
    """
    vetor_a = list()
    vetor_b = list()
    for elemento in args:
        if elemento % 2 == 0:
            vetor_a.append(elemento)
        else:
            vetor_b.append(elemento)
    return f'O Vetor A(PARES) é {vetor_a}\nO Vetor B(ÍMPARES) é {vetor_b}'


vetor_original = tuple(randint(0, 100) for _ in range(31))
print(f'Vetor original {vetor_original}')
print(analisador_elementar(*vetor_original))

# Tentando obter o mesmo resultado, mas simplificando o código.
print(f'Vetor PAR CALCULADO COM FILTER {list(filter(lambda valor: valor % 2 == 0, vetor_original))}')
print(f'Vetor ÍMPAR CALCULADO COM FILTER {list(filter(lambda valor: valor % 2 != 0, vetor_original))}')