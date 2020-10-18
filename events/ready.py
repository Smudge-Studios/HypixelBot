import discord
from discord.ext import commands
import asyncio
import requests
        
class OnReady(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(' Successfully logged in as ' + self.bot.user.name + ' | ' + str(self.bot.user.id) + '.')
        delay=60
        r = requests.get('https://api.hypixel.net/playerCount?key=abe73fdc-9735-4677-859a-a34fa0cb14e4')
        data = r.json()
        while True:
            if data['success'] != True:
                await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="on the Hypixel Network."))
                await asyncio.sleep(delay)
            else:
                await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name=f"with {data['playerCount']} players on the Hypixel Network."))
                await asyncio.sleep(delay)

def setup(bot):
    bot.add_cog(OnReady(bot))