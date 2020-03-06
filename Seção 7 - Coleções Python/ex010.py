""" Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule e imprima a média geral."""
from random import randint
medias = [randint(0, 10) for notas in range(1, 16)]  # Colocando os valores na lista.
print(f'Lista com as notas dos alunos {medias}')
print(f'A média geral é igual a {sum(medias) / len(medias) :.1f}')
