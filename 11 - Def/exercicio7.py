#Crie uma função que receba uma quantidade qualquer de números, e retorne a média dos números.
# O nome da funcao deve ser media_nums.
# Desafio: Tente fazer com que, se você rodar a função sem nenhuma entrada, ela retorne o valor 0.

def media_nums(*args):

    if args != ():
        media = sum(args) / len(args)

        return media

    else:
        return 0.0

print(media_nums())