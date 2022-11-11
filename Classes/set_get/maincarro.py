from carro import Carro

print('*'*25,'CABEÇALHO','*'*25)
print('Carro 1')
carro = Carro(str(input('Digite a marca do carro:> ')),str(input('Digite o modelo:> ')),str(input('Digite a cor:> ')),str(input('Digite a categoria:> ')))

print('Carro modelo {} de cor {} da marca {}.\n'.format(Carro.get_modelo(carro),Carro.get_cor(carro),Carro.get_marca(carro)))

print('Carro 2:')
carro2 = Carro(str(input('Digite a marca do carro:> ')),str(input('Digite o modelo:> ')),str(input('Digite a cor:> ')),str(input('Digite a categoria:> ')))

print('Carro modelo {} de cor {} da marca {}.\n'.format(Carro.get_modelo(carro2),Carro.get_cor(carro2),Carro.get_marca(carro2)))