from Q01 import Pessoa
from datetime import datetime

nomePessoa = input("Informe seu nome: ")
diaNas = int(input("Qual dia nasceu? "))
mesNas = int(input("Qual mês nasceu? "))
anoNas = int(input("Qual ano nasceu? "))
totAltura = float(input("Qual é sua altura (m): "))
totPeso = float(input("Qual é seu peso? (Kg): "))
totSal = float(input("Informe seu salário: "))

data = datetime(anoNas, mesNas, diaNas)
pessoa1 = Pessoa(nome=nomePessoa, dtNascimento=data, altura=totAltura, peso=totPeso, salario=totSal)

while True:
    print("-"*45)
    opcao = int(input("O QUE VOCÊ DESEJA FAZER?\n [1]-CALCULAR IMC\n [2]-APRESENTAR\n [3]-ALTERAR SALÁRIO\n [0]-SAIR DA EXECUÇÃO "))
    if opcao == 1:
        pessoa1.calcularimc()
    elif opcao == 2:
        pessoa1.apresentar()
    elif opcao == 3:
        mudarSal = float(input("Informe o novo salário: "))
        pessoa1.alterarsalario(mudarSal)
        pessoa1.apresentar()
    elif opcao == 0:
        break
    else:
        print("OPÇÃO INVÁLIDA!!")
    print("*"*35)

