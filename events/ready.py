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
            try:
                channel = self.bot.get_channel(logchannel)
                if channel is not None:
                    embed = discord.Embed(title=f"Bot started.", description=f"```\nBot started successfully.\n```", color=0x00ff00)
                    try:
                        await channel.send(embed=embed)
                    except discord.Forbidden:
                        raise ValueError("The bot does not have permissions to send messages in the logchannel specified in botconfig.ini.")
                else:
                    raise ValueError("The logchannel specified in botconfig.ini is not visible to the bot, or does not exist.")

def setup(bot):
    bot.add_cog(OnReady(bot))