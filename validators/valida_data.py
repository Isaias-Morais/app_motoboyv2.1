from datetime import date

def valida_data(dia=None,mes=None,ano=None):
    if dia is None and mes is None and ano is None:
        return True,date.today()

    try:
        return True,  date(ano, mes, dia)
    except ValueError:
        return False, 'Data inexitente'
