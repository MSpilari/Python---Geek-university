""" Crie uma função que receba como parâmetro um número inteiro e devolva o seu dobro."""


def dobro(number):
    """
    ->Função que calcula o dobro de um número.
    :param number: Número informado pelo usuário.
    :return: Retorna uma mensagem com o number e o dobro.
    """
    return f'O dobro de {number} é {number * 2}'


print('Informe um número para saber o dobro dele.')
print(dobro(int(input('N° '))))
