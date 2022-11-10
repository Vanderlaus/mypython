class Animal:
    
    # __init__ = construtor
    def __init__(self, especie, genero, idade, cor):
        print(f"Imprimindo Construtor {self}")
        
        self.especie = especie
        self.genero = genero
        self.idade = idade
        self.cor = cor