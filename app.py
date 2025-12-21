
from BancoDeDados.abastecimento_repositorio import *
from servicos.add_abastecimento import registra_abastecimento
from BancoDeDados.init_db import criar_tabelas
criar_tabelas()

registra_abastecimento(None,'BR',10,60,True,1000)
listar_abastecimento()