""" Faça um programa que receba do usuário um arquivo de texto e mostre na tela quantas letras são vogais e quantas são
consoantes."""
vogais = consoantes = 0
with open('Notas alunos.txt', 'w') as arquivo:
    arquivo.write(str(input('Qual seu nome ? ')).strip().title())
    arquivo.write('\n')
    arquivo.write(str(input('Em que cidade você nasceu ? ')).strip().title())
    arquivo.write('\n')
with open('Notas alunos.txt', 'r') as arquivo:
    texto = arquivo.read()
    for caractere in texto:
        if caractere in 'AÁÀáàaEÉeéIÍíiOÓoóUÚuú':
            vogais += 1
        elif caractere != ' ' and caractere != '\n':
            consoantes += 1
print(f'O arquivo possui {vogais} vogais e {consoantes} consoantes.')
