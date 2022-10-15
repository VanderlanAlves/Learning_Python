#A partir do dicionário regiao_SP, que está com os dados do IBGE, 
# qual dos comandos abaixo podemos usar para pegar a região do país 
# onde se encontra o município de São Paulo?

regiao_SP = {
  "id":35061,
  "nome":"São Paulo",
  "mesorregiao":{
     "id":3515,
     "nome":"Metropolitana de São Paulo",
     "UF":{
        "id":35,
        "sigla":"SP",
        "nome":"São Paulo",
        "regiao":{
           "id":3,
           "sigla":"SE",
           "nome":"Sudeste"
        }
     }
  }
}

print(regiao_SP['mesorregiao']['UF']['regiao']['nome'])