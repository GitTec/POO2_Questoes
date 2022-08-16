from Q04 import Funcionario
func01 = Funcionario(nome="Rock", salario=5000, cargo="Gerente")

while True:
    print("-"*30)
    opcao = int(input("O QUE DESEJA FAZER? [1]-INFORMAÇÕES DO FUNCIONÁRIO [2]-VER SALÁRIO [3]-MUDAR O CARGO DO FUNCIONÁRIO [0] SAIR DA EXECUÇÃO"))
    if opcao == 1:
        print("." * 28)
        print("INFORMAÇÕES DO FUNCIONÁRIO")
        print("." * 28)
        func01.apresentarfunc()
    elif opcao == 2:
        porc = int(input("Quantos % terá de aumento o salário?"))
        func01.porcentando(porcent=porc)
        #func01.porcentando()
    elif opcao == 3:
        mudSal = input("Informe o novo cargo: ")
        func01.mudarcargo(mudSal)
        func01.apresentarfunc()
    elif opcao == 0:
        print("ACABOU A EXECUÇÃO!!")
        break
    else:
        print("OPÇÃO INVÁLIDA!!!")
