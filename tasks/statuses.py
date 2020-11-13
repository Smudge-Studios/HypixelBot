import discord
from discord.ext import commands, tasks
from utils.utils import con, utils
from aiohttp import ClientSession
from configparser import ConfigParser

parser = ConfigParser()
parser.read('botconfig.ini')
API_KEY = parser.get('CONFIG', 'api_key')

class Statuses(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = ClientSession()
        self.statuses.start()

    def cog_unload(self):
        self.session.close()
        self.statuses.cancel()
    
    @tasks.loop(minutes=1.0)
    async def statuses(self):
        async with self.session.get('https://api.hypixel.net/playerCount?key=' + API_KEY) as response:
            data = await response.json()
        if data['success'] != True:
            await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.streaming, name="on the Hypixel Network.", url = 'https://www.twitch.tv/technoblade'))
        else:
            await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.streaming, name=f"{utils.comma(data['playerCount'])} player's stats.", url = 'https://www.twitch.tv/technoblade'))

    @statuses.before_loop
    async def before_statuses(self):
        con.log('Waiting to run Statuses task...')
        await self.bot.wait_until_ready()
        con.log('Running Statuses...')

def setup(bot):
    bot.add_cog(Statuses(bot))