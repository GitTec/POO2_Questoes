from Q05 import Triangulo

print("*"*25)
print("CALCULANDO O TRIÂNGULO")
print("*"*25)

catOpos = int(input("INFORME O CATETO OPOSTO DO TRIÂNGULO: "))
catAdj = int(input("INFORME O CATETO ADJASCENTE: "))
hipot = int(input("INFORME A HIPOTENUSA: "))

triangulo01 = Triangulo(catetoOposto=catOpos, catetoAdjascente=catAdj, hipotenusa=hipot)
while True:
    opcao = int(input("O QUE DESEJA SABER? [1]-INFORMAÇÕES DO TRIÂNGULO [2]-SENO [3]-COSSENO [4]-TANGENTE [5]-SOMA GERAL [0]-SAIR"))
    if opcao == 1:
        triangulo01.exibirtriangulo()
    elif opcao == 2:
        triangulo01.calcularseno()
    elif opcao == 3:
        triangulo01.calcularcosseno()
    elif opcao == 4:
        triangulo01.calculartangente()
    elif opcao == 5:
        triangulo01.calculartotal()
        #triangulo01.calculartotal(seno=calculaseno, cosseno=calculacosseno, tangente=calculatangente)
    elif opcao == 0:
        print("-"*30)
        print("A EXECUÇÃO ESTÁ ENCERRADA")
        print("-" * 30)
        break
    else:
        print("OOPS, OPÇÃO INVÁLIDA!!!!")