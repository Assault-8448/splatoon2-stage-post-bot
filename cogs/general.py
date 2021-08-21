import discord.ext.commands as commands
import discord

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx, *message):
        await ctx.send(' '.join(message))

def setup(bot):
    bot.add_cog(General(bot))
