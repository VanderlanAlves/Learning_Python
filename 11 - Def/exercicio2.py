#Crie uma função que checa se a palavra dada (com as letras todas em minúsculas), é um palíndromo.

palavra = 'reviver'

def checar_palindromo(word):
    if word[::-1] == word:
        return True
    
    else: 
        return False

print(checar_palindromo(word = palavra))