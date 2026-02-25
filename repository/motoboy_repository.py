from models.motoboy_model import Motoboy

def listar_motoboys(session):
    return session.query(Motoboy).all()

def busca_moto_ativa_motoboy(session):
    moto = session.query(Motoboy).filter(Motoboy.moto_ativa != None).first()
    return moto.id if moto else None

def definir_moto_ativa_motoboy(session,moto_id):
    motoboy = session.query(Motoboy).filter(Motoboy.id == 2).first()
    if motoboy:
        motoboy.moto_ativa = moto_id
        session.commit()
    else:
        return False

def redefinir_moto_ativa_motoboy(session):
    motoboy = session.query(Motoboy).filter(Motoboy.id == 1).first()
    if motoboy:
        motoboy.moto_ativa = None
        session.commit()
    else:
        return False

