class Onibus:

    def __init__(self, cor, motorista):
        self.__Ligado = False
        self.__cor = cor
        self.__motoris = motorista
        self.__qtdPass = 0
        self.__nmPassageiros = []

    def detalhes(self):
        print(f"É de cor {self.__cor}")
        print(f"O nome do motorista é {self.__motoris}")
        print(f"Tem um total de {self.__qtdPass} passageiros no ônibus")
        print(f"Os passageiros são: {self.__nmPassageiros}")
        print("-" * 30)

    def ligarDesligar(self):
            if self.__qtdPass == 0:
                self.__Ligado = not self.__Ligado
            else:
                print("Ainda existem passageiros no ônibus")
                return
            if self.__Ligado:
                print("Liguei o ônibus")
                print("-"*25)
            else:
                print("Desliguei o ônibus")
                print("-" * 25)

    def embarcar(self, nmPass):
        if self.__Ligado:
            self.__nmPassageiros.append(nmPass)
            print(f"{nmPass} entrou...")
            self.__qtdPass += 1
        else:
            print(f"NÃO ENTRA, Onibus está desligado!!")

    def exibirpass(self):
        if self.__qtdPass == 0:
            print("AINDA NÃO HÁ PASSAGEIROS")
        else:
            print(f"Tem {self.__qtdPass} passageiros no ônibus")
            print(f"--->{self.__nmPassageiros}")

    def mudarnome(self, mudanome):
        self.__motoris = mudanome
