# Faça um programa que pede um nome, um cargo, um número de inscrição, e crie um 
# dicionário com estes dados. Mostre o dicionário usando print

lista_funcionarios = []
lista_nomes = []
lista_cargos = []
lista_inscricao = []
funcionarios = {}

for n in range(0, 2):
    nome = input("Digite um nome: ")
    lista_nomes.append(nome)

    cargo = input("Digite um cargo: ")
    lista_cargos.append(cargo)

    num_inscricao = input("Digite um número de inscricao: ")
    lista_inscricao.append(num_inscricao)

lista_cargo_inscricao = list(zip(lista_cargos, lista_inscricao))

for i in range(0, 2):
    funcionarios[lista_nomes[i]] = lista_cargo_inscricao[i]

print(funcionarios)

#lista_funcionarios = list(zip(lista_nomes, lista_cargos, lista_inscricao)) - TRANSFORMA EM TUPLA
#funcionarios = dict(lista_funcionarios) - COLOCA DENTRO DO DICT