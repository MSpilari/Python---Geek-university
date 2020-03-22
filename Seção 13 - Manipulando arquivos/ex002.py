""" Faça um programa que receba do usuário um arquivo de texto e mostre na tela quantas linhas este arquivo possui."""
with open('Texto do usuário', 'w') as arquivo:  # Criando/sobrescrevendo o documento.
    while True:
        print('Digite seu texto, para ir a outra linha digite enter para terminar digite 0(zero).')
        texto = str(input('Texto -> ')).strip()
        if texto != '0':
            arquivo.write(texto)
            arquivo.write('\n')
        else:
            break
with open('Texto do usuário.txt', 'r') as arquivo:  # Lendo o documento.
    lista = arquivo.readlines()  # Cada linha do documento vira um elemento da lista, facilitando a contagem.
    print(arquivo.read())
    print(f'O texto informado possui {len(lista)} linha(s).')
