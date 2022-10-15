

cpf = '929278600'


def calculaDigitos(cpf):

    #calculo primeiro digito
    soma = (
    ((int(cpf[0])) * 10) + 
    ((int(cpf[1])) * 9) +
    ((int(cpf[2])) * 8) + 
    ((int(cpf[3])) * 7) + 
    ((int(cpf[4])) * 6) + 
    ((int(cpf[5])) * 5) + 
    ((int(cpf[6])) * 4) + 
    ((int(cpf[7])) * 3) + 
    ((int(cpf[8])) * 2))

    calculo = 11 - (soma % 11)

    if soma > 9:
        primeiro_digito = 0

    elif soma < 0:
        print("CPF inválido")

    else:
        

    #Cálculo segundo digito
    soma2 = (
    ((int(cpf[0])) * 11) + 
    ((int(cpf[1])) * 10) +
    ((int(cpf[2])) * 9) + 
    ((int(cpf[3])) * 8) + 
    ((int(cpf[4])) * 7) + 
    ((int(cpf[5])) * 6) + 
    ((int(cpf[6])) * 5) + 
    ((int(cpf[7])) * 4) + 
    ((int(cpf[8])) * 3) +
    (primeiro_digito * 2))

    if soma > 9:
        primeiro_digito = 0

    elif soma < 0:
        print("CPF inválido")

    else:
        primeiro_digito = 11 - (soma % 11)

    return primeiro_digito



print(calculaDigitos(cpf))


# def formataCPF(cpf):

#     cpf_formatado = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'

#     return cpf_formatado

# lista_cpfs = ['05517576397', '12345678910', '98569864353']

# lista_cpf_formatado = [formataCPF(cpf) for cpf in lista_cpfs]



# print(lista_cpf_formatado)