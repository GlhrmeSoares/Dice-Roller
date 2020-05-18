import random


class Rolagem:

    @staticmethod
    def dado4():
        dado = random.randrange(1, 5)
        return dado

    @staticmethod
    def dado6():
        dado = random.randrange(1, 7)
        return dado

    @staticmethod
    def dado8():
        dado = random.randrange(1, 9)
        return dado

    @staticmethod
    def dado10():
        dado = random.randrange(1, 11)
        return dado

    @staticmethod
    def dado12():
        dado = random.randrange(1, 13)
        return dado

    @staticmethod
    def dado20():
        dado = random.randrange(1, 21)
        return dado

    @staticmethod
    def dado100():
        dado = random.randrange(1, 101)
        return dado


class Visualizador:

    def __init__(self):
        self.valores = [0]

    def __eq__(self, other):
        return self.valores[-1] != other.numero_final or self.valores == other.numero_final

    def mostra_hist(self):
        print(self.valores[:])

    def arquivo_hist(self, valor):
        self.valores.append(valor)
        return self.valores

    def sem_numero_repetido(self, numero_final):

        i = 0
        while numero_final != self.valores[-1] and i < 1:
            antirepeticao = self.arquivo_hist(numero_final)
            i += 1
            return antirepeticao

    def tem_numero_repetido(self, numero_final, dice):
        numero = Rolagem()
        while self.valores[-1] == numero_final:
            if dice == 'd4':
                numero_final = numero.dado4()
                return numero_final
            if dice == 'd6':
                numero_final = numero.dado6()
                return numero_final

            if dice == 'd8':
                numero_final = numero.dado8()
                return numero_final

            if dice == 'd10':
                numero_final = numero.dado10()
                return numero_final

            if dice == 'd12':
                numero_final = numero.dado12()
                return numero_final

            if dice == 'd20':
                numero_final = numero.dado20()
                return numero_final

            if dice == 'd100':
                numero_final = numero.dado100()
                return numero_final

    def refatorado_com_e_sem_repeticao(self, numero_final, dice):
        if dice == 'd4':
            if self.valores[-1] != numero_final:
                self.sem_numero_repetido(numero_final)
                return numero_final

            else:
                numero_refatorado = self.tem_numero_repetido(numero_final, 'd4')
                self.arquivo_hist(numero_refatorado)
                return numero_refatorado
        if dice == 'd6':
            if self.valores[-1] != numero_final:
                self.sem_numero_repetido(numero_final)
                return numero_final

            else:
                numero_refatorado = self.tem_numero_repetido(numero_final, 'd6')
                self.arquivo_hist(numero_refatorado)
                return numero_refatorado
        if dice == 'd8':
            if self.valores[-1] != numero_final:
                self.sem_numero_repetido(numero_final)
                return numero_final

            else:
                numero_refatorado = self.tem_numero_repetido(numero_final, 'd8')
                self.arquivo_hist(numero_refatorado)
                return numero_refatorado

        if dice == 'd10':
            if self.valores[-1] != numero_final:
                self.sem_numero_repetido(numero_final)
                return numero_final

            else:
                numero_refatorado = self.tem_numero_repetido(numero_final, 'd10')
                self.arquivo_hist(numero_refatorado)
                return numero_refatorado

        if dice == 'd12':
            if self.valores[-1] != numero_final:
                self.sem_numero_repetido(numero_final)
                return numero_final

            else:
                numero_refatorado = self.tem_numero_repetido(numero_final, 'd12')
                self.arquivo_hist(numero_refatorado)
                return numero_refatorado

        if dice == 'd20':
            if self.valores[-1] != numero_final:
                self.sem_numero_repetido(numero_final)
                return numero_final

            else:
                numero_refatorado = self.tem_numero_repetido(numero_final, 'd20')
                self.arquivo_hist(numero_refatorado)
                return numero_refatorado

        if dice == 'd100':
            if self.valores[-1] != numero_final:
                self.sem_numero_repetido(numero_final)
                return numero_final

            else:
                numero_refatorado = self.tem_numero_repetido(numero_final, 'd100')
                self.arquivo_hist(numero_refatorado)
                return numero_refatorado

    def mostra_para_o_usuario(self):
        while True:
            numero = Rolagem()

            dice = input('Qual dado vamos rodar??')

            if dice == 'd4':

                numero_final = numero.dado4()
                refatorado = self.refatorado_com_e_sem_repeticao(numero_final, 'd4')
                self.mostra_hist()
                print(refatorado)

            if dice == 'd6':
                numero_final = numero.dado6()
                refatorado = self.refatorado_com_e_sem_repeticao(numero_final, 'd6')
                self.mostra_hist()
                print(refatorado)

            if dice == 'd8':
                numero_final = numero.dado8()
                refatorado = self.refatorado_com_e_sem_repeticao(numero_final, 'd8')
                self.mostra_hist()
                print(refatorado)

            if dice == 'd10':
                numero_final = numero.dado10()
                refatorado = self.refatorado_com_e_sem_repeticao(numero_final, 'd10')
                self.mostra_hist()
                print(refatorado)

            if dice == 'd12':
                numero_final = numero.dado12()
                refatorado = self.refatorado_com_e_sem_repeticao(numero_final, 'd12')
                self.mostra_hist()
                print(refatorado)

            if dice == 'd20':
                numero_final = numero.dado20()
                refatorado = self.refatorado_com_e_sem_repeticao(numero_final, 'd20')
                self.mostra_hist()
                print(refatorado)

            if dice == 'd100':
                numero_final = numero.dado100()
                refatorado = self.refatorado_com_e_sem_repeticao(numero_final, 'd100')
                self.mostra_hist()
                print(refatorado)
