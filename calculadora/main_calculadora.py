from controller import *

def menu():
    print('*'*25,'MENU', '*'*25)
    
    cond = 'sim'
    while cond == 'sim':
        Op = [1,2,3,4]
        n1 = int(input('Digite primeiro número: '))
        n2 = int(input('Digite segundo número: '))
        Op = int(input("\nQual a operação que deseja fazer?\n1 - soma\n2 - subtracao\n3 - multiplicacao\n4 - divisao\ndigite a opcao: "))
                
        Soma = soma(n1,n2)
        Subtracao = subtrai(n1,n2)
        Multiplica = multiplica(n1,n2)
        Divisao = divide(n1,n2)
        
        match Op:
            case 1:
                print("\nOperação escolhida foi SOMA")
                print("\nO resultado da operacao é: {:.2f}".format(Soma))
            case 2:
                print("\nOperação escolhida foi SUBTRACAO")
                print("\nO resultado da operacao é: {:.2f}".format(Subtracao))
            case 3:
                print("\nOperação escolhida foi MULTIPLICACAO")
                print("\nO resultado da operacao é: {:.2f}".format(Multiplica))
            case 4:
                print("\nOperação escolhida foi DIVISAO")
                print("\nO resultado da operacao é: {:.2f}".format(Divisao))
            case _:
                print("\nDigite uma opção válida")
        
        cond = str(input('Deseja continuar?\nsim\nnão\n:>'))
        
menu()

print('Você saiu da sua aplicação')