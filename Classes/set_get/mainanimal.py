from animal import Animal

print('*'*25,'CABEÇALHO','*'*25)
print('Animal 1')
animal = Animal(str(input('Digite a especie do animal:> ')),str(input('Digite a raça:> ')),str(input('Digite a cor:> ')),str(input('Digite o porte:> ')))

print('O animal da especie {} da raça {} de porte {} e cor {}.\n'.format(Animal.get_especie(animal),Animal.get_raca(animal),Animal.get_porte(animal),Animal.get_cor(animal)))
print(animal)

print('Animal 2:')
animal2 = Animal(str(input('Digite a especie do animal:> ')),str(input('Digite a raça:> ')),str(input('Digite a cor:> ')),str(input('Digite o porte:> ')))

print('O animal da especie {} da raça {} de porte {} e cor {}.\n'.format(Animal.get_especie(animal2),Animal.get_raca(animal2),Animal.get_porte(animal2),Animal.get_cor(animal2)))
print(animal2)