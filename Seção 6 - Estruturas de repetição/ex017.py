""" Faça um programa que leia um número inteiro positivo N e calcule a soma dos N primeiros números naturais."""
somador = 0
while True:
    try:
        numero = int(input('Informe um número inteiro e positivo: '))
        if numero < 0:
            print('ERRO. Informe um número POSITIVO. Tente novamente.')
            continue
    except:
        print('ERRO. O número informado não é inteiro. Tente novamente.')
        continue
    else:
        for contador in range(0, numero):
            somador = somador + contador
    print('=' * 50)
    print(f'A soma dos {numero} primeiros números naturais é {somador}.')
    print('=' * 50)
    break
print('Fim do programa. Volte sempre !')
