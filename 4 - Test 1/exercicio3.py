# Faça um programa que pede uma lista de palavras (pelo menos dez) para o usuário, que deve digitar uma por vez, e depois mostre 4 listas:
# palavras que começam com vogal,
# palavras que começam com consoantes,
# palavras que terminam com vogal, e
# palavras que terminam em consoantes

comecoVogal = []
comecoConsoante = []
finalVogal = []
finalConsoante = []

for i in range(1, 11):
    nome = input("Digite um nome: ")

    if (nome[0].lower() == 'a') or (nome[0].lower() == 'e') or (nome[0].lower() == 'i') or (nome[0].lower() == 'o') or (nome[0].lower() == 'u'):
        comecoVogal.append(nome)

    else:
        comecoConsoante.append(nome)

    if (nome[-1].lower() == 'a') or (nome[-1].lower() == 'e') or (nome[-1].lower() == 'i') or (nome[-1].lower() == 'o') or (nome[-1].lower() == 'u'):
        finalVogal.append(nome)

    else:
        finalConsoante.append(nome)


print(f"As palavras que começam com vogal são: {comecoVogal}")
print(f"As palavras que começam com consoantes são: {comecoConsoante}")
print(f"As palavras que terminam com vogal são: {finalVogal}")
print(f"As palavras que terminam em consoantes são: {finalConsoante}")
