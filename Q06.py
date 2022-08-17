class Tv:

    def __init__(self):
        self.__canal = 0
        self.__volume = 0
        self.__ligada = False

    def ligarDesligar(self):
        self.__ligada = not self.__ligada
        if self.__ligada:
            print("Ligou a TV")
        else:
            print("Desligou a TV")

    def altervolume(self, vol):
        if self.__ligada:
            if vol == "+":
                if self.__volume == 100:
                    print("NÃO AUMENTA!! VOLUME JÁ ESTÁ NO MÁXIMO!!!")
                else:
                    print("Aumentando volume....")
                    self.__volume += 1
            elif vol == "-":
                if self.__volume == 0:
                    print("NÃO DIMINUI!! VOLUME JÁ ESTÁ NO MÍNIMO!!!")
                else:
                    print("Diminuindo volume....")
                    self.__volume -= 1
            else:
                print("SINAL DE VOLUME ERRADO!!!")

    def alterCanal(self, can):
        if self.__ligada:
            if can == ">":
                print("Passando canal....")
                self.__canal += 1
            elif can == "<":
                print("Voltando canal....")
                self.__canal -= 1
            else:
                print("SINAL DE CANAL ERRADO!!!")

    def exibirtv(self):
        if self.__ligada:
            print("-" * 25)
            print("A TV está ligada")
            print(f"Está no volume {self.__volume}")
            print(f"Está no canal {self.__canal}")
            print("-" * 25)
        else:
            print("-" * 20)
            print("A TV está desligada")
            print("-" * 20)

    # def aumentarvolume(self):
    #     if self.ligada:
    #         print("Aumentando volume....")
    #         self.volume += 1
    #     else:
    #         print("A TV está desligada...")
    #         print("-" * 20)
    #
    # def diminuirvolume(self):
    #     if self.ligada:
    #         print("Diminuindo volume....")
    #         self.volume -= 1
    #     else:
    #         print("A TV está desligada...")
    #         print("-" * 20)

    # def passarcanal(self):
    #     if self.ligada:
    #         print("Passando canal....")
    #         self.canal += 1
    #     else:
    #         print("A TV está desligada...")
    #         print("-" * 20)
    #
    # def voltarcanal(self):
    #     if self.ligada:
    #         print("Voltando canal....")
    #         self.canal -= 1
    #     else:
    #         print("A TV está desligada...")
    #         print("-" * 20)


