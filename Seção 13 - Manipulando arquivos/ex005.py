""" Faça um programa que receba um arquivo de texto e um caractere. Mostre na tela quantas vezes aquele caractere ocorre
dentro do arquivo."""
with open('Notas alunos.txt', 'r') as arquivo:
    caractere = str(input('Digite um caractere para saber quantas vezes ele aparece no arquivo: ')).lower()
    texto = arquivo.read()
    minusculo = texto.lower()  # Passei o texto todo para minúsculo para não haver diferenciação de letras.
print(f'O caractere "{caractere}" apareceu {minusculo.count(caractere)} vezes')
