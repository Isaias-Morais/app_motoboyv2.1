def validacao_motoboy(nome,idade,email):

    if not isinstance(nome,(str)) or len(nome) == 0:
       return False , 'Digite um nome valido'
    if not isinstance(idade,(int)) or idade <=0:
        return False , 'Digite uma idade valida '
    if not '@' in email:
        return False , 'Digite um email valido'
    else:
        return True, 'Sucesso na operaçao'

