from BancoDeDados.init_db import get_conexao

def salvar_manutecao(manutencao):
    conn = get_conexao()
    curso = conn.cursor()
    curso.execute(
        '''
            INSERT INTO manutencao(
                data_manutencao,
                tipo,
                descricao,
                valor,
                moto_id,
                quilometragem
            )   
             VALUES(?,?,?,?,?,?)  
        ''',(
            manutencao._data,
            manutencao._tipo,
            manutencao._descricao,
            manutencao._valor,
            manutencao._moto,
            manutencao._quilometragem
        )
        )
    manutencao.id = curso.lastrowid
    conn.commit()
    conn.close()

def listar_manutencao():
    conn = get_conexao()
    curso = conn.cursor()
    curso.execute(
        """
            SELECT * FROM manutencao
        """
    )
    manutencoes = curso.fetchall()

    for manutencao in manutencoes:
        print(manutencao)


def excluir_manutencao(moto_id):
    conn = get_conexao()
    curso = conn.cursor()

    sql = '''
          DELETE 
          FROM manutencao
          WHERE moto_id = ? 
          '''

    curso.execute(sql, (moto_id,))

    conn.commit()
    conn.close()


def historico_manutencoes(moto_id):
    conn = get_conexao()
    cursor = conn.cursor()
    sql = '''
    SELECT
        m.data_manutencao,
        m.tipo,
        m.descricao,
        m.valor,
        m.quilometragem
    FROM manutencao m
        WHERE m.moto_id = ?
    ORDER BY m.data_manutencao ASC
          '''
    cursor.execute(sql,(moto_id,))
    dados = cursor.fetchall()
    conn.close()

    return dados