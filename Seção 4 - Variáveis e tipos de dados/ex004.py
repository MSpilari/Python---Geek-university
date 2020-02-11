""" Leia um número real e imprima o resultado do quadrado desse número."""
numero = float(input('Digite um número para saber seu quadrado: '))
""" Existem 2 formas de calcular o quadrado de um número:
-> Matematicamente:
    quadrado = numero ** 2
    
-> Usando a função pow()
    pow(numero, 2) 
"""
quadrado = pow(numero, 2)
print(f'O quadrado do número {numero} é {quadrado:.2f}')
