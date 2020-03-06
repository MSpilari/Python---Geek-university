""" Sejam A e B os catetos de um triângulo. Faça uma função que receba os valores de A e B e calule a hipotenusa através
da equação."""


def hipotenusa(adjacente, oposto):
    """
    -> Função que recebe os catetos e calcula a hipotenusa.
    :param adjacente: Cateto fornecido pelo usuário em centimetros.
    :param oposto: Cateto fornecido pelo usuário em centimetros.
    :return: Retorna o valor da hipotenusa.
    """
    return f'O triângulo possui hipotenusa igual a {(adjacente ** 2 + oposto ** 2) ** (1 / 2)} cm.'


print(hipotenusa(float(input('Informe o valor do cateto adjacente: ')),
                 float(input('Informe o valor do cateto oposto: '))))
