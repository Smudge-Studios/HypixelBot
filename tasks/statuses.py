import discord
from discord.ext import commands, tasks
from utils.utils import con, utils, hypixel
from configparser import ConfigParser

parser = ConfigParser()
parser.read('config.ini')
API_KEY = parser.get('CONFIG', 'api_key')
try:
    logchannel = int(parser.get('CONFIG', 'log_channel'))
except Exception as e:
    print(f"Couldn't define logchannel: {e}")
    logchannel = None


class Statuses(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.statuses.start()

    def cog_unload(self):
        self.statuses.cancel()
    
    @tasks.loop(minutes=1.0)
    async def statuses(self):
        data = await hypixel.counts()
        if data['success'] != True:
            con.log(f"Couldn't set status.\nSuccess: {data['success']}")
            if logchannel is not None:
                channel = self.bot.get_channel(logchannel)
                if channel is not None:
                    embed = discord.Embed(title=f"Couldn't set custom status.", description=f"```\nAPI Success: {data['success']}\n```", color=0xff0000)
                    try:
                        await channel.send(embed=embed)
                    except discord.Forbidden:
                        raise ValueError("The bot does not have permissions to send messages in the logchannel specified in config.ini.")
                else:
                    raise ValueError("The logchannel specified in config.ini is not visible to the bot, or does not exist.")
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