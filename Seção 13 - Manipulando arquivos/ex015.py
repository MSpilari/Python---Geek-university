""" Faça uma programa que receba como entrada o ano corrente e o nome de dois arquivos: um de entrada outro de saída.
Cada linha do arquivo de entrada contém o nome de uma pessoa e o seu ano de nascimento. O programa deverá ler o arquivo
de entrada e gerar um arquivo de saída onde aparece o nome da pessoa seguida por uma string que representa a sua idade.
"""
from datetime import date
ano_atual = date.today().year
with open('Cadastro de pessoas.txt', 'r', encoding='utf-8') as entrada:
    lista = entrada.read().strip().split()
    for k, v in enumerate(lista):
        if k % 2 != 0:
            lista[k] = int(lista[k])
            lista[k] = ano_atual - lista[k]
            if lista[k] < 18:
                lista[k] = 'Menor de idade.'
            elif lista[k] == 18:
                lista[k] = 'Entrando na maior idade.'
            else:
                lista[k] = 'Maior de idade.'
    idades = lista
with open('Idade das pessoas.txt', 'w', encoding='utf-8') as saida:
    for k, v in enumerate(idades):
        if k % 2 == 0 and k != 0:
            saida.write('\n')
            saida.write(v)
            saida.write('  ')
        else:
            saida.write(v)
            saida.write('  ')
