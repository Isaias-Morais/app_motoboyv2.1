from BancoDeDados.conexao import get_conexao
def criar_tabelas():
    criar_tabela_motoboy()
    criar_tabela_motos()
    criar_tabela_abatecimento()
    criar_tabela_manutencao()
    criar_tabela_dia_de_trabalho()

def criar_tabela_motoboy():
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                '''
                    CREATE TABLE IF NOT EXISTS motoboy(
                    id SERIAL PRIMARY KEY ,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL,
                    email TEXT NOT NULL,
                    moto_ativa_id INTEGER 
                    );
                '''
                )


def criar_tabela_motos():
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                    CREATE TABLE IF NOT EXISTS moto(
                    id SERIAL PRIMARY KEY ,
                    marca TEXT NOT NULL,
                    modelo TEXT NOT NULL,
                    ano INTEGER NOT NULL,
                    quilometragem INTEGER NOT NULL,
                    cosumo REAL NOT NULL,
                    motoboy_id INTEGER NOT NULL,
                    FOREIGN KEY (motoboy_id) REFERENCES motoboy(id)
                    );
                """
                )


def criar_tabela_abatecimento():
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                    CREATE TABLE IF NOT EXISTS abastecimento(
                    id SERIAL PRIMARY KEY ,
                    moto_id INTEGER NOT NULL,
                    data_abastecimento DATE,
                    posto TEXT NOT NULL,
                    valor REAL NOT NULL,
                    litros REAL NOT NULL,
                    valor_litro REAL NOT NULL,
                    tanque_completo BOOLEAN NOT NULL,
                    quilometragem INTEGER NOT NULL,
                    FOREIGN KEY (moto_id) references moto(id)
                );
                """
        
                )

def criar_tabela_manutencao():
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                '''
                    CREATE TABLE IF NOT EXISTS manutencao(
                    id SERIAL PRIMARY KEY ,
                    moto_id INTEGER NOT NULL,
                    data_manutencao DATE,
                    tipo TEXT NOT NULL,
                    descricao TEXT,
                    valor REAL NOT NULL,
                    quilometragem INTEGER NOT NULL,
                    FOREIGN KEY (moto_id) references moto(id)
                    );
                '''
                )


def criar_tabela_dia_de_trabalho():
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                '''
                    CREATE TABLE IF NOT EXISTS dia_de_trabalho(
                    id SERIAL PRIMARY KEY ,
                    moto_id INTEGER NOT NULL,
                    data_trabalhada DATE,
                    quilometragem_inicial INTEGER NOT NULL,
                    quilometragem_final INTEGER NOT NULL,
                    ganho_bruto REAL NOT NULL,
                    FOREIGN KEY (moto_id) references moto(id)
                    )   ;
                '''
            )