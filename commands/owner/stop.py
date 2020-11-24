import discord
from discord.ext import commands
from utils.utils import con
from configparser import ConfigParser

parser = ConfigParser()
parser.read('botconfig.ini')
TOKEN = parser.get('CONFIG', 'token')
try:
    logchannel = int(parser.get('CONFIG', 'log_channel'))
except Exception as e:
    print(f"Couldn't define logchannel: {e}")
    logchannel = None

class StopCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['shutdown','logout'], hidden=True)
    @commands.is_owner()
    async def stop(self, ctx):
        con.log(f'{ctx.author.id} is attempting to remotely shutdown the bot...')
        await ctx.send('Stopping the bot...')
        if logchannel is not None:
            channel = self.bot.get_channel(logchannel)
            if channel is not None:
                embed = discord.Embed(title=f"Bot shutting down", description=f"```\n{ctx.author} is remotely shutting down the bot.\n```", color=0xff0000)
                try:
                    await channel.send(embed=embed)
                except discord.Forbidden:
                    raise ValueError("The bot does not have permissions to send messages in the logchannel specified in botconfig.ini.")
            else:
                raise ValueError("The logchannel specified in botconfig.ini is not visible to the bot, or does not exist.")
        await self.bot.logout()

def setup(bot):
    bot.add_cog(StopCMD(bot))