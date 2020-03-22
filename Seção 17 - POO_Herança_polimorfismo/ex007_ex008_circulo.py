""" Escreva um código que apresente a classe Circulo, com atributos raio, área e comprimento da circunferência, métodos
calcular_area, calcular_comprimento_circunferencia e imprimir. Os métodos calcular_area e calcular_perimetro devem
efetuar seus respectivos cálculos e colocar os valores nos atributos área e perímetro. O método imprimir deve mostrar
na tela os valores de todos os atributos."""
from Secao17_POO_Heranca_Polimorfismo.classes.circulo import Circulo

circ = Circulo(4)
circ.imprimir()
circ.calcular_area()
circ.imprimir()
circ.calcular_comp_circunf()
circ.imprimir()