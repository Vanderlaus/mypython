from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica

pessoa_fisica = PessoaFisica('Vander','03281099912',5000.0)

print('\n','-='*10, 'Menu Pessoa Fisica Inicial', '-='*10)
print('Conta número:> {}\n''Tipo conta:> {}\n''Titular:> {}\n''CPF:> {}\n''Saldo Inicial:> {}\n''Segundo Titular:> {}'.format(pessoa_fisica.numero,pessoa_fisica.tipo,pessoa_fisica.titular,pessoa_fisica.cpf,pessoa_fisica.saldo_inicial,pessoa_fisica.segundo_titular))

pessoa_fisica.segundo_titular = '2º titular'

print('\n','-='*10, 'Menu Pessoa Fisica com Alterações', '-='*10)
print('Conta número:> {}\n''Tipo conta:> {}\n''Titular:> {}\n''CPF:> {}\n''Saldo Inicial:> {}\n''Segundo Titular:> {}'.format(pessoa_fisica.numero,pessoa_fisica.tipo,pessoa_fisica.titular,pessoa_fisica.cpf,pessoa_fisica.saldo_inicial,pessoa_fisica.segundo_titular))
      
pessoa_juridica = PessoaJuridica('Vll Negocios','84375849000130',15000.0)
print('\n','-='*10, 'Menu Pessoa Juridica Inicial', '-='*10)
print('Conta número:> {}\n''Tipo conta:> {}\n''Titular:> {}\n''CNPJ:> {}\n''Saldo Inicial:> {}\n''Segundo Titular:> {}'.format(pessoa_juridica.numero,pessoa_juridica.tipo,pessoa_juridica.titular,pessoa_juridica.cnpj,pessoa_juridica.saldo_inicial,pessoa_juridica.segundo_titular))

pessoa_juridica.segundo_titular = '2º titular'

print('\n','-='*10, 'Menu Pessoa Juridica com Alterações', '-='*10)
print('Conta número:> {}\n''Tipo conta:> {}\n''Titular:> {}\n''CNPJ:> {}\n''Saldo Inicial:> {}\n''Segundo Titular:> {}'.format(pessoa_juridica.numero,pessoa_juridica.tipo,pessoa_juridica.titular,pessoa_juridica.cnpj,pessoa_juridica.saldo_inicial,pessoa_juridica.segundo_titular))