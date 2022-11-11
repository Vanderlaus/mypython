from pessoa import Pessoa

print('*'*25,'CABEÇALHO','*'*25)
print('Pessoa 1')
pessoa = Pessoa(str(input('Digite o nome:> ')),str(input('Digite o CPF:> ')),int(input('Digite a idade:> ')),float(input('Digite a altura:> ')))

print('A pessoa {} portador do CPF {} tem {} anos e possui {}m de altura.\n'.format(Pessoa.get_nome(pessoa),Pessoa.get_cpf(pessoa),Pessoa.get_idade(pessoa),Pessoa.get_altura(pessoa)))

print('Pessoa 2:')
pessoa2 = Pessoa(str(input('Digite o nome:> ')),str(input('Digite o CPF:> ')),int(input('Digite a idade:> ')),float(input('Digite a altura:> ')))

print('A pessoa {} portador do CPF {} tem {} anos e possui {}m de altura.\n'.format(Pessoa.get_nome(pessoa2),Pessoa.get_cpf(pessoa2),Pessoa.get_idade(pessoa2),Pessoa.get_altura(pessoa2)))