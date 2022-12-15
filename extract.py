import os
import pandas as pd
from dotenv import load_dotenv
import datetime
import discord
import Utils

load_dotenv()

message_columns = ['id', 'time', 'channel', 'author_id', 'author', 'content', 'reactions', 'title', 'embeds', 'interaction', 'sticker'] 
emoji_columns = ['id', 'name', 'code', 'url']
member_columns = ['author_id', 'author', 'joined_at', 'bot', 'display_avatar', 'roles']
mes = Utils.months(11)

def get_users(server):
    members = pd.DataFrame(columns=member_columns)
    for member in server.members:
        print(member.name, member.joined_at, member.roles, member.display_avatar)
        members = pd.concat([members, pd.DataFrame([[
            member.id,
            member.name,
            member.joined_at,
            member.bot,
            member.display_avatar,
            member.roles
        ]], columns=member_columns)])
    members.to_csv('./output/members.csv')
    print('Membros atualizados')

def get_emojis(server):
    emojis = pd.DataFrame(columns=emoji_columns)
    for emoji in server.emojis:
        emojis = pd.concat([emojis, pd.DataFrame([[
            emoji.id,
            emoji.name,
            '<:' + emoji.name + ':' + str(emoji.id) + '>',
            emoji.url,
        ]], columns=emoji_columns)])    
    emojis.to_csv('./output/emojis.csv')
    print('Emojis atualizados')

async def get_month_messages(client, server, month):
    data = pd.DataFrame(columns=message_columns) 
    for channel in server.channels:
        counter = 0
        if channel.type.name in ['voice', 'text'] and channel.id not in [862556909160759307]:
            try:
                async for msg in client.get_channel(channel.id).history(limit=month['limit'], after=datetime.datetime(2022, month['month'], 1, 0, 0, 0), before=datetime.datetime(2022, month['month'], month['last_day'], 23, 59, 59)):
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
                        
                    if len(data) == month['limit']:
                        break
            except Exception as e:
                print('deu ruim')
                print(e)
                break;
        print(datetime.datetime.now(), channel.name, channel.id, len(data.index))
    data.to_csv('./output/2022-'+ month['name'] + '.csv')
    print('terminou')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'logged on as {self.user}')
        alberguz = self.get_guild(855694948707991593)
        print(mes['name'], mes['limit'])
        # get_users(alberguz)
        # get_emojis(alberguz)
        await get_month_messages(self, alberguz, mes)

intents = discord.Intents.all()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ.get("DISCORD_TOKEN"))



