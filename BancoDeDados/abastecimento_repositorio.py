from BancoDeDados.conexao import get_conexao

def salvar_abastecimeto(abastecimento):
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
        '''
            INSERT INTO abastecimento(
                data_abastecimento,
                posto,
                valor,
                litros,
                valor_litro,
                tanque_completo,
                moto_id,
                quilometragem
            )
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
            RETURNING id
        ''',(
            abastecimento._data,
            abastecimento._posto,
            abastecimento._valor,
            abastecimento._litros,
            abastecimento.preco_litro,
            abastecimento._tcompleto,
            abastecimento._moto,
            abastecimento._qilometragem
        )
            )
            abastecimento.id = cursor.fetchone()[0]


def listar_abastecimento():
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
        """
            SELECT * FROM abastecimento
        """
    )
            abastecimentos = cursor.fetchall()

            for abastecimento in abastecimentos:
                print(abastecimento)

def excluir_abastecimentos(moto_id):
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            sql = '''
            DELETE FROM abastecimento
            WHERE moto_id = %s
            '''

            cursor.execute(sql,(moto_id,))




def historico_abastecimentos(moto_id):
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            sql = '''
                  SELECT a.data_abastecimento,
                         a.posto,
                         a.litros,
                         a.valor,
                         a.tanque_completo,
                         a.quilometragem
                  FROM abastecimento a
                  WHERE a.moto_id = %s
                  ORDER BY a.data_abastecimento ASC
                  '''
            cursor.execute(sql, (moto_id,))
            dados = cursor.fetchall()


            return dados


def atualizar_consumo(moto_id,consumo):
    with get_conexao() as conn:
        with conn.cursor() as cursor:

            sql = '''
                  UPDATE moto
                  SET cosumo = %s
                  WHERE id = %s 
                  '''

            cursor.execute(sql, (consumo, moto_id))




