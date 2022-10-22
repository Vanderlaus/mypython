import os

def salvar(dados):
    with open('gerenciar_hospedes/pessoas.txt', 'a') as arquivo:
        arquivo.write(str(dados)+"\n")
        
def listar():
    hospedes = []
    with open('gerenciar_hospedes/pessoas.txt', 'r') as arquivo:
        print(arquivo.read())
            
def buscar():
    index=0
    flag=0
    print(">>> BUSCAR HOSPEDE <<<")
    hospedeFind = input("Digite o nome completo: ")
    with open('gerenciar_hospedes/pessoas.txt', 'r') as arquivo:
        hospede = arquivo.readlines()
        for line in hospede:
            index +=1
            if hospedeFind == eval(line)['nome']:
                print(line)
                flag =1
        if flag == 0:
            print("Cliente não encontrado")

def checkout():
    print(">>> CHECKOUT <<<")
    hospedeFind = str(input("Digite o nome do hóspede que deseja fazer o checkout: "))
    with open('gerenciar_hospedes/pessoas.txt', 'r') as arquivo:
    
        with open('gerenciar_hospedes/temp.txt', 'w') as output:
            # iterate all lines from file
            for line in arquivo:
                # if substring contain in a line then don't write it
                if hospedeFind in line.strip("\n"):
                    output.write(line)
    os.replace('temp.txt', 'pessoas.txt')
#    hospede = [] 
#    with open('gerenciar_hospedes/pessoas.txt', 'r') as arquivo:
#        hospede = arquivo.readlines()
#        print(hospede)
#        for line in hospede:
#            if hospedeFind in line:
#                print(hospede.index(line))
#                return
#        print("Hospede não encontrado")    
#
#        for number, line in enumerate(hospede):
#            print(number, line)
    
def sair():
    print('Programa finalizado com sucesso'.center(50, "*"))