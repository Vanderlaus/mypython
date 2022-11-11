from conta import Conta

def menu():
    poli = "="*70
    espaco = " "*29
    print(f"{poli}\n{espaco}MENU CONTA{espaco}\n{poli}")
    print(f"Cadastre a sua Conta")
    print(poli)
    print('Conta 1:')
    conta = Conta(str(input('Digite o titular da conta:> ')),int(input('Digite o número da conta:> ')),float(input('Digite o saldo da conta:> ')),float(input('Digite o limite da conta:> ')))
    
    print(poli)
    print('Conta 2:')
    conta2 = Conta(str(input('Digite o titular da conta:> ')),int(input('Digite o número da conta:> ')),float(input('Digite o saldo da conta:> ')),float(input('Digite o limite da conta:> ')))
    
    print()
    print('A conta 1 numero {} de titularidade de {} possui um saldo de {}.\n'.format(conta.numero,conta.titular,conta.saldo))
    print('A conta 2 numero {} de titularidade de {} possui um saldo de {}.\n'.format(conta2.numero,conta2.titular,conta2.saldo))
    print()
    
menu()
