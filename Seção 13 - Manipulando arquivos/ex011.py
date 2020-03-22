""" Faça um programa na qual o usuário informa o nome do arquivo e uma palavra, e retorne o número de vezes que a
palavra apareceu no texto."""

nome_arquivo = str(input('Informe o nome do arquivo que deseja abrir: ').strip().capitalize() + '.txt')
busca = str(input('Qual a palavra que deseja saber o número de ocorrências ? ')).strip().lower()
try:
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        ocorrencias = arquivo.read().lower().count(busca)
        print(f'A palavra "{busca}" apareceu {ocorrencias} vez(es).')
except FileNotFoundError:
    print(f'ERRO. O arquivo {nome_arquivo} não existe no seu computador.')
