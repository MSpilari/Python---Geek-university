""" Faça um programa que possua um vetor denominado A que armazene 6 números inteiros. O programa deve executar os
seguintes passos:
a) Atribua os seguintes valores a esse vetor 1, 0, 5, -2, -5, 7
b) Armazene em uma variável inteira (simples) a soma entre os valores das posições A[0], A[1] e A[5] do vetor e mostre
na tela essa soma.
c) Modifique o vetor na posição A[4], atribuindo 100 a ele.
d) Mostre na tela cada valor do vetor A um em cada linha. """

vetor_A = list()
vetor_A.extend([1, 0, 5, -2, -5, 7])  # Adicionando os valores na lista.
print(f'Vetor inicial {vetor_A}')
soma_dos_valores = vetor_A[0] + vetor_A[1] + vetor_A[5]
print(f'A soma dos valores de A[0] + A[1] + A[5] é igual a {soma_dos_valores}')  # Soma dos valores.
vetor_A[4] = 100
print(f'Vetor atualizado {vetor_A}')
print(f'Um valor do vetor por linha.')
for valor in vetor_A:
    print(valor)