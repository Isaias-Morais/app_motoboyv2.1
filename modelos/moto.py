from datetime import datetime

class Moto:

    def __init__(self,modelo,cor,quilometragem = 0):
        self._modelo = modelo
        self._cor = cor
        self._quilometragem_total = quilometragem
        self._abastecimento = []
        self._manutencoes = []

    def __str__(self):
        return f"{self._modelo},{self._cor}"

    def RegistraAbastecimento(self,valor,litros,completo = False,quilometragem_de_abastecimento = None,  data = None):
        if not isinstance(valor,(int ,float)) or valor <0:
            return f'Digite um valor valido'
        if not isinstance(litros,(int ,float)) or valor <=0:
            return f'Digite um litragem valida'
        if not isinstance(completo,(bool)):
            return f'Digite um valor bool valido'
        if not isinstance(quilometragem_de_abastecimento(int,float)) or valor <0:
            return f'Digite quilometragem valida'
        dia = data or datetime.today()
        if not isinstance(dia,(datetime)):
            return f'Digite uma data valida'
        else:
            if quilometragem_de_abastecimento > self._quilometragem_total:
                self._quilometragem_total = quilometragem_de_abastecimento
            tanque_completo = completo
            preco_litro = valor / litros
            registor ={
                'Dia':dia.strftime('%d/%m/%Y'),
                'Valor':valor,
                'Litros':litros,
                'Preço_Do_litro':preco_litro,
                'Quilometragem_ultimo_abastecimento':quilometragem_de_abastecimento,
                'Completou':'Sim' if tanque_completo else 'Não'
            }
            self._abastecimento.append(registor)

    def RegistraManutencao(self,peca='',valor_servico=0,quilometragem_de_troca=None, data = None):

        if not isinstance(valor_servico, (int , float)):
            return 'Digite um valor valido'
        if quilometragem_de_troca is None:
            quilometragem_de_troca = 0
        if not isinstance(quilometragem_de_troca,(int,float)):
            return  'Digite uma quilometragem de troca '
        dia = data or datetime.today()
        if not isinstance(dia,(datetime)):
            return 'Digite uma data valida'
        else:
            if quilometragem_de_troca > self._quilometragem_total:
                self._quilometragem_total = quilometragem_de_troca
            registro = {
                'Dia':dia.strftime('%d/%m/%Y'),
                'Peça_trocada':peca,
                'Valor':valor_servico,
                'Quilometragem_de_troca':quilometragem_de_troca
            }
            self._manutencoes.append(registro)

    @property
    def consumo_medio(self):
        total_km = 0
        total_litros = 0

        if len(self._abastecimento) >=7:
            ultimos = self._abastecimento[-7]
            for i in range(1,len(ultimos)):
                km_anterios = ultimos[i-1]['quilometragem_de_abastecimento']
                km_atual = ultimos[i]['quilometragem_de_abastecimento']
                diferenca = km_atual - km_anterios
                total_km +=diferenca

        else:
            todos = self._abastecimento
            for i in range(1, len(todos)):
                km_anterios = todos[i - 1]['quilometragem_de_abastecimento']
                km_atual = todos[i]['quilometragem_de_abastecimento']
                diferenca = km_atual - km_anterios
                total_km += diferenca






    def manutencao_km(self):





