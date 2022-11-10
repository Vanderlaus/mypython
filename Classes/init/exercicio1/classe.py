class Conta:
    
    # __init__ = metodo construtor
    def __init__(self, numero, titular, saldo, limite):
        print(f"Imprimindo Construtor {self}")
        
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite