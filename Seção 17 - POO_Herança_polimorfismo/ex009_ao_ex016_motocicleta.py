""" Escreva um código que apresente a classe Moto, com atributos como Marca, modelo, cor e marcha e o método imprimir. O
método imprimir deve mostrar na tela os valores de todos os atributos. O atributo marcha indica em que marcha a moto se
encontra no momento, sendo representado de forma inteira de 0 - Neutro, 1 - Primeira, 2 - Segunda, 3 - Terceira,
4 - Quarta, 5 - Quinta.
Baseando-se no enunciado acima adicione os métodos marcha_acima e marcha_abaixo que deverão efetuar as trocas de marcha.
Adicione o atributo ligar que será do tipo booleano e indicará se a moto está ligada ou não.
"""
from Secao17_POO_Heranca_Polimorfismo.classes.motocicleta import Moto

moto = Moto('Kawasaki', 'Ninja', 'Verde')
moto.imprimir()
moto.marcha_acima()
moto.marcha_abaixo()
