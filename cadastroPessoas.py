import sqlite3
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
email = input("Digite o email: ")

banco = sqlite3.connect('pessoas.db')
cursor = banco.cursor() # objeto cursor é responsável por executar comandos SQL no banco de dados

#cursor.execute('CREATE TABLE pessoas (nome TEXT, idade INTEGER, email TEXT)') # cria a tabela pessoas com os campos nome, idade e email

cursor.execute("INSERT INTO pessoas VALUES ('"+nome+"', "+str(idade)+", '"+email+"')") # insere um registro na tabela pessoas

cursor.execute("UPDATE pessoas SET idade = ? WHERE nome = ?", (idade, nome)) # atualiza a idade de uma pessoa com base no nome
banco.commit() # salva as alterações no banco de dados


# cursor.execute('SELECT * FROM pessoas') #seleciona todos os registros da tabela pessoas
# for pessoa in cursor.fetchall(): # percorre todos os registros retornados pela consulta
#     print(pessoa) # imprime cada registro no console

