import discord
import time
from datetime import datetime
from discord.ext import commands
from functions import conversions


        

class Time(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    



    @commands.Cog.listener()
    async def on_ready(self):
        print("Time cog loaded")

    @commands.command()
    #@commands.has_permissions(administrator=True)
    async def time(self, ctx):
        
        #from_date = "2022-03-03 06:00:00"
        #time1 = int(datetime.strptime(from_date, "%Y-%m-%d %H:%M:%S").timestamp())
        #time1 = int(time.time())
        
        await ctx.channel.send(conversions.convert_to_unix_time(29,12,2023,11,30))

# adding Facts class as a cog
async def setup(bot):
    
    await bot.add_cog(Time(bot))