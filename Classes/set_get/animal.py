class Animal:
    
    def __init__(self, especie, raca, cor, porte):
        self.__especie = especie
        self.__raca = raca
        self.__cor = cor
        self.__porte = porte

    #@property
    #def especie(self):
    #    return self.__especie
    #@especie.setter
    #def especie(self, especie):
    #    self.__especie = especie
        
    def set_especie(self, especie):
        self.__especie = especie
    def get_especie(self):
        return self.__especie
    
    def set_raca(self, raca):
        self.__raca = raca
    def get_raca(self):
        return self.__raca
    
    def set_cor(self, cor):
        self.__cor = cor
    def get_cor(self):
        return self.__cor
    
    def set_porte(self, porte):
        self.__porte = porte
    def get_porte(self):
        return self.__porte

    def __str__(self):
        return f'{self.get_especie()} - {self.get_raca()} - {self.get_cor()} - {self.get_porte()}'
    #    return f'{self.especie()} - {self.raca()} - {self.cor()} - {self.porte()}'