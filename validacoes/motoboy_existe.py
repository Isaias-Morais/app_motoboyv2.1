from BancoDeDados.conexao import get_conexao


def motoboy_existe():
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            sql = '''
            SELECT 1 
            FROM motoboy
            WHERE id = 1
            LIMIT 1
            '''

            cursor.execute(sql)
            resultado = cursor.fetchone()

            return  resultado is not None
