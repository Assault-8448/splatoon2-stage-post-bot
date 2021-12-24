from discord.ext import commands
import discord

class General(commands.Cog):
    __slots__ = "bot"
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def guide(self, ctx: commands.Context):
        embed = discord.Embed(title="つかいかた",
                              description="``;map``コマンドを叩くだけで全部出てきます。",
                              color=0x333333)
        embed.set_footer(text="APIは毎度叩いているので連投はお控え下さい")

        await ctx.send(embed=embed)

    @commands.command()
    async def bpm(self, ctx: commands.Context, *arg: int) -> None:
        if len(arg) == 0:
            await ctx.send('BPMを指定してください')
            return
        else:
            bpm_calc = 24 * arg / 60
            await ctx.send(bpm_calc)

def setup(bot):
    bot.add_cog(General(bot))
