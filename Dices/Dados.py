import random


class Visualizador:

    def __init__(self):
        self.valores = [0]

    def __eq__(self, other):
        return self.valores[-1] != other.numero_final or self.valores == other.numero_final

    @staticmethod
    def dado(quantos_lados):
        dado = random.randrange(1, quantos_lados + 1)
        return dado

    def arquivo_hist(self, valor):
        self.valores.append(valor)
        return self.valores

    def sem_numero_repetido(self, numero_final):

        i = 0
        while numero_final != self.valores[-1] and i < 1:
            antirepeticao = self.arquivo_hist(numero_final)
            i += 1
            return antirepeticao

    def tem_numero_repetido(self, numero_final, quantos_lados):
        while self.valores[-1] == numero_final:

            numero_final = self.dado(quantos_lados)
            return numero_final

    def mostra_para_o_usuario(self):

        while True:
            dice = input('Qual dado vamos rodar??')
            lado = dice.split(sep='d')
            quantos_lados, vezes, n = lado[-1], lado[0], 1
            quantos_lados, vezes = int(quantos_lados), int(vezes)
            while n <= vezes:
                numero_final = self.dado(quantos_lados)
                refatorado = self.refatorado_com_e_sem_repeticao(numero_final, quantos_lados + 1)
                print(refatorado)
                n += 1

    def refatorado_com_e_sem_repeticao(self, numero_final, quantos_lados):

        if self.valores[-1] != numero_final:
            self.sem_numero_repetido(numero_final)
            return numero_final

        else:
            numero_refatorado = self.tem_numero_repetido(numero_final, quantos_lados)
            self.arquivo_hist(numero_refatorado)
            return numero_refatorado
