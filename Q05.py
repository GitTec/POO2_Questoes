class Triangulo:

    def __init__(self, catetoOposto, catetoAdjascente, hipotenusa):
        self.__catetOposto = catetoOposto
        self.__catetAdjascente = catetoAdjascente
        self.__hipot = hipotenusa

    def exibirtriangulo(self):
        print("-" * 25)
        print("   DADOS DO TRIÂNGULO")
        print("-" * 25)
        print(f"Cateto Oposto-> {self.__catetOposto}")
        print(f"Cateto Adjascente-> {self.__catetAdjascente}")
        print(f"Hipotenusa-> {self.__hipot}")
        print("-" * 25)

    def calcularseno(self):
        resultSeno = (self.__catetOposto / self.__hipot)
        print(f"Seno-> {resultSeno}")
        return resultSeno

    def calcularcosseno(self):
        resultCosseno = (self.__catetAdjascente / self.__hipot)
        print(f"Cosseno-> {resultCosseno}")
        return resultCosseno

    def calculartangente(self):
        resultTangente = (self.__catetOposto / self.__catetAdjascente)
        print(f"Tangente-> {resultTangente}")
        return resultTangente

    def calculartotal(self):
        calculaseno = self.calcularseno()
        calculacosseno = self.calcularcosseno()
        calculatangente = self.calculartangente()
        resultTotal = calculaseno+calculacosseno+calculatangente
        print(f"A soma é {resultTotal}")
