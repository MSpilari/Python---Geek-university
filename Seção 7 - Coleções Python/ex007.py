""" Escreva um programa que leia 10 números inteiros e os armazene em um vetor. Imprima o vetor, o maior elemento e a
posição que ele se encontra."""
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f'O MAIOR elemento do vetor é o {max(tupla)} e ele está na {tupla.index(max(tupla)) + 1}ª posição.')
