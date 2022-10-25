from time import sleep
def contador(inicio, fim, passo):
    print('-'*35)
    passo = abs(passo) if passo != 0 else 1 
    #definindo o passo com o valor absoluto (deixa sinal positivo), e caso seja zero, recebe 1
    print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}')
    sleep(1.0)
    
    if inicio <fim:
        for cont in range(inicio, fim +1, +passo):
            print(cont, end=' ', flush=True)
            sleep(0.3)
    elif inicio > fim:
        for cont in range(inicio, fim -1, -passo):
            print(cont, end=' ', flush=True)
            sleep(0.3)
    print("\n\nFuncionando\n")
        
contador(10, 30, 2)
print('-'*30, "Personalize seu For ", '-'*30)
contador(int(input('Inicio: ')), int(input('Fim: ')),int(input('Passo: ')))