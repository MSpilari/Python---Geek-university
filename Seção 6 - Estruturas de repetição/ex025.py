""" Faça um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3 ou 5."""
somador = 0
for divisores in range(1, 1000):
    if divisores % 3 == 0 or divisores % 5 == 0:
        somador = somador + divisores
print(f'A soma entre os multiplos de 3 ou de 5 são é igual a {somador}')
