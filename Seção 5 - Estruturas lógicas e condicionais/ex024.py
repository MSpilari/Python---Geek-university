""" Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa diferente de imposto
sobre o produto(MG 7%; SP 12%; RJ 15%; MS 8%). Faça um programa em que o usuário entre com o valor e o estado do destino
do produto e o programa retorne o preço final do produto acrescido do imposto do estado em que ele será vendido. Se o
estado digitado não for válido, mostrar uma mensagem de erro."""
print('=' * 40)
print(f'{"SINFOROSO ENTREGAS":^40}')
print('=' * 40)
while True:
    print('Digite valor 0 para ENCERRAR O PROGRAMA.')
    valor = float(input('Qual o valor do produto ? '))
    print('=' * 40)
    if valor == 0:
        print('Programa encerrado. Volte sempre !')
        break
    print("""--> Entregas apenas para MG/SP/RJ/MS
    1 -> Minas Gerais - 7% de imposto
    2 -> São Paulo - 12% de imposto
    3 -> Rio de Janeiro - 15% de imposto
    4 -> Mato Grosso do Sul - 8% de imposto """)
    print('=' * 40)
    while True:
        resposta = int(input('Qual a localização que deseja ? '))
        if resposta < 1 or resposta > 4:
            print('\033[1;31mOpção INVÁLIDA. Tente novamente.\033[m')
            print('=' * 40)
            continue
        elif resposta == 1:
            total = valor * 1.07
            print(f'Para Minas Gerais o seu produto custará R${total:.2f}')
            print('=' * 40)
            break
        elif resposta == 2:
            total = valor * 1.12
            print(f'Para São Paulo o seu produto custará R${total:.2f}')
            print('=' * 40)
            break
        elif resposta == 3:
            total = valor * 1.15
            print(f'Para o Rio de Janeiro o seu produto custará R${total:.2f}')
            print('=' * 40)
            break
        else:
            total = valor * 1.08
            print(f'Para o Mato Grosso do Sul o seu produto custará R${total:.2f}')
            print('=' * 40)
            break
