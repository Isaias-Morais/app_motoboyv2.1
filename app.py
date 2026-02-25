import sys
from database.base import Base
from database.create_tables import create_table
from database.engine import engine
from repository.moto_repository import listar_moto
from repository.abastecimento_repositorio import listar_abastecimento
from repository.dia_de_trabalho_repositorio import listar_dia_de_trabalho
from repository.manutencao_repository import listar_manutencao
from repository.motoboy_repository import listar_motoboys, definir_moto_ativa_motoboy, busca_moto_ativa_motoboy
from service.abastecimento_service import *
from service.manutencao_service import registra_manutencao
from service.moto_service import *
from service.dia_de_trabalho_service import *
from service.motoboy_service import *
from service.exluir_moto import excluir_moto_geral
from service.resumo_dia_service import *
from validacoes.motoboy_existe import *
from interface.utilidades import *



session = SessionLocal()

print(listar_motoboys(session))
create_table()

cabecalho("APP_MOTOBOY",55)

moto = busca_moto_ativa_motoboy(session)

while True:
    if not motoboy_existe_id(session):
        print('Adicione seus dados para continuarmos')
        nome = (input("Nome : "))
        idade = leiaint('Idade : ')
        email = (input('Email : '))
        resultado = registrar_motoboy(nome, idade, email)
        print(resultado)
        if resultado == True:
            break


    while True:

        cabecalho("RESUMO DO DIA", 55)
        resumo = resumo_dia()
        print(f'moto ativa - {moto}')
        for chave, valor in resumo.items():
            print(f'{chave:<26} : {str(valor):>26}')

        resposta_menu = menu("MENU", ['MOTO', 'DIA_TRABALHADO', 'ABASTECIMENTO/MANUTENÇAO', 'HISTORICO', 'SAIR'], 55)

        match resposta_menu:
            case 1:
                cabecalho('MOTO', 55)
                while True:
                    resposta_moto_menu = menu('MOTO', ['REGISTRA MOTO',"ATIVA MOTO","EXCLUIR MOTO",'VOLTAR'])
                    match resposta_moto_menu:
                        case 1:
                                marca = input('Qual e a marca de sua moto? ')
                                modelo = input('Qual o modelo de sua moto? ')
                                ano = leiaint('Qual o ano de sua moto? ')
                                quilometragem = leiaint('Qual a quilometragem de sua moto? ')
                                consumo = leiaint("Qual consumo medio de sua moto? ")
                                print(registra_moto(marca,modelo,ano,quilometragem,consumo))

                        case 2:
                            print(listar_moto(session))
                            id = leiaint('ID : ')
                            print(definir_moto_ativa_motoboy(session,id))

                        case 3:
                            listar_moto(session)
                            id = leiaint('ID : ')
                            excluir_moto_geral(id)

                        case 4:
                            break

                        case _:
                            print('digite um opcao valida ')
                            continue

            case 2:
                cabecalho('DIA DE TRABALHO',55)
                resp = sim_ou_nao('Quer definir uma data especifica? ')
                if not resp:
                    dia = None
                    mes = None
                    ano = None
                else:
                    dia = leiaint("DIA : ")
                    mes = leiaint("MES : ")
                    ano = leiaint('ANO : ')

                km_inicial = leiaint('Quilometragem inicial : ')
                km_final = leiaint("Quilometragem final : ")
                ganho_bruto = leiafloat("Faturamento bruto :  ")
                listar_moto(session)
                moto_id = leiaint('ID : ')

                print(registra_dia_de_trabalho(dia,mes,ano,km_inicial,km_final,ganho_bruto,moto_id))

            case 3:
                while True:
                    resposta_menu_abasmanu = menu('ABASTECIMENTO/MANUTENÇÕES',['ABASTECIMENTO','MANUTENÇÕES',"VOLTAR"], 55)
                    match resposta_menu_abasmanu:
                        case 1 :
                            cabecalho('ABASTECIMENTO', 55)
                            resp = sim_ou_nao('Quer definir uma data especifica? ')
                            if not resp:
                                dia = None
                                mes = None
                                ano = None
                            else:
                                dia = leiaint("DIA : ")
                                mes = leiaint("MES : ")
                                ano = leiaint('ANO : ')
                            posto = input("Local do abastecimento : ")
                            litros = leiafloat('Litros/L : ')
                            valor = leiafloat('Valor R$ : ')
                            tanque_completo = sim_ou_nao('Tanque cheio : ')
                            quilometragem_abastecimento = leiaint('KM do abastecimento')
                            listar_moto(session)
                            moto_id = leiaint('ID : ')
                            print(registra_abastecimento(dia,mes,ano,posto,litros,valor,tanque_completo,quilometragem_abastecimento,moto_id))

                        case 2:
                            cabecalho('MANUTENÇÃO', 55)
                            resp = sim_ou_nao('Quer definir uma data especifica')
                            if not resp:
                                dia = None
                                mes = None
                                ano = None
                            else:
                                dia = leiaint("DIA : ")
                                mes = leiaint("MES : ")
                                ano = leiaint('ANO : ')
                            tipo = input('Tipo de manuteção : ')
                            descricao = input('Descricao : ')
                            valor = leiafloat('Valor : ')
                            quilometragem_manutencao = leiaint('KM da Manutenção : ')
                            listar_moto()
                            moto_id = leiaint('ID : ')
                            print(registra_manutencao(dia, mes, ano, tipo, descricao, valor, quilometragem_manutencao, moto_id))
                        case 3:
                            break

                        case _:
                            print('digite um opcao valida ')
                            continue


            case 4 :
                resp_historico = menu('HISTORICO',['Dia',"Abastecimenos" , 'Manutenção'],55)

                match resp_historico:
                    case 1:
                        listar_dia_de_trabalho()
                    case 2:
                        listar_abastecimento()
                    case 3:
                        listar_manutencao()

            case 5:
                sys.exit()

            case _:
                print('digite um opcao valida ')
                continue