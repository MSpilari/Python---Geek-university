""" Faça um programa que receba do usuário um arquivo de texto e mostre na tela quantas vezes cada letra do alfabeto
aparece dentro do arquivo."""
alfabeto = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z')
with open('Notas alunos.txt', 'r') as arquivo:
    contador = 0
    texto = arquivo.read()
    minusculo = texto.lower()
    for letra in alfabeto:  # Para cada letra em no alfabeto vou fazer a verificação de vezes que a mesma aparece.
        print(f'A letra "{letra}" aparece', end=' ')
        for algarismo in minusculo:  # Verificando quantas vezes a letra aparece no texto
            if letra == algarismo:
                contador += 1
        print(f'{contador} vez(es) no texto.')
        contador = 0
