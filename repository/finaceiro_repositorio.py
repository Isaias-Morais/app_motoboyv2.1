from database.setup import get_conexao

def buscar_dia_de_trabalho(moto_id):
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            sql = '''
                SELECT
                    d.ganho_bruto AS ganho,
                    d.quilometragem_final - d.quilometragem_inicial AS km
                FROM dia_de_trabalho d
                JOIN moto m ON m.id = d.moto_id
                WHERE m.id = %s
                    and d.data_trabalhada = CURRENT_DATE
            '''
            cursor.execute(sql,(moto_id,))
            resultado = cursor.fetchone()


            if resultado is None:
                return {
                    'ganho':0.0,
                    'km_dia':0.0
                }
            ganho,km = resultado

            return {
                'ganho':ganho,
                'km_dia':km
            }

def busca_abastecimento(moto_id):
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            sql = '''
                SELECT
                    SUM(a.valor) AS valor,
                    SUM(a.litros) AS litros,
                    MAX(a.quilometragem) - MIN(a.quilometragem) AS km
                FROM abastecimento a
                JOIN moto m ON m.id = a.moto_id
                WHERE m.id = %s
                AND a.data_abastecimento >= NOW() - INTERVAL '30 days'
                AND a.data_abastecimento <= NOW()
                '''
            cursor.execute(sql,(moto_id,))
            valor,litros,km = cursor.fetchone()

            return {
                'valor_abastecimento':valor,
                'litros':litros,
                'km_abastecimento': km
            }

def busca_manutencoes(moto_id):
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            sql = ''' 
                SELECT
                    SUM(m.valor) AS valor,
                    MAX(m.quilometragem) - MIN(m.quilometragem) AS km
                FROM manutencao m 
                JOIN moto mo ON mo.id = m.moto_id
                WHERE mo.id = %s
                AND m.data_manutencao >= NOW() - INTERVAL '30 days'
                AND m.data_manutencao <= NOW()
            '''
            cursor.execute(sql,(moto_id,))
            valor,km = cursor.fetchone()

            return {
                'valor_manutencao':valor,
                'km_manutencao':km
            }

def busca_abastecimento_consumo_medio(moto_id):
    with get_conexao() as conn:
        with conn.cursor as cursor:

            sql = '''
                SELECT 
                    a.quilometragem AS km,
                    a.litros AS litros
                FROM abastecimento a
                JOIN moto m ON m.id = a.moto_id
                WHERE m.id = %s
                    AND a.tanque_completo = True
                ORDER BY a.quilometragem ASC
                LIMIT 10
            '''

            cursor.execute(sql, (moto_id,))
            dados = cursor.fetchall()

            return dados



def busca_consumo_moto(moto_id):
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            sql = '''
                SELECT
                    mo.consumo AS consumo
                FROM moto mo
                JOIN moto m ON m.id = m.id
                WHERE m.id =%s
            '''

            cursor.execute(sql,(moto_id,))
            consumo = cursor.fetchone()

            return consumo
