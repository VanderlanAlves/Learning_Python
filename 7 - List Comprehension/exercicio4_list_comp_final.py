#4 Crie um código que faça uma lista de quais pessoas possuem mais de 18 anos
# no dicionário abaixo.

cadastros = {
982432: {'name': 'Clarice Barbosa', 'sex': 'F', 'idade': 101},
 929103: {'name': 'Yuri Aragão', 'sex': 'M', 'idade': 63},
 930428: {'name': 'Kaique Viana', 'sex': 'M', 'idade': 16},
 547921: {'name': 'Emilly da Luz', 'sex': 'F', 'idade': 2},
 766567: {'name': 'Guilherme Lopes', 'sex': 'M', 'idade': 58},
 514041: {'name': 'Igor Peixoto', 'sex': 'M', 'idade': 16},
 613153: {'name': 'Lívia Lima', 'sex': 'F', 'idade': 10},
 326839: {'name': 'Lucas Pinto', 'sex': 'M', 'idade': 2},
 322292: {'name': 'Maria Farias', 'sex': 'F', 'idade': 58},
 119132: {'name': 'Sr. Daniel Pinto', 'sex': 'M', 'idade': 51},
 436737: {'name': 'Dr. Ian da Conceição', 'sex': 'M', 'idade': 106},
 239127: {'name': 'Bruna Ferreira', 'sex': 'F', 'idade': 81},
 326000: {'name': 'Alícia da Luz', 'sex': 'F', 'idade': 81},
 454248: {'name': 'Sr. Leandro Sales', 'sex': 'M', 'idade': 71},
 656414: {'name': 'Benício Campos', 'sex': 'M', 'idade': 93},
 740236: {'name': 'Bianca da Rosa', 'sex': 'F', 'idade': 59},
 78234: {'name': 'Gabriela Alves', 'sex': 'F', 'idade': 14},
 811343: {'name': 'Raul Castro', 'sex': 'M', 'idade': 5},
 838719: {'name': 'Srta. Bianca Teixeira', 'sex': 'F', 'idade': 16},
 41316: {'name': 'Dra. Marcela Moreira', 'sex': 'F', 'idade': 39},
 547931: {'name': 'Daniela Alves', 'sex': 'F', 'idade': 49},
 945726: {'name': 'Pedro Lucas Rocha', 'sex': 'M', 'idade': 6},
 132689: {'name': 'Enzo Gabriel Melo', 'sex': 'M', 'idade': 110},
 368911: {'name': 'Yasmin Silveira', 'sex': 'F', 'idade': 29},
 13789: {'name': 'Francisco Carvalho', 'sex': 'M', 'idade': 24},
 286652: {'name': 'Vitor Hugo Rezende', 'sex': 'M', 'idade': 16},
 696760: {'name': 'Sophia Moreira', 'sex': 'F', 'idade': 44},
 5293: {'name': 'André da Paz', 'sex': 'M', 'idade': 71},
 452742: {'name': 'Carolina Fogaça', 'sex': 'F', 'idade': 8},
 987830: {'name': 'Joaquim Barbosa', 'sex': 'M', 'idade': 18},
 219271: {'name': 'Calebe da Mota', 'sex': 'M', 'idade': 95},
 583886: {'name': 'Giovanna Ramos', 'sex': 'F', 'idade': 8},
 322316: {'name': 'Ana Luiza Cunha', 'sex': 'F', 'idade': 3},
 731939: {'name': 'Mirella Costela', 'sex': 'F', 'idade': 76},
 396426: {'name': 'Pedro Lucas Freitas', 'sex': 'M', 'idade': 62},
 621867: {'name': 'Letícia Santos', 'sex': 'F', 'idade': 14},
 147939: {'name': 'Julia Rocha', 'sex': 'F', 'idade': 68},
 660287: {'name': 'Sra. Maria Cecília Cavalcanti', 'sex': 'F', 'idade': 66},
 680444: {'name': 'Sra. Emanuelly da Mota', 'sex': 'F', 'idade': 93},
 790899: {'name': 'Luna Fogaça', 'sex': 'F', 'idade': 100}
 }

lista_maiores_18_anos = [f"Cadastro {item[0]} - {item[1]['name']} - Idade {item[1]['idade']}" for item in cadastros.items() if item[1]['idade'] > 18]

print(lista_maiores_18_anos)