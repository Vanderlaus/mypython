class Produto:
    
    # __init__ = construtor
    def __init__(self, id, NomeProduto, valor, quantidade):
        print(f"Imprimindo Construtor {self}")
        
        self.id = id
        self.NomeProduto = NomeProduto
        self.valor = valor
        self.quantidade = quantidade