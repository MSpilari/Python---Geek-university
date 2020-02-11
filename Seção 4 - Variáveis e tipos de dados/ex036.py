""" Leia o raio e a altura de um cilindro circular e imprima o volume do cilindro."""
raio = float(input('Qual o raio do cilindro em metros: '))
altura = float(input('Qual a altura do cilindro em metros: '))
# Volume_cilindro = (3,14 * (raio ** 2)) * altura
volume_cilindro = (3.14 * (raio ** 2)) * altura
print(f'Um cilindro com {raio}m de raio e {altura}m de altura, tem um volume de {volume_cilindro}m³.')
