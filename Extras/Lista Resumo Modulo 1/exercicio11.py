#Faça um programa que simule um caixa de supermercado. Você deve entrar com o nome do produto,
#  o preço do produto, e a quantidade de unidades compradas. Ao final, deve mostrar a lista de 
# produtos, o preço total do produto e o valor total da compra. Os preços e quantidades devem ser
#  informados com casas decimais. 

lista_produto = []
lista_valores = []
lista_qtd_itens = []
opcao = 'S'

while opcao.upper() != 'N':
    nome_produto = input("Digite o nome do produto: ")

    valor_unitário = float(input("Digite o valor unitário do produto: "))

    qtd_itens = float(input("Digite a quantidade de items comprados: "))

    preco = qtd_itens * valor_unitário

    opcao = input("Deseja adicionar mais itens? S/N: ")

    if valor_unitário <= 0 or qtd_itens <= 0:
        print("Quantidade ou valor inválido. Tente novamente.")
        continue

    else: 
        lista_produto.append(nome_produto)
        lista_valores.append(preco)

preco_total = sum(lista_valores)
lista_total = list(zip(lista_produto, lista_valores))

#Print Final
for item in lista_total:
    print(f'Produto: {item[0]}, preço total do produto: {item[1]}')
    
print(f'Preço total da compra: R${preco_total:.02f}')    










#saida = "O valor de {produto} é igual a R${valor}."

#print(saida.format(produto = nome_produto, valor = valor_unitário * qtd_itens))