""" Escreva um programa de ajuda para os vendedores. A partir de um valor total lido, mostre:
-> O total a pagar com desconto de 10%;
-> O valor de cada parcela no parcelamento de 3x sem juros;
-> A comissão do vendedor, no caso da venda ser a vista(5% sobre o valor com desconto)
-> A comissão do vendedor, no caso da venda ser parcelada(5% sobre o valor total)"""
print('='*40)
print(f'{"Lojas Sinforoso":^40}')
print('='*40)
while True:
    valor_do_produto = float(input('Qual o valor do produto ?(0 encerra o programa) '))
    if valor_do_produto == 0:
        print('Programa encerrado. Volte sempre !!')
        break
    print("""Escolha a forma de pagamento:
        1 -> À vista com desconto de 10%
        2 -> Parcelado em 3x sem juros. """)
    while valor_do_produto != 0:
        forma_de_pagamento = int(input('Forma de pagamento: '))
        if forma_de_pagamento == 1:
            valorf = valor_do_produto * 0.9
            comissao = valorf * 0.05
            print('Opção 1 selecionada - À vista com desconto de 10%')
            print(f'O preço do produto é {valorf:.2f} e a comissão do vendedor é R${comissao:.2f}')
            break
        elif forma_de_pagamento == 2:
            valor_parcela = valor_do_produto / 3
            comissao = valor_do_produto * 0.05
            print('Opção 2 selecionada - Parcelado em 3x sem juros.')
            print(f'Cada parcela será de R${valor_parcela:.2f} e a comissão do vendedor é R${comissao:.2f}')
            break
        elif forma_de_pagamento != 1 and forma_de_pagamento != 2:
            print('Opção Inválida. Tente novamente.')
            continue


