#estrutura de decisao

n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

média = (n1 + n2) /2

print(f"sua media {média}")
if média >= 7:
    print("voce atingiu a media")

else:
    print("voce nao atingiu a media")