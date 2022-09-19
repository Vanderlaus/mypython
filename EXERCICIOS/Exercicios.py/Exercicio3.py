#Com base nas aulas passadas vamos criar uma calculadora utilizando o conceito de estrutura de decisão.

#crie duas variáveis recebendo dados numéricos com casas decimais

#a descrição deve ser relacionada com primeira nota e segunda nota!

#crie uma variável para realizar este cálculo, não esqueça de utilizar o conceito de ordem de procedência aritmética

#crie uma função de impressão utilizando polimorfismo e quebra de linhas para definir um cabeçalho para sua aplicação console.

#utilizando máscara de substituição imprima de forma descritiva a primeira nota

#utilize quebra de linha, imprima a segunda nota

#utilize a quebra de linha e imprima o resultado.

#usando estrutura de decisão crie uma condição onde o resultado for maior que sete imprima na sua aplicação console que este aluno está acima da média.

#usando estrutura de decisão crie uma condição onde o resultado for entre cinco e sete imprima na sua aplicação console que este aluno pode solicitar recuperação.

#usando estrutura de decisão crie uma condição onde o resultado for entre quatro e cinco imprima na sua aplicação console que este aluno deve procurar o professor.

#Usando estrutura de decisão crie uma condição de saída e imprima na sua aplicação console que este aluno infelizmente não atingiu o esperado!


nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

média = (nota1 + nota2) /2

print(f"sua media {média}")
 
print("a nota entre {} e {} é o resultado {}".format(nota1, nota2, média))

if média >= 7:
    print("voce atingiu a media")
elif média >= 5:
    print("pode recuperar a nota colega")
elif média >= 4:
    print("pode solicitar ajuda do prof")
elif média <= 4: 
    print("infelizmente voce nao passou")