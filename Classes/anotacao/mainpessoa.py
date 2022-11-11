from pessoa import Pessoa

def menu():
    poli = "="*70
    espaco = " "*29
    print(f"{poli}\n{espaco}MENU PESSOA{espaco}\n{poli}")
    print(f"Cadastre a Pessoa")

    print(poli)
    print('Pessoa 1:')
    pessoa = Pessoa(str(input('Digite o nome:> ')),str(input('Digite o CPF:> ')),int(input('Digite a idade:> ')),float(input('Digite a altura:> ')))

    print(poli)
    print('Pessoa 2:')
    pessoa2 = Pessoa(str(input('Digite o nome:> ')),str(input('Digite o CPF:> ')),int(input('Digite a idade:> ')),float(input('Digite a altura:> ')))

    print()
    print('A pessoa {} portador do CPF {} tem {} anos e possui {}m de altura.\n'.format(pessoa.nome,pessoa.cpf,pessoa.idade,pessoa.altura))
    print('A pessoa {} portador do CPF {} tem {} anos e possui {}m de altura.\n'.format(pessoa2.nome,pessoa2.cpf,pessoa2.idade,pessoa2.altura))
    print()

menu()