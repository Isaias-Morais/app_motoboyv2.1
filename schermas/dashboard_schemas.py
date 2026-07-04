from pydantic import BaseModel

class DashboardBase(BaseModel):
    lucro_bruto:float
    gasto_combustivel:float
    gasto_manutencao:float
    
