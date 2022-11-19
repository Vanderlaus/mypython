from conta import Conta
from controller import create, read, update, delete

def menu():
    conta = Conta()
    conta.titular = 'Vander Luis'
    conta.numero = 123456
    conta.saldo = 2000.0
    create(conta)
    
    #lista_contas = read()
    
    #for c in lista_contas:
    #    print(c)
    
    #delete(85472)
    
    #update(85472)
    
menu()