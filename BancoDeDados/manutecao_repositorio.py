from BancoDeDados.init_db import get_conexao

def salvar_manutecao(manutencao):
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                '''
                    INSERT INTO manutencao(
                        data_manutencao,
                        tipo,
                        descricao,
                        valor,
                        moto_id,
                        quilometragem
                      
                    )   
                    VALUES(%s,%s,%s,%s,%s,%s)  
                    RETURNING id
                ''',(
                    manutencao._data,
                    manutencao._tipo,
                    manutencao._descricao,
                    manutencao._valor,
                    manutencao._moto,
                    manutencao._quilometragem
                )
                )
            manutencao.id = cursor.fetchone()[0]

def listar_manutencao():
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                    SELECT * FROM manutencao
                """
            )
            manutencoes = cursor.fetchall()

            for manutencao in manutencoes:
                print(manutencao)


def excluir_manutencao(moto_id):
    with get_conexao() as conn:
        with conn.cursor() as cursor:

            sql = '''
                  DELETE 
                  FROM manutencao
                  WHERE moto_id = %s 
                  '''

            cursor.execute(sql, (moto_id,))


def historico_manutencoes(moto_id):
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            sql = '''
            SELECT
                m.data_manutencao,
                m.tipo,
                m.descricao,
                m.valor,
                m.quilometragem
            FROM manutencao m
                WHERE m.moto_id = %s
            ORDER BY m.data_manutencao ASC
                  '''
            cursor.execute(sql,(moto_id,))
            dados = cursor.fetchall()


            return dados