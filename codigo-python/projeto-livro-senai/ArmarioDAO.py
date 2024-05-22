import Conexao

# Obter conexão e cursor
conexao = Conexao.get_conexao()
cursor = conexao.cursor()

def listar_armario():
    sql = "SELECT * FROM armario;"
    cursor.execute(sql)
    armario = cursor.fetchall()
    return armario

def buscar_armario(id):
    sql = "SELECT * FROM armario WHERE id = {};".format(id)
    cursor.execute(sql)
    armario = cursor.fetchone()
    return armario

def cadastrar_armario(nome):
    sql = "INSERT INTO armario VALUES (null,'{}');".format(nome)
    cursor.execute(sql)
    conexao.commit()

def atualizar_armario(id, nome):
    sql = "UPDATE armario SET nome = '{}' WHERE id = {};".format(nome, id)
    cursor.execute(sql)
    conexao.commit()


def deletar_armario(nome):
    sql = "DELETE FROM armario WHERE id = {};".format(nome)
    cursor.execute(sql)
    conexao.commit()