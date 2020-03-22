class Agenda:
    contador = 1

    def __init__(self):
        self.__agenda = list()
        self.__agendatemp = dict()
        self.__contador = Agenda.contador

    def armazena_pessoa(self, nome=None, idade=0, altura=0):
        if Agenda.contador <= 2 and nome is not None:
            self.__agendatemp = {'Nome': nome, 'Idade': idade, 'Altura': altura}
            self.__agenda.append(self.__agendatemp.copy())
            self.__contador += 1
            Agenda.contador = self.__contador
            print(f'{nome} adicionado com sucesso.')
        elif nome is None:
            print('Você precisa informar, pelo menos, um nome para adicionar alguém a sua agenda.')
        else:
            print('Sua agenda atingiu a capacidade máxima. Apague alguém para poder adicionar mais pessoas.')

    def imprime_agenda(self):
        print(f'{"Agenda Completa":^30}')
        for elemento in self.__agenda:
            print('=' * 30)
            for key in elemento.keys():
                print(f'{key:^10}', end='')
            print()
            print('=' * 30)
            for value in elemento.values():
                print(f'{value:^10}', end='')
            print()
        print('=' * 30)

    def remove_pessoa(self, nome=None):
        contador = 0
        if len(self.__agenda) > 0:
            for dicionario in self.__agenda:
                if nome in dicionario.values():
                    self.__agenda.remove(dicionario)
                    print(f'{nome} REMOVIDO da agenda com sucesso.')
                else:
                    contador += 1
                    if contador == len(self.__agenda):
                        print(f'Não encotrei o nome {nome} na lista.')
        else:
            print('Sua agenda está vazia. Não é possível remover ninguém.')

    def busca_pessoa(self, nome=None):
        contador = 0
        for dicionario in self.__agenda:
            if nome in dicionario.values():
                print(f'O {nome} está na {self.__agenda.index(dicionario) + 1}ª posição da agenda.')
            else:
                contador += 1
                if contador == len(self.__agenda):
                    print(f'O {nome} não está no dicionário.')

    def imprime_posicao(self, posicao=None):
        try:
            if 0 < posicao <= len(self.__agenda):
                print('=' * 30)
                [print(f'{key:^10}', end='')for key in self.__agenda[posicao - 1].keys()]
                print()
                print('=' * 30)
                [print(f'{value:^10}', end='')for value in self.__agenda[posicao - 1].values()]
                print()
                print('=' * 30)
            else:
                print(f'Não existe a {posicao}ª posição na agenda.')
        except TypeError:
            print('ERRO! Informe a posição, em NUMERAL, do elemento que deseja mostrar.')
