""" Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima na saída cada um dos algarismos que compõe
o número."""
while True:
    try:
        numero = int(input('Informe um número inteiro entre 100 e 999: '))
        if numero < 100 or numero > 999:
            print('ERRO ! Informe um número entre 100 e 999. Tente novamente.')
            continue
    except:
        print('ERRO ! Informe um número INTEIRO. Tente novamente.')
        continue
    else:
        novo_numero = str(numero)
        print(f'Os algarismos do número {novo_numero} são:')
        for algarismo in novo_numero:
            print(algarismo, end=' ')
        break
print('\nPrograma encerrado. Volte sempre !!')
