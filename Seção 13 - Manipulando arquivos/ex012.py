"""Abra um arquivo de texto, calcule e escreva o número de caracteres, o número de linhas e o número de palavras neste
arquivo. escreva também quantas vezes cada letra ocorre no arquivo(ignorando letras com acento)"""

with open('Objetos e ruas.txt', 'r', encoding='utf-8') as arquivo:
    num_palavras = arquivo.read().strip().split()
    arquivo.seek(0)
    print(f'O arquivo {arquivo.name} tem {len(num_palavras)} palavras.')  # Nº de palavras.
    num_caracteres = arquivo.read()  # Nº de caracteres.
    arquivo.seek(0)
    print(f'O número de caracteres do arquivo {arquivo.name} é igual a {len(num_caracteres)} caracteres.')
    num_linhas = arquivo.read().count('\n')
    print(f'O arquivo {arquivo.name} possui {num_linhas} linha(s).')   # Nº de linhas.
