#01

import random

participante1 = str(input("Digite seu nome: "))
participante2 = str(input("Digite seu nome: "))
participante3 = str(input("Digite seu nome: "))
participante4 = str(input("Digite seu nome: "))

participantes = [participante1, participante2, participante3, participante4]

sorteio = random.choice(participantes)

print("-"*5, "SORTEIO", "-"*5)

print("o ganhador do sorteio: {}! ".format(sorteio))