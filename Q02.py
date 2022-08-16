class Elevador:

    def __init__(self, totAndares, capElevador=0):
        self.andartual = 0
        self.totAndares = totAndares
        self.capElevador = capElevador
        self.qtdPessoas = 0

    def entra(self):
        if self.qtdPessoas == self.capElevador:
            print("*"*50)
            print("NÃO PODE ENTRAR MAIS NINGUEM, O ELEVADOR JÁ ESTÁ LOTADO!!")
        else:
            self.qtdPessoas += 1
            print("-"*35)
            print(f"PODE ENTRAR, HÁ VAGA PRA {self.capElevador - self.qtdPessoas} PESSOAS")

    def sair(self):
        if self.qtdPessoas == 0:
            print("NÃO TEM NINGUEM NO ELEVADOR")
        else:
            print("SAINDO UMA PESSOA")
            self.qtdPessoas -= 1

    def subir(self):
        if self.totAndares == self.andartual:
            print("*"*30)
            print("NÃO SOBE, POIS JA ESTÁ NO ÚLTIMO ANDAR")
        elif self.andartual > self.totAndares:
            print(f"ERRO! O PRÉDIO SÓ POSSUI {self.totAndares}")
        else:
            print("O ELEVADOR ESTÁ SUBINDO")
            self.andartual += 1

    def descer(self):
        if self.andartual == 0:
            print("*" * 30)
            print("NÃO DESCE, POIS JA ESTÁ NO PRIMEIRO ANDAR")
        else:
            print("O ELEVADOR ESTÁ DESCENDO")
            self.andartual -= 1

    def apresentar(self):
        print(f"O ELEVADOR TEM {self.qtdPessoas} PESSOAS DENTRO")
        print(f"O ELEVADOR ESTÁ NO {self.andartual}° ANDAR")