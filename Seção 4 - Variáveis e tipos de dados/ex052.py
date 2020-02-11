""" Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada
deu para a realização da aposta. Faça um programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima
quanto cada um ganharia do prêmio com base no valor investido."""
pessoa1 = float(input('Quanto a 1ª pessoa contribuiu ? R$'))
pessoa2 = float(input('Quanto a 2ª pessoa contribuiu ? R$'))
pessoa3 = float(input('Quanto a 3ª pessoa contribuiu ? R$'))
valor_premio = float(input('Qual o valor do prêmio ? R$'))
somar = pessoa1 + pessoa2 + pessoa3
print(f'A primeira pessoa deve ganhar um valor de {(pessoa1 / somar) * valor_premio}')
print(f'A segunda pessoa deve ganhar um valor de {(pessoa2 / somar) * valor_premio}')
print(f'A terceira pessoa deve ganhar um valor de {(pessoa3 / somar) * valor_premio}')
