from controllerlista import *

def menu():
    while True:
        opcao = int(input("1-Cadastro de Pessoas\n2-Listar Pessoas\n3-Sair do Programa\n=>"))
        match opcao:
            case 1:
                cadastrar()
            case 2:
                listar()
            case 3:
                print("Você saiu da aplicação")
                break

menu()