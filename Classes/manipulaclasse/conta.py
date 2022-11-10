class Conta:
    titular = ""
    numero = 0
    saldo = 0
    limite = 0
    def __str__(self):
        return f'{self.titular} - {self.numero} - {self.saldo} - {self.limite}'
    
    def extrato(self):
        print('A conta n° {} de titularidade de {} possui o saldo inicial de {}'.format(self.numero,self.titular,self.saldo))
        
    def deposito(self, valor):
        self.saldo += valor
        return valor
    
    def saque(self, valor):
        self.saldo -= valor
        return valor
    
    def transferencia(self, valor, origem, destino):
        origem.saque(valor)
        destino.deposito(valor)
        return valor