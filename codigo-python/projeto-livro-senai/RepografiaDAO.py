import Conexao

# Obter conexão e cursor
conexao = Conexao.get_conexao()
cursor = conexao.cursor()

def listar_repografia():
    sql = "SELECT * FROM repografia;"
    cursor.execute(sql)
    repografia = cursor.fetchall()
    return repografia

def buscar_repografia(id):
    sql = "SELECT * FROM repografia WHERE id = {};".format(id)
    cursor.execute(sql)
    repografia = cursor.fetchone()
    return repografia

def cadastrar_repografia(data, quantidade, material_didatico_id, professor_id):
    sql = "INSERT INTO repografia VALUES (null,'{}','{}','{}','{}');".format(data, quantidade, material_didatico_id, professor_id)
    cursor.execute(sql)
    conexao.commit()

def atualizar_repografia(id, data, quantidade, material_didatico_id, professor_id):
    sql = "UPDATE repografia SET data = '{}', quantidade = '{}', material_didatico_id = '{}', professor = '{}' WHERE id = {};".format( data, quantidade, material_didatico_id, professor_id, id)
    cursor.execute(sql)
    conexao.commit()


def deletar_repografia(id):
    sql = "DELETE FROM repografia WHERE id = {};".format(id)
    cursor.execute(sql)
    conexao.commit()