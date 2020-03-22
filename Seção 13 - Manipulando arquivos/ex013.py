""" Faça um programa que permita que o usuário entre com diversos nomes e telefone para cadastro e crie um arquivo com
essas informações uma por linha. O usuário finaliza a entrada com '0' para telefone."""
while True:
    with open('Cadastro de clientes.txt', 'a', encoding='utf-8') as cadastro:
        nome = input('Nome: ').strip().capitalize()
        telefone = input('Telefone(0 - Encerra o programa): ').strip()
        if telefone != '0':
            cadastro.write(nome)
            cadastro.write('  ')
            cadastro.write(telefone)
            cadastro.write('\n')
        else:
            break
