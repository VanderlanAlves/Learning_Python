# #Uma escola nos contratou para desenvolver um sistema que a ajude a monitorar o rendimento de seus(suas) alunos(as).
# O nosso time de desenvolvedores preparou o banco de dados e montou uma API que nos retorna as notas de cada aluno(a) de uma turma na forma de 
# um dicionário.
# A API só retorna as últimas 4 notas, como uma lista.
# Assim, essa API nos retorna sempre um dicionário onde a chave é o nome do(a) aluno(a), e o valor é uma lista com 4 números inteiros.
# Escreva um código que pegue a média das quatro notas de um aluno, dado o seu nome. Seu código deve dar um print em uma mensagem que apresente o resultado.
# Após isso, escreva um código que pegue a média geral da turma em cada uma das quatro provas, separadamente. (Ou seja, o resultado será uma média na
#  prova 1, uma segunda média na prova 2, uma terceira média na prova 3, e uma quarta média na prova 4)
# Seu código deve dar um print em uma mensagem que apresente uma lista com os quatro valores.

notas_alunos = {
    'Ana Beatriz Moura':[8, 8, 9, 5],
    'Bernardo Moraes':[6, 6, 7, 6],
    'Bruna da Paz':[4, 3, 5, 2],
    'Bárbara Teixeira':[5, 6, 7, 4],
    'Carolina Araújo':[0, 0, 0, 2],
    'Clara Melo':[4, 2, 1, 4],
    'Samuel Silva':[3, 5, 1, 6],
    'Camila Ramos':[1, 1, 0, 0],
    'Esther da Conceição':[8, 8, 4, 8],
    'Guilherme Costela':[0, 1, 0, 0],
    'Isabelly Nunes':[9, 7, 9, 9],
    'Joana da Costa':[5, 1, 0, 1],
    'Maria Julia Gonçalves':[4, 3, 2, 1],
    'Nina Moreira':[5, 7, 9, 8],
    'Pietra Cardoso':[5, 5, 8, 9],
    'Samuel Pires':[6, 7, 4, 3],
    'Bryan Gonçalves':[3, 5, 5, 7],
    'Sophie Novaes':[1, 6, 1, 3],
    'Vitória Farias':[7, 3, 5, 6],
    'Yago Cavalcanti':[0, 5, 5, 1],
}

#funcao media aluno
def calcula_media_aluno(nome_aluno):
    
    media_aluno = sum(nome_aluno) / len(nome_aluno)

    return media_aluno

#funcao media provas
def calcula_media_provas(lista_notas_alunos):
        notas_P1 = [lista_notas_alunos[0] for lista_notas_alunos in lista_notas_alunos.values()]
        media_P1 = sum(notas_P1) / len(notas_P1)

        notas_P2 = [lista_notas_alunos[1] for lista_notas_alunos in lista_notas_alunos.values()]
        media_P2 = sum(notas_P2) / len(notas_P2)

        notas_P3 = [lista_notas_alunos[2] for lista_notas_alunos in lista_notas_alunos.values()]
        media_P3 = sum(notas_P3) / len(notas_P3)

        notas_P4 = [lista_notas_alunos[3] for lista_notas_alunos in lista_notas_alunos.values()]
        media_P4 = sum(notas_P4) / len(notas_P4)

        return media_P1, media_P2, media_P3, media_P4 

#logica
while True:
    opcao = input("\n--------- OPÇÕES --------- \n1 - Ver média de um aluno \n2 - Ver média das provas aplicadas \n3 - Encerrar o programa \n\nOpção: ")

    if opcao == '1':
        #pegando o nome do aluno:
        entrada_aluno = input("Digite o nome do aluno para calcular sua média: ")
        aluno = notas_alunos.get(entrada_aluno, "Não há este aluno na lista")

        #verificando se pode rodar a função:
        if type(aluno) is list:
            print(f"A média das 4 notas de {entrada_aluno} é {calcula_media_aluno(nome_aluno = aluno):.02f}.")

        else:
            print(aluno)
    
    elif opcao == '2':
        nota_P1, nota_P2, nota_P3, nota_P4 = calcula_media_provas(lista_notas_alunos = notas_alunos)
        print(f"A nota média da P1 é {nota_P1:.02f} \nA nota média da P2 é {nota_P2:.02f} \nA nota média da P3 é {nota_P3:.02f} \nA nota média da P4 é {nota_P4:.02f}")

    elif opcao == '3':
        break

    else:
        print("Comando inválido.")
        continue






