# Crie um código que recebe

# uma lista de nomes de alunos,
# uma lista de tuplas, com 4 números cada tupla, representando as notas de cada aluno,
# o nome de um aluno,
# e retorna a tupla que representa as 4 notas daquele aluno.

lista_alunes = ["José", "Maria", "João"]
lista_notas = [(8, 7, 8, 8), (9, 10, 10, 9.5), (6, 7.8, 6.9, 7.2)]
alune = "Maria"

alunos_e_notas = list(zip(lista_alunes, lista_notas))

def notas_aluno(nome_aluno = alune):
    for item in alunos_e_notas:
        if item[0] == nome_aluno:
            return item[1]

print(f"As 4 notas de {alune} são: {notas_aluno()}.")
    

