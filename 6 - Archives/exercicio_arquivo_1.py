#Imagina que temos um arquivo com vários números escritos em sequência, um em cada linha.
# O conteúdo do arquivo estará da seguinte forma:

# 55.4
# 1
# 2.9
# 2
# 7.1
# -20.3

# Podendo ter mais do que só 6 números.
# Crie uma função que recebe o nome desse arquivo, e retorne a média dos números contidos no arquivo.

# Exemplo:
# Input: "arquivo_teste_01.txt" O conteúdo do arquivo sendo 1 2 3 4
# Output: 2.5

def calculaMedia(arquivo_com_notas):

    with open(arquivo_com_notas, 'r') as arquivo_notas:

        qtd_linhas = 0
        soma = 0

        for row in arquivo_notas.readlines():
            nota = float(row)
            qtd_linhas += 1
            soma += nota

            media = soma / qtd_linhas

    return media
        
media_calculada = calculaMedia(arquivo_com_notas = 'notas_alunos.txt')

print(media_calculada)
    
