import mysql.connector
def get_conexao():
    con = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'palmeiras',
        database = 'livros')
    return con

print(get_conexao().is_connected())

