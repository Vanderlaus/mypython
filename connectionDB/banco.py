import psycopg2

try:
    conn = psycopg2.connect(host = "localhost", port = "5433", database = "postgres", user="teste", password = "123456")
    print("Conexao realizada com sucesso.")
except:
    print("Conexao com problema.")

if conn is not None:
    print("Conexao estavel.")

cursor = conn.cursor()
#cursor.execute("CREATE TABLE teste (id serial PRIMARY KEY, nome VARCHAR(15), sobreNome VARCHAR(15));")
#print("Tabela Criada.")

nome = 'Vander'
sobrenome = 'Lauschner'

cursor.execute("insert into teste (nome, sobrenome) values(%s,%s)", (nome, sobrenome))
print("Cadastro efetuado")
print("Cadastro efetuado")

conn.commit()
cursor.close()
conn.close()