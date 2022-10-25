funcionario = []

def cadastrar():
    dados = {}
    dados["nome"] = str(input('Digite seu nome: '))
    dados["anonas"] = str(input('Ano de Nascimento: '))
    while True:
        dados["carteira"] = str(input('Digite sua carteira de trabalho: '))
        if dados["carteira"] != "":
            dados["anocont"] = str(input('Digite o ano da contratação: '))
            dados["salario"] = str(input('Digite seu salário: '))
            break
        else:
            print(funcionario)
            break
    funcionario.append(dados)
      
def listar():
    print(funcionario)