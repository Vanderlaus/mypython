from carro import Carro

def menu():
    poli = "="*70
    espaco = " "*29
    print(f"{poli}\n{espaco}MENU CARRO{espaco}\n{poli}")
    print(f"Cadastre o seu Carro")
    print(poli)

    print('Carro 1:')
    carro = Carro(str(input('Digite a marca do carro:> ')),str(input('Digite o modelo:> ')),str(input('Digite a cor:> ')),str(input('Digite a categoria:> ')))

    print(poli)
    print('Carro 2:')
    carro2 = Carro(str(input('Digite a marca do carro:> ')),str(input('Digite o modelo:> ')),str(input('Digite a cor:> ')),str(input('Digite a categoria:> ')))
    
    print()
    print('Carro 1 modelo {} de cor {} da marca {}.\n'.format(carro.modelo,carro.cor,carro.marca))
    print('Carro 2 modelo {} de cor {} da marca {}.\n'.format(carro2.modelo,carro2.cor,carro2.marca))
    print()
    
menu()