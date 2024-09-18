menu = f"""{'=' * 21} MENU {'=' * 22}
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> Digite sua opção: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    opcao = opcao.lower()

    if opcao == "d":

        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print('Depósito realizado com sucesso!')
        else:
            print("Valor de depósito não pode ser menor ou igual a 0.")

    elif opcao == "s":

        if saldo <= 0:

            print("Operação falhou! Você não tem saldo suficiente.")

        else:

            valor = float(input("Informe o valor do saque: "))

            if valor <= 0:

                print("Valor do saque não pode ser menor ou igual a 0.")
            
            else:

                excedeu_limite = valor > limite
                excedeu_saques = numero_saques >= LIMITE_SAQUES

                if excedeu_limite:

                    print("Operação falhou! O valor do saque excede o limite.")

                elif excedeu_saques:

                    print("Operação falhou! Número máximo de saques excedido.")

                elif valor > saldo:

                    print("Operação falhou! Valor do saque é maior que o saldo!")
                
                else:
                    
                    saldo -= valor
                    extrato += f"Saque: R$ {valor:.2f}\n"
                    numero_saques += 1
                    print("Saque realizado com sucesso!")

                
    
    elif opcao == "e":

        print("=" * 20 + " EXTRATO " + "=" * 20)
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=" * 49)

    elif opcao == "q":

        print("Sessão encerrada, até logo!")
        break

    else:
        print("Operação inválida, por favor selecione operação correta.")
