months_data = [
    {
        'month': 1,
        'name': 'jan',
        'full_name': 'Janeiro',
        'last_day': 31, 
        'limit': 27000
    },
    {
        'month': 2,
        'name': 'fev',
        'full_name': 'Fevereiro',
        'last_day': 28, 
        'limit': 28000
    },
    {
        'month': 3,
        'name': 'mar',
        'full_name': 'Março',
        'last_day': 31, 
        'limit': 23000
    },
    {
        'month': 4,
        'name': 'abr',
        'full_name': 'Abril',
        'last_day': 30, 
        'limit': 23000
    },
    {
        'month': 5,
        'name': 'mai',
        'full_name': 'Maio',
        'last_day': 31, 
        'limit': 10000
    },
    {
        'month': 6,
        'name': 'jun',
        'full_name': 'Junho',
        'last_day': 30, 
        'limit': 20000
    },
    {
        'month': 7,
        'name': 'jul',
        'full_name': 'Julho',
        'last_day': 31, 
        'limit': 180000
    },
    {
        'month': 8,
        'name': 'ago',
        'full_name': 'Agosto',
        'last_day': 31, 
        'limit': 117000
    },
    {
        'month': 9,
        'name': 'set',
        'full_name': 'Setembro',
        'last_day': 30, 
        'limit': 66000
    },
    {
        'month': 10,
        'name': 'out',
        'full_name': 'Outubro',
        'last_day': 31, 
        'limit': 44000
    },
    {
        'month': 11,
        'name': 'nov',
        'full_name': 'Novembro',
        'last_day': 30, 
        'limit': 50000
    },
]

def is_command(msg):
    if len(msg.content) == 0:
        return False
    elif msg.content.split()[0] == '_scan':
        return True
    else: 
        return False

def emoji_code(name, id):
    return '<:' + name + ':' + str(id) + '>',


def months(m): 
    return [month for month in months_data if month['month'] == m][0]

ignore = ['$m', 'o', '$p', 'de', 'que', 'eu', 'a', 'é', 'e', 'pra', '$tu', 'do', 'no', 
        'mas', 'q', 'um', 'nan', 'da', 'tem', 'não', 'com', '$im', 'mais', 'se', 'na', 
        'só', 'em', 'nao', 'n', 'isso', 'uma', 'meu', 'to', '$w', 'os', 'ele', 'tá', 
        '$h', 'ta', 'me', 'vai', 'esse', 'ai', 'y', 'mto', 'por', '$d', 'acho', 'foi', 
        'pq', 'as', 'vou', '$arl', '1', 'nem', 'era', 'aqui', 'agora', 'tava', 'essa']