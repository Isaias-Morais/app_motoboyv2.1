from BancoDeDados.conexao import get_conexao
def criar_tabelas():
    criar_tabela_motoboy()
    criar_tabela_motos()

def criar_tabela_motoboy():
    conn = get_conexao()
    curso = conn.cursor()
    curso.execute(
        '''
            CREATE TABLE IF NOT EXISTS motoboy(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            email TEXT NOT NULL
            )
        '''
    )
    conn.commit()
    conn.close()

def criar_tabela_motos():
    conn = get_conexao()
    curso = conn.cursor()
    curso.execute(
        """
            CREATE TABLE IF NOT EXISTS moto(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            marca TEXT NOT NULL,
            modelo TEXT NOT NULL,
            ano INTEGER NOT NULL,
            quilometragem INTEGER NOT NULL,
            cosumo REAL NOT NULL,
            motoboy_id INTEGER NOT NULL,
            FOREIGN KEY (motoboy_id) REFERENCES motoboy(id)
            )
        """
    )
    conn.commit()
    conn.close()