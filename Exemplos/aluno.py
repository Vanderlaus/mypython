from controlleraluno import cadastrar,resultado
import os

os.system('cls')

def menu():
    while True:
        opcao = str(input("1-Cadastro de Alunos\n2-Resultado\n3-Sair do Programa\n=>"))
        match opcao:
            case '1':
                cadastrar()
            case '2':
                resultado()
                print("\nResultado dos alunos\n")
                resultado()
                break
            case _:
                print("Digite uma opção válida")

menu()