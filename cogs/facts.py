import discord
import requests
import json
from discord.ext import commands

class Facts(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Facts cog loaded")

    @commands.command()
    #@commands.has_permissions(administrator=True)
    async def facts(self, ctx):
        # generating quote
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + " -" + json_data[0]['a']
        # sending quote as an embed
        embed=discord.Embed(description=quote)
        await ctx.channel.send(embed=embed)

# adding Facts class as a cog
async def setup(bot):
    await bot.add_cog(Facts(bot))