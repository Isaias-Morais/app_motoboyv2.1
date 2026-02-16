from database.setup import get_conexao
from validacoes.moto_exitente import moto_existe

def salvar_moto(moto):
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                '''
                    INSERT INTO moto(
                        marca,
                        modelo,
                        ano,
                        quilometragem,
                        consumo,
                        motoboy_id
                    )
                    VALUES (%s,%s,%s,%s,%s,%s)
                    RETURNING id
                ''',(moto._marca,
                     moto._modelo,
                     moto._ano,
                     moto._quilometragem_total,
                     moto._consumo,
                     moto._motoboy
                     )
            )
            moto.id = cursor.fetchone()[0]


def listar_moto():
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                    SELECT * FROM moto
                """
            )
            moto = cursor.fetchall()

            for moto in moto:
                print(moto)


def excluir_moto(moto_id):
    with get_conexao() as conn:
        with conn.cursor() as cursor:

            sql = '''
                  DELETE 
                  FROM moto
                  WHERE id = %s 
                  '''

            cursor.execute(sql, (moto_id,))


def busca_moto_ativa():
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                SELECT 
                    m.moto_ativa_id AS id
                FROM motoboy m 
                WHERE m.id = 1
            ''')

            id = cursor.fetchone()

            return id[0] if id and id[0] is not None else None


def definir_moto_ativa(moto_id):
    if not moto_existe(moto_id):
        return False,'moto não existe'
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            sql = '''
                    UPDATE motoboy 
                    SET moto_ativa_id = %s
                    WHERE id = 1
                '''
            cursor.execute(sql,(moto_id,))


def redefinir_moto_ativa():
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            sql = '''
                UPDATE motoboy
                SET moto_ativa_id = NULL
                WHERE id = 1
            '''
            cursor.execute(sql)


