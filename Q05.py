class Triangulo:

    def __init__(self, catetoOposto, catetoAdjascente, hipotenusa):
        self.catetOposto = catetoOposto
        self.catetAdjascente = catetoAdjascente
        self.hipot = hipotenusa

    def exibirtriangulo(self):
        print("-" * 25)
        print("   DADOS DO TRIÂNGULO")
        print("-" * 25)
        print(f"Cateto Oposto-> {self.catetOposto}")
        print(f"Cateto Adjascente-> {self.catetAdjascente}")
        print(f"Hipotenusa-> {self.hipot}")
        print("-" * 25)

    def calcularseno(self):
        resultSeno = (self.catetOposto / self.hipot)
        print(f"Seno-> {resultSeno}")
        return resultSeno

    def calcularcosseno(self):
        resultCosseno = (self.catetAdjascente / self.hipot)
        print(f"Cosseno-> {resultCosseno}")
        return resultCosseno

    def calculartangente(self):
        resultTangente = (self.catetOposto / self.catetAdjascente)
        print(f"Tangente-> {resultTangente}")
        return resultTangente

    def calculartotal(self):
        calculaseno = self.calcularseno()
        calculacosseno = self.calcularcosseno()
        calculatangente = self.calculartangente()
        resultTotal = calculaseno+calculacosseno+calculatangente
        print(f"A soma é {resultTotal}")
