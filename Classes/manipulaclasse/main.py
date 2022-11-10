from conta import Conta

conta1 = Conta()
conta2 = Conta()

print('*'*25,'CABEÇALHO','*'*25)
print('Conta 1')
conta1.titular = input('Digite o titular da conta:> ')
conta1.numero = int(input('Digite o numero da conta:> '))
conta1.saldo = float(input('Digite o saldo da conta:> '))
conta1.limite = float(input('Digite o limite da conta:> '))

print('\n','-'*25,'Extrato inicial conta1','-'*25)
conta1.extrato()
print()

conta1.deposito(float(input('Qual valor deseja depositar:> ')))

print('\n','-'*25,'Extrato atual conta1','-'*25)
conta1.extrato()
print()

conta1.saque(float(input('Qual valor deseja sacar:> ')))

print('\n','-'*25,'Extrato atual conta1','-'*25)
conta1.extrato()
print()

print('Conta 2:')
conta2.titular = input('Digite o titular da conta:> ')
conta2.numero = int(input('Digite o numero da conta:> '))
conta2.saldo = float(input('Digite o saldo da conta:> '))
conta2.limite = float(input('Digite o limite da conta:> '))

print('\n','-'*25,'Extrato inicial conta2','-'*25)
conta2.extrato()
print()

valor = conta1.transferencia(float(input('Qual valor deseja transferir:> ')),conta1,conta2)
print()
print('----- O valor transferido foi de: ',valor,'-----')

print('\n','-'*25,'Extrato atual conta1','-'*25)
conta1.extrato()

print('\n','-'*25,'Extrato atual conta2','-'*25)
conta2.extrato()
print()