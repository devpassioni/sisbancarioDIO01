menu = ('''   
                   Para Saques [B]
                   Para Depósitos [A]
                   Para Extrato [C]
                   Para Sair [S]
    ''')



saque_limite = 500
saldo = 300
limite_saque = 3
nro_saques = 0
extrato = ""

while True:
    op = input(menu).lower()

    if op == "a":
        valor = float(input("Digite o valor a ser depositado:  "))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito de R$ {valor}\n'
        else:
            print("Erro, valor não identificado. Refaça")
    elif op == "b":
        valor = float(input("Digite o valor a ser sacado:   "))
    
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > saque_limite
        excedeu_saque = nro_saques > limite_saque

        if excedeu_saldo:
            print("Você excedeu o limite de saldo, contate o gerente para acionar o saldo de contas ou deposite mais")
        elif excedeu_limite:
            print("Você excedeu o valor destinado de limite para cada saldo")
        elif excedeu_saque:
            print("Você excedeu sua quantidade diária de saques")
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque de R$ {valor}\n'
            nro_saques += 1
        else:
            print("Erro, formato ou valor inválido!")
    elif op == "c":
        print("==================EXTRATO==================")
        print("Não foram encontradas movimentações até o momento." if not extrato else extrato)
        print(f'Saldo disponível em conta R$ {saldo}')
        print("==========================================")
    elif op == "s":
        break

    else:
        print("Operação inválida, por gentileza, recomece.")