from controller import *

funcoes = ['1','2','3','4','5']

def menu():
    from datetime import datetime

    dataatual = datetime.today()
    horaatual = datetime.now()

    hora = horaatual.strftime("%H:%M")

    saudacao = 0

    if hora>="00:00"<"12:00":
        saudacao = 1
    if hora>="12:00"<"18:00": 
        saudacao = 2
    if hora>="18:00"<="23:59":
        saudacao = 3    

    match saudacao:
        case 1:
            print("\nBom dia!!!\nSeja bem vindo ao nosso Hotel, escolha uma das opções no menu abaixo!")
        case 2:
            print("\nBoa tarde!!!\nSeja bem vindo ao nosso Hotel, escolha uma das opções no menu abaixo!")
        case 3:
            print("\nBoa noite!!!\nSeja bem vindo ao nosso Hotel, escolha uma das opções no menu abaixo!")
            
    poli = "="*70
    espaco = " "*29
    print(f"{poli}\n{espaco}MENU DO MOTEL{espaco}\n{poli}")
    print(f"{espaco}MENU{espaco}".center(70,"="))
    print(f"(1) Fazer check-In\n(2) Relatório Hospedes\n(3) Procurar Hospedes\n(4) Fazer Check-Out\n(5) Finalizar Atendimento")
    print(poli)
         
    while True:
        opcao = input("=> ")
        if not(opcao in funcoes):
            print("Digite uma opção válida.\n Uma das opções do MENU.")

        elif opcao == '1':
            hospede=[]
            dados={}
            dados["nome"] = str(input('Digite o seu nome: '))
            dados["telefone"] = str(input('Digite o seu telefone(ddxxxxxxxxx): '))
            dados["idade"] = str(input('Digite sua idade: '))
            hospede.append(dados)
            salvar(dados)
        
            print('Hospede cadastrado com sucesso!!')

        elif opcao == '2':
            listar()
        
        elif opcao == '3':
            buscar()

        elif opcao == "4":
            checkout()
            
        elif opcao == '5':
            sair()
            break

menu()

