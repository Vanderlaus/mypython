from conta import Conta

class PessoaJuridica(Conta):
    __segundo_titular = ''
    
    def __init__(self, titular, CNPJ, saldo_inicial):
        super().__init__('2050','Pessoa Juridica')
        self.__titular = titular
        self.__cnpj = CNPJ
        self.__saldo_inicial = saldo_inicial
        print('Passando pelo construtor da classe Pessoa Juridica')
        
    @property
    def segundo_titular(self):
        return self.__segundo_titular
    
    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular
        
    def __str__(self):
        return f'{super().__str__()} {self.__titular} {self.__cnpj} {self.__saldo_inicial} {self.__segundo_titular}'