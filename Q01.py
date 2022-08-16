from datetime import datetime
import math


class Pessoa:

    def __init__(self, nome, dtNascimento, altura, peso, salario):
        self.nome = nome
        self.dtNasc = dtNascimento
        self.altura = altura
        self.peso = peso
        self.salario = salario

    def apresentar(self):
        print("*"*35)
        print(f"SEU NOME É: {self.nome}")
        print(f"VOCÊ NASCEU EM: {self.dtNasc}")
        idade = self.calcidade()
        print(f"VOCÊ TEM {idade} anos")
        print(f"SUA ALTURA É: {self.altura}m")
        print(f"SEU PESO É: {self.peso}Kg")
        print(f"SEU SALÁRIO É: {self.salario}R$")
        print("*" * 35)

    def calcularimc(self):
        print(f"SEU IMC É {self.peso / (self.altura**2):.3f}")

    def alterarsalario(self, novoSal):
        print("*"*30)
        print(f"Seu novo salário é: {novoSal}")
        self.salario = novoSal

    def calcidade(self):
        anoAtual = datetime.now()
        qtdDias = (anoAtual - self.dtNasc).days
        idade = math.floor(qtdDias/365)
        return idade

