""" Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma de todos os seus
algarismos. Por exemplo o número 251 corresponderá ao valor 8(2+5+1). Se o número lido não for maior do que zero, o
programa terminará com a mensagem número inválido."""
numero = int(input('Informe um número inteiro: '))
if numero > 0:
    linha = str(numero)  # Passando int para string
    lista = []
    for algarismo in linha:
        novo = int(algarismo)  # Passando string para int, para conseguir efetuar a soma.
        lista.append(novo)
    print(f'O número digitado foi {numero} e a soma dos seus algarismo é igual a {sum(lista)}')
else:
    print('Número inválido.')
