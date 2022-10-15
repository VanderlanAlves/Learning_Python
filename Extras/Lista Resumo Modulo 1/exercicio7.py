#Faça um programa que peça o nome de um produto, o valor unitário, a quantidade de itens comprados, 
# e mostre o valor total a pagar

nome_produto = input("Digite o nome do produto: ")

valor_unitário = float(input("Digite o valor unitário do produto: "))

qtd_itens = int(input("Digite a quantidade de items comprados: "))

saida = "O valor de {produto} é igual a R${valor}."

print(saida.format(produto = nome_produto, valor = valor_unitário * qtd_itens))