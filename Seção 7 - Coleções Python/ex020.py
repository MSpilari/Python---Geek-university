""" Escreva um programa que leia números inteiros no intervalo [0, 50] e os armazene num vetor com 10 posições. Preencha
um segundo vetor apenas com números ímpares do primeiro vetor. Imprima os dois vetores, 2 elementos por linha."""
from random import randint
impares = list()
i = j = 0
lista = [randint(0, 50) for _ in range(1, 11)]
for elemento in lista:
    if elemento % 2 != 0:
        impares.append(elemento)
print(f'Vetor com todo os números {lista}')
for _ in lista:  # Lista principal com os elementos impressos 2 a 2.
    while i < len(lista) - 1:
        print(lista[i], lista[i + 1])
        i += 2
print(f'Vetor somente com Ímpares {impares}')
for _ in impares:
    while j < len(impares) - 1:   # Impressão dos elementos 2 a 2, caso o vetor gerado tenha tamanho par.
        if len(impares) % 2 == 0:
            print(impares[j], impares[j + 1])
            j += 2
        else:
            while j < len(impares) - 1:  # Impressão dos elementos 2 a 2, caso o vetor gerado tenha tamanho ímpar.
                print(impares[j], impares[j + 1])
                j += 2
            print(impares[j])
