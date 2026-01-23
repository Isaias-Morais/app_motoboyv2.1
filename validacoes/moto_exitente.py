from BancoDeDados.conexao import get_conexao


def moto_existe(moto_id=0):
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            sql = '''
                SELECT 1 
                FROM moto
                WHERE id = %s
                LIMIT 1
                '''

            cursor.execute(sql,(moto_id,))
            resultado = cursor.fetchone()

            return resultado is not None
