from sqlalchemy import Date, Numeric, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from database.base import Base
from decimal import Decimal

class Dia_de_trabalho(Base):
    __tablename__ = 'dia_de_trabalho'

    id : Mapped[int] = mapped_column(primary_key=True)
    data_trabalhada : Mapped[date] = mapped_column(Date,nullable=False)
    quilometragem_inicial : Mapped[int] = mapped_column(nullable=False)
    quilometragem_final : Mapped[int] = mapped_column(nullable=False)
    ganho_bruto : Mapped[Decimal] = mapped_column(Numeric(10, 2),nullable=False)

    moto_id : Mapped[int] = mapped_column(Integer,ForeignKey('motos.id'))

    moto : Mapped['Moto'] = relationship(back_populates="dias_trabalhados")

    def __repr__(self):
        return f'|{self.id}|{self.data_trabalhada}|{self.quilometragem_inicial}|{self.quilometragem_final}|{self.ganho_bruto}|{self.moto_id}|'