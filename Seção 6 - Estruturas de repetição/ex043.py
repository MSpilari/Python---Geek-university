""" Faça um programa que leia um número indeterminado de idades de indivíduos(pare quando for informada a idade 0),
calcule a idade média desse grupo."""
somador = contador = 0
while True:
    print('Para encerrar o programa digite 0.')
    idade = int(input('Informe sua idade: '))
    print('Idade cadastrada com sucesso !!')
    print('-' * 40)
    if idade <= 0:
        break
    else:
        somador = somador + idade
        contador = contador + 1
print(f'No total foram cadastradas {contador} pessoas e a média da idade delas é de {somador / contador:.2f} anos.')
print('Programa encerrado. Volte sempre !! ')