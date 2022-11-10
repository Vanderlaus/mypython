from classe import Carro

carro1 = Carro('Ford', 'Fusion', 80000.00)
print('*'*50)
print(f"Imprimindo carro1 {carro1}")
print('*'*50)

carro2 = Carro('Chevrolet','Onix', 60000.00)
print('*'*50)
print(f"Imprimindo carro2 {carro2}")
print('*'*50)

carro3 = Carro('Hyundai','Azera', 40000.00)
print('*'*50)
print(f"Imprimindo carro3 {carro3}")
print('*'*50)

carro2.marca = 'Chevrolet'
carro2.modelo = 'Onix'
carro2.valor = 60000.00

print(f'\nDados carro2: {carro2.marca} - {carro2.modelo} - {carro2.valor}\n')