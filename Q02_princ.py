from Q02 import Elevador

totalAndares = int(input("Quantos andares tem o prédio? "))
capacElevador = int(input("Quantas pessoas suporta? "))

elev01 = Elevador(totAndares=totalAndares, capElevador=capacElevador)
while True:
    opcao = int(input("[1]-ENTRAR [2]-SAIR [3]-SUBIR [4]-DESCER [0] ENCERRAR EXECUÇÃO"))
    if opcao == 1:
        elev01.entra()
    elif opcao == 2:
        elev01.sair()
    elif opcao == 3:
        elev01.subir()
    elif opcao == 4:
        elev01.descer()
    elif opcao == 0:
        break
    else:
        print("OPÇÃO INVÁLIDA!!")
    elev01.apresentar()