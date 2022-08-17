from Q07 import Onibus
print("-"*30)
print("TRANSPORTANDO COM QUALIDADE")
print("-"*30)

nmMtrista = input("Informe o nome do motorista: ")
corOnibus = input("Informe a cor do ônibus: ")

onibus1 = Onibus(cor=corOnibus, motorista=nmMtrista)

print("-"*30)
while True:
    opcoes = int(input("QUAL OPÇÃO DESEJA:\n [1]-EXIBIR DETALHES\n [2]-EMBARCAR\n [3]-MOSTRAR OS PASSAGEIROS\n [4]-MUDAR MOTORISTA\n [5]-LIGAR/DESLIGAR\n [6]-FECHAR AS PORTAS"))
    if opcoes == 1:
        print("-" * 30)
        onibus1.detalhes()
    elif opcoes == 2:
        print("<->" * 8)
        print("ENTRADA DE PASSAGEIROS")
        print("<->" * 8)
        nmPass = input("Informe seu nome antes de entrar: ")
        onibus1.embarcar(nmPass)
        print("-"*30)
    elif opcoes == 3:
        print("-"*30)
        onibus1.exibirpass()
        print("-" * 30)
    elif opcoes == 4:
        mudanome = input("Informe o nome do novo motorista: ")
        onibus1.mudarnome(mudanome)
    elif opcoes == 5:
        print("-" * 25)
        escolha = input("Deseja Ligar/Desligar: ")
        print("-" * 25)
        if escolha == "sim":
            onibus1.ligarDesligar()
        else:
            print("Você optou por Ligar/Desligar")
            print("-"*25)
    elif opcoes == 6:
        print("-"* 40)
        print("SIMBORAA, NÃO PODE MAIS ENTRAR NINGUEM!!!")
        print("-" * 40)
        break
    else:
        print("OPÇÃO INVÁLIDA!!!")





