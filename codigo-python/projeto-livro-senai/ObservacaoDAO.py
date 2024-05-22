import Conexao

# Obter conexão e cursor
conexao = Conexao.get_conexao()
cursor = conexao.cursor()

def listar_observacao():
    sql = "SELECT * FROM observacao;"
    cursor.execute(sql)
    observacao = cursor.fetchall()
    return observacao

def buscar_observacao(id):
    sql = "SELECT * FROM observacao WHERE id = {};".format(id)
    cursor.execute(sql)
    observacao = cursor.fetchone()
    return observacao

def cadastrar_observacao(data_observacao, professor_id,descricao):
    sql = "INSERT INTO observacao VALUES (null,'{}', '{}','{}');".format(data_observacao, professor_id,descricao)
    cursor.execute(sql)
    conexao.commit()

def atualizar_observacao(id, data_observacao, professor_id,descricao):
    sql = "UPDATE observacao SET data_observacao = '{}', professor_id = '{}', descricao ='{}' WHERE id = '{}';".format(data_observacao, professor_id,descricao, id)
    conexao.commit()

def deletar_observacao(id):
    sql = "DELETE FROM observacao WHERE id = {};".format(id)
    cursor.execute(sql)
    conexao.commit()

