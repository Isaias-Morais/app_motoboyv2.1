from database.engine import engine
from database.base import Base
from database.session import SessionLocal
from models.motoboy_model import Motoboy
from models.moto_model import Moto
from models.abastecimento_model import Abastecimento
from models.manutencao_model import Manutencao
from models.dia_de_trabalho_model import Dia_de_trabalho
from repository.motoboy_repository import listar_motoboys



# cria as tabelas
Base.metadata.create_all(bind=engine)

db = SessionLocal()

motoboy = Motoboy(
    nome="Zal",
    email="zal@email.com",
    idade=18
)

db.add(motoboy)
db.commit()

motoboys = listar_motoboys(db)
print(motoboys)

