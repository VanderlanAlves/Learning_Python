#Crie uma função que receba uma string, e retorne se há caracteres repetidos na string.

palavra =  'abacaxi'

def caracteres_repetidos(word):
    cont = 0

    for i in range(len(word)):
        for j in range(len(word)):
            if word[i] == word[j]:
                cont += 1
                    
    if cont > len(word):
        return True

    else: 
        return False

print(caracteres_repetidos(word = palavra))