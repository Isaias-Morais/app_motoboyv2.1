from database.engine import engine
from database.base import Base
from models.motoboy_model import Motoboy
from models.moto_model import Moto
from models.abastecimento_model import Abastecimento
from models.manutencao_model import Manutencao
from models.dia_de_trabalho_model import Dia_de_trabalho



# cria as tabelas
def create_table():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        raise Exception(f'Erro a criar tabelas no banco de dados: {e}')
