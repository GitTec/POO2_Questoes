class Filme:

    def __init__(self, titulo, duracao, categoria):
        self.titulo = titulo
        self.duracao = duracao
        self.categoria = categoria

    def verdetalhes(self):
        print("*"*30)
        print(f"O TÍTULO DO FILME É: {self.titulo}")
        print(f"A DURAÇÃO É DE {self.duracao} Hora(s) ")
        print(f"SUA CATEGORIA É {self.categoria}")
        print("*" * 30)