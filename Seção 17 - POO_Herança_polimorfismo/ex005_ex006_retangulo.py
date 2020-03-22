""" Escreva um código que apresente a classe Retangulo, com atributos, comprimento, largura, área e perímetro, métodos
calcular_area, calcular_perimetro e imprimir. Os métodos calcular_area e calcular_perimetro devem efetuar seus
respectivos cálculos e colocar os valores nos atributos área e perímetro. O método imprimir deve mostrar na tela os
valores de todos os atributos."""
from Secao17_POO_Heranca_Polimorfismo.classes.retangulo import Retangulo

ret = Retangulo(2, 5)
ret.imprimir()
ret.calcular_area()
ret.imprimir()
ret.calcular_perimetro()
ret.imprimir()