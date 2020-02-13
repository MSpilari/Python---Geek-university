""" Leia um número positivo do usuário, então calcule e imprima a sequência de Fibonacci, até o primeiro número superior
ao número lido. Exemplo : Se o usuário informou o número 30, a sequência a ser impressa será de :
0 1 1 2 3 5 8 13 21 34.
Na matemática, a Sucessão de Fibonacci, é uma sequência de números inteiros, começando normalmente por 0 e 1, na qual,
cada termo subsequente corresponde à soma dos dois anteriores. """

a = 0
b = 1
numero = int(input('Até qual número da sequência ? '))
print(a, b, end='  ')
for sequencia in range(0, numero):
    c = a + b
    if c <= numero:
        print(c, end='  ')
        a = b
        b = c
