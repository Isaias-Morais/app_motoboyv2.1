from BancoDeDados.conexao import get_conexao

def salvar_motoboy(motoboy):
    conn = get_conexao()
    curso = conn.cursor()
    curso.execute(
        """
            INSERT INTO motoboy(nome,idade,email)
            VALUES (%s,%s,%s)
            RETURNING id
        """,(motoboy._nome,motoboy._idade,motoboy._email)
    )
    id_gerado = curso.fetchone()[0]

    motoboy.id = id_gerado

    conn.commit()
    conn.close()


def listar_motoboy():
    conn = get_conexao()
    curso = conn.cursor()
    curso.execute(
        """
            SELECT * FROM motoboy
        """
    )
    motoboy = curso.fetchall()

    for motoboy in motoboy:
        print(motoboy)

    conn.close()
