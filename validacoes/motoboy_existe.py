from BancoDeDados.conexao import get_conexao


def motoboy_existe():
    conn = get_conexao()
    cursor = conn.cursor()
    sql = '''
    SELECT 1 
    FROM motoboy
    WHERE id = 1
    LIMIT 1
    '''

    cursor.execute(sql)
    resultado = cursor.fetchone()

    conn.close()

    return  resultado is not None
