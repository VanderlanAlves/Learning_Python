#Crie um programa que simule o funcionamento de uma urna eletrônica.
#Deve receber votos para presidente (2 numeros), governador (2 numeros), senador (3 numeros), deputado federal (4 numeros) e deputado estadual (5 numeros).
#Considere que a pessoa so pode digitar numeros.
#Caso a pessoa digite um quantidade de numeros inválida para o cargo, mostrar a mensagem "valor inválido, voto anulado"
#Ao final, mostre todos os votos da pessoa.

presidente = input("Voto presidente: ")
governador = input("Voto governador: ")
senador = input("Voto senador: ")
depFederal = input("Voto depFederal: ")
depEstadual = input("Voto depEstadual: ")

if (presidente.isdigit()) and ((len(presidente))==2) and (governador.isdigit()) and ((len(governador))==2) and (senador.isdigit()) and ((len(senador))==3) and (depFederal.isdigit()) and ((len(depFederal))==4) and (depEstadual.isdigit()) and ((len(depEstadual))==5):
    print(f"Seus votos foram: {presidente} para presidente, {governador} para governador, {senador} para senador, {depFederal} para depFederal e {depEstadual} para depEstadual.")

else:
    print("Digite valores válidos.")



