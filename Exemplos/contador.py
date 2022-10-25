from time import sleep
from controllercontador import contador
        
contador(1, 10, 1)
contador(10, 0, 2)
print('-'*30, "Personalize seu For ", '-'*30)
contador(int(input('Inicio: ')), int(input('Fim: ')),int(input('Passo: ')))