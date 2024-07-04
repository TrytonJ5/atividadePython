#sistema bancario
#operaçao de saque deposito e visualizar extrato
#depositar apenas valores positivos
#o sistema pode liberar 3 saques diarios com limite de 500 reais cada
#no final da listagem deve exibir o saldo atual da conta usando o formato "RS xxx,xx"

menu = """
        SISTEMA BANCARIO
        
        [D] - Depositar
        [S] - Sacar
        [E] - Extrato
        [Q] - Sair
        
        => """

saldo = 0
LIMITE = 500
extrato = "" 
numero_saques = 0
LIMITE_DIARIO_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("digite um valor para depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"\nDeposito: R$ {valor: .2f}"
            print(f"valor depositado R${valor: .2f} o saldo atual é R${saldo: .2f}")

        else:
            print(f"valor {valor} invalido")

    elif opcao == "s":
        if numero_saques < LIMITE_DIARIO_SAQUES:
            valor = float(input("digite um valor para sacar: "))

            if (valor <= LIMITE) and (valor <= saldo):
                numero_saques += 1
                saldo -= valor
                extrato += f"\nSaque: R$ {valor: .2f}"
                print(f"valor sacado R${valor: .2f} o saldo atual é R${saldo: .2f}")

            else:                 
                print(f"valor {valor} invalido")
        
        else:
            print("numero de saques excedido")        

    elif opcao == "e":
        print("extrato".center(13,"#"))
        print("Nao foram realizadas movimentaçoes." if not extrato else extrato)
        print(f"saldo: R$ {saldo: .2f}")
        print("".center(13,"#"))
    
    elif opcao == "q": 
        print("saindo...")
        break

    else:
        print("opçao invalida tente novamente")