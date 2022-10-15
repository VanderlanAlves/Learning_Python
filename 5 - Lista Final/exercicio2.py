num_pacientes = [25, 58, 110, 15, 35, 47, 65, 21,
                 34, 58, 17, 59, 31, 24, 47, 49, 28,
                 56, 23, 27, 34, 59, 97, 31, 17, 5,
                 12, 68, 23, 124, 25, 39, 49]

# Eu quero uma lista com o número de pacientes de todos os dias
# cuja quantidade foi menor que 40
lista_menor_40 = [n for n in num_pacientes if n < 40]
print(lista_menor_40)

# Eu quero a média de todas as quantidades de pacientes
# ímpares.
listaImpares = [n for n in num_pacientes if n % 2 != 0]

media = sum(listaImpares) / len(listaImpares)
print(media)

# Eu quero uma lista com OS DIAS (assume que a lista começa do dia 1)
# nos quais o número de pacientes foi maior que 50
lista = (list(enumerate(num_pacientes)))
print(lista)


print(lista[0][1])