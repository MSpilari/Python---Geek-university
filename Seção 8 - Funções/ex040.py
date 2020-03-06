""" Faça uma função que receba um vetor de inteiros e retorne quantos valores pares ele possui."""
from random import randint
lista = [randint(0, 10) for sequencia in range(11)]


def buscador_par(*args):
    """
    -> Função que busca os valores pares dentro de um iterável.
    :param args: Vetor passado pelo usuário que será analisado.
    :return: Retorna a quantidade de valores pares existentes no vetor.
    """
    contador = 0
    for valor in args:
        if valor % 2 == 0:
            contador += 1
    return f'No vetor informado existem {contador} números PARES.'


print(f'O vetor original é {lista}')
print(buscador_par(*lista))  # Utilizando uma função def criada

""" Uma outra forma que encontrei foi usando a função lambda em conjunto com o filter assim consigo separar os elementos
pares em outra lista um nº menor de linhas"""

lista_par = list(filter(lambda valor: valor % 2 == 0, lista))  # Utilizando uma função lambda com filter
print(f'Existem {len(lista_par)} valores PARES no vetor analisado.')
