import discord
import asyncio
import config 
import os

from discord.ext import commands
from discord import app_commands




# creating bot
intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)

tree = app_commands.CommandTree(client)
bot = commands.Bot(command_prefix='!', intents=intents, case_insensitive=False, application_id='1191641638557196319')



@bot.event
async def on_ready():
    
    print('Online')

# listens for and processes commands
@bot.event
async def on_message(message):
    # process commands
    await bot.process_commands(message)
    # then if author is bot or is the start of a command return nothing
    if message[0] == '!':
        return
    if message.author == bot.user:
        return
    await message.channel.send('Hello friend.')

@bot.command()
async def sync(ctx):
    print('sync command')
    if ctx.author.id == 289228060732162049:
        
        fmt = await bot.tree.sync(guild=ctx.guild)
        await ctx.send(f'Command tree synced. {len(fmt)} commands synced')
    else:
        await ctx.send('You myst be the owner to use this command!')

# loads all cogs
async def load():
    # finds files
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            # loads files                     without '.py'
            await bot.load_extension(f'cogs.{filename[:-3]}')
    
# loads cogs and starts bot 
async def main():
    await load()
    await bot.start(config.TOKEN)

    
# run starts bot command
asyncio.run(main())