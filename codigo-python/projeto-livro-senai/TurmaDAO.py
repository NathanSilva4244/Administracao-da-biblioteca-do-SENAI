import Conexao

# Obter conexão e cursor
conexao = Conexao.get_conexao()
cursor = conexao.cursor()

def listar_turma():
    sql = "SELECT * FROM turma;"
    cursor.execute(sql)
    turma = cursor.fetchall()
    return turma

def buscar_turma(id):
    sql = "SELECT * FROM turma WHERE id = {};".format(id)
    cursor.execute(sql)
    turma = cursor.fetchone()
    return turma

#def cadastrar_turma(categoria,nome):
 #   sql = "INSERT INTO turma VALUES(null,'{}', '{}');".format(categoria,nome)
  #  cursor.execute(sql)
   # conexao.commit()

def cadastrar_turma(categoria, nome):
    sql = "INSERT INTO turma VALUES (null, '{}', '{}');".format(categoria, nome)
    cursor.execute(sql)
    conexao.commit()




def atualizar_turma(id, categoria, nome):
    sql = "UPDATE turma SET categoria = '{}', nome = '{}' WHERE id = {};".format(categoria, nome, id)
    cursor.execute(sql)
    conexao.commit()


def deletar_turma(nome):
    sql = "DELETE FROM turma WHERE id = {};".format(nome)
    cursor.execute(sql)
    conexao.commit()