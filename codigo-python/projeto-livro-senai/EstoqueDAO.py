import Conexao

# Obter conexão e cursor
conexao = Conexao.get_conexao()
cursor = conexao.cursor()

def listar_estoque():
    sql = "SELECT * FROM estoque;"
    cursor.execute(sql)
    estoque = cursor.fetchall()
    return estoque

def buscar_estoque(id):
    sql = "SELECT * FROM estoque WHERE id = {};".format(id)
    cursor.execute(sql)
    estoque = cursor.fetchone()
    return estoque

def cadastrar_estoque(descricao, numero_nota, estoque):
    sql = "INSERT INTO estoque VALUES (null,'{}','{}','{}');".format(descricao,  numero_nota, estoque)
    cursor.execute(sql)
    conexao.commit()

def atualizar_estoque(id, descricao, numero_nota, material_didatico_id):
    sql = "UPDATE estoque SET descricao = '{}', numero_nota = '{}', material_didatico_id = '{}' WHERE id = {};".format(descricao, numero_nota, material_didatico_id, id)
    cursor.execute(sql)
    conexao.commit()

def deletar_estoque(descricao):
    sql = "DELETE FROM estoque WHERE id = {};".format(descricao)
    cursor.execute(sql)
    conexao.commit()