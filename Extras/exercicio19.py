#Defina uma função que calcula um desconto em um preço. Para isso ela deve receber dois numeros,
#  o preço inicial e a porcentagem de desconto. A função deve retornar o preço com o desconto 
# aplicado.

def calculaDesconto(preco_inicial, porcentagem_desconto):
    preco_final = (preco_inicial * (1 - (porcentagem_desconto / 100)))
    return preco_final

preco = float(input("Digite o preço inicial: "))
porcentagem = float(input("Digite a porcentagem do desconto: "))

print(f"O valor após o desconto é de R${calculaDesconto(preco_inicial=preco, porcentagem_desconto=porcentagem):.02f}.")