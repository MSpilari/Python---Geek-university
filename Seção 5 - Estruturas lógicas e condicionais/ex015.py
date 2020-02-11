""" Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este
número. Isto é, domingo se 1, segunda feira se 2, e assim por diante."""
dias_da_semana = ('Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado')
numero = int(input('Digite um nº entre 1 e 7, para saber o dia da semana correspondete: '))
if 1 <= numero <= 7:
    print(f'O nº {numero} corresponde ao dia da semana {dias_da_semana[numero - 1]}')
else:
    print(f'O número {numero} não é válido.')
