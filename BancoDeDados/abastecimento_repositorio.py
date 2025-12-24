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
