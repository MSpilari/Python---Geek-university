""" Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. Se o número
for negativo, mostre uma mensagem dizendo que o número é inválido."""
numero = float(input('Informe um número: '))
if numero >= 0:
    raiz = numero ** (1/2)
    print(f'A raiz quadrada de {numero} é {raiz:.1f}')
else:
    print('Número inválido.')
