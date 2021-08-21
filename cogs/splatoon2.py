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
        ua = "Splatoon2MapPostBot/WIP (twitter @SzlyNe_, Discord Assault#6639"
        headers = {"User-Agent": ua}
        response = requests.get(url)
        jsonData = response.json()

        await ctx.send(jsonData["result"][0]["rule"])

def setup(bot):
    bot.add_cog(Splatoon2(bot))
