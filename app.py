import asyncio
import traceback
import os
import yaml

import discord
import discord.ext.commands as cmd

COGS = [
    "cogs.general",
    "cogs.splatoon2"
]

class Bot(cmd.Bot):
    def __init__(self, prefix):
        super().__init__(command_prefix=prefix)

        for cog in COGS:
            try:
                self.load_extension(cog)
            except Exception as e:
                print(f"Failed to load extension {cog}.")
                traceback.print_exc()

    async def on_ready(self):
        print(f"Logged in as: {self.user.name}, {self.user.id}")

        game = discord.Game(";help")
        await self.change_presence(status=discord.Status.online, activity=game)

default_token_data = {
        "using": "main",
        "main": "<your bot token here>"
        }

def main():
    if not os.path.exists("token.yml"):
        with open("token.yml", "w") as f:
            yaml.dump(default_token_data, f)
            print(
                    """
                    edit token.yml to add your bot token.
                    in default, it will selected 'main'.
                    """
                    )
            exit()
    else:
        with open("token.yml", "r") as f:
            data = yaml.safe_load(f)
            token_key = data['using']
            token = data[token_key]

        bot = Bot(prefix=f";"   # Prefix定義
        bot.run(token)

if __name__ == "__main__":
    main()
