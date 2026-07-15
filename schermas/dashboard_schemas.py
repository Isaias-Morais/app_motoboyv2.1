from pydantic import BaseModel

class DashboardBase(BaseModel):
    lucro_bruto:float
    gasto_combustivel:float
    gasto_manutencao:float
    km_rodados:int
    lucro_liquido:float


class DashboardGastoMedio(DashboardBase):
    gasto_medio_manutencao:float
    gasto_media_abastecimento:float
