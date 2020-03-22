""" Faça um programa que receba o nome de um arquivo de entrada e outro de saída. O arquivo de entrada contém em cada
linha o nome de uma cidade e o seu número de habitantes. O programa deverá ler um arquivo de entrada e gerar um arquivo
de saída onde aparece o nome da cidade mais populosa seguida pelo seu número de habitantes."""
dicionario = dict()

with open('Cidades.txt', 'r', encoding='utf-8') as arquivobase:
    cidades = arquivobase.readlines()
    for indice in range(len(cidades)):
        cidades[indice] = cidades[indice].rstrip('\n').split(' - ')
        cidades[indice][1] = float(cidades[indice][1])
    print(cidades)
with open('Cidade mais populosa.txt', 'w', encoding='utf-8') as arquivofinal:
    mais_populosa = max(cidades, key=lambda cidade: cidade[1])
    # Criei a função lambda para ele iterar e pegar o maior valor da população nas listas aninhadas
    mais_populosa = str(mais_populosa)
    for dado in mais_populosa:
        arquivofinal.write(dado)
