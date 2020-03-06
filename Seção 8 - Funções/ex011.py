""" Elabore uma função que receba três notas de um aluno como parâmetros e uma letra. Se a letra for A, a função deverá
calcular a média aritmética das notas do aluno; se for P deverá calcular a média ponderada, com pesos 5, 3 e 2."""


def calculo_notas(grade1, grade2, grade3, option):
    """
    -> Função que calcula a média aritmética ou ponderada de um aluno.
    :param grade1: Nota informada pelo usuário.
    :param grade2: Nota informada pelo usuário.
    :param grade3: Nota informada pelo usuário.
    :param option: Qual tipo de média o usuário deseja fazer, aritmética ou ponderada.
    :return: Retorna a média desejada pelo usuário, ou mensagem de erro caso de opção inválida.
    """
    if option == 'A':
        return f'A média aritmética das notas é {(grade1 + grade2 + grade3) / 3}'
    elif option == 'P':
        return f'A média ponderada das notas é {((grade1 * 5) + (grade2 * 3) + (grade3 * 2)) / (5+3+2)}'
    else:
        return f'ERRO ! Informe uma opção válida.'


print(calculo_notas(int(input('Informe a 1ª nota: ')),
                    int(input('Informe a 2ª nota: ')),
                    int(input('Informe a 3ª nota: ')),
                    str(input('Qual média deseja calcular ? [A] - Aritmética / [P] - Ponderada: ')).strip().upper()
                    )
      )
