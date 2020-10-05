from datetime import datetime

import discord
from discord.ext import commands, tasks


client = commands.Bot(command_prefix = '.')

_warnings = 'Logs are not saved to chatlogs.txt'

@client.event
async def on_ready():
    print(f"Bot connected {round(client.latency * 1000)}ms")
    print("============\nWarning \n" + _warnings + "\n============")

@client.event
async def on_message(message):
    text_file = open("chatlogs.txt", "w")
    output = f'[{datetime.now().strftime("%H:%M:%S")}][{message.channel}]{message.author}: {message.content}'
    print(output)
    text_file.write("\a" + f'[{datetime.now().strftime("%H:%M:%S")}][{message.channel}]{message.author}: {message.content}')
    text_file.close()

#@client

token = open("token.txt", "r")
client.run(token.read())
