import discord
from discord.ext import commands
from utils.utils import *


try:
    logchannel = int(parser.get('CONFIG', 'log_channel'))
except Exception as e:
    print(f"Couldn't define logchannel: {e}")
    logchannel = None

class OnReady(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        con.log('Successfully logged in as ' + self.bot.user.name + ' | ' + str(self.bot.user.id) + '.')
        if logchannel is not None:
            channel = self.bot.get_channel(logchannel)
            embed = discord.Embed(title=f"Bot started.", description=f"```\nBot started successfully.\n```", color=0x00ff00)
            await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(OnReady(bot))