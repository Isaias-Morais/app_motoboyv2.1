class Motoboy:
    def __init__(self,nome="",idade=0,email='',moto_ativa = None):
        self._nome = nome
        self._idade = idade
        self._email = email
        self._moto_ativa_id = moto_ativa

    def __str__(self):
        return f'{self._nome},{self._idade},{self._email},{self._moto_ativa_id}'

