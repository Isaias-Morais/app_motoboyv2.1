from models.abastecimento_model import Abastecimento



def listar_abastecimento(session):
    abastecimentos = session.query(Abastecimento).all()
    return abastecimentos


def excluir_abastecimentos(session,moto_id):
    abastecimento = session.query(
        Abastecimento
    ).filter(
        Abastecimento.moto_id == moto_id
    ).first
    if abastecimento:
        session.delete(abastecimento)
        session.commit()
        return True
    else:
        return False


def historico_abastecimentos(session,moto_id):
    abastecimentos = session.query(
        Abastecimento
    ).filter(
        Abastecimento.moto_id == moto_id
    ).order_by(
        Abastecimento.data_abastecimento
    ).all()
    return abastecimentos
