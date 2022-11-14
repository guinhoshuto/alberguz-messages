import os
import pandas as pd
from dotenv import load_dotenv
import discord

load_dotenv()

message_columns= ['id', 'time', 'channel', 'author_id', 'author', 'content', 'embeds'] 
limit = 1000000

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
        data = pd.DataFrame(columns=message_columns) 
        print(f'logged on as {self.user}')
        for channel in alberguz.channels:
            print(channel.name, channel.id, channel.type)
            if channel.type.name in ['voice', 'text'] and channel.id not in [862556909160759307]:
                try:
                    async for msg in self.get_channel(channel.id).history(limit=limit):
                        try:
                            embed = msg.embeds[0].to_dict()
                        except:
                            embed = ''
                        
                        if not is_command(msg):
                            data = pd.concat([data, pd.DataFrame([[
                                                msg.id,
                                                msg.created_at, 
                                                msg.channel,
                                                msg.author.id,
                                                msg.author.name,
                                                msg.content,
                                                embed
                                                ]], columns=message_columns)])
                        if len(data) == limit:
                            break
                except:
                    print('deu ruim')
                    break;
        data.to_csv('./output/messages.csv')
        print('terminou')
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ.get("DISCORD_TOKEN"))



