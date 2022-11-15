class Conta:
    
    def __init__(self,numero,tipo):
        self.__numero = numero
        self.__tipo = tipo
        print('Passando pelo construtor da classe mãe')
    
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero):
        self._numero = numero
        
    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo
        
    def __str__(self):
        return f'{self.numero} {self.tipo}'