""" Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado, uma sequência arbitrária de
notas(válidas no intervalo de 10 a 20) e que mostre na tela, como resultado, a correspondente média aritmética. O número
de notas que o aluno pretende efetuar o cálculo não será fornecido ao programa, o qual terminará quando for introduzido
um valor que não seja válido como nota de aprovação."""
somador = contador = 0
print('=' * 40)
print(f'{"CALCULADORA DE MÉDIAS":^40}')
print('=' * 40)
while True:
    print('Para encerrar o programa informe uma nota \033[1;33mMENOR que 10\033[m ou \033[1;31mMAIOR que 20\033[m')
    nota = float(input('Informe a sua nota: '))
    if nota < 10 or nota > 20:
        break
    else:
        somador = somador + nota
        contador = contador + 1
try:   # Coloquei esse tratamento de erro, caso o usuário digite a 1ª nota como flag, assim não dará erro no programa.
    media = somador / contador
except ZeroDivisionError:
    media = somador / 1
print('=' * 60)
print(f'Com a(s) \033[1;34m{contador}\033[m nota(s) que você me informou, sua média é de \033[1;34m{media:.2f}\033[m')
print('=' * 60)
print('Programa encerrado. Volte sempre.')
