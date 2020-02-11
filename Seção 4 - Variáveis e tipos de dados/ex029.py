""" Leia quatro notas, calcule a média aritmética e imprima o resultado."""
somador = contador = 0
for sequencia in range(1, 5):
    numero = float(input(f'Informe o {sequencia}º número: '))
    somador = somador + numero
    contador = contador + 1
print(f'A média aritmética dos {contador} números é {somador/contador}')
