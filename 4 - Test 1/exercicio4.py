#Crie duas listas com 20 números não iguais, e depois crie uma função que recebe as duas listas e retorna uma lista com os 25 maior números, em ordem inversa

lista1 = list(range(1, 1000, 2))[:21]
lista2 = list(range(2, 1000, 5))[:21]

print(lista1)
print(lista2)

lista1.extend(lista2)

novaLista = sorted(lista1, reverse=True)

print(novaLista[:25])