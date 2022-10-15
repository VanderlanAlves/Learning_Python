# Faça um programa que registre um pedido de um cliente. O cliente pode escrever, de forma livre, mas um por vez, a entrada, o prato principal, a bebida e se quer sobremesa. Caso queira a sobremesa, pedir para que digite. No final, mostre o pedido completo em letras maiúsculas, um item por linha.

print("Bem-vindo ao restaurante!\n")
entrada = input("Digite a entrada: ")
pratoPrincipal = input("Digite o prato principal: ")
bebida = input("Digite a bebida: ")

opcaoSobremesa = input("Você gostaria de pedir sobremesa? S/N: ")

if opcaoSobremesa.upper() == 'S':
    sobremesa = input("Digite a sobremesa :")

    print(f"Seu pedido é: \n'{entrada.upper()}', \n'{pratoPrincipal.upper()}', \n'{bebida.upper()}', \n'{sobremesa.upper()}'.")

else: 
    print(f"Seu pedido é: \n'{entrada.upper()}', \n'{pratoPrincipal.upper()}', \n'{bebida.upper()}'.")



