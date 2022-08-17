from datetime import datetime
import math


class Pessoa:

    def __init__(self, nome, dtNascimento, altura, peso, salario):
        self.__nome = nome
        self.__dtNasc = dtNascimento
        self.__altura = altura
        self.__peso = peso
        self.__salario = salario

    def apresentar(self):
        print("*"*35)
        print(f"SEU NOME É: {self.__nome}")
        print(f"VOCÊ NASCEU EM: {self.__dtNasc}")
        idade = self.calcidade()
        print(f"VOCÊ TEM {idade} anos")
        print(f"SUA ALTURA É: {self.__altura}m")
        print(f"SEU PESO É: {self.__peso}Kg")
        print(f"SEU SALÁRIO É: {self.__salario}R$")
        print("*" * 35)

    def calcularimc(self):
        print(f"SEU IMC É {self.__peso / (self.__altura**2):.3f}")

    def alterarsalario(self, novoSal):
        print("*"*30)
        print(f"Seu novo salário é: {novoSal}")
        self.salario = novoSal

    def calcidade(self):
        anoAtual = datetime.now()
        qtdDias = (anoAtual - self.__dtNasc).days
        idade = math.floor(qtdDias/365)
        return idade

