""" Escreva uma função para determinar a quantidade de números primos abaixo de N."""


def qtdade_primos(number):
    lista = [sequencia for sequencia in range(1, number + 1)]
    primos = list()
    contador = 0
    print(lista)
    for numerador in lista:
        for denominador in lista:
            calc = numerador / denominador
            if calc % 1 == 0:
                contador += 1
        if contador == 2:
            primos.append(numerador)
        contador = 0
    return f'Até o nº {number} existem {len(primos)} números primos.'


print(qtdade_primos(int(input('Informe um nº: '))))
