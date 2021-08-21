from discord.ext import commands
import discord as discord

import datetime
import requests
import json

dt = datetime.datetime.now()

class Splatoon2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def regular(self, ctx):

        url = "https://spla2.yuu26.com/regular/now"
        url_2 = "https://spla2.yuu26.com/regular/next"
        ua = "Splatoon2MapPostBot_regular/WIP (twitter @SzlyNe_, Discord Assault#6639"
        headers = {"User-Agent": ua}

        response = requests.get(url)
        jsonData = response.json()

        regular_map0 = jsonData["result"][0]["maps"][0]
        regular_map1 = jsonData["result"][0]["maps"][1]

        response = requests.get(url_2)
        jsonData = response.json()

        regular_nextmap0 = jsonData["result"][0]["maps"][0]
        regular_nextmap1 = jsonData["result"][0]["maps"][1]

        regular_embed = discord.Embed(
                                    title = "現在と次のレギュラーマッチ ステージローテーション",
                                    color=0x00ff00,
                                    description=f"{dt.strftime('%Y年%m月%d日 %H:%M:%S')}時点でのステージと次のステージ")
        regular_embed.add_field(name=f"現在は**{regular_map0}**", value=f"次は「**{regular_nextmap0}**」")
        regular_embed.add_field(name=f"現在は**{regular_map1}**", value=f"次は「**{regular_nextmap1}**」")
        regular_embed.set_thumbnail(url="https://cdn.wikimg.net/en/splatoonwiki/images/4/4c/Mode_Icon_Regular_Battle_2.png")
        regular_embed.set_footer(text="APIは https://spla2.yuu26.com を利用しています。")

        await ctx.send(embed=regular_embed)

    @commands.command()
    async def ranked(self, ctx):

        url = "https://spla2.yuu26.com/gachi/now"
        ua = "Splatoon2MapPostBot_ranked/WIP (twitter @SzlyNe_, Discord Assault#6639"
        headers = {"User-Agent": ua}
        response = requests.get(url)
        jsonData = response.json()

        ranked_mode = jsonData["result"][0]["rule"]
        ranked_map0 = jsonData["result"][0]["maps"][0]
        ranked_map1 = jsonData["result"][0]["maps"][1]

        await ctx.send(f"現在のルール: {ranked_mode} / 現在のマップ: {ranked_map0}, {ranked_map1}")

def setup(bot):
    bot.add_cog(Splatoon2(bot))
