class Tv:

    def __init__(self):
        self.canal = 0
        self.volume = 0
        self.ligada = False

    def ligartv(self):
        self.ligada = True
        print("Ligou a TV")

    def desligartv(self):
        self.ligada = False
        print("Desligou a TV")

    def aumentarvolume(self):
        if self.ligada:
            print("Aumentando volume....")
            self.volume += 1
        else:
            print("A TV está desligada...")

    def diminuirvolume(self):
        if self.ligada:
            print("Diminuindo volume....")
            self.volume -= 1
        else:
            print("A TV está desligada...")

    def passarcanal(self):
        if self.ligada:
            print("Passando canal....")
            self.canal += 1
        else:
            print("A TV está desligada...")

    def voltarcanal(self):
        if self.ligada:
            print("Voltando canal....")
            self.canal -= 1
        else:
            print("A TV está desligada...")

    def exibirtv(self):
        if self.ligada:
            print("A TV está ligada")
        else:
            print("A TV está desligada")
        print(f"Está no volume {self.volume}")
        print(f"Está no canal {self.canal}")