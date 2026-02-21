from models.manutencao_model import Manutencao
from database.session import SessionLocal
from repository.base_repository import salvar_objeto
from validacoes.manutencao_validacao import validacao_manutencao
from validacoes.valida_data import valida_data
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
    return manutencao