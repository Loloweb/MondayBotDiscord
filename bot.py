import discord, time, logging
from discord.ext import tasks
from discord import app_commands
from tokenfolder import secret

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
id = 552886687118655489 # Change this if different server. Currently Bloops'
channel = 729426983699742791 # Change this if different channel. Currently update-avenue
handler = logging.FileHandler(filename='bot.log', encoding='utf-8', mode='w')

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id))
    print(f'Bot connected as {client.user}')
    print(f'UTC time is {time.strftime("%H:%M:%S", time.gmtime())}')
    print(f'today is {time.strftime("%A", time.gmtime())}')
    monday.start(client)

@tree.command(name = "monday", description = "Is it Monday yet?", guild=discord.Object(id)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction):
    if time.strftime("%A", time.gmtime()) == "Monday":
        await interaction.response.send_message("Monday!")
    else:
        await interaction.response.send_message("It's not Monday.", ephemeral=False)

@tasks.loop(hours=1)
async def monday(client):
    # check if monday
    if time.strftime("%A", time.gmtime()) == "Monday":
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Monday!"))
        # check if midnight
        if time.strftime("%H", time.gmtime()) == "00":
            client.get_channel(channel) # Change to desired channel
            message = "Monday!"
            await channel.send(message)
            print(f'Monday delivered.')
    else:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=None))

client.run(secret.secrettoken, log_handler=handler, log_level=logging.DEBUG, reconnect=True )
