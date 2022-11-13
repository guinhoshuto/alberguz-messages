import pandas as pd

messages = pd.read_csv('./output/messages.csv')

print(messages['time'].tail())

# mensagens por canal
channel = messages.groupby('channel')['channel'].count()
print(channel)
channel.to_csv('./output/channels.csv')

# usuarios por canal
channel_author = messages.groupby(['channel', 'author']).size()
print(channel_author)
channel_author.to_csv('./output/channel_author.csv')

# mensagens por usuário
author = messages.groupby('author')['author'].count()
author.to_csv('./output/author.csv')


# print(messages.groupby('channel')['time', 'author', 'content'].last())