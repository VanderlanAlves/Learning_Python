# Usando funções, faça um programa que simule um hotel de animais, 
# onde tem vaga para 10 cachorros, 5 gatos e 8 capivaras. Peça o nome do animal e 
# qual animal é, e retorne se é possível hospedar o animal ou não. Se for possível 
# hospedar, guarde o nome do animal e qual animal é. Se não for possível hospedar, 
# diga "não é possível hospedar"

lista_cachorros = []
lista_gatos = []
lista_capivaras = []

opcao_inicial = -1
vaga_cachorros = 10
vaga_gatos = 5
vaga_capivaras = 8

#funcoes
def compatibilidadeAnimal(tipo_animal):
    if tipo_animal.upper() == 'CACHORRO' or tipo_animal.upper() == 'GATO' or tipo_animal.upper() == 'CAPIVARA':
        return True

    else:
        return False

def adicionarAnimal(nome, tipo_animal, vaga_cachorros, vaga_gatos, vaga_capivaras):
    if tipo_animal.upper() == 'CACHORRO':
        lista_cachorros.append(nome)
        vaga_cachorros -= 1

        return lista_cachorros

    if tipo_animal.upper() == 'GATO':
        lista_gatos.append(nome)
        vaga_gatos = vaga_gatos - 1

        return lista_gatos, vaga_gatos
    
    if tipo_animal.upper() == 'CAPIVARA':
        lista_capivaras.append(nome)
        vaga_capivaras -= 1

        return lista_capivaras

def retirarPet(tipo_animal, pet_removido, vaga_cachorros, vaga_gatos, vaga_capivaras):
    if tipo_animal.upper() == 'CACHORRO':
        for i in range(len(lista_cachorros)):
            if lista_cachorros[i] == pet_removido:
                lista_cachorros.pop(i)
        vaga_cachorros += 1

        return lista_cachorros

    if tipo_animal.upper() == 'GATO':
        for i in range(len(lista_gatos)):
            if lista_gatos[i] == pet_removido:
                lista_gatos.pop(i)
        vaga_gatos += 1

        return lista_gatos
    
    if tipo_animal.upper() == 'CAPIVARA':
        for i in range(len(lista_capivaras)):
            if lista_capivaras[i] == pet_removido:
                lista_capivaras.pop(i)
        vaga_capivaras += 1

        return lista_capivaras    
    
#logica
while opcao_inicial != '0':
    opcao_inicial = input("\nSeja bem-vindo ao Pet-Hotel! Digite 1 se gostaria de hospedar um animal, 2 se gostaria de retirar seu pet, 3 se gostaria de ver a lista dos pets hospedados ou 0 para encerrar: ")

    if opcao_inicial == '1':
        while True:
            if vaga_cachorros == 0 or vaga_gatos == 0 or vaga_capivaras == 0:
                print("Desculpe, não temos mais vagas.")
                break

            else:
                tipo_animal = input("Digite o tipo de animal: ")

                if compatibilidadeAnimal(tipo_animal):
                    opcao = input(f"\nAceitamos o tipo do seu pet no nosso hotel! Temos {vaga_cachorros} vagas para Cachorros, {vaga_gatos} vagas para Gatos e {vaga_capivaras} para Capivaras. \nDigite 1 para adicionar o pet, 0 para encerrar: ")

                    if opcao == '1':
                        nome = input("\nDigite o nome do pet: ")

                        adicionarAnimal(nome, tipo_animal, vaga_cachorros, vaga_gatos, vaga_capivaras)
                        
                        print(f"\nSeu pet foi adicionado com sucesso! Veja a lista dos nossos pets hospedados: \nCachorros: {lista_cachorros} \nGatos: {lista_gatos} \nCapivaras: {lista_capivaras}")

                        break

                    elif opcao == '0':
                        break

                    else:
                        print("\nOpção inválida.")
                        continue

                else:
                    print("\nNão é possível hospedar seu pet.")

    elif opcao_inicial == '2':
        tipo_animal = input("\nDigite o tipo de animal: ")
        pet_removido = input("\nDigite o nome do pet que gostaria de retirar: ")

        retirarPet(tipo_animal, pet_removido, vaga_cachorros, vaga_gatos, vaga_capivaras)

        print(f"\nO pet {pet_removido} fez check-out.")

    elif opcao_inicial == '3':
        print(f"\nVeja a lista dos nossos pets hospedados: \nCachorros: {lista_cachorros} \nGatos: {lista_gatos} \nCapivaras: {lista_capivaras}")

    elif opcao_inicial == '0':
        print("\nPrograma encerrado.")