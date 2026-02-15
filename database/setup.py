import psycopg

CONN_FING = "host=localhost user=postgres password=postgres dbname=motoboy_finacias"

def cria_banco():
    conn = psycopg.connect(
        host='localhost',
        user="postgres",
        password='postgres',
        dbname="postgres"
    )
    conn.autocommit = True

    with conn.cursor() as cur:
        sql = "CREATE DATABASE motoboy_finacias"
        cur.execute(sql)
    conn.close()

def get_conexao():
    try:
        conn = psycopg.connect(CONN_FING)
        return conn
    except Exception as e:
        print('Erro : ' ,e)
        return None

cria_banco()