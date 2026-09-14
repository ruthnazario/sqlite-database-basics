import sqlite3

try:
    banco = sqlite3.connect('pessoas.db') #objeto banco é responsável por gerenciar a conexão com o banco de dados
    cursor = banco.cursor() 

    cursor.execute("DELETE FROM pessoas WHERE idade = ?", (12,)) # deleta um registro da tabela pessoas
    banco.commit() # salva as alterações no banco de dados
    print("Registro deletado com sucesso!")


except sqlite3.Error as erro:
    print("Erro ao deletar registro:", erro)

finally:
    if banco:
        banco.close()
