import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'logged on as {self.user}')
    
    async def on_message(self, message):
        print(f'{message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('OTk3MjY1MTc0NjgxNjMyNzg4.GLzT5i.5Hn139j9aKqauDEt5ALdwfcq2I_PXFULKs3Auc')
