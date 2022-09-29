pessoas = [
    {"nome": 'João Vitor de Jesus Casali', "cpf": '052.827.732-44', "genero": "Masculino"},
    {"nome": 'Thiago França', "cpf": '052.897.322-44', "genero": "Feminino"},
    {"nome": 'Vander fi do Vander', "cpf": '321.927.732-54', "genero": "Masculino"},
    {"nome": 'Luiza chata', "cpf": '121.987.542-54', "genero": "Feminino"}
]

tamanhoColunas = [0, 0, 0]

for pessoa in pessoas:
    if len(pessoa['nome']) > tamanhoColunas[0]:
        tamanhoColunas[0] = len(pessoa['nome']) + 2

    if len(pessoa['cpf']) > tamanhoColunas[1]:
        tamanhoColunas[1] = len(pessoa['cpf']) + 2
    
    if len(pessoa['genero']) > tamanhoColunas[2]:
        tamanhoColunas[2] = len(pessoa['genero']) + 2

print('-'*(sum(tamanhoColunas)+4))
print('|', end='')

for i, nome in enumerate(pessoas[0].keys()):
    print(f"\033[1;32m{nome.upper()}\033[0;0m".center(tamanhoColunas[i] + 13, " "), end='')
    print('|', end='')

print('\n' + '-'*(sum(tamanhoColunas)+4))

for pessoa in pessoas:
    print(f"|{pessoa['nome'].center(tamanhoColunas[0], ' ')}|", end='')
    print(f"{pessoa['cpf'].center(tamanhoColunas[1], ' ')}|", end='')
    print(f"{pessoa['genero'].center(tamanhoColunas[2], ' ')}|")
    print('-'*(sum(tamanhoColunas)+4))