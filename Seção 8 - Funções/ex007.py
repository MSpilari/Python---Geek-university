""" Faça uma função que receba uma temperatura em °C e a retorne convertida em F."""


def conversor_temperatura(celsius):
    """
    -> Conversor de temperatura de Celsius para Fahrenheit.
    :param celsius: Temperatura em Celsius passada pelo usuário.
    :return: Retorna a temperatura convertida para Fahrenheit.
    """
    return f'A temperatura {celsius} °C em Fahrenheit é igual a {(celsius * (9 / 5)) + 32} F.'


print(conversor_temperatura(float(input('Informe a temperatura em °C:'))))
