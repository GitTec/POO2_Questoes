class Funcionario:

    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def apresentarfunc(self):
        print(f"O nome do funcionário é {self.nome}")
        print(f"{self.nome} recebe um salário de {self.salario}R$")
        print(f"{self.nome} é {self.cargo} da empresa")
        print("-"*30)

    def porcentando(self, porcent):
        print(f"O SALÁRIO ATUAL É {self.salario}")
        calcSal = self.salario + (porcent / 100 * porcent)
        self.salario = calcSal
        print(f"O SALÁRIO NOVO É {self.salario} COM AUMENTO DE {porcent}")

    def mudarcargo(self, newCargo):
        print("-"*30)
        self.cargo = newCargo
        print("-" * 30)
