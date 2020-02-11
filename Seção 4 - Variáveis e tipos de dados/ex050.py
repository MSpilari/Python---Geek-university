""" Implemente um programa que calcule o ano de nascimento de uma pessoa a partir da sua idade e do ano atual."""
from datetime import date
ano = int(input('Qual seu ano de nascimento ? '))
idade = date.today().year - ano
print(idade)
