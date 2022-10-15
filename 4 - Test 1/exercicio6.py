# Defina uma função que recebe 5 palavras e retorne uma lista com as palavras em ordem de tamanho da palavra.

listaPalavras = []
listaOrdenada = []

for i in range(1, 6):
    palavra = input("Digite uma palavra: ")

    listaPalavras.append(palavra)

listaOrdenada = sorted(listaPalavras, key = len)
print(listaOrdenada)
