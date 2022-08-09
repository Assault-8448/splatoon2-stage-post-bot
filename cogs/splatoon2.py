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
        ua = "Splatoon2MapPostBot_regular/WIP (twitter @SzlyNe_, Discord Assault#1892"
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
                                    title = "レギュラーマッチ（ナワバリバトル）",
                                    color=0x00ff00,
                                    description=f"{dt.strftime('%Y年%m月%d日 %H:%M:%S')}時点と次のステージ情報")
        regular_embed.add_field(name=f"いま: **{regular_map0}** / **{regular_map1}**",
                                value=f"つぎ: **{regular_nextmap0}** / **{regular_nextmap1}**",
                                inline=False)
        regular_embed.set_thumbnail(url="https://cdn.wikimg.net/en/splatoonwiki/images/4/4c/Mode_Icon_Regular_Battle_2.png")
        regular_embed.set_footer(text="API: https://spla2.yuu26.com")

        await ctx.send(embed=regular_embed)

    @commands.command()
    async def ranked(self, ctx):

        url = "https://spla2.yuu26.com/gachi/now"
        url_2 = "https://spla2.yuu26.com/gachi/next"
        ua = "Splatoon2MapPostBot_regular/WIP (twitter @SzlyNe_, Discord Assault#1138"
        headers = {"User-Agent": ua}

        response = requests.get(url)
        jsonData = response.json()

        ranked_mode = jsonData["result"][0]["rule"]
        ranked_map0 = jsonData["result"][0]["maps"][0]
        ranked_map1 = jsonData["result"][0]["maps"][1]

        response = requests.get(url_2)
        jsonData = response.json()

        ranked_nextmode = jsonData["result"][0]["rule"]
        ranked_nextmap0 = jsonData["result"][0]["maps"][0]
        ranked_nextmap1 = jsonData["result"][0]["maps"][1]

        ranked_embed = discord.Embed(
                                    title = "ガチマッチ",
                                    color=0xff0000,
                                    description=f"{dt.strftime('%Y年%m月%d日 %H:%M:%S')}時点と次のモードとステージ情報")
        ranked_embed.add_field(name=f"いま: **{ranked_mode}**", value=f"つぎ: **{ranked_nextmode}**", inline=False)
        ranked_embed.add_field(name=f"いま: **{ranked_map0}** / **{ranked_map1}**",
                              value=f"つぎ: **{ranked_nextmap0}** / **{ranked_nextmap1}**",
                              inline=False)
        ranked_embed.set_thumbnail(url="https://cdn.wikimg.net/en/splatoonwiki/images/2/2c/Mode_Icon_Ranked_Battle_2.png")
        ranked_embed.set_footer(text="API: https://spla2.yuu26.com")

        await ctx.send(embed=ranked_embed)

    @commands.command()
    async def league(self, ctx):

        url = "https://spla2.yuu26.com/league/now"
        url_2 = "https://spla2.yuu26.com/league/next"
        ua = "Splatoon2MapPostBot_regular/WIP (twitter @SzlyNe_, Discord Assault#1138"
        headers = {"User-Agent": ua}

        response = requests.get(url)
        jsonData = response.json()

        league_mode = jsonData["result"][0]["rule"]
        league_map0 = jsonData["result"][0]["maps"][0]
        league_map1 = jsonData["result"][0]["maps"][1]

        response = requests.get(url_2)
        jsonData = response.json()

        league_nextmode = jsonData["result"][0]["rule"]
        league_nextmap0 = jsonData["result"][0]["maps"][0]
        league_nextmap1 = jsonData["result"][0]["maps"][1]

        league_embed = discord.Embed(
                                    title = "リーグマッチ",
                                    color=0xffc0cb,
                                    description=f"{dt.strftime('%Y年%m月%d日 %H:%M:%S')}時点と次のモードとステージ情報")
        league_embed.add_field(name=f"いま: **{league_mode}**", value=f"つぎ: **{league_nextmode}**", inline=False)
        league_embed.add_field(name=f"いま: **{league_map0}** / **{league_map1}**",
                               value=f"つぎ: **{league_nextmap0}** / **{league_nextmap1}**",
                               inline=False)
        league_embed.set_thumbnail(url="https://cdn.wikimg.net/en/splatoonwiki/images/9/9b/Symbol_LeagueF.png")
        league_embed.set_footer(text="API: https://spla2.yuu26.com")

        await ctx.send(embed=league_embed)

    @commands.command()
    async def salmon(self, ctx):

        url = "https://spla2.yuu26.com/coop/schedule"
        ua = "Splatoon2MapPostBot_regular/WIP (twitter @SzlyNe_, Discord Assault#1138"
        headers = {"User-Agent": ua}

        response = requests.get(url)
        jsonData = response.json()

        # 現在のサーモンランのデータを取得

        salmon_map   = jsonData["result"][0]["stage"]["name"]
        salmon_wpn_1 = jsonData["result"][0]["weapons"][0]["name"]
        salmon_wpn_2 = jsonData["result"][0]["weapons"][1]["name"]
        salmon_wpn_3 = jsonData["result"][0]["weapons"][2]["name"]
        salmon_wpn_4 = jsonData["result"][0]["weapons"][3]["name"]
        salmon_logo  = jsonData["result"][0]["stage"]["image"]

        salmon_time_epoch = jsonData["result"][0]["end_t"]  # 今のサーモンランが終了する時間を取得
        salmon_time = datetime.datetime.fromtimestamp(salmon_time_epoch)  # Unix時間からJSTに変換

        # 次のサーモンランのデータを取得

        salmon_nextMap   = jsonData["result"][1]["stage"]["name"]
        salmon_nextWpn_1 = jsonData["result"][1]["weapons"][0]["name"]
        salmon_nextWpn_2 = jsonData["result"][1]["weapons"][1]["name"]
        salmon_nextWpn_3 = jsonData["result"][1]["weapons"][2]["name"]
        salmon_nextWpn_4 = jsonData["result"][1]["weapons"][3]["name"]

        salmon_nextTime_epoch = jsonData["result"][1]["start_t"]  # 次のサーモンランが始まる時間を取得
        salmon_nextTime = datetime.datetime.fromtimestamp(salmon_nextTime_epoch)  # Unix時間からJSTに変換

        salmon_embed = discord.Embed(
                                    title = "サーモンラン",
                                    color = 0xff7f50,
                                    description=f"{dt.strftime('%Y年%m月%d日 %H:%M:%S')}時点のブキとステージ情報\n\nいまのは**{salmon_time.strftime('%Y年%m月%d日 %H:%M:%S')}**まで継続\nつぎのは**{salmon_nextTime.strftime('%Y年%m月%d日 %H:%M:%S')}**にて開始")
        salmon_embed.add_field(name=f"ブキ: {salmon_wpn_1}, {salmon_wpn_2}, {salmon_wpn_3}, {salmon_wpn_4}",
                               value=f"ステージ: **{salmon_map}**",
                               inline=False)
        salmon_embed.add_field(name=f"次のブキ: {salmon_nextWpn_1}, {salmon_nextWpn_2}, {salmon_nextWpn_3}, {salmon_nextWpn_4}",
                               value=f"ステージ: **{salmon_nextMap}**",
                               inline=False)
        salmon_embed.set_thumbnail(url=f"{salmon_logo}")
        salmon_embed.set_footer(text="API: https://spla2.yuu26.com")

        await ctx.send(embed=salmon_embed)

def setup(bot):
    bot.add_cog(Splatoon2(bot))
