#Usando o programa criado no exercício 15, crie uma lista de funcionários. Você deve pedir os dados, até que o nome digitado seja "0" (o número zero). Ao terminar de cadastrar todos os funcionários, mostre a lista.

nome = None
cadastro = {}

while True:
    nome = input("Digite o nome e finalize o cadastro. Para parar de cadastrar, digite 0: ")

    if nome == '0':
        break

    cargo = input("Digite o cargo: ")
    numero_incricao = input("Digite o número da inscrição: ")

    cadastro[nome] = cargo, numero_incricao

print(cadastro)
