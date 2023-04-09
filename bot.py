import discord, logging
from datetime import datetime, timedelta
from discord.ext import tasks
from discord import app_commands
from tokenfolder import secret

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
id = 552886687118655489 # Change this if different server. Currently Bloops'
channel = 729426983699742791 # Change this if different channel. Currently update-avenue
handler = logging.FileHandler(filename='bot.log', encoding='utf-8', mode='w')

def gmtplusone():
    return datetime.utcnow() + timedelta(hours=1)

starttime = datetime.strftime(gmtplusone(), "%H:%M:%S")

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id))
    print(f'Bot connected as {client.user}')
    print(f'UTC+1 time is {starttime}')
    print(f'today is {datetime.strftime(gmtplusone(), "%A")}')
    monday.start(client)

@tree.command(name = "monday", description = "Is it Monday yet?", guild=discord.Object(id))
async def check_monday(interaction):
    if datetime.strftime(gmtplusone(), "%A") == "'Monday'":
        await interaction.response.send_message("Monday!")
    else:
        await interaction.response.send_message("It's not Monday.", ephemeral=False) # make this ephemeral when bossman feels like it

@tree.command(name="gmtime", description="What time is it? (England) (Where Bloops is)", guild=discord.Object(id))
async def check_time(interaction):
    await interaction.response.send_message(f"It's {datetime.strftime(gmtplusone(), '%H:%M:%S')}", ephemeral=True)

@tree.command(name="checksync", description="Check the time the bot was started on.", guild=discord.Object(id))
async def check_sync(interaction):
    await interaction.response.send_message(f"Bot started at {starttime} GMT+1. Should the bot stay up until then, Monday will be dropped around 00:{datetime.strftime(starttime, '%M:%S')} next Monday.", ephemeral=True)

@tasks.loop(hours=1)
async def monday(client):
    # check if monday
    if datetime.strftime(gmtplusone(), "%A") == "'Monday'":
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="Monday!"))
        # check if midnight
        if datetime.strftime(gmtplusone(), "%H") == "00":
            monday = client.get_channel(channel) # Change to desired channel
            message = "Monday!"
            await monday.send(message)
            print(f'Monday delivered.')
    else:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for Mondays..."))

client.run(secret.secrettoken, log_handler=handler, log_level=logging.DEBUG, reconnect=True )
