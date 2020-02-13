""" Faça um programa que peça ao usuário para digitar 10 valores e some-os."""
somador = 0
for numeros in range(1, 11):
    escolha = float(input(f'Informe o {numeros}º valor: '))
    somador = somador + escolha
print(f'Você digitou 10 números e a soma entre eles é {somador}')
