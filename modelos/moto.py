from datetime import datetime

class Moto:

    def __init__(self,modelo,cor,quilometragem = 0):
        self.modelo = modelo
        self.cor = cor
        self.quilometrgem = quilometragem
        self.abastecimento = []
        self.manutencoes = []

    def __str__(self):
        return f"{self.modelo},{self.cor}"

    def RegistraAbastecimento(self,valor,litros,completo = False,  data = None):
        if not isinstance(valor,int ,float) or valor <0:
            return f'Digite um valor valido'
        if not isinstance(litros,int ,float) or valor <0:
            return f'Digite um litragem valida'
        if not isinstance(completo,bool):
            return f'Digite um valor bool valido'
        if not isinstance(data,datetime) or data == None:
            return f'Digite uma data valida'
        else:
            dia = data or datetime.today()
            valorRS = valor
            litrosL = litros
            tanque_completo = completo
            tanque_completo_str = 'Sim' if tanque_completo else 'Não'
            PrecoLitro = valor / litros
            registor ={
                'Dia':dia,
                'Valor':valorRS,
                'Litros':litrosL,
                'Preço_Do_litro':PrecoLitro,
                'Completou':tanque_completo_str
            }
            self.abastecimento.append(registor)

    def RegistraManutencao(self,peca='',valor_peca=0,quilometrgem_de_troca=None, data = None):

        if not isinstance(valor_peca, int , float):
            return 'Digite um valor valido'

        if not isinstance(quilometrgem_de_troca,int,float):
            return  'Digite uma quilometragem de troca '

        if not isinstance(data,datetime) or data == None:
            return 'Digite uma data valida'
        else:
            dia = data
            pecaStr = peca
            valor = valor_peca
            QuilometrgemDeTroca = quilometrgem_de_troca

            registro = {
                'Dia':dia,
                'Peça_trocada':pecaStr,
                'Valor':valor,
                'Quilometragem_de_troca':QuilometrgemDeTroca
            }
            self.manutencoes.append(registro)





