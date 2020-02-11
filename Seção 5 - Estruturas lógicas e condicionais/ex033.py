""" Um produto vai sofrer um aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e escreva o preço novo,
e escreva uma mensagem em função do preço novo.
Preço antigo            Percentual de aumento              Preço novo                   Mensagem
Até R$ 50                       5%                    Até R$ 80                         Barato
Entre R$ 50 e R$ 100            10%                   Entre R$ 80 e R$ 120              Normal
Acima de R$ 100                 15%                   Entre R$ 120 e R$ 200             Caro
                                                      Acima de R$ 200                   Muito caro """
preco = float(input('Informe o preço do produto: R$'))
if preco <= 50:
    precof = preco * 1.05
elif 50 < preco <= 100:
    precof = preco * 1.10
else:
    precof = preco * 1.15
if precof <= 80:
    print(f'O preço final de seu produto com o aumento foi de R${precof:.2f}. Assim ele é BARATO.')
elif 80 < precof <= 120:
    print(f'O preço final de seu produto com aumento foi de R${precof:.2f}. Assim ele é NORMAL.')
elif 120 < precof <= 200:
    print(f'O preço final do seu produto com o aumento foi de R$ {precof:.2f}. Assim ele é CARO.')
else:
    print(f'O preço final do seu produto com aumento foi R${precof:.2f}. Assim ele é MUITO CARO.')
