class Animal:
    especie = ""
    cor = ""
    raca = ""
    def __str__(self):
        return f'{self.especie} - {self.cor} - {self.raca}'