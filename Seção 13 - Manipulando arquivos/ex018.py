""" Faça um programa que leia um arquivo contendo o nome e o preço de diversos produtos(separados por linha) e calcule
o total da compra."""
with open('Lista de coisas.txt', 'r', encoding='utf-8') as arquivo:
    lista_produtos = arquivo.readlines()
    precos = list()
    for indice in range(len(lista_produtos)):
        lista_produtos[indice] = lista_produtos[indice].strip()
        if indice % 2 != 0:
            lista_produtos[indice] = float(lista_produtos[indice])
            precos.append(lista_produtos[indice])
    print(f'Sua compra final totalizou R$ {sum(precos):.2f}')

