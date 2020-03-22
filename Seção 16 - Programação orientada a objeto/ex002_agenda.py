""" Crie uma classe agenda que pode armazenar 10 pessoas e seja capaz de realizar as seguintes operações:
-> Armazena pessoa(String nome, int idade, float altura)
-> Remove pessoa(String nome)
-> Busca pessoa(String nome) Informa em que posição da agenda está a pessoa.
-> Imprime agenda. Imprime os dados de todas as pessoas da agenda.
-> Imprime pessoa(int index). Imprime os dados da pessoa que está na posição i da agenda."""
from Secao16_Programacao_orientada_a_objeto.agenda import Agenda

ag = Agenda()
ag.armazena_pessoa('Matheus', 25, 1.70)
ag.armazena_pessoa('Otávio', 13, 1.35)
ag.armazena_pessoa('Timóteo', 76, 1.56)
ag.armazena_pessoa()
