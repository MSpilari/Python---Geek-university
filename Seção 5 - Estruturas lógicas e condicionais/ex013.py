""" Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda provas têm peso 1 e a
terceira tem peso 2. Ao final mostrar a média do aluno e indicar se o aluno foi aprovado(>=7) ou reprovado."""
p1 = float(input('Nota 1ª prova: '))
p2 = float(input('Nota 2ª prova: '))
p3 = float(input('Nota 3ª prova: '))
media_ponderada = ((p1 * 1) + (p2 * 1) + (p3 * 2)) / 4
if media_ponderada >= 7:
    print(f'APROVADO ! Sua média foi de {media_ponderada}')
else:
    print(f'REPROVADO ! Sua média foi de {media_ponderada}')
