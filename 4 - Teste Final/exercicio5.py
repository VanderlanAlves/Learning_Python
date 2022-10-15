# Crie um programa que simule um caixa eletrônico. O que precisa implementar:
# Depósito
# Saque
# Pagamento de conta
# Listagem de movimentações (extrato)

listaMovimentacoes = []
saldo = 0
entrada = None

print("\nBem-vindo ao banco Vanderlan!\n")

while entrada != '0':
    print("Opções: ")
    print("Opção 0 - Sair")
    print("Opção 1 - Depósito")
    print("Opção 2 - Saque")
    print("Opção 3 - Pagar conta")
    print("Opção 4 - Extrato")

    entrada = input("\nDigite a opção desejada: ")

    if entrada == '1':
        deposito = float(input("Digite quanto você quer depositar: "))
        saldo = saldo + deposito
        print(f"\nDepósito realizado com sucesso! Seu saldo agora é de R${saldo:.02f}\n")
        listaMovimentacoes.append(deposito)

    if entrada == '2':
        saque = float(input("Digite quanto você quer sacar: "))
        saque = saque*(-1)
        saldo = saldo + saque
        print(f"\nSaque realizado com sucesso! Seu saldo agora é de R${saldo:.02f}\n")
        listaMovimentacoes.append(saque)

    if entrada == '3':
        pagamento = float(input("Digite quanto você quer pagar: "))
        pagamento = pagamento*(-1)
        saldo = saldo + pagamento
        print(f"\nPagamento realizado com sucesso! Seu saldo agora é de R${saldo:.02f}\n")
        listaMovimentacoes.append(pagamento)

    if entrada == '4':
        print(f"\nA lista do seu extrato é: {listaMovimentacoes}\n")

print("\nVocê saiu do banco Vanderlan. Obrigado!")