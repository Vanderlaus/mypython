pessoas = []

def cadastrar():
    dados = {}
    dados["nome"] = str(input('Digite seu nome: '))
    dados["sexo"] = int(input('Digite seu Sexo\n1-Masculino\n2-Feminino: '))
    dados["idade"] = int(input('Idade: '))
    pessoas.append(dados)
      
def listar():
    print(pessoas)