# Altere o programa do exercício 07, verificando se o valor do produto é maior que zero e se 
# a quantidade de itens é maior que zero. Caso seja zero, mostre uma mensagem de erro e peça o
#  valor novamente, até o valor ser digitado corretamente

while True:
    nome_produto = input("Digite o nome do produto: ")

    valor_unitário = float(input("Digite o valor unitário do produto: "))

    qtd_itens = int(input("Digite a quantidade de items comprados: "))

    if valor_unitário <= 0 or qtd_itens <= 0:
        print("Quantidade ou valor inválido. Tente novamente.")
        continue

    saida = "O valor de {produto} é igual a R${valor}."

    print(saida.format(produto = nome_produto, valor = valor_unitário * qtd_itens))