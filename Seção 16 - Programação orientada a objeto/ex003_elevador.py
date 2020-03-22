""" Crie uma classe denominada Elevador para armazenar as informações de um elevador dentro de um prédio. A classe deve
armazenar o andar atual(térreo = 0), total de andares no prédio, excluindo o térreo, capacidade do elevador e quantas
pessoas estão presentes nele.
A classe deve também disponibilizar os seguintes métodos:
-> Inicializa: que deve receber como parâmetros a capacidade do elevador e o total de andares no prédio(o elevador
sempre começa no térreo e vazio);
-> Entra: para acrescentar uma pessoa no elevador(só deve acrescentar se ainda houver espaço);
-> Sai: para remover uma pessoa do elevador(só deve remover se houver alguém dentro dele);
-> Sobe: para subir um andar(não deve subir, se já estiver no último andar)
-> Desce: para descer um andar(não deve descer, se já estiver no térreo.)
Encapsular todos os atributos da classe(criar métodos get e set).
"""
from Secao16_Programacao_orientada_a_objeto.elevador import Elevador

el = Elevador(3, 0)
el.entra(2)
Elevador.passageiros_total()
el.entra(3)
Elevador.passageiros_total()


