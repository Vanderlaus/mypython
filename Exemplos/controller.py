#funcao list() para criar lista e dict() para criar dicionário
funcionario = list()
dados = dict()

def cadastrar():
    dados["nome"] = input('Digite seu nome: ').strip().capitalize()
    dados["anonas"] = int(input('Ano de Nascimento: '))
    while True:
        dados["carteira"] = str(input('Digite sua carteira de trabalho: '))
        if dados["carteira"] != "":
            dados["anocont"] = int(input('Digite o ano da contratação: '))
            dados["salario"] = float(input('Digite seu salário: '))
            break
        else:
            break
    funcionario.append(dados)
      
def listar():
    print('-'*35, 'Dados Funcionarios', '-'*35)
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

    