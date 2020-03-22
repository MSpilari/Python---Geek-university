class Elevador:
    __andar = 0  # Começa no térreo
    __num_passageiros = 0  # Elevador começa vazio.

    @classmethod
    def andar_atual(cls):
        if cls.__andar == 0:
            print(f'Agora estamos no Térreo.')
        else:
            print(f'Agora estamos no {cls.__andar}º andar.')

    @classmethod
    def passageiros_total(cls):
        print(f'No total tem/temos {cls.__num_passageiros} passageiro(s)')

    def __init__(self, capacity, building_lenght):
        """
        -> Método construtor da classe Elevador.
        :param capacity: Pede a entrada de um número inteiro que informa a capacidade total de passageiros no elevador.
        :param building_lenght: Pede a entrada de um número inteiro informando o Nº de andares do prédio.
        """
        self.__capacidade_elevador = capacity
        self.__tamanho_predio = building_lenght
        self.__passageiros = 0

    def entra(self, number):
        """
        -> Método que permite a entrada de um ou mais pessoas no elevador. Inclusive se houver vagas liberadas, o método
        consegue calcular quantas existem e preencher o elevador até sua capacidade total.
        :param number: Nº inteiro que informa quantas passageiros entrarão no elevador.
        :return: Sem retorno.
        """
        if Elevador.__num_passageiros + number <= self.__capacidade_elevador:
            self.__passageiros = Elevador.__num_passageiros + number
            Elevador.__num_passageiros = self.__passageiros
            print(f'Mais {number} passageiro(s) entrou/entraram no elevador.')
        else:
            print('Entrada não permitida ! O Nº de passageiros excede a capacidade total do elevador.')

    def sai(self, number):
        if Elevador.__num_passageiros > 0 and number > 0:
            if number <= Elevador.__num_passageiros:
                self.__passageiros = Elevador.__num_passageiros - number
                Elevador.__num_passageiros = self.__passageiros
                print(f'{number} passageiro(s) saiu/saíram do elevador.')
            else:
                n = 0
                while n != Elevador.__num_passageiros:
                    self.__passageiros = Elevador.__num_passageiros - 1
                    Elevador.__num_passageiros = self.__passageiros
                    n += 1
                    if Elevador.__num_passageiros == 0:
                        break
                print(f'Não existiam {number} passageiros, por isso {n} passageiro(s) saiu/saíram do elevador.')
        else:
            if number < 0:
                print('Informe um número maior que zero.')
            elif Elevador.__num_passageiros == 0:
                print('Não existem mais passageiros no elevador.')

    def sobe(self):
        if Elevador.__andar < self.__tamanho_predio:
            Elevador.__andar += 1
            print(f'Subindo para o {Elevador.__andar}º andar.')
        else:
            print('Chegamos ao último andar não é possível subir mais.')

    @staticmethod
    def desce():
        if Elevador.__andar > 0:
            Elevador.__andar -= 1
            if Elevador.__andar == 0:
                print('Descendo para o térreo')
            else:
                print(f'Descendo para o {Elevador.__andar}º andar.')
        else:
            print('Já estamos no térreo, não é possível descer mais.')
