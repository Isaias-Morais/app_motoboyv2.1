from sqlalchemy.orm import Mapped, mapped_column, relationship, Session
from sqlalchemy import REAL, ForeignKey
from database.base import Base
from models.motoboy_model import Motoboy

class Moto(Base):
    __tablename__ = 'motos'

    id : Mapped[int] = mapped_column(primary_key=True)
    marca : Mapped[str] = mapped_column(nullable=False)
    modelo : Mapped[str] = mapped_column(nullable=False)
    ano : Mapped[int] = mapped_column(nullable=False)
    quiometragem : Mapped[int] = mapped_column(nullable=False)
    cosumo : Mapped[float] = mapped_column(REAL,nullable=False)
    motoboy_id : Mapped[int] = mapped_column(ForeignKey('motoboy.id'))
    abastecimentos : Mapped[list['Abastecimento']] = relationship(back_populates='moto')
    motoboy : Mapped['Motoboy'] = relationship(back_populates='moto')

    def __repr__(self):
        return f'{self.id},{self.marca},{self.modelo},{self.ano},{self.quiometragem},{self.cosumo},{self.motoboy_id}'
