from sqlalchemy import Date, Numeric, Integer, ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship
from decimal import Decimal
from database.base import Base
from datetime import date

class Manutencao(Base):
    __tablename__ = "manutencao"

    id : Mapped[int] = mapped_column(primary_key=True)
    data_manutencao : Mapped[date] = mapped_column(Date,nullable=False)
    tipo : Mapped[str] = mapped_column(nullable=False)
    descricao : Mapped[str]  = mapped_column(nullable=True)
    valor : Mapped[Decimal] = mapped_column(Numeric(10, 2),nullable=False)
    quilometragem_manutencao : Mapped[int] = mapped_column(nullable=False)

    moto_id : Mapped[int] = mapped_column(Integer,ForeignKey('motos.id',ondelete="CASCADE"))

    moto: Mapped['Moto'] = relationship(back_populates='manutencoes')

    def __repr__(self):
        return f'{self.id}|{self.data_manutencao}|{self.tipo}|{self.descricao}|{self.valor}|{self.quilometragem_manutencao}|'


