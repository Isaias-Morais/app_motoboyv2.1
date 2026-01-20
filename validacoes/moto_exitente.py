from BancoDeDados.conexao import get_conexao


def moto_existe(moto_id=0):
    conn = get_conexao()
    cursor =  conn.cursor()
    sql = '''
        SELECT 1 
        FROM moto
        WHERE id = %s
        LIMIT 1
        '''

    cursor.execute(sql,(moto_id,))
    resultado = cursor.fetchone()

    conn.close()

    return resultado is not None
