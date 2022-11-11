class Carro:
    
    def __init__(self, marca, modelo, cor, categoria):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__categoria = categoria

    def set_marca(self, marca):
        self.__marca = marca
    def get_marca(self):
        return self.__marca
    
    def set_modelo(self, modelo):
        self.__modelo = modelo
    def get_modelo(self):
        return self.__modelo
    
    def set_cor(self, cor):
        self.__cor = cor
    def get_cor(self):
        return self.__cor
    
    def set_categoria(self, categoria):
        self.__categoria = categoria
    def get_categoria(self):
        return self.__categoria

    def __str__(self):
        return f'{self.get_marca()} - {self.get_modelo()} - {self.get_cor()} - {self.get_categoria()}'