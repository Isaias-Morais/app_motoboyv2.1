from models.dia_de_trabalho_model import Dia_de_trabalho
from database.session import SessionLocal
from repository.base_repository import salvar_objeto
from validacoes.dia_de_trabalho_validacao import validacao_dia_de_trabalho
from validacoes.valida_data import valida_data
from datetime import date

session = SessionLocal()

def registra_dia_de_trabalho(
        dia=None,
        mes=None,
        ano=None,
        km_inicial=None,
        km_final=None,
        ganhon_bruto=None,
        moto_id=None
    ):

    valido , erro = validacao_dia_de_trabalho(km_inicial,km_final,ganhon_bruto,moto_id)
    if not valido:
        return erro

    valido_data, data = valida_data(dia, mes, ano)
    if not valido_data:
        data = date.today()

    dia_de_trabalho = Dia_de_trabalho(
        data_trabalhada=data,
        quilometragem_inicial=km_inicial,
        quilometragem_final=km_final,
        ganho_bruto= ganhon_bruto,
        moto_id=moto_id
    )
    salvar_objeto(session,dia_de_trabalho)
    return dia_de_trabalho
