from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import  ForeignKey
from database.base import Base



class Moto(Base):
    __tablename__ = 'motos'

    id : Mapped[int] = mapped_column(primary_key=True)
    marca : Mapped[str] = mapped_column(nullable=False)
    modelo : Mapped[str] = mapped_column(nullable=False)
    ano : Mapped[int] = mapped_column(nullable=False)
    quilometragem : Mapped[int] = mapped_column(nullable=False)
    consumo : Mapped[float] = mapped_column(nullable=False)

    motoboy_id : Mapped[int] = mapped_column(ForeignKey('motoboys.id',ondelete="CASCADE"))

    motoboy: Mapped['Motoboy'] = relationship(back_populates='motos')
    abastecimentos : Mapped[list['Abastecimento']] = relationship(back_populates='moto',cascade="all, delete-orphan")
    manutencoes : Mapped[list['Manutencao']] = relationship(back_populates='moto',cascade="all, delete-orphan")
    dias_trabalhados : Mapped[list['Dia_de_trabalho']] = relationship(back_populates='moto',cascade="all, delete-orphan")

    def __repr__(self):
        return f'{self.id},{self.marca},{self.modelo},{self.ano},{self.quilometragem},{self.consumo},{self.motoboy_id}'
