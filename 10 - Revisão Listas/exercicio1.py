populacao = 2
cont = 0
lista_coelhos = []

for n in range(1, 8):
    cont += 1

    if cont == 3:
        populacao = populacao - 4
        cont = 0

    else:
        populacao = populacao * 2

    lista_coelhos.append(populacao)

print(lista_coelhos)