class Carro:
    
    # __init__ = construtor
    def __init__(self, marca, modelo, valor):
        print(f"Imprimindo Construtor {self}")
        
        self.marca = marca
        self.modelo = modelo
        self.ivalor = valor