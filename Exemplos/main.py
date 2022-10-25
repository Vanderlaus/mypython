from controller import cadastrar, listar

def menu():
    while True:
        opcao = int(input("1-Cadastro de Funcionarios\n2-Listar Funcionarios\n3-Sair do Programa\n=>"))
        match opcao:
            case 1:
                cadastrar()
            case 2:
                listar()
            case 3:
                print("Você saiu da aplicação")
                break
            case _:
                print("Digite uma opção válida")

menu()