from Secao17_POO_Heranca_Polimorfismo.classes.eletrodomestico import Eletrodomestico


class Microondas(Eletrodomestico):
    def __init__(self, ligado=False):
        super().__init__(ligado)
        self.__porta_fechada = True

    def imprimir(self):
        print('--Dados do Microondas--\n'
              f'Situação: {"Ligado" if self.ligado is True else "Desligado"}\n'
              f'Porta: {"Aberta" if self.__porta_fechada is False else "Fechada"}')
        print('=' * 30)

    def ligar_desligar(self):
        if self.__porta_fechada:
            if self.ligado is False:
                self._Eletrodomestico__ligado = True
                print('Com a porta fechada, o Microondas pode ser ligado...')
                print('=' * 30)
            else:
                self._Eletrodomestico__ligado = False
                print('Com a porta fechada, o Microondas pode ser desligado...')
                print('=' * 30)
        else:
            self._Eletrodomestico__ligado = False
            print('Com a porta aberta, o Microondas não pode ser ligado...')
            print('=' * 30)

    def abrir_porta_fechar_porta(self):
        if self.ligado is False:
            if self.__porta_fechada:
                self.__porta_fechada = False
                print('Abrindo a porta...')
                print('=' * 30)
            else:
                self.__porta_fechada = True
                print('Fechando a porta...')
                print('=' * 30)
        else:
            print('Não posso abrir a porta, pois o Microondas está ligado.')
            print('=' * 30)
