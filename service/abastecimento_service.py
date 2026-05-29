from models.moto_model import Moto
from repository.abastecimento_repository import abastecimento_existe
from repository.finaceiro_repository import busca_abastecimento_consumo_medio
from database.session import SessionLocal
from models.abastecimento_model import Abastecimento
from repository.base_repository import salvar_objeto
from repository.moto_repository import quilometragem_atual, atualizar_quilometragem
from sqlalchemy.orm import Session
from service.motoboy_service import busca_moto_ativa_service
from service.moto_service import atualizar_consumo_moto
from service.calculos_service import calcular_km_rodados, calcular_consumo_medio_real
from validators.moto_validacao import validar_quilometragem_nova
from validators.valida_data import valida_data
from datetime import date
from schermas.abastecimento_schermas import AbastecimentoCreate


def registra_abastecimento(abastecimento:AbastecimentoCreate,session:Session,motoboy_id:int):
    valido_data, data = valida_data(abastecimento.dia,abastecimento.mes, abastecimento.ano)
    if not valido_data:
        data = date.today()

    moto:Moto = busca_moto_ativa_service(session=session,motoboy_id=motoboy_id)

    novo_abastecimento = Abastecimento(
            data_abastecimento=data,
            posto=abastecimento.posto,
            litros=abastecimento.litros,
            valor=abastecimento.valor,
            tanque_completo=abastecimento.tanque_completo,
            quilometragem_abastecimento=abastecimento.quilometragem_abastecimento,
            moto_id=moto.id
        )


    if not abastecimento_existe(session,moto.id,abastecimento.quilometragem_abastecimento):
        return salvar_objeto(session,novo_abastecimento)
    else:
        return 'abastecimento ja existente'


# def cosumo_ou_historico_abastecimento(session:Session,moto_id:int):
#
#     historico = busca_abastecimento_consumo_medio(session,moto.id)
#
#     if not historico or len(historico) < 3:
#         return None
#
#     km_litros = calcular_km_rodados(historico)
#
#     if not km_litros:
#         return None
#
#
#     consumo_medio = calcular_consumo_medio_real(km_litros)
#
#     atualizar_consumo_moto(session=session,moto_id=moto.id,consumo=consumo_medio)
#
#     km_atual = quilometragem_atual(session, moto.id)
#
#     valido, erro = validar_quilometragem_nova(km_atual, abastecimento.quilometragem_abastecimento)
#     if valido:
#         atualizar_quilometragem(session, moto.id, abastecimento.quilometragem_abastecimento)
#     else:
#         return False
#
#     return abastecimento
#
