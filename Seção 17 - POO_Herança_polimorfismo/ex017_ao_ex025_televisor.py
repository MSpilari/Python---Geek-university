"""-->Escreva um código que apresent e a classe Eletrodoméstico, com atributo ligado e o método imprimir. O método
imprimir deve mostrar na tela os valores de todos os atributos. O atributo ligado será booleano e deverá indicar o
estado atual do eletrodoméstico, se ligado ou desligado.
-->Escreva um código que apresente a classe Televisor, com atributos ligado, canal, volume e o método imprimir. O método
imprimir deve mostrar na tela os valores de todos os atributos. O atributo ligado será boleano e deverá indicar o estado
atual do televisor, se ligado ou desligado.O atributo canal deverá indicar o canal atual em que o televisor está
sintonizado. O atributo volume deverá indicar o volume atual do televisor.
--> Adicione os atributos numeros_canais, indica o número máximo de canais e volume_maximo que indica o volume máximo.
--> Adicione os métodos canal_acima e canal_abaixo, sendo que o método canal acima deve sintonizar sempre o próximo
canal em relação ao canal atual, onde ao chegar ao maior canal possível deverá voltar ao canal 1. O método canal_abaixo
deve sintonizar sempre o canal anterior em relação ao canal atual, onde ao chegar ao canal 1 deverá voltar ao maior
canal.
--> Adicione os métodos volume_acima e volume_abaixo, caso o volume chegue no máximo ou no mínimo, não será possível
aumentá-lo ou diminui-lo, respectivamente.
"""
from Secao17_POO_Heranca_Polimorfismo.classes.televisor import Televisor

tv = Televisor()
tv.imprimir()
tv.ligar_desligar()
tv.aumentar_volume()
tv.imprimir()
tv.abaixar_volume()
tv.imprimir()

