import Conexao

conexao = Conexao.get_conexao()
cursor = conexao.cursor()


def listar_mov():
    sql = "SELECT * FROM movimentacao;"
    cursor.execute(sql)
    movimentacao = cursor.fetchall()
    return movimentacao



def atualizar_mov(id,quantidade,tipo,data,material_didatico_id,estoque_id):
    sql = "UPDATE movimentacao SET quantidade = '{}', tipo = '{}',data = '{}',material_didatico_id = '{}',estoque_id = '{}';".format(quantidade,tipo,data,material_didatico_id,estoque_id,id)
    cursor.execute(sql)
    conexao.commit()


def buscar_mov(id):
    sql = "SELECT * FROM movimentacao WHERE id = {};".format(id)
    cursor.execute(sql)
    movimentacao = cursor.fetchone()
    return movimentacao

    #for i in buscar_mov(id):
    #    print(i)

def cadastrar_mov(quantidade,tipo,data,material_didatico_id,estoque_id):
    sql = "INSERT INTO movimentacao VALUES(null,'{}', '{}','{}', '{}','{}');".format(quantidade,tipo,data,material_didatico_id,estoque_id)
    cursor.execute(sql)
    conexao.commit()





def deletar_mov(id):
    sql = "DELETE FROM movimentacao WHERE id = {};".format(id)
    cursor.execute(sql)
    conexao.commit()
