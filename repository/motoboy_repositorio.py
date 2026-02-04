from database.setup import get_conexao

def salvar_motoboy(motoboy):
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                    INSERT INTO motoboy(nome,idade,email)
                    VALUES (%s,%s,%s)
                    RETURNING id
                """,(motoboy._nome,motoboy._idade,motoboy._email)
            )
            id_gerado = cursor.fetchone()[0]

            motoboy.id = id_gerado



def listar_motoboy():
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                    SELECT * FROM motoboy
                """
            )
            motoboy = cursor.fetchall()

            for motoboy in motoboy:
                print(motoboy)
