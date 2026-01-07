from BancoDeDados.conexao import get_conexao

def salvar_abastecimeto(abastecimento):
    conn = get_conexao()
    curso = conn.cursor()
    curso.execute(
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
            VALUES(?,?,?,?,?,?,?,?)
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
    abastecimento.id = curso.lastrowid
    conn.commit()
    conn.close()

def listar_abastecimento():
    conn = get_conexao()
    curso = conn.cursor()
    curso.execute(
        """
            SELECT * FROM abastecimento
        """
    )
    abastecimentos = curso.fetchall()

    for abastecimento in abastecimentos:
        print(abastecimento)

def excluir_abastecimentos(moto_id):
    conn = get_conexao()
    curso = conn.cursor()

    sql = '''
    DELETE FROM abastecimento
    WHERE moto_id = ?
    '''

    curso.execute(sql,(moto_id,))

    conn.commit()
    conn.close()


def historico_abastecimentos(moto_id):
    conn = get_conexao()
    cursor = conn.cursor()
    sql = '''
          SELECT a.data_abastecimento,
                 a.posto,
                 a.litros,
                 a.valor,
                 a.tanque_completo,
                 a.quilometragem
          FROM abastecimento a
          WHERE a.moto_id = ?
          ORDER BY a.data_abastecimento ASC
          '''
    cursor.execute(sql, (moto_id,))
    dados = cursor.fetchall()
    conn.close()

    return dados


def atualizar_consumo(moto_id,consumo):
    conn = get_conexao()
    cursor = conn.cursor()

    sql = '''
          UPDATE moto
          SET cosumo = ?
          WHERE id = ? 
          '''

    cursor.execute(sql, (consumo, moto_id))
    conn.commit()
    conn.close()



