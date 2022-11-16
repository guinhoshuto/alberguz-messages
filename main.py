import pandas as pd
import numpy as np
from collections import Counter

messages = pd.read_csv('./output/messages.csv')

def author_top_keywords(author):
    top_kw = Counter(" ".join(messages[messages['author'] == author]["content"].astype(str).str.lower()).split()).most_common(100)
    kw = [k[0] for k in top_kw]
    kw_times = [k[1] for k in top_kw]
    # for kw in top_kw:
    #     kw_arr.append(kw.replace('(','').replace(')','').split(','))
    df = pd.DataFrame({'author': [author]*len(top_kw), 'kw': kw, 'times': kw_times})
    return df

messages = messages[messages['time'] > '2022-01-01']
messages['date'] = [msg.split(' ')[0] for msg in messages['time']]
# print(messages['time'].tail())

# mensagens por canal
channel = messages.groupby('channel')['channel'].count()
print(channel)
channel.to_csv('./output/channels.csv')

# usuarios por canal
channel_author = messages.groupby(['channel', 'author']).size()
print(channel_author)
channel_author.to_csv('./output/channel_author.csv')

# usuarios por canal
channel_author_date = messages.groupby(['channel', 'author', 'date']).size()
print(channel_author_date)
channel_author.to_csv('./output/channel_author_date.csv')

# mensagens por usuário
author = messages.groupby('author')['author'].count()
author.to_csv('./output/author.csv')

print(messages.dtypes)

author_df = pd.DataFrame(columns=['author', 'kw', 'times'])
for author in messages['author'].unique():
    author_df = pd.concat([author_df, author_top_keywords(author)])
    
author_df.to_csv('./output/author_top_kw.csv')

# print(Counter(" ".join(messages[messages['author'] != 'Mudae']["content"].astype(str)).split()).most_common(100))

#por tempo mes
# print(messages.groupby('channel')['time', 'author', 'content'].last())