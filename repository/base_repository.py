from sqlalchemy.orm import Session

from service.resumo_dia_service import session


def salvar_objeto(session:Session, obj):

    session.add(obj)
    session.commit()
    return obj


def atualizar_objeto(session:Session,objeto, dados):
    for campo, valor in dados.model_dump(
        exclude_unset=True
    ).items():

        setattr(objeto, campo, valor)

        session.commit()
        session.refresh(objeto)


    return objeto