from database.setup import get_conexao

def listar_dia_de_trabalho():
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                    SELECT * FROM dia_de_trabalho
                """
            )
            dias = cursor.fetchall()

            for dia in dias:
                print(dia)


def excluir_dias_trabalhados(moto_id):
    with get_conexao() as conn:
        with conn.cursor() as cursor:

            sql = '''
                  DELETE 
                  FROM dia_de_trabalho
                  WHERE moto_id = %s 
                  '''

            cursor.execute(sql, (moto_id,))


def historico_dias(moto_id):
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            sql = '''
            SELECT 
                d.data_trabalhada,
                d.quilometragem_final - d.quilometragem_inicial,
                d.ganho_bruto
            FROM dia_de_trabalho d
                WHERE d.moto_id = %s
            ORDER BY d.data_trabalhada ASC
            '''
            cursor.execute(sql,(moto_id,))
            dados = cursor.fetchall()

    return dados

