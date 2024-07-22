# Crie uma função que receba um horário e imprima "Bom dia!", "Boa tarde!" ou "Boa noite!" conforme o horário.

def recebe_horario(horario, nome):
    if horario >= 5 and horario <= 12:
       return(f"Bom dia, {nome}!")

    elif horario > 12 and horario <= 18:
       return(f"Boa tarde, {nome}!")

    else:
       return(f"Boa noite, {nome}!")
    

horas = recebe_horario(nome='Gabriel', horario=10)

print(horas)