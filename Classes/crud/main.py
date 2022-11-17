from conta import Conta
from controller import create, read

def menu():
    conta = Conta()
    conta.titular = 'Vander Lauschner'
    conta.numero = 456785
    conta.saldo = 3000.0
    create(conta)
    
    lista_contas = read()
    
    for c in lista_contas:
        print(c)
        
menu()