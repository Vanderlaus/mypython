import os
from statistics import mean

pessoas = list()
dados = dict()    

def cadastrar():
    os.system('cls')
    dados['nome'] = str(input('Digite seu nome: '))
    while True:
        dados['sexo'] = str(input('Digite seu sexo M/F: ')).upper()[0]
        if dados['sexo'] in "MF":
            break
        print("Digite uma opção valida")
    dados['idade'] = int(input('Digite sua idade: '))
    pessoas.append(dados.copy())
      
def listar():
    print(pessoas)
    
def finalizar():
    os.system('cls')
    media = mean(list(c['idade'] for c in pessoas))
    mqam = list(c for c in pessoas if c['idade'] > media)
    print(f"A) Ao todo temos {len(pessoas)} pessoas cadastradas.")
    print(f"B) A média de  idade é de {media:5.2f} anos.")
    print("C) A lista das mulheres cadastradas:")
    for m in pessoas:
        if m['sexo'] == 'F':
            for k, v in m.items():
                print(f'    {k} = {v};', end=' ')
            print()
    print(f"D) Lista das pessoas que estão cima da média:")
    for p in mqam:
        for k, v in p.items():
            print(f'    {k} = {v};', end=' ')
        print()
    print("ENCERRADO")
    
