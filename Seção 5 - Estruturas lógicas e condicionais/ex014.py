""" A nota de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 a 10, respectivamente, a
um trabalho de laboratório, uma avaliação semestral e um exame final. A média das três notas mencionadas anteriormente
obedece aos pesos 2, 3 e 5. De acordo com o resultado, mostre na tela se o aluno está reprovado(média entre 0 e 2.9), de
recuperação(entre 3 e 4.9) ou se foi aprovado. Faça todas a verificações necessárias."""
n1 = float(input('Nota do trabalho de laboratório: '))
n2 = float(input('Nota da avaliação semestral: '))
n3 = float(input('Nota do Exame Final: '))
media_ponderada = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10
if media_ponderada < 3:
    print(f'REPROVADO ! Sua média final foi de {media_ponderada}')
elif 3 <= media_ponderada < 5:
    print(f'RECUPERAÇÃO ! Sua média final foi de {media_ponderada}')
else:
    print(f'APROVADO ! Sua média final foi de {media_ponderada}')
