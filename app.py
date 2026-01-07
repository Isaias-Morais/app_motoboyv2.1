from BancoDeDados.conexao import get_conexao
from BancoDeDados.init_db import criar_tabelas
from servicos.add_motoboy import registrar_motoboy
from validacoes.motoboy_existe import motoboy_existe

get_conexao()
criar_tabelas()
while True:
    if not  motoboy_existe():
        nome  = (input("Nome : "))
        idade = (input('Idade : '))
        email = (input('Email : '))
        print(registrar_motoboy(nome,idade,email))
        break

