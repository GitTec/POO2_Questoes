class Elevador:

    def __init__(self, totAndares, capElevador=0):
        self.__andartual = 0
        self.__totAndares = totAndares
        self.__capElevador = capElevador
        self.__qtdPessoas = 0

    def entra(self):
        if self.__qtdPessoas == self.__capElevador:
            print("*"*50)
            print("NÃO PODE ENTRAR MAIS NINGUEM, O ELEVADOR JÁ ESTÁ LOTADO!!")
        else:
            self.__qtdPessoas += 1
            print("-"*35)
            print(f"PODE ENTRAR, HÁ VAGA PRA {self.__capElevador - self.__qtdPessoas} PESSOAS")

    def sair(self):
        if self.__qtdPessoas == 0:
            print("NÃO TEM NINGUEM NO ELEVADOR")
        else:
            print("SAINDO UMA PESSOA")
            self.__qtdPessoas -= 1

    def subir(self):
        if self.__totAndares == self.__andartual:
            print("*"*30)
            print("NÃO SOBE, POIS JA ESTÁ NO ÚLTIMO ANDAR")
        elif self.__andartual > self.__totAndares:
            print(f"ERRO! O PRÉDIO SÓ POSSUI {self.__totAndares}")
        else:
            print("O ELEVADOR ESTÁ SUBINDO")
            self.__andartual += 1

    def descer(self):
        if self.__andartual == 0:
            print("*" * 30)
            print("NÃO DESCE, POIS JA ESTÁ NO PRIMEIRO ANDAR")
        else:
            print("O ELEVADOR ESTÁ DESCENDO")
            self.__andartual -= 1

    def apresentar(self):
        print("-"*30)
        print(f"O ELEVADOR TEM {self.__qtdPessoas} PESSOA(S) DENTRO")
        print(f"O ELEVADOR ESTÁ NO {self.__andartual}° ANDAR")
        print("-" * 30)