from animal import Animal

def menu():
    poli = "="*70
    espaco = " "*29
    print(f"{poli}\n{espaco}MENU ANIMAL{espaco}\n{poli}")
    print(f"Cadastre o seu Animal")
    print(poli)

    print('Animal 1:')
    animal = Animal(str(input('Digite a especie do animal:> ')),str(input('Digite a raça:> ')),str(input('Digite a cor:> ')),str(input('Digite o porte:> ')))
    
    print(poli)
    print('Animal 2:')
    animal2 = Animal(str(input('Digite a especie do animal:> ')),str(input('Digite a raça:> ')),str(input('Digite a cor:> ')),str(input('Digite o porte:> ')))
    
    print()
    print('O animal 1 da especie {} da raça {} de porte {} e cor {}.\n'.format(animal.especie,animal.raca,animal.porte,animal.cor))
    print('O animal 2 da especie {} da raça {} de porte {} e cor {}.\n'.format(animal2.especie,animal2.raca,animal2.porte,animal2.cor))
    print()
    
menu()