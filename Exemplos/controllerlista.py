pessoas = []

def cadastrar():
    dados = {}
    dados["nome"] = str(input('Digite seu nome: '))
    dados["sexo"] = int(input('Digite seu sexo\n1-Masculino\n2-Feminino\n=>'))
    dados["idade"] = int(input('Digite sua idade: '))
    pessoas.append(dados)
      
def listar():
    print(pessoas)
    
