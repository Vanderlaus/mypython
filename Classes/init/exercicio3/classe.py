class Pessoa:
    
    # __init__ = construtor
    def __init__(self, nome, sobreNome, idade, cpf):
        print(f"Imprimindo Construtor {self}")
        
        self.nome = nome
        self.sobreNome = sobreNome
        self.idade = idade
        self.cpf = cpf