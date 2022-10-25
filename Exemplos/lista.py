from controllerlista import cadastrar,listar,finalizar
import os

os.system('cls')

def menu():
    while True:
        opcao = str(input("1-Cadastro de Pessoas\n2-Listar Pessoas\n3-Sair do Programa\n=>"))
        match opcao:
            case '1':
                cadastrar()
            case '2':
                print('-='*30)
                listar()
            case '3':
                print("\nResultado dos dados cadastrados\n")
                finalizar()
                break
            case _:
                print("Digite uma opção válida")

menu()