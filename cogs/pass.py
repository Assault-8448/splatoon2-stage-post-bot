import discord.ext.commands as commands
import discord

import string
import secrets

class Pass(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def genpass(self, ctx, arg: int) -> int:
        size = arg
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + "!#$%&()=~|`{+*}<>?_,./;:]@[-^"

        generatedPass = "".join(secrets.choice(chars) for x in range(size))
    
        await ctx.send(generatedPass)
        

def setup(bot):
    bot.add_cog(Pass(bot))
