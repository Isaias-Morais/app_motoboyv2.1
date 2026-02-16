from sqlalchemy import Date, Boolean, Numeric, ForeignKey
from database.base import Base
from datetime import date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from decimal import Decimal


class Abastecimento(Base):
    __tablename__ = 'abastecimentos'

    id: Mapped[int] = mapped_column(primary_key=True)
    data_abastecimento: Mapped[date] = mapped_column(Date, nullable=False)
    posto: Mapped[str] = mapped_column(nullable=False)
    litros: Mapped[float] = mapped_column(nullable=False)
    valor: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    tanque_completo: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    quilometragem_abastecimento: Mapped[int] = mapped_column(nullable=False)

    moto_id: Mapped[int] = mapped_column(ForeignKey('motos.id'), nullable=False)

    moto : Mapped['Moto'] = relationship(back_populates='abastecimentos')

    def __repr__(self):
        return f'data-{self.data_abastecimento},valor-{self.valor},litros-{self.liros}taque_cheio{self.tanque_completo},quilometro_do_abastecimento{self.tcompleto}'

    @property
    def preco_litro(self) -> Decimal:
        if self.litros <= 0:
            raise ValueError("litro deve ser maior que zero")
        else:
            return self.valor / Decimal(str(self.litros))
