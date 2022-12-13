import os
import pandas as pd
from dotenv import load_dotenv
from Utils import months_data
import sqlalchemy as db
from rich import print
load_dotenv()

# engine = db.create_engine(os.environ.get("DATABASE_URL"))
# connection = engine.connect()

# recalp_db = db.Table('recalp')
# print(recalp_db.columns.keys())
def month_columns(date):
    month = str(date).split('-')[1]
    month_name = [m['name'] for m in months_data if m['month'] == int(month)]
    return ' '.join(month_name)


members = pd.read_csv('./output/members.csv')
messages = pd.read_csv('./output/channel_author_date.csv')
messages['month'] = messages['date'].apply(lambda d: month_columns(d))
messages.to_csv('./output/recalp_month.csv')
print(messages.head())

jan = pd.read_csv('./output/2022-fev.csv')
rewind_columns = ['username', 'user_id', 'periodo', 'allMessages', 'messagesByPeriod', 'messagesByChannel', 'joined_at', 'avatar']
user_rewind = pd.DataFrame(columns=rewind_columns)

recalp = pd.DataFrame(columns=rewind_columns)


def get_messages_by_period_all():
    return get_messages_by_month(1)
def get_messages_by_channel_all():
    return get_messages_by_channel(1)

def get_messages_by_month(user):
    months = {}
    user_messages = messages[messages['author_id'] == user]
    for m in months_data:
        qtd = user_messages[user_messages['month'] == m['name']]['0'].sum()
        # if m['name'] == 'jan':
        #     print(user_messages[user_messages['month'] == m['name']]['author'].iloc(0), m['name'], qtd)
        months[m['name']] = qtd
    return months

def get_messages_by_channel(user):
    channels = {}
    user_messages = messages[messages['author_id'] == user]
    for c in messages['channel'].unique():
        channels[c] = user_messages[user_messages['channel'] == c ]['0'].sum()
    return channels

def get_user_info(user):
    user_info = members[members['author_id'] == user]
    return user_info

recalp = pd.concat([recalp, pd.DataFrame([[
    'alberguz',
    1,
    '2022',
    messages['0'].sum(),
    get_messages_by_period_all(),
    get_messages_by_channel_all(),
    '',
    ''
]], columns=rewind_columns)])

for user in messages['author_id'].unique():
    tmp = messages[messages['author_id'] == user]
    author = tmp['author'].iloc[0]
    allMessages = tmp['0'].sum()
    messagesByPeriod = get_messages_by_month(user)
    messagesByChannel = get_messages_by_channel(user)
    user_info = get_user_info(user)
    # print(user_info.joined_at.values[0])
    joined_at = ''
    if len(user_info.joined_at.values) > 0:
        joined_at = user_info.joined_at.values[0]

    display_avatar = ''
    if len(user_info.display_avatar.values) > 0:
        display_avatar = user_info.display_avatar.values[0]

    recalp = pd.concat([recalp, pd.DataFrame([[
        author,
        user,
        '2022',
        allMessages,
        messagesByPeriod,
        messagesByChannel,
        joined_at,
        display_avatar
    ]], columns=rewind_columns)])

print(recalp.head())
recalp.to_csv('./output/recalp.csv')
# def preenche_usuario(user):

# 1 capa 
    # username (username)
    # periodo  (periodo)
# 2 mandou x mensagens
    # messages (allmessages, allmessages:alberguz)
# 3 por mës
    # messagesByPeriod
# 4 canal mais usado
    # messagesByChannel 
# 5 quantos dias vc já está no server
    # user (outrobd)
# 6 resumo/obg

# print(messages.head())
# print(len(jan.index))

# server info

# user info

# def get_most_used_emoji():
#     return {"emoji": "", "times_used": 0}

# def get_most_popular_word():
#     return {"word": "", "times_used": 0}

# def get_user_most_used_emoji(user):
#     return {"emoji": "", "times_used": 0}

# def get_user_most_used_word(user):
#     return {"word": "", "times_used": 0}
