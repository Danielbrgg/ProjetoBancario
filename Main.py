from Banco import banco
import subprocess
senha = "1234"

isRunning = True
acesso = False

saldo = 0
contador = 0
nome = input("Digite seu nome: ")
idade = input("Digite a sua idade: ")

objPessoa = {
        "nome" : nome,
        "idade" : idade,
        "saldo" : saldo
    }

pessoa = banco(objPessoa)

while not acesso and isRunning:
    tentativa = input("Digite a sua senha: ")
    if senha != tentativa:
        print("Senha invalida! tente novamente")
        contador += 1
        if contador == 3:
            print("Bloqueamos por excesso de tentativas!")
            break 
    else:
        acesso = True
        
while acesso == True and isRunning:
    print("1 - Mostrar Saldo")
    print("2 - Depósito")
    print("3 - Saque")
    print("0 - Sair")
    op = input("Escolha uma dessas alternativas (0-3)\n")
    match op:
        case "1":
            pessoa.mostrarSaldo()
            
        case "2":
            pessoa.deposito()
            continue
        case "3":
            pessoa.saque()
            continue
        case "0":
            isRunning = False
        case "":
            print("Opção inválida!")
    