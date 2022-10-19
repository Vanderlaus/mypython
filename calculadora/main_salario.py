from controller import somasal

def menu():
    print("="*15, "CALCULADORA DE SALARIO", "="*15, "\n")
    var = 'sim'
    while var == 'sim':
        n1 = float(input("Digite seu primeiro salario: "))
        n2 = float(input("Digite seu segundo salario: "))
        n3 = float(input("Digite seu terceiro salario: "))
        n4 = float(input("Digite seu quarto salario: "))
        
        resultado = somasal(n1,n2,n3,n4)
        print("A soma dos salarios é: {:.2f}".format(resultado))
        
        var = input("Você deseja continuar? \n sim \nnão\n:>")
        
menu()
print("Você saiu do programa")