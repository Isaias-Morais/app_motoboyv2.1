from database.engine import engine
from database.base import Base


# cria as tabelas
def create_table():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        raise Exception(f'Erro a criar tabelas no banco de dados: {e}')
