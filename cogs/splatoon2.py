from discord.ext import commands
import discord as discord

import requests
import json

class Splatoon2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def regular(self, ctx):

        url = "https://spla2.yuu26.com/regular/now"
        response = requests.get(url)
        jsonData = response.json()

        await ctx.send(jsonData["result"])

def setup(bot):
    bot.add_cog(Splatoon2(bot))
