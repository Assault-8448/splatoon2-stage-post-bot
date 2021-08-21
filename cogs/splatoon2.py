from discord.ext import commands
import discord as discord

class Splatoon2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send("唐澤貴洋殺す")

def setup(bot):
    bot.add_cog(Splatoon2(bot))
