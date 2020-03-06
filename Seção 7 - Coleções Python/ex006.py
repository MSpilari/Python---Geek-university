""" Faça um programa que receba do usuário um vetor com 10 posições. Em seguida deverá ser impresso o maior e o menor
elemento do vetor."""
lista = list()
for contador in range(1, 11):
    lista.append(int(input(f'Informe o {contador}º número: ')))
lista.sort()
print(f'Os números informados foram {lista}')
print(f'O MAIOR número informado foi o {max(lista)} e o MENOR foi o {min(lista)}')
