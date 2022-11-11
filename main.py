import os
import pandas as pd
from dotenv import load_dotenv
import discord

load_dotenv()

def is_command(msg):
    if len(msg.content) == 0:
        return False
    elif msg.content.split()[0] == '_scan':
        return True
    else: 
        return False

class MyClient(discord.Client):
    async def on_ready(self):
        alberguz = self.get_guild(855694948707991593)
        data = pd.DataFrame(columns=['id', 'time', 'channel', 'author_id', 'author', 'content', 'embeds']) 
        print(f'logged on as {self.user}')
        # print(self.get_guild(855694948707991593))
        # print(next(self.get_channel(855695828856864799).history(limit=10000)))
        for channels in alberguz.channels:
            print(channels.name, channels.id)
        # async for channel in alberguz.channels:
        #     print(channel.name)

        limit = 10
        async for msg in self.get_channel(896104609188298762).history(limit=limit):
            try:
                embed = msg.embeds[0].to_dict()
            except:
                embed = ''
                
            if not is_command(msg):
                data = data.append({'id': msg.id,
                                    'time': msg.created_at, 
                                    'channel': msg.channel,
                                    'author_id': msg.author.id,
                                    'author': msg.author.name,
                                    'content': msg.content,
                                    'embeds': embed
                                    }, ignore_index=True)
            if len(data) == limit:
                break
    # async def on_message(self, message):
    #     print(f'{message.author}: {message.content}')
        data.to_csv('cassino_.csv')
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ.get("DISCORD_TOKEN"))



