menu = """

Digite a opção desejada

[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair

=> """

usuario_logado = True
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(valor):
    global saldo
    global extrato
    if valor <= 0:
        print("Saldo insuficiente para deposito")
    else:
        saldo += valor
        extrato += f"Depósito: R${valor}\n"
        print(f"valor depositado de R${valor}")

def sacar(valor_saque):
    global saldo
    global numero_saques
    global LIMITE_SAQUES
    global extrato
    if numero_saques >= LIMITE_SAQUES:
        print(f"""
              
Você ultrapassou o número de saques permitidos
Saques efetuados: {numero_saques}
              
              """)
    elif valor_saque > saldo:
        print(f"""
              
Saldo insuficiênte
Saldo disponível: R${saldo}
              
              """)
    elif valor_saque > 500.00:
        print(f"""
              
Limite de saque é: R$500,00
Saldo disponível: R${saldo}
              
              """)    
    elif valor_saque > 0:
        saldo -= valor_saque
        numero_saques += 1
        extrato += f"Saque: R${valor_saque}\n"
        print(f"""
              
Saque no valor de: R${valor_saque:.2f}
Saldo disponível: R${saldo:.2f}
              
              """)
    else:
        print("""
              
            Operação falhou, valor informado inválido,
        
              """)

def mostrar_extrato():
    global extrato
    global saldo
    print("============= EXTRATO =============\n")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"Saldo: R${saldo:.2f}")
    print("\n===================================")

while usuario_logado:
    opcao = input(menu)
    if opcao == "1":
        valor_deposito = float(input("digite o valor do depósito: R$"))
        depositar(valor_deposito)

    elif opcao == "2":
        valor_saque = float(input("digite o valor do saque: R$"))
        sacar(valor_saque)

    elif opcao == "3":
        mostrar_extrato()

    elif opcao == "4":
        usuario_logado = False
    else:
        print()




