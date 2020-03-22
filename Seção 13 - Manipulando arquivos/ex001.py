""" Escreva um programa que:
a) Crie/abra um arquivo texto de nome 'arq.txt'.
b) Permite ao usuário gravar diversos caracteres nesse arquivo, até que o usuário entre com o caractere zero(0).
c) Feche o arquivo.
Agora abra e leia o arquivo, caractere por caractere, e escreva na tela todos os caracteres armazenados."""

with open('Lista de coisas.txt', 'a') as listagem:
    while True:
        obj = str(input('Informe o objeto que deseja cadastrar na lista: ')).strip().title()
        if obj != '0':
            listagem.write(obj)
            listagem.write('\n')
        else:
            break
with open('Lista de coisas.txt', 'r') as listagem:
    for coisa in listagem:
        print(coisa, end='')
print('Eu tenho uma maçã')