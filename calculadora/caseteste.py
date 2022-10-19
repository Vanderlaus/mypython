from controller import *

poli = "*"*20 

print(f"\n {poli} Calculadora Python {poli} \n")

Op = [1,2,3,4]
num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))
Op = int(input("\nQual a operação que deseja fazer?\n1 - soma\n2 - subtracao\n3 - multiplicacao\n4 - divisao\ndigite a opcao: "))

cond = "sim"
while cond == "sim":
    match Op:
        case 1:
            print("\nOperação escolhida foi SOMA")
            print("\nO resultado da operacao é: {:.2f}".format(soma(num1,num2)))
        case 2:
            print("\nOperação escolhida foi SUBTRACAO")
            print("\nO resultado da operacao é: {:.2f}".format(subtrai(num1,num2)))
        case 3:
            print("\nOperação escolhida foi MULTIPLICACAO")
            print("\nO resultado da operacao é: {:.2f}".format(multiplica(num1,num2)))
        case 4:
            print("\nOperação escolhida foi DIVISAO")
            print("\nO resultado da operacao é: {:.2f}".format(divide(num1,num2)))
        case _:
            print("\nDigite uma opção válida")
    cond = str(input("Você deseja continuar?\nsim\nnão:>"))
        
print(f"\n {poli} Calculadora Finalizada {poli}\n")