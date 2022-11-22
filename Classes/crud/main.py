from conta import Conta
from controller import create, read, update, delete

conta = Conta()
conta.titular = 'Gisele Boladona'
conta.numero = 85472
conta.saldo = 1000.0

#create(conta)
    
#lista_contas = read()

#print(lista_contas)

#print("*"*30)

#for c in lista_contas:
    #print(c)
    
update(conta)

#delete(123456)
