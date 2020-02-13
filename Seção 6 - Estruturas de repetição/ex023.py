""" Faça um algoritmo que leia um número positivo e imprima seus divisores."""
while True:
    try:
        numero = int(input('Informe um número positivo para saber seus divisores: '))
        if numero < 0:
            print('ERRO ! Informe um número POSITIVO. Tente novamente.')
            continue
    except ValueError:
        print('ERRO! Informe um número INTEIRO, não escreva por extenso ou com ponto flutuante.')
        continue
    else:
        print(f'Os divisores do número {numero} são: ')
        for divisor in range(1, numero + 1):
            if numero % divisor == 0:
                print(divisor, '->' if divisor < numero else 'FIM', end=' ')
        break
