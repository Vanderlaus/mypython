from lib2to3.pgen2.literals import simple_escapes
from controller import salvar, listar

def menu():
    print('*'*20, 'MENU', '*'*20)
    
    cond = 'sim'
    while cond == 'sim':
        nome = salvar(input('Digite seu nome: '))
        cond = str(input("Deseja continuar? \n Sim \n Não \n :> "))
        
menu()

print('A lista de Nomes inseridos\n', listar())