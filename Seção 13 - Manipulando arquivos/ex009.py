""" Faça uma programa que receba dois arquivos do usuário e crie um terceiro arquivo com os dois primeiros juntos
(o conteúdo do primeiro seguido do conteúdo do segundo)."""
with open('Lista de coisas.txt', 'r') as arquivo1:
    primeira_parte = arquivo1.read()
with open('Nomes de ruas.txt', 'r') as arquivo2:
    segunda_parte = arquivo2.read()
with open(input('Informe o nome do novo arquivo: ') + '.txt', 'w') as arquivo3:
    arquivo3.write(primeira_parte)
    arquivo3.write(segunda_parte)
