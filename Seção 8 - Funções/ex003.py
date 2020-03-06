""" Faça uma função para verificar se um número inteiro é positivo ou negativo. Sendo que o valor do retorno será 1, se
positivo, -1 se negativo e 0 se for zero."""
from random import randint


def positivo_negativo(number):
    """
    -> Função que informa se o número sorteado é positivo ou negativo.
    :param number: Número sorteado / informado pelo usuário.
    :return: Retorna uma mensagem informando se o valor é positivo, negativo ou zero.
    """
    if number > 0:
        return f' {number} - Número positivo'
    elif number < 0:
        return f'{number} - Número negativo'
    else:
        return f'{number} - Número igual a zero'


print(positivo_negativo(randint(-100, 100)))
