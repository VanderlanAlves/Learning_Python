# Crie um programa que peça a um usuário o nome de um produto, a quantidade e o preço, e no final mostre o valor total a pagar. Depois de mostrar o valor a pagar, pergunte como será o pagamento, e mostre as opções "dinheiro", "cartão" ou "pix".
# Se for dinheiro, dar um desconto de 5%, se for pix um desconto de 9.5%, e se for cartão não tem desconto.

while True:
    nomeProduto = input("Digite o nome do produto: ")
    quantidadeProduto = int(input("Digite a quantidade: "))
    precoProduto = float(input("Digite o preco: "))

    total = quantidadeProduto * precoProduto

    formaPagto = input("Digite a forma de pagamento: Pix, Dinheiro ou Cartao: ")

    if formaPagto != 'Pix' and formaPagto != 'Dinheiro' and formaPagto != 'Cartao':
        print("Por favor, digite uma forma de pagamento válida.")
        continue

    if formaPagto == 'Pix':
        descontoPix = 0.905
        totalPix = total * descontoPix
        print(f"O valor total do Pix após o desconto é de R$ {totalPix:.02f}.")
    
    elif formaPagto == 'Dinheiro':
        descontoDinheiro = 0.95
        totalDinheiro = total * descontoDinheiro
        print(f"O total para pagamento em dinheiro é de R$ {totalDinheiro:.02f}.")

    else:
        print(f"Com cartão, você pagará R$ {total:.02f}.")


