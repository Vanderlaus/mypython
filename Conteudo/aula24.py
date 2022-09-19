from time import sleep

situacao = "reprovado"
nome = str(input("Digite seu nome: "))
sobrenome = str(input("Digite seu sobrenome: "))
idade = int(input("Digite sua idade: "))
lista_notas = []
while situacao != "aprovado":

    for list in range(0, 2):
        nota = int(input("Digite sua nota: "))
        lista_notas.append(nota)

    media = sum(lista_notas)/ len(lista_notas)



    if media >=7: 
        #sleep(2)
        print("*")
        situacao = "aprovado"
    lista_notas = []
    dicionario_alunos = {"nome":nome, "sobrenome":sobrenome, "idade":idade, "situacao":situacao}
    print(f"{dicionario_alunos['nome']} {dicionario_alunos['sobrenome']} {dicionario_alunos ['idade']} - {dicionario_alunos['situacao']}")
0