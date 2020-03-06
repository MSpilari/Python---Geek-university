""" Faça uma função que receba a data atual (dia, mês e ano em inteiro) e exiba na tela no formato textual por extenso.
Exemplo 01/01/2010 -> 01 de Janeiro de 2010."""
from datetime import date


def data_atual(day, month, year):
    """
    -> Função que recebe a data em inteiros e a retorna  por extenso.
    :param day: Dia atual em inteiro.
    :param month: Mês atual em inteiro.
    :param year: Ano atual em inteiro.
    :return: Retorna a data atual por extenso.
    """
    meses_do_ano = ('Janeiro', 'Fevereiro', 'Março', 'Abril', ' Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
                    'Outubro', 'Novembro', 'Dezembro')
    return f'{day} de {meses_do_ano[month - 1]} de {year}'


print(data_atual(date.today().day, date.today().month, date.today().year))
