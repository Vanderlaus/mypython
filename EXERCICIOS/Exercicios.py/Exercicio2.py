#02

from random import shuffle 

A1 = str(input("Digite seu naipe: "))
A2 = str(input("Digite seu naipe: "))
A3 = str(input("Digite seu naipe: "))
A4 = str(input("Digite seu naipe: "))

cartas = [A1, A2, A3, A4]

shuffle(cartas)

print("-"*5, "EMBARALHAMENTO", "-"*5)

print("as cartas embaralhadas sao: {}! ".format(cartas))