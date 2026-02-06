from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, foreign

from database.base import Base

class Motoboy(Base):
    __tablename__ = 'motoboy'

    id : Mapped[int] = mapped_column(primary_key=True)
    nome : Mapped[str] = mapped_column(nullable=False)
    idade : Mapped[int] = mapped_column(nullable=False)
    email : Mapped[str] = mapped_column(nullable=False)
    moto_ativa : Mapped[int] = mapped_column(ForeignKey("moto.id"),nullable=True)

    def __repr__(self):
        return f'|ID-{self.id}|nome-{self.nome}|idade-{self.idade}|email-{self.email}|moto_ativa-{self.moto_ativa}|'

