class Conta:
    
    def __init__(self,numero,tipo):
        self.__numero = numero
        self.__tipo = tipo
        print('Passando pelo construtor da classe mãe')
        
    def __str__(self):
        return f'{self.__numero} {self.__tipo}'