""" Faça um programa que leia três números inteiros positivos e efetue o cálculo de uma das seguintes médias de acordo
com um valor numérico digitado pelo usuário."""
print('=' * 40)
print(f'{"Calculadora de Médias":^40}')
print('=' * 40)
x = float(input('Informe o 1º valor: '))
y = float(input('Informe o 2º valor: '))
z = float(input('Informe o 3º valor: '))
print("""--> Médias Disponíveis:
1 -> Geométrica
2 -> Ponderada
3 -> Harmônica
4 -> Aritmética""")
while True:
    try:
        resposta = int(input('Qual média deseja saber ? '))
        if resposta < 1 or resposta > 4:
            print('Opção inválida. Digite um numeral entre 1 e 4. Tente novamente.')
            continue
    except:
        print('Opção inválida. Digite o numeral, não escreva por extenso. Tente novamente.')
        continue
    else:
        if resposta == 1:
            media = (x * y * z) ** (1/3)
            print(f'A média geométrica é {media:.2f}')
            break
        elif resposta == 2:
            media = ((x * 1) + (y * 2) + (z * 3)) / 6
            print(f'A média ponderada é {media:.2f}')
            break
        elif resposta == 3:
            media = 1/((1 / x) + (1 / y) + (1 / z))
            print(f'A média harmônica é {media:.2f}')
            break
        else:
            media = (x + y + z) / 3
            print(f'A média aritmética é {media:.2f}')
            break

