months_data = [
    {
        'month': 1,
        'name': 'jan',
        'last_day': 31, 
        'limit': 27000
    },
    {
        'month': 2,
        'name': 'fev',
        'last_day': 28, 
        'limit': 28000
    },
    {
        'month': 3,
        'name': 'mar',
        'last_day': 31, 
        'limit': 23000
    },
    {
        'month': 4,
        'name': 'abr',
        'last_day': 30, 
        'limit': 23000
    },
    {
        'month': 5,
        'name': 'mai',
        'last_day': 31, 
        'limit': 10000
    },
    {
        'month': 6,
        'name': 'jun',
        'last_day': 30, 
        'limit': 20000
    },
    {
        'month': 7,
        'name': 'jul',
        'last_day': 31, 
        'limit': 180000
    },
    {
        'month': 8,
        'name': 'ago',
        'last_day': 31, 
        'limit': 117000
    },
    {
        'month': 9,
        'name': 'set',
        'last_day': 30, 
        'limit': 66000
    },
    {
        'month': 10,
        'name': 'out',
        'last_day': 31, 
        'limit': 44000
    },
    {
        'month': 11,
        'name': 'nov',
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

def months(m): 
    return [month for month in months_data if month['month'] == m][0]
