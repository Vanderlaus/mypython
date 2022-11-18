from model.pessoaFisica import PessoaFisica
from model.pessoaJuridica import PessoaJuridica

from controller.juridico import create_pj, read_pj
from controller.fisico import create_psf, read_psf

def menu():
    menu = 1
    while(menu!=0):
        
        print('*'*25,'CADASTRO DE CONTAS','*'*25)
        print('\nDigite a opção desejada')
        menu_inicial = int(input("\n1.Pessoa Física\n2.Pessoa Juridica\n:> "))
        
        match menu_inicial:
            case 1:
                print('*'*20,'CADASTRO DE CONTA PESSOA FÍSICA','*'*20)
                
                print('\nDigite a opção desejada')
                
                menu = int(input('\n1.Cadastrar Conta\n2.Listar Conta\n0.Sair do Programa\n:> '))
                
                match menu:
                    
                    case 1:
                        conta = PessoaFisica()
                        conta.titular = input('Digite o titular da conta:> ')
                        conta.cpf = input('Digite o CPF:> ')
                        conta.saldo_inicial = input('Digite o saldo inicial:> ')
                        
                        condicao = input('Deseja cadastrar o segundo titular? digite sim/nao :>')
                        if condicao == 'sim':
                            conta.segundo_titular = input('Digite o segundo titular:> ')
                        create_psf(conta)
                    case 2:
                        read_psf()

            case 2:
                print('*'*20,'CADASTRO DE CONTA PESSOA JURÍDICA','*'*20)
                print('\nDigite a opção desejada')
                menu = int(input('\n1.Cadastrar Conta\n2.Listar Conta\n0.Sair do Programa\n:> '))
                match menu:
                    case 1:
                        conta = PessoaJuridica()
                        conta.titular = input('Digite o titular da conta:> ')
                        conta.cnpj = input('Digite o CNPJ:> ')
                        conta.saldo_inicial = input('Digite o saldo inicial:> ')
                        condicao = input('Deseja cadastrar o segundo titular? digite sim/nao :>')
                        if condicao == 'sim':
                            conta.segundo_titular = input('Digite o segundo titular:> ')
                        create_pj(conta)
                    case 2:
                        read_pj()