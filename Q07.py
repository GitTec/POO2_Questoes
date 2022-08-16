class Onibus:

    def __init__(self, cor, motorista):
        self.Ligado = False
        self.cor = cor
        self.motoris = motorista
        self.qtdPass = 0
        self.nmPassageiros = []

    def detalhes(self, querligar):
        if querligar == "S" or querligar == "s":
            self.Ligado = True
            print("O ônibus está ligado")
        else:
            print("O ônibus está desligado")

        print(f"É de cor {self.cor}")
        print(f"O nome do motorista é {self.motoris}")
        print(f"Tem um total de {self.qtdPass} passageiros no ônibus")
        print(f"Os passageiros são: {self.nmPassageiros}")
        print("-" * 30)

    def embarcar(self, nmPass):
        if self.Ligado:
            self.nmPassageiros.append(nmPass)
            print(f"{nmPass} entrou...")
            self.qtdPass += 1
        else:
            print(f"NÃO ENTRA, Onibus está desligado!!")


    def exibirpass(self):
        if self.qtdPass == 0:
            print("AINDA NÃO HÁ PASSAGEIROS")
        else:
            print(f"Tem {self.qtdPass} passageiros no ônibus")
            print(f"--->{self.nmPassageiros}")

    def mudarnome(self, mudanome):
        self.motoris = mudanome
