import discord.ext.commands as commands
import discord

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def guide(self, ctx):
        embed = discord.Embed(title="つかいかた",
                              description="``;map``コマンドを叩くだけで全部出てきます。",
                              color=0x333333)
        embed.set_footer(text="APIは毎度叩いているので連投はお控え下さい")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(General(bot))
