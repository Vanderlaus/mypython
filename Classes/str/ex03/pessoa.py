class Pessoa:
    nome = ""
    cpf = ""
    idade = 0
    def __str__(self):
        return f'{self.nome} - {self.cpf} - {self.idade}'