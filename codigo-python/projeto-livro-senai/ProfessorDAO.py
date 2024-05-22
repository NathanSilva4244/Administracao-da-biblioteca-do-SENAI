import Conexao

# Obter conexão e cursor
conexao = Conexao.get_conexao()
cursor = conexao.cursor()

def listar_professor():
    sql = "SELECT * FROM professor;"
    cursor.execute(sql)
    professor = cursor.fetchall()
    return professor

def buscar_professor(id):
    sql = "SELECT * FROM professor WHERE id = {};".format(id)
    cursor.execute(sql)
    professor = cursor.fetchone()
    return professor

def cadastrar_professor(nome):
    sql = "INSERT INTO professor VALUES (null,'{}');".format(nome)
    cursor.execute(sql)
    conexao.commit()

def atualizar_professor(id, nome):
    sql = "UPDATE professor SET nome = '{}' WHERE id = {};".format(nome, id)
    cursor.execute(sql)
    conexao.commit()


def deletar_professor(nome):
    sql = "DELETE FROM professor WHERE id = {};".format(nome)
    cursor.execute(sql)
    conexao.commit()