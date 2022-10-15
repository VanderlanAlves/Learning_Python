#Faça um programa que recebe uma frase e mostra quantas palavras a frase tem.
contador = 1

frase = ' uma frase bonita inspiradora '
frase_strip = frase.strip()

for i in frase_strip:
    if i == ' ':
        contador += 1

print(f"Há {contador} palavras na frase.")