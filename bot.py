import discord, asyncio, os
from discord.ext import commands, tasks
import time
from tokenfolder import secret

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot connected as {client.user}')
    print(f'UTC time is {time.strftime("%H:%M:%S", time.gmtime())}')
    print(f'today is {time.strftime("%A", time.gmtime())}')
    monday.start(client)

@tasks.loop(hours=1)
async def monday(client):
    # check if monday
    if time.strftime("%A", time.gmtime()) == "Monday":
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Monday!"))
        # check if midnight
        if time.strftime("%H", time.gmtime()) == "20":
            channel = client.get_channel(239054461656498177)
            message = "Monday!"
            await channel.send(message)
            print(f'Monday delivered.')
    else:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=None))

client.run(secret.secrettoken)