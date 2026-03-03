from models.motoboy_model import Motoboy

def motoboy_existe_id(session,id_motoboy=1):
    return session.get(Motoboy,id_motoboy)