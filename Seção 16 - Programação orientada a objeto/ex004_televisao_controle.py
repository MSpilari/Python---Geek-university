""" Crie uma classe Televisão e uma classe ControleRemoto que pode controlar o volume e trocar os canais da televisão.
-> O controle permite aumentar ou diminuir a potência do volume de som em uma unidade de cada vez;
-> O controle de canal também permite aumentar e diminuir o número do canal em uma unidade, porém, também possibilita
trocar para um canal indicado.
-> Também devem existir métodos para consultar o valor do volume de som e o canal selecionado."""

from Secao16_Programacao_orientada_a_objeto.televisao import Televisao
from Secao16_Programacao_orientada_a_objeto.controle_remoto import ControleRemoto

tv = Televisao()
cr = ControleRemoto(modelo='abc', televisao=tv)
cr.televisao.diminuir_volume()
cr.televisao.escolhendo_canal(-2)
