from pydantic import BaseModel

class DashboardBase(BaseModel):
    lucro_bruto:float
    gasto_combustivel_km:float
    gasto_manutencao_km:float
    km_rodados:int
    lucro_liquido:float


class DashboardGastoMedio(DashboardBase):
    gasto_medio_manutencao:float
    gasto_media_abastecimento:float
