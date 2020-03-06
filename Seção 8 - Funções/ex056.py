""" Faça uma função que recebe, por parâmetro, uma matriz 7x6 e uma linha N e retorne a soma dos elementos dessa linha.
"""
from random import randint


def elementos_matriz_linha(line, *args):
    """
    -> Função que calcula a soma dos elementos da linha informada pelo usuário.
    :param line: Número da linha que o usuário deseja somar.
    :param args: Matriz informada pelo usuário.
    :return: Retorna a soma dos elementos da linha, caso seja compatível com o nº de linhas. Do contário, retorna erro.
    """
    for listas in args:
        for valor in listas:
            print(f'{valor:^5}', end='')
        print()
    if line <= 7:
        soma = sum(args[line - 1])
        return f'A soma dos elementos da linha {line} é igual a {soma}'
    else:
        return f'ERRO ! Informe uma linha entre 1 e 7.'


matriz = [[randint(0, 10)for _ in range(6)], [randint(0, 10)for _ in range(6)], [randint(0, 10)for _ in range(6)],
          [randint(0, 10)for _ in range(6)], [randint(0, 10)for _ in range(6)], [randint(0, 10)for _ in range(6)],
          [randint(0, 10)for _ in range(6)]
          ]  # Matriz 7x6
nlinha = int(input('Qual a linha que deseja somar seus valores ? '))
print(elementos_matriz_linha(nlinha, *matriz))
