class Moto:

    def __init__(self,marca = '',modelo = '',ano = 0,quilometragem = 0, consumo = 0,motoboy_id=0):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self._quilometragem_total = int(quilometragem)
        self._consumo = consumo
        self._motoboy = motoboy_id

    def __str__(self):
        return f"marca-{self._marca},modelo-{self._modelo},ano-{self._ano},quilometragem-{self._quilometragem_total},consumo-{self._consumo}"