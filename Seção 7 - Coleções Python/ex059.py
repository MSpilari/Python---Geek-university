""" Faça um programa que leia uma matriz de 5 linhas e 4 colunas contendo as seguintes informações sobre alunos de uma
disciplina, sendo todas as informações do tipo inteiro:
-> Primeira coluna: número da matrícula.
-> Segunda coluna: média das provas.
-> Terceira coluna: média dos trabalhos.
-> Quarta coluna: nota final.
Elabore um programa que:
a) Leia as três primeiras informações de cada aluno.
b) Calcule a nota final como sendo a soma da média das provas e da média dos trabalhos.
c) Imprima a matrícula do aluno que obteve a maior nota final.
d) Imprima a média aritmética das notas finais."""
escola = []
aluno = []
maior_nota = matr_maior = m_notas_finais = 0
cabecalho = ('Nº da matrícula', 'Média das provas', 'Média dos trabalhos', 'Notas finais')
for alunos in range(1, 6):
    matricula = int(input('Nº da matrícula: '))
    media_provas = float(input('Média das provas: '))
    media_trabalhos = float(input('Média dos trabalhos: '))
    nota_final = (media_provas + media_trabalhos) / 2
    m_notas_finais += nota_final
    aluno.extend([matricula, media_provas, media_trabalhos, nota_final])
    if alunos == 1:
        maior_nota = nota_final
        matr_maior = matricula
    else:
        if maior_nota < nota_final:
            maior_nota = nota_final
            matr_maior = matricula
    escola.append(aluno.copy())
    aluno.clear()
print('=' * 100)
print(f'{"BOLETIM":^100}')
print('=' * 100)
[print(f'{item:^25}', end='') for item in cabecalho]
print()
for listas in escola:
    for valores in listas:
        print(f'{valores:^25}', end='')
    print()
print('=' * 100)