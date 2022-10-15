# Faça um jogo de adinhação para duas pessoas. A primeira digita um número, e a segunda vai digitar esse número. Cada vez que a segunda pessoa digitar uma resposta, o programa deve dizer e é maior ou menor que o numero a ser descoberto, ou se acertou. No caso de ter acertado, mostrar em quantas tentativas houve o acerto.

import random

numeroADescobrir = random.choice(range(0,101))
print(numeroADescobrir)
contador = 0

while True:
    contador = contador + 1
    numeroDigitado = int(input("Digite um número: "))

    if numeroDigitado != numeroADescobrir:
        if numeroDigitado < numeroADescobrir:
            print("Aumente um pouco mais")
            continue
        elif numeroDigitado > numeroADescobrir:
            print("Diminua um pouco")
            continue
    else:
        print(f"Você acertou com {contador} tentativas!")
        break

