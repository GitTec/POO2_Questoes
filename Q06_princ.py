from Q06 import Tv

print("-"*30)
print("MINHA TELEVISÃO")
print("-"*30)

tv1 = Tv()
pergunta = input("DESEJA ASSISTIR TV? [S] - [N]")
print("-"*35)
if pergunta == "S" or pergunta == "s":
    while True:
        acoes = int(input(f"O QUE DESEJA FAZER?\n [1]-LIGAR/DESLIGAR TV\n [2]-AUMENTAR[+]/DIMINUIR VOLUME[-]\n [3]-PASSAR[>]/VOLTAR CANAL[<]\n [0]-SAIR\n "))
        if acoes == 1:
            tv1.ligarDesligar()
        elif acoes == 2:
            vol = input("Deseja aumentar [+] ou baixar [-] o volume? ")
            tv1.altervolume(vol)
        elif acoes == 3:
            can = input("Deseja Passar [>] ou Voltar [<] canal?")
            tv1.alterCanal(can)
        elif acoes == 0:
            print("SAINDO DA EXECUÇÃO!!")
            break
        else:
            print("-"*20)
            print("AÇÃO INVÁLIDA!!!")
        tv1.exibirtv()
elif pergunta == "N" or pergunta == "n":
    print("AH TUDO BEM, DECULPE PERGUNTAR")
else:
    print("ESCOLHA ERRADA, [S] ou [N]!!!")
