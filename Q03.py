class Filme:

    def __init__(self, titulo, duracao, categoria):
        self.__titulo = titulo
        self.__duracao = duracao
        self.__categoria = categoria

    def verdetalhes(self):
        print("*"*30)
        print(f"O TÍTULO DO FILME É: {self.__titulo}")
        print(f"A DURAÇÃO É DE {self.__duracao} Hora(s) ")
        print(f"SUA CATEGORIA É {self.__categoria}")
        print("*" * 30)