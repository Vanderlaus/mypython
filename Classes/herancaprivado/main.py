from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica

pessoa_fisica = PessoaFisica('Vander','03281099912',5000.0)

print('\n','-='*10, 'Menu Pessoa Fisica Inicial', '-='*10)
print(pessoa_fisica)

pessoa_fisica.segundo_titular = '2º titular'

print('\n','-='*10, 'Menu Pessoa Fisica com Alterações', '-='*10)
print(pessoa_fisica)

      
pessoa_juridica = PessoaJuridica('Vll Negocios','84375849000130',15000.0)
print('\n','-='*10, 'Menu Pessoa Juridica Inicial', '-='*10)
print(pessoa_juridica)

pessoa_juridica.segundo_titular = '2º titular'

print('\n','-='*10, 'Menu Pessoa Juridica com Alterações', '-='*10)
print(pessoa_juridica)

