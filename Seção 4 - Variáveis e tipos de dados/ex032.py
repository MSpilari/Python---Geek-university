""" Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro."""
numero = int(input('Digite um número inteiro: '))
sucessor = (numero * 3) + 1  # Sucessor do seu triplo.
antecessor = (numero * 2) - 1 # Antecessor do seu dobro.
resp = sucessor + antecessor
print(f'A soma final é igual a {resp}')
