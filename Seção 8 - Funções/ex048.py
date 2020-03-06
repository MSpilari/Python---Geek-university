""" Faça uma função que receba uma matriz de 3x3 elementos. Calcule a soma dos elementos que estão acima da diagonal
principal."""
from random import randint


def acima_principal(*args):
    """
    -> Função que soma os valores localizados acima da diagonal principal.
    :param args: Matriz fornecida pelo usuário.
    :return: Retorna a soma dos valores localizados acima da diagonal principal.
    """
    i = j = somador = 0
    for listas in args:
        for _ in listas:
            if i < j:
                num = args[i][j]
                somador += num
            j += 1
        i += 1
        j = 0
    return f'A soma dos valores que estão ACIMA da diagonal principal é {somador}'


matriz = [[randint(0, 10) for _ in range(3)], [randint(0, 10) for _ in range(3)], [randint(0, 10) for _ in range(3)]]
for linhas in matriz:    # Impressão da matriz de forma organizada.
    for valores in linhas:
        print(f'{valores:^5}', end='')
    print()
print(acima_principal(*matriz))