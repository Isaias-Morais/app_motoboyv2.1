from models.moto_model import Moto
from database.session import SessionLocal
from repository.base_repository import salvar_objeto
from validators.moto_validacao import validacao_moto
from validators.abastecimento_validators import validacao_consumo
from repository.moto_repository import atualizar_consumo,excluir_moto,moto_existe
from repository.motoboy_repository import redefinir_moto_ativa_motoboy, busca_moto_ativa_motoboy
from repository.dia_de_trabalho_repositorio import excluir_dias_trabalhados
from repository.manutencao_repository import excluir_manutencao
from repository.abastecimento_repository import excluir_abastecimentos


session = SessionLocal()

def registra_moto(
        marca=None,
        modelo=None,
        ano=None,
        quilometragem=None,
        consumo=None
    ):

    valido , erro = validacao_moto(marca,modelo,ano,quilometragem,consumo)

    if not valido:
        return erro
    else:
        moto = Moto(
            marca=marca,
            modelo=modelo,
            ano=ano,
            quilometragem=quilometragem,
            consumo=consumo,
            motoboy_id=1)

        print(moto.__dict__)
        salvar_objeto(session,moto)

        return moto


def atualizar_consumo_moto(session,moto_id=0,consumo=0):

    if not moto_existe(session,moto_id):
        return False, 'moto não existe'

    if not validacao_consumo(consumo):
        return False, 'consumo invalido'

    atualizar_consumo(session,moto_id,consumo)
    return True,"consumo atualizado"


def excluir_moto_geral(session,moto_id):
    id = busca_moto_ativa_motoboy(session)
    if not moto_existe(session,moto_id):
        return False, 'Moto nao existente'

    excluir_manutencao(session,moto_id)
    excluir_abastecimentos(session,moto_id)
    excluir_dias_trabalhados(session,moto_id)
    excluir_moto(session,moto_id)

    if id == moto_id:
        redefinir_moto_ativa_motoboy(session)

    return True,'Moto excluida com sucesso'
