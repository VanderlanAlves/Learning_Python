#Eu quero fazer um tabuleiro com cores preto e branco, xadrez, mas usando listas. Esse tabuleiro sempre será quadrado.
# A cor preta será representada pelo dígito 1, e a cor branca será representada pelo dígito 0.
# Assim, quando temos um dígito 1, todos os digitos ao seu redor (acima, abaixo, na esquerda e na direita) devem ser o dígito 0, e vice versa.
# O seu objetivo é montar uma função com o nome monta_tabuleiro, que recebe a largura do tabuleiro, e retorna o tabuleiro. Lembrando que os dois lados do tabuleiro terão mesmo tamanho.
# Assuma que a casa no canto superior esquerdo será sempre o dígito 1.
# Abaixo seguem alguns exemplos do comportamento esperado da sua função.

largura = 8
linha_normal = []
linha_invertida = []
tabuleiro_completo = []

def monta_tabuleiro(width):
    #montando a lista
    for i in range(width, 0, -1):

        #linhas normais
        if i % 2 == 0:
            linha_normal.append(1)
        
        else:
            linha_normal.append(0)

        #linhas invertidas:
        linha_invertida = linha_normal[::-1]

    #inserindo linhas no tabuleiro
    for j in range(0, (width // 2)):
        tabuleiro_completo.append(linha_normal)
        tabuleiro_completo.append(linha_invertida)

    return tabuleiro_completo

#apresentando o tabuleiro :)
for row in monta_tabuleiro(width = largura):
    print(row)    

    
