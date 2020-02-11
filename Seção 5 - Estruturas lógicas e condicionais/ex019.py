""" Faça um programa para verificar se um determinado número inteiro é divisível por 3 ou por 5, mas não simultaneamente
pelos dois."""
numero = float(input('Informe um nº para saber se ele é divisível por 3 ou 5: '))
if numero % 3 == 0 and numero % 5 != 0:
    print(f'O número {numero} é divisivel por 3.')
elif numero % 5 == 0 and numero % 3 != 0:
    print(f'O número {numero} é divisível por 5.')
elif numero % 5 == 0 and numero % 3 == 0:
    print(f'O número {numero} é divisível por 3 e 5.')
else:
    print(f'O número {numero} não é divisível por 3 e por 5.')
