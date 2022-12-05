import pandas as pd

messages = pd.read_csv('./output/channel_author_date.csv')

jan = pd.read_csv('./output/2022-fev.csv')
rewind_columns = ['id', 'username', 'user_id', 'periodo', 'allMessages', 'emojis', 'popularWord', 'messagesByPeriod', 'messagesByChannel']
user_rewind = pd.DataFrame(columns=rewind_columns)

recalp = pd.DataFrame(columns=rewind_columns)

# def preenche_usuario(user):

# 1 capa 
    # username (username)
    # periodo  (periodo)
# 2 mandou x mensagens
    # messages (allmessages, allmessages:alberguz)
# 3 emoji mais usado
    # emojis (emojis, emojis:alberguz)
# 4 palavra mais falada
    # palavra (popularword, popularword:alberguz)
# 5 por mës
    # messagesByPeriod
# 6 canal mais usado
    # messagesByChannel 
# 7 quantos dias vc já está no server
    # user (outrobd)
# 8 resumo/obg

print(messages.head())
print(len(jan.index))

# server info

# user info