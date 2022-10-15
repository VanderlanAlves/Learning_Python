# Repita o problema da questão 5, mas agora, permita que a sua função monta_tabuleiro possa receber dois parâmetros extras:
# digito_branco, que define qual inteiro representa a cor branca
# digito_preto, que define qual inteiro representa a cor preta.

largura = 4
digito_branco = 9
digito_preto = 6
linha_normal = []
linha_invertida = []
tabuleiro_completo = []

def monta_tabuleiro(width, white_digit, black_digit):
    #montando a lista
    for i in range(width, 0, -1):

        #linhas normais
        if i % 2 == 0:
            linha_normal.append(black_digit)
        
        else:
            linha_normal.append(white_digit)

        #linhas invertidas:
        linha_invertida = linha_normal[::-1]

    #inserindo linhas no tabuleiro
    for j in range(0, (width // 2)):
        tabuleiro_completo.append(linha_normal)
        tabuleiro_completo.append(linha_invertida)

    return tabuleiro_completo

#apresentando o tabuleiro :)
for row in monta_tabuleiro(width = largura, white_digit = digito_branco, black_digit = digito_preto):
    print(row)    