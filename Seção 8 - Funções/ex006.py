""" Faça uma função que receba 3 números inteiros como parâmetro, representando horas, minutos e segundos, e os converta
em segundos."""


def conversor_de_tempo(hours, minutes, seconds):
    """
    -> Função que converte horas e minutos em segundos.
    :param hours: Horas informadas pelo usuário.
    :param minutes: Minutos informados pelo usuário.
    :param seconds: Segundos informados pelo usuário.
    :return: Retorna os valores convertidos para segundos.
    """
    return f'{hours} h {minutes} mins e {seconds} segs, convertidos ficam com {(hours*3600) + (minutes*60) + seconds} segs'


print(conversor_de_tempo(int(input('Informe quantas horas deseja converter: ')),
                         int(input('Informe quantos minutos deseja converter: ')),
                         int(input('Informe quantos segundos deseja converter: '))))
