import Conexao

# Obter conexão e cursor
conexao = Conexao.get_conexao()
cursor = conexao.cursor()

def listar_material_didatico():
    sql = "SELECT * FROM material_didatico;"
    cursor.execute(sql)
    material_didatico = cursor.fetchall()
    return material_didatico

def buscar_material_didatico(id):
    sql = "SELECT * FROM material_didatico WHERE id = {};".format(id)
    cursor.execute(sql)
    material_didatico = cursor.fetchone()
    return material_didatico

def cadastrar_material_didatico(categoria, titulo, data_publicacao):
    sql = "INSERT INTO material_didatico VALUES (null,'{}', '{}','{}');".format(categoria, titulo, data_publicacao)

    cursor.execute(sql)
    conexao.commit()

def atualizar_material_didatico(id, categoria, titulo, data_publicacao):
    sql = "UPDATE material_didatico SET categoria = '{}', titulo = '{}', data_publicacao ='{}' WHERE id = '{}';".format(categoria, titulo, data_publicacao, id)
    cursor.execute(sql)
    conexao.commit()

def deletar_material_didatico(id):
    sql = "DELETE FROM material_didatico WHERE id = {};".format(id)
    cursor.execute(sql)
    conexao.commit()