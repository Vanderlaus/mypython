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
    hospedeFind = input("Digite o indice do hóspede que deseja fazer o CHECKOUT: ")
    hospede = [] 
    with open('gerenciar_hospedes/pessoas.txt', 'r') as arquivo:
        hospede = arquivo.readlines()
        print(hospede)
#        for line in hospede:
#            if hospedeFind in line:
#                print(hospede.index(line))
#                return
#        print("Hospede não encontrado")    

        for number, line in enumerate(hospede):
            print(number, line)
    
def sair():
    print('Programa finalizado com sucesso'.center(50, "*"))