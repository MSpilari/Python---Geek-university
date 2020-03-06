""" Faça um programa para ler 10 números diferentes a serem armazenados em um vetor. Os dados deverão ser armazenados na
ordem que forem lidos, sendo que caso o usuario digite um valor que já foi digitado anteriormente, o programa deverá
pedir para ele digitar outro número. Exiba o vetor final na tela."""
lista = list()
while len(lista) != 10:
    numero = int(input('Informe um valor: '))
    if numero in lista:
        print('Não adicionei este número, pois ele já estava na lista. Tente novamente.')
    else:
        lista.append(numero)
print(f'O vetor final com 10 elementos é {lista}')
