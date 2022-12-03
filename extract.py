import os
import pandas as pd
from dotenv import load_dotenv
import datetime
import discord
import Utils

load_dotenv()

message_columns = ['id', 'time', 'channel', 'author_id', 'author', 'content', 'reactions', 'title', 'embeds', 'interaction', 'sticker'] 
emoji_columns = ['id', 'name', 'code', 'url']
mes = Utils.months(7)

class MyClient(discord.Client):
    async def on_ready(self):
        alberguz = self.get_guild(855694948707991593)
        print(mes['name'], mes['limit'])
        # Exporta lista de Emojis
        emojis = pd.DataFrame(columns=emoji_columns)
        for emoji in alberguz.emojis:
            emojis = pd.concat([emojis, pd.DataFrame([[
                emoji.id,
                emoji.name,
                '<:' + emoji.name + ':' + str(emoji.id) + '>',
                emoji.url,
            ]], columns=emoji_columns)])    
        emojis.to_csv('./output/emojis.csv')
        print('Emojis atualizados')
        # Exporta conversas
        data = pd.DataFrame(columns=message_columns) 
        print(f'logged on as {self.user}')
        for channel in alberguz.channels:
            # print(channel.name, channel.id, channel.type)
            counter = 0
            if channel.type.name in ['voice', 'text'] and channel.id not in [862556909160759307]:
                try:
                    async for msg in self.get_channel(channel.id).history(limit=mes['limit'], after=datetime.datetime(2022, mes['month'], 1, 0, 0, 0), before=datetime.datetime(2022, mes['month'], mes['last_day'], 23, 59, 59)):
                        try:
                            title = ''
                            embed = msg.embeds[0].to_dict()
                            if hasattr(msg.embeds[0], 'title'):
                                title = msg.embeds[0].title
                        except:
                            embed = ''
                        
                        if not Utils.is_command(msg):
                            data = pd.concat([data, pd.DataFrame([[
                                                msg.id,
                                                msg.created_at, 
                                                msg.channel,
                                                msg.author.id,
                                                msg.author.name,
                                                msg.content,
                                                msg.reactions,
                                                title,
                                                embed,
                                                msg.interaction,
                                                msg.stickers
                                                ]], columns=message_columns)])
                            counter += 1
                            print(datetime.datetime.now(), channel.name, counter, end='\r')
                            
                        if len(data) == mes['limit']:
                            break
                except Exception as e:
                    print('deu ruim')
                    print(e)
                    break;
            print(datetime.datetime.now(), channel.name, len(data.index))
        data.to_csv('./output/2022-'+ mes['name'] + '.csv')
        print('terminou')
intents = discord.Intents.default()
intents.message_content = True


client = MyClient(intents=intents)
# client.setStart(datetime.datetime(2022,1,1))
# client.setEnd(datetime.datetime(2022,1,31))
client.run(os.environ.get("DISCORD_TOKEN"))



