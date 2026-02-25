from repository.moto_repository import *
from repository.dia_de_trabalho_repositorio import excluir_dias_trabalhados
from repository.manutencao_repository import excluir_manutencao
from repository.abastecimento_repositorio import excluir_abastecimentos
from repository.motoboy_repository import redefinir_moto_ativa_motoboy, busca_moto_ativa_motoboy

from validacoes.moto_exitente import moto_existe


def excluir_moto_geral(moto_id):
    id = busca_moto_ativa_motoboy()
    if not moto_existe(moto_id):
        return False, 'Moto nao existente'

    excluir_manutencao(moto_id)
    excluir_abastecimentos(moto_id)
    excluir_dias_trabalhados(moto_id)
    excluir_moto(moto_id)

    if id == moto_id:
        redefinir_moto_ativa_motoboy()

    return True,'Moto excluida com sucesso'

