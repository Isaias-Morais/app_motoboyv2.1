from models.manutencao_model import Manutencao
from database.session import SessionLocal
from repository.base_repository import salvar_objeto
from repository.moto_repository import quilometragem_atual, atualizar_quilometragem
from validators.manutencao_validacao import validacao_manutencao
from validators.moto_validacao import validar_quilometragem_nova
from validators.valida_data import valida_data
from datetime import date

session = SessionLocal()

def registra_manutencao(
        dia=None,
        mes=None,
        ano=None,
        tipo=None,
        descricao=None,
        valor=None,
        quilometragem_manutencao=None,
        moto_id=None
    ):

    valido , erro = validacao_manutencao(tipo,descricao,valor,quilometragem_manutencao,moto_id)
    if not valido:
        return erro

    valido_data , data = valida_data(dia,mes,ano)
    if not valido_data:
        data = date.today

    manutencao = Manutencao(
        data_manutencao=data,
        tipo=tipo,
        descricao=descricao,
        valor=valor,
        quilometragem_manutencao=quilometragem_manutencao,
        moto_id=moto_id
        )
    salvar_objeto(session,manutencao)

    km_atual = quilometragem_atual(session, moto_id)

    if validar_quilometragem_nova(km_atual, quilometragem_manutencao):
        atualizar_quilometragem(session, moto_id, quilometragem_manutencao)

    return manutencao