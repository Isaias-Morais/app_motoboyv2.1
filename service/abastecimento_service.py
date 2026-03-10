from repository.abastecimento_repository import abastecimento_existe
from repository.finaceiro_repository import busca_abastecimento_consumo_medio
from database.session import SessionLocal
from models.abastecimento_model import Abastecimento
from repository.base_repository import salvar_objeto
from repository.moto_repository import quilometragem_atual, atualizar_quilometragem
from service.moto_service import atualizar_consumo_moto
from service.calculos_service import calcular_km_rodados, calcular_consumo_medio_real
from validators.abastecimento_validators import validacao_abastecimento
from validators.moto_validacao import validar_quilometragem_nova
from validators.valida_data import valida_data
from datetime import date

session = SessionLocal()

def registra_abastecimento(
        dia=None,
        mes=None,
        ano=None,
        posto=None,
        litros=None,
        valor=None,
        tanque_completo=False,
        quilometragem_abastecimento=None,
        moto_id=None
    ):
    valido , erro = validacao_abastecimento(posto,litros,valor,tanque_completo,quilometragem_abastecimento,moto_id)
    if not valido:
        return erro

    valido_data , data = valida_data(dia,mes,ano)
    if not valido_data:
        data = date.today()



    abastecimento = Abastecimento(
        data_abastecimento=data,
        posto=posto,
        litros=litros,
        valor=valor,
        tanque_completo=tanque_completo,
        quilometragem_abastecimento=quilometragem_abastecimento,
        moto_id=moto_id
        )

    if not abastecimento_existe(session,moto_id,quilometragem_abastecimento):
        salvar_objeto(session,abastecimento)
    else:
        return 'abastecimento ja existente'

    if not tanque_completo:
        return None

    historico = busca_abastecimento_consumo_medio(session,moto_id)

    if not historico or len(historico) < 3:
        return None

    km_litros = calcular_km_rodados(historico)

    if not km_litros:
        return None


    consumo_medio = calcular_consumo_medio_real(km_litros)

    atualizar_consumo_moto(session=session,moto_id=moto_id,consumo=consumo_medio)

    km_atual = quilometragem_atual(session, moto_id)

    valido, erro = validar_quilometragem_nova(km_atual, quilometragem_abastecimento)
    if valido:
        atualizar_quilometragem(session, moto_id, quilometragem_abastecimento)
    else:
        return False

    return abastecimento

