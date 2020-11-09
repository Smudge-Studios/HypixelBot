import discord
from discord.ext import commands
import asyncio
from urllib.request import Request, urlopen
import json
from utils.utils import *

class OnReady(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        con.log(' Successfully logged in as ' + self.bot.user.name + ' | ' + str(self.bot.user.id) + '.')
        delay=60
        req = Request('https://api.hypixel.net/playerCount?key=abe73fdc-9735-4677-859a-a34fa0cb14e4')
        req.add_header('plun1331', 'https://plun1331.github.io')
        content = urlopen(req)
        data = json.load(content)
        while True:
            if data['success'] != True:
                await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.streaming, name="on the Hypixel Network.", url = 'https://www.twitch.tv/technoblade'))
                await asyncio.sleep(delay)
            else:
                await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.streaming, name=f"{utils.comma(data['playerCount'])} player's stats.", url = 'https://www.twitch.tv/technoblade'))
                await asyncio.sleep(delay)

def setup(bot):
    bot.add_cog(OnReady(bot))