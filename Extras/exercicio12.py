# Faça um programa que peça o nome de um aluno, depois cada uma das quatro disciplinas 
# (matematica, portugues, ciências e comunicação) e depois as 4 notas da prova daquela disciplina. 
# Mostre depois a média de cada disciplina. 
# 
# Se as quatro médias forem acima de 6, 
# mostre a frase "aprovado". Caso uma das médias for abaixo de 6, 
# mostrar a frase "reprovado na matéria (nome da matéria)", para cada uma das 
# matérias com média abaixo do esperado.

notas_matematica = []
notas_portugues = []
notas_ciencias = []
notas_comunicacao = []

aluno = input("Digite o nome do aluno: ")

for i in range(1, 4):
    nota = float(input(f"Digite o valor da nota {i} de Matemática: "))
    notas_matematica.append(nota)

for i in range(1, 4):
    nota = float(input(f"Digite o valor da nota {i} de Português: "))
    notas_portugues.append(nota)

for i in range(1, 4):
    nota = float(input(f"Digite o valor da nota {i} de Ciências: "))
    notas_ciencias.append(nota)    

for i in range(1, 4):
    nota = float(input(f"Digite o valor da nota {i} de Comunicacão: "))
    notas_comunicacao.append(nota)

media_portugues = sum(notas_portugues) / len(notas_portugues)
media_matematica = sum(notas_matematica) / len(notas_matematica)
media_ciencias = sum(notas_ciencias) / len(notas_ciencias)
media_comunicacao = sum(notas_comunicacao) / len(notas_comunicacao)

if media_ciencias < 6:
    print(f"Reprovado em Ciências com média {media_ciencias:.02f}.")

if media_matematica < 6:
    print(f"Reprovado em Matemática com média {media_matematica:.02f}.")

if media_comunicacao < 6:
    print(f"Reprovado em Comunicacão com média {media_comunicacao:.02f}.")

if media_portugues < 6:
    print(f"Reprovado em Português com média {media_portugues:.02f}.")

if media_ciencias >= 6 and media_portugues >= 6 and media_comunicacao >= 6 and media_matematica >= 6:
    print(f"Aprovado em todas as matérias! Parabéns! \nPortuguês com média {media_portugues:.02f} \nComunicacão com média {media_comunicacao:.02f} \nMatemática com média {media_matematica:.02f} \nCiências com média {media_ciencias:.02f}")

