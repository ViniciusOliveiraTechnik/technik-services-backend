import datetime

def date_to_text(date_string):

    month_name = {
        '1': 'Janeiro',
        '2': 'Fevereiro',
        '3': 'Março',
        '4': 'Abril',
        '5': 'Maio',
        '6': 'Junho',
        '7': 'Julho',
        '8': 'Agosto',
        '9': 'Setembro',
        '10': 'Outubro',
        '11': 'Novembro',
        '12': 'Dezembro',
    }

    date = datetime.datetime.strptime(date_string, '%Y-%m-%d')

    return f'{date.day} de {month_name[str(date.month)]} de {date.year}'

print(date_to_text('2025-05-01'))