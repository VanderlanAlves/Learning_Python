# Crie uma função que receba vários argumentos nomeados (que devem ser strings), e
# retorne duas strings:
# Uma formada pelos valores dos argumentos
# Outra formada pelos nomes dos argumentos

def formata_string(**kwargs):
    string_chaves = ""
    string_valores = ""

    #fazer lista com as chaves
    lista_chaves = [chave for chave in kwargs.keys()]

    #inserir cada chave na string
    for chave in lista_chaves:
        string_chaves += f"{chave}"

    #fazer lista com os valores
    lista_valores = [valor for valor in kwargs.values()]

    #inserir cada valor na string
    for valor in lista_valores:
        string_valores += f"{valor}"

    #retorno da funcao
    return string_chaves, string_valores

print(formata_string(a = "Comunidados", b = "Muito", c = "Boa"))