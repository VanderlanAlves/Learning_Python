# Crie uma lista com 5 nomes de pessoas, 5 sobrenomes, e exiba os 25 nomes completos que podem surgir dos cruzamentos entre nomes e sobrenomes

lista1 = ["Abel", "Jorge", "Jorjana", "Luis", "Carlos"]
lista2 = ["Alves", "Almeida", "Sousa", "Feuers", "Silva"]

for i in range(len(lista1)):
    for j in range(len(lista2)):
        print(f"{lista1[i]} {lista2[j]}")