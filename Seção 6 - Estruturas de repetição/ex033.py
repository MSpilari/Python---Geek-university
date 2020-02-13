""" Dados N e dois números inteiros positivos, i e j, diferentes de 0, imprimir em ordem crescente os N primeiros
números naturais que são múltiplos de I ou de J e ou de ambos."""
somador = multiplos = 0


qtidade_multiplos = int(input('Quantos múltiplos você quer saber ? '))  # N
while qtidade_multiplos == 0:
    print('ERRO ! Digite um número diferente de 0.')
    qtidade_multiplos = int(input('Quantos múltiplos você quer saber ? '))


numero1 = int(input('Qual o 1º número ? '))  # I
while numero1 == 0:
    print('ERRO ! Digite um número diferente de 0.')
    numero1 = int(input('Qual o 1º número ? '))


numero2 = int(input('Qual o 2º número ? '))  # J
while numero2 == 0:
    print('ERRO ! Digite um número diferente de 0.')
    numero2 = int(input('Qual o 2º número ? '))

print(f'Os múltiplos de {numero1}; {numero2} e de ambos são:', end=' ')
while qtidade_multiplos > multiplos:
    if somador % numero1 == 0 or somador % numero2 == 0:
        multiplos = multiplos + 1
        print(somador, ',' if qtidade_multiplos > multiplos else '', end=' ')
        somador = somador + 1
    else:
        somador = somador + 1
