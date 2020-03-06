""" Faça uma função para verificar se um número é um quadrado perfeito. Um quadrado perfeito é um número inteiro, não
negativo que pode ser expresso como quadrado de um número inteiro."""


def quadrado_perfeito(number):
    """
    -> Informa se um n° é um quadrado perfeito ou não.
    :param number: Número informado pelo usuário.
    :return: Retorna uma mesnagem informando se o valor é ou não quadrado perfeito.
    """
    from math import sqrt
    if number > 0 and sqrt(number) % 1 == 0:
        return f'O {number} é um quadrado perfeito.'
    return f'O {number} não é um quadrado perfeito.'


print(quadrado_perfeito(int(input('Informe um n° para saber se ele é ou não um quadrado perfeito: '))))
