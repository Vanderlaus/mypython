import os

def salvar(dados):
    os.system('cls')
    with open('gerenciar_hospedes/pessoas.txt', 'a') as arquivo:
        arquivo.write(str(dados)+"\n")
        
def listar():
    os.system('cls')
    hospedes = []
    with open('gerenciar_hospedes/pessoas.txt', 'r') as arquivo:
        print(arquivo.read())
                
def buscar():
    os.system('cls')
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

def checkout(hospedeCheckout):
    os.system('cls')
    with open('gerenciar_hospedes/pessoas.txt') as file:
        lines = file.readlines()

    if(hospedeCheckout <= len(lines)):
        del lines[hospedeCheckout - 1]

        with open('gerenciar_hospedes/pessoas.txt', "w") as file:
            for line in lines:
                file.write(line)
    else:
        print(f"\nNão existe um hospede com este índice > {hospedeCheckout} <\n")
    
def sair():
    print('Programa finalizado com sucesso'.center(50, "*"))