class Funcionario:

    def __init__(self, nome, salario, cargo):
        self.__nome = nome
        self.__salario = salario
        self.__cargo = cargo

    def apresentarfunc(self):
        print(f"O nome do funcionário é {self.__nome}")
        print(f"{self.__nome} recebe um salário de {self.salario}R$")
        print(f"{self.__nome} é {self.cargo} da empresa")
        print("-"*30)

    def porcentando(self, porcent):
        print(f"O SALÁRIO ATUAL É {self.__salario}")
        calcSal = self.__salario + (porcent / 100 * porcent)
        self.salario = calcSal
        print(f"O SALÁRIO NOVO É {self.salario} COM AUMENTO DE {porcent}")

    def mudarcargo(self, newCargo):
        print("-"*30)
        self.cargo = newCargo
        print("-" * 30)
