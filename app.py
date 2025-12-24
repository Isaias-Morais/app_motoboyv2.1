
from BancoDeDados.manutecao_repositorio import *
from servicos.add_manutecao import registra_manutencao
from BancoDeDados.init_db import criar_tabelas

import sqlite3
criar_tabelas()
registra_manutencao(None,None,None,'oleo','2 troca do mes ',40,17000,1)
listar_manutencao()


conn = get_conexao()
curso = conn.cursor()
curso.execute("""
        SELECT
            motoboy.nome,
            moto.modelo,
            abastecimento.litros,
            abastecimento.valor,
            abastecimento.data_abastecimento
        FROM motoboy
        JOIN moto ON moto.motoboy_id = motoboy.id
        JOIN abastecimento ON abastecimento.moto_id = moto.id
""")

print("Motoboy | Moto | Litros | Valor | Data")
print("-" * 50)

resultados = curso.fetchall()

for linha in resultados:
    print(linha)

conn.close()


