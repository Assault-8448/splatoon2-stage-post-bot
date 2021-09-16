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

def main():
        bot = Bot(prefix=f';')
        bot.run("ODc1NjM4MDM5NDEyNjA0OTU5.YRYbeQ.zA6Y6FmoDg3yEc5r1s8IOn0jUi8")

if __name__ == "__main__":
    main()
