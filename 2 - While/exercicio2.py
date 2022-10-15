# Faça um cadastro de pessoas que aceita os seguintes dados: nome, sobrenome, idade, gênero que se identifica, cep e pronome de tratamento. Todos os dados devem ser validados com o seguinte critério:
# nome nao pode estar em branco e tem que ter mais de 3 caracteres
# sobrenome não pode estar em branco e tem que ter mais de 3 caracteres
# idade deve ser numero acima de 18
# genero e pronome de tratamento podem estar em branco
# CEP deve ser apenas numeros


while True:
    nome = input("Digite seu nome: ")
    if (len(nome) < 3):
        print("Digite um nome válido.")
        nome = " "
        continue

    sobrenome = input("Digite seu sobrenome: ")
    if (len(sobrenome) < 3):
        print("Digite um sobrenome válido.")
        sobrenome = " "
        continue

    idade = int(input("Digite sua idade: "))
    if (idade < 18):
        print("Digite uma idade válida maior que 18 anos.")
        idade = None
        continue

    genero = input("Digite seu genero: ")

    pronome = input("Digite seu pronome de tratamento: ")

    cep = input("Digite seu cep: ")
    if (not cep.isdigit()):
        print("Digite um CEP válido.")
        cep = " "

    else:
        print("Dados válidos! Obrigado.")

    


