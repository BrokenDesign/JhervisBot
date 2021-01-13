import discord
import os
from discord.ext import commands

token = os.environ.get('BOT_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(msg):
    if(msg.author.id==497442139664285716):
        await delete_message(msg.id)
        await msg.channel.send('<!@497442139664285716> go to bed!!!')
        

client.run(token)
