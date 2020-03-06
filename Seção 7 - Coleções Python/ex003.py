"""Ler um conjunto de números reais, armazenando-o em um vetor e calcular o quadrado das componentes deste vetor,
armazenando o resultado em outro vetor. Os conjuntos têm 10 elementos cada. Imprimir todos os conjuntos."""
from random import randint
conjunto = set()
while len(conjunto) != 10:
    conjunto.add(randint(1, 100))
print(f'Conjunto inicial {conjunto}')
quadrado = {valor ** 2 for valor in conjunto}  # Dictionary Comprehension
print(f'Conjunto ao quadrado {quadrado}')
