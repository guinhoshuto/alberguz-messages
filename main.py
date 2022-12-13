import pandas as pd
import numpy as np
from collections import Counter
from os import listdir
from os.path import isfile, join
from Utils import ignore

message_columns = ['id', 'time', 'channel', 'author_id', 'author', 'content', 'reactions', 'title', 'embeds', 'interaction', 'sticker'] 
#juntar todos os meses em 1 dataframe
def merge_months():
    messages_files = [f for f in listdir('./output') if isfile(join('./output/', f)) and f[0:4] == '2022']
    recalp_messages = pd.DataFrame(columns=message_columns)
    for file in messages_files:
        tmp = pd.read_csv('./output/' + file)
        recalp_messages = pd.concat([recalp_messages, tmp])
    print(recalp_messages.info())
    print(len(messages_files))
    recalp_messages.drop('Unnamed: 0', inplace=True, axis=1)
    recalp_messages.to_csv('./output/messages.csv')
    return messages_files

messages = pd.read_csv('./output/messages.csv')
messages['date'] = [msg.split(' ')[0] for msg in messages['time']]

# messages = messages[messages['time'] > '2022-01-01']
# print(messages['time'].tail())

def author_top_keywords(messages, author, ignore):
    author_id = messages[messages['author'] == author]['author_id'].unique()[0]
    top_kw = Counter(" ".join(messages[messages['author'] == author]["content"].astype(str).str.lower()).split()).most_common(1000)
    # for word in top_kw:
    #     if word[0] in ignore:
    #         print(word)
    #         del word

    kw = [k[0] for k in top_kw]
    kw_times = [k[1] for k in top_kw]
    # for kw in top_kw:
    #     kw_arr.append(kw.replace('(','').replace(')','').split(','))
    df = pd.DataFrame({'author_id': author_id, 'author': [author]*len(top_kw), 'kw': kw, 'times': kw_times})
    return df


# mensagens por canal
def channels_csv(messages):
    channel = messages.groupby('channel')['channel'].count()
    channel.to_csv('./output/channels.csv')

# usuarios por canal
def channels_author_csv(messages):
    channel_author = messages.groupby(['channel', 'author']).size()
    channel_author.to_csv('./output/channel_author.csv')

# usuarios por canal
def channels_author_date_csv(messages):
    channel_author_date = messages.groupby(['channel', 'author_id', 'author', 'date']).size()
    channel_author_date.to_csv('./output/channel_author_date.csv')

# mensagens por usuário
def author_csv(messages):
    author = messages.groupby('author')['author'].count()
    author.to_csv('./output/author.csv')

def author_top_kw(messages, ignore):
    author_df = pd.DataFrame(columns=['author_id', 'author', 'kw', 'times'])
    for author in messages['author'].unique():
        author_df = pd.concat([author_df, author_top_keywords(messages, author, ignore)])

    # for word in list(top_kw):
    #     if word in ignore:
    #         del top_kw[word]
    # for word in author_df:
    #     if word['kw'] in ignore:
    #         del word

    author_df = author_df[~author_df['kw'].isin(ignore)]
    author_df.to_csv('./output/author_top_kw.csv')

# merge_months()
# channels_csv(messages)
# channels_author_csv(messages)
# channels_author_date_csv(messages)
# author_csv(messages)
author_top_kw(messages, ignore)
# print(messages['Unnamed: 0'].unique())

# print(Counter(" ".join(messages[messages['author'] != 'Mudae']["content"].astype(str)).split()).most_common(100))

#por tempo mes
# print(messages.groupby('channel')['time', 'author', 'content'].last())