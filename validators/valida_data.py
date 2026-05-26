from datetime import date

def valida_data(dia=None,mes=None,ano=None):
    if dia is None and mes is None and ano is None:
        return None

    try:
        date(ano, mes, dia)
    except ValueError:
        raise ValueError
