from Q06 import Tv

print("-"*30)
print("MINHA TELEVISÃO")
print("-"*30)

tv1 = Tv()
pergunta = input("OLÁ TUDO BEM? DESEJA ASSISTIR TV? [S] - [N]")
if pergunta == "S":
    while True:
        acoes = int(input(f"O QUE DESEJA FAZER?\n [1]-LIGAR TV\n [2]-DESLIGAR TV\n [3]-AUMENTAR VOLUME\n [4]-DIMINUIR VOLUME\n [5]-PASSAR CANAL\n [6]-VOLTAR CANAL\n [0]-SAIR\n "))
        if acoes == 1:
            tv1.ligartv()
        elif acoes == 2:
            tv1.desligartv()
        elif acoes == 3:
            tv1.aumentarvolume()
        elif acoes == 4:
            tv1.diminuirvolume()
        elif acoes == 5:
            tv1.passarcanal()
        elif acoes == 6:
            tv1.voltarcanal()
        elif acoes == 0:
            print("SAINDO DA EXECUÇÃO!!")
            break
        else:
            print("AÇÃO INVÁLIDA!!!")
        tv1.exibirtv()
elif pergunta == "N":
    print("AH TUDO BEM, DECULPE PERGUNTAR")
else:
    print("ESCOLHA ERRADA!!!")
