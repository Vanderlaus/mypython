from controller import *

poli = "*"*20 

print(f"\n {poli} CALCULADORA {poli} \n")

salario01 = float(input("Digite seu salario: "))
salario02 = float(input("Digite sua salario: "))
salario03 = float(input("Digite seu salario: "))
salario04 = float(input("Digite seu salario: "))

print("Salario 1 é: {:.2f}".format(salario01))
print("Salario 2 é: {:.2f}".format(salario02))
print("Salario 3 é: {:.2f}".format(salario03))
print("Salario 4 é: {:.2f}".format(salario04))

print("\nA soma dos salarios : {:.2f}".format(somasal(salario01,salario02,salario03,salario04)))

print(f"\n {poli} Calculadora Finalizada {poli}\n")