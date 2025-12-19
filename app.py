from servicos.add_motoboy import registrar_motoboy
from BancoDeDados.motoboy_repositorio import *
from BancoDeDados.moto_repositorio import *
from servicos.add_moto import registra_moto
from BancoDeDados.init_db import criar_tabelas
criar_tabelas()

registra_moto('HONDA','AFRICA TWIN',2025,0,20,1)
listar_moto()