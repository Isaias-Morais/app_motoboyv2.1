from sqlalchemy import Date,Numeric
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from database.base import Base
from decimal import Decimal

class dia_de_trabalho(Base):
    __tablename__ = 'dia_de_trabalho'

    id : Mapped[int] = mapped_column(primary_key=True)
    data_trabalhada : Mapped[date] = mapped_column(Date,nullable=False)
    quilometragem_inicial : Mapped[int] = mapped_column(nullable=False)
    quilometragem_final : Mapped[int] = mapped_column(nullable=False)
    ganho_bruto : Mapped[Decimal] = mapped_column(Numeric(10, 2),nullable=False)