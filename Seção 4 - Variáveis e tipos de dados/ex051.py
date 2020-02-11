""" Escreva um programa que leia as coordenadas X e Y de pontos no R² e calcule a distância para a origem (0,0)"""
coordx = float(input('Qual o valor da abcissa(coordenada X) ? '))
coordy = float(input('Qual o valor da ordenada(coordenada Y) ? '))
"""Distância entre 2 pontos:
    D² = (x - xo)² + (y - yo)²"""
distancia = ((coordx - 0) ** 2 + (coordy - 0) ** 2) ** 1/2
print(distancia)
