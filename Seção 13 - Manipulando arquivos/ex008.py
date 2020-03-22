""" Faça um programa que leia o conteúdo de um arquivo e crie um arquivo com o mesmo conteúdo, mas com todas as letras
minúsculas convertidas para maiúsculas. Os nomes dos arquivos serão fornecidos via teclado pelo usuário."""

with open('Lista de coisas.txt', 'r') as arquivo1:
    base = arquivo1.read()
with open(str(input('Dê um nome para seu arquivo: ')) + '.txt', 'w') as arquivo2:
    novo_texto = base.upper()
    arquivo2.write(novo_texto)