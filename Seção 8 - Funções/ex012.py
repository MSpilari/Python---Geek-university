""" Escreva uma função que receba um número inteiro maior do que zero e retorne a soma de todos os seus algarismos. Se o
valor não for maior do que zero, o programa terminará com a mensagem 'número inválido'."""


def somador_algarismos(number):
    """
    -> Função que soma cada algarismo de um número passado pelo usuário.
    :param number: Número informado pelo usuário.
    :return: Retorna a soma dos algarismos passados pelo usuário.
    """
    if number > 0:
        linha = str(number)
        lista = list()
        x = number
        for sequencia in range(0, len(linha)):  # Com este laço eu separo os algarismos do número informado.
            valor = x % 10
            lista.append(valor)     # Adiciono os números em uma lista para facilitar a soma.
            x = x // 10
        return f'A soma dos algarismos de {number} é igual a {sum(lista)}'
    else:
        return 'ERRO ! Informe um nº maior que zero para acessar o programa.'

print(somador_algarismos(int(input('Digite um número para saber a soma dos seus algarismos: '))))
