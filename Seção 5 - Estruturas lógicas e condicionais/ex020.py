""" Dados três valores A, B e C, verificar se eles podem ser valores dos lados de um triângulo ,se forem, se é um
triângulo escaleno, equilátero ou isósceles."""
print('='*40)
print(f'{"Conversor de Triângulos":^40}')
print('='*40)
a = float(input('Digite a medida do lado A: '))
b = float(input('Digite a medida do lado B: '))
c = float(input('Digite a medida do lado C: '))
if a < b + c and b < a + c and c < a + b:
    if a != b and a != c and b != c:
        print(f'Os valores informados {a}, {b} e {c}, formam um triângulo e ele é ESCALENO.')
    elif a == b and a != c or c == a and b != c or c == b and c != a:
        print(f'Os valores informados {a}, {b} e {c} formam um triângulo e ele é ISÓSCELES.')
    else:
        print(f'Os valores informados {a}, {b} e {c}, formam um triângulo e ele é EQUILÁTERO.')
else:
    print(f'Os valores informados {a}, {b} e {c}, NÃO formam um triângulo. ')
