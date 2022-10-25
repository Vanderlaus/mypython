import os

alunos = list()
dados = dict()  

def cadastrar():
    os.system('cls')
    dados['nome'] = str(input('Digite seu nome: '))
    dados['nota1'] = float(input('Digite a nota 1: '))
    dados['nota2'] = float(input('Digite a nota 2: '))
    dados['nota3'] = float(input('Digite a nota 3: '))
    dados['media'] = (dados['nota1'] + dados['nota2'] + dados['nota3']) / 3
    
def resultado():
    os.system('cls')
    print("O aluno {} teve as seguintes notas:\nNota1: {:.2f}\nNota2: {:.2f}\nNota3: {:.2f}\nObteve uma média de {:.2f}".format(dados["nome"],dados["nota1"],dados["nota2"],dados["nota3"],dados["media"]))
    print()
    if dados["media"] > 7.00:
        print("Aluno foi APROVADO")
    else:
        print("Aluno foi REPROVADO")
    