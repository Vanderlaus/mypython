from conta import Conta

print('*'*25,'CABEÇALHO','*'*25)
print('Conta 1')
conta = Conta(str(input('Digite o titular da conta:> ')),int(input('Digite o número da conta:> ')),float(input('Digite o saldo da conta:> ')),float(input('Digite o limite da conta:> ')))

print('A conta numero {} de titularidade de {} possui um saldo de {}.\n'.format(Conta.get_numero(conta),Conta.get_titular(conta),Conta.get_saldo(conta)))

print('Conta 2:')
conta2 = Conta(str(input('Digite o titular da conta:> ')),int(input('Digite o número da conta:> ')),float(input('Digite o saldo da conta:> ')),float(input('Digite o limite da conta:> ')))

print('A conta numero {} de titularidade de {} possui um saldo de {}.\n'.format(Conta.get_numero(conta2),Conta.get_titular(conta2),Conta.get_saldo(conta2)))

